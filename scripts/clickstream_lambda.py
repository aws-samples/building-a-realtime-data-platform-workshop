from __future__ import print_function

import base64
import json
import re
from dateutil.parser import parse
from datetime import datetime, tzinfo, timedelta

print('Loading function')


class UTC(tzinfo):
    """UTC"""

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return timedelta(0)

utc = UTC()


def lambda_handler(event, context):

    print ("This is the raw event: {}".format(event))
    output = []
    succeeded_record_cnt = 0
    failed_record_cnt = 0
    
    safe_string_to_int = lambda x: int(x) if x.isdigit() else x

    ## Because data in Kinesis is base64 encoded, we have to decode it before changing the output as a JSON document
    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data'])
        payload = payload.decode("utf-8")
        print ("This is the payload: {}".format(payload)) 
        
        # check if clickstream log format else fall back to other log format
        regex = '^([\d.]+) (\S+) (\S+) \[([\w:\/]+)(\s[\+\-]\d{4}){0,1}\] "(.+?)" (\d{3}) (\d+) (".+?") (".+?") "user = ([^;]*)' 
        p = re.compile(regex)
        m = p.match(payload)
        
        if p.match(payload) is None: # log format doesnt have cookie data (username)
            regex = '^([\d.]+) (\S+) (\S+) \[([\w:/]+)(\s[\+\-]\d{4}){0,1}\] \"(.+?)\" (\d{3}) (\d+) (".+?") (".+?")'
            p = re.compile(regex)
            m = p.match(payload)
        
        if m:
            succeeded_record_cnt += 1

            ts = m.group(4)
            ## changing the timestamp format
            try:
                d = parse(ts.replace(':', ' ', 1))
                ts = d.isoformat()
            except:
                print('Parsing the timestamp to date failed.')
            ## Creating our dictionary (hash map) using extracted values from our log file
            data_field = {
                'host': m.group(1),
                'ident': m.group(2),
                'authuser': m.group(3),
                '@timestamp': ts,
                'request': m.group(6),
                'response': safe_string_to_int(m.group(7)),
                'bytes': safe_string_to_int(m.group(8)),
                'referer': safe_string_to_int(m.group(9)),
                'user-agent': safe_string_to_int(m.group(10))
            }
            ## Clickstream log, adding username from cookie field
            if (len(m.groups()) > 10):
                data_field['username'] = safe_string_to_int(m.group(11))
    
            if m.group(6) and len(m.group(6).split()) > 1:
                data_field['verb'] = m.group(6).split()[0]

            # If time offset is present, add the timezone and @timestamp_utc fields
            if m.group(5):
                data_field['timezone'] = m.group(5).strip()
                try:
                    ts_with_offset = m.group(4) + m.group(5)
                    d = parse(ts_with_offset.replace(':', ' ', 1))
                    utc_d = d.astimezone(utc)
                    data_field['@timestamp_utc'] = utc_d.isoformat()
                except:
                    print('Calculating UTC time failed.')

            output_record = {
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': base64.b64encode(json.dumps(data_field))
            }
        else:
            print('Parsing failed')
            failed_record_cnt += 1
            output_record = {
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data']
            }

        output.append(output_record)
    
    ## This returns the transformed data back to Kinesis Data Firehose for delivery to our Elasticsearch domain
    print('Processing completed.  Successful records {}, Failed records {}.'.format(succeeded_record_cnt, failed_record_cnt))
    print ("This is the output: {}".format(output))
    return {'records': output}
