import uuid
import random
from datetime import datetime
from datetime import timedelta 
import time
import json
import boto3

# change value for firehoseName with your Connect stream's name e.g. CTRFHStream
region = "ap-southeast-2"
firehoseName = "<YOUR_CONNECT_STREAM>"

client = boto3.client("firehose", region)

def set_userNumber():
    phoneList = [
        "+61428921911",
        "+61468457600",
        "+61478388994",
        "+61448295201",
        "+61482107117",
        "+61432784228",
        "+61414537801",
        "+61428901833",
        "+61433354650",
        "+61453610894",
        "+61442806542",
        "+61486624761",
        "+61425558428",
        "+61483270375",
        "+61422851375",
        "+61455336318",
        "+61444809744",
        "+61444182410",
        "+61483483285",
        "+61438293837",
        "+61418444598",
        "+61443234260",
        "+61418787400",
        "+61449251972",
        "+61449251972",
        "+61446679164",
        "+61490486472",
        "+61423792504",
        "+61415563345",
        "+61434898150",
        "+61488842748",
        "+61413408781",
        "+61426788814",
        "+61471321703",
        "+61457418539",
        "+61459968718",
        "+61430933455",
        "+61442669251",
        "+61441604202",
        "+61445143923",
        "+61459990911",
        "+61449341734",
        "+61457121207",
        "+61456340800",
        "+61449130717",
        "+61438542895",
        "+61411122707",
        "+61488769680",
        "+61469568615",
        "+61441171975",
        "+61416876161",
        "+61440494600",
        "+61418608341",
        "+61450935301",
        "+61454291203",
        "+61425309599",
        "+61418460262",
        "+61418328540",
        "+61433101236",
        "+61476379548",
        "+61414856432",
        "+61435395838",
        "+61455518530",
        "+61438509201",
        "+61426715144",
        "+61452863489",
        "+61413287353",
        "+61484720517",
        "+61421696295",
        "+61445857801",
        "+61431858291",
        "+61484264824",
        "+61418523184",
        "+61471123568",
        "+61470982804",
        "+61413777363",
        "+61416725378",
        "+61415776592",
        "+61482939132",
        "+61439303551",
        "+61480778128"
    ]
    return (random.choice(phoneList))

def set_startEndTime():
    # generate start time
    startTime = datetime.now() - timedelta(days=random.randint(1,30),hours=random.randint(1,24),minutes=random.randint(1,60))
    # end time
    endTime = startTime + timedelta(minutes=random.randint(1,30),seconds=random.randint(1,60))
    # changing to timestamp format to "2018-10-30T02:24:33Z"
    timestampFormat = "%Y-%m-%dT%H:%M:%SZ"
    # return single object with 2 values to unpack later on
    return (startTime.strftime(timestampFormat), endTime.strftime(timestampFormat))

def set_agentName():
    nameList = [
        "James",
        "Rachel",
        "Adam",
        "Bob",
        "Emily",
        "Taylor"
    ]
    return (random.choice(nameList))

def set_queue():
    queueList = [
        "Sales",
        "Support",
        "Members"
    ]
    return (random.choice(queueList))

def generate_connectCallLog():
    myTime = set_startEndTime()
    customerObj = {"Address": set_userNumber(), "Type": "TELEPHONE_NUMBER"}
    queueObj = {"Duration": random.randint(1,600), "EnqueueTimestamp": myTime[0], "DequeueTimestamp": myTime[1], "ARN": "arn:aws:connect:ap-southeast-2:708252083442:instance/8f1400f1-4492-46a2-85ac-90b2a7a5fdb8", "Name": set_queue()}

    callData = {
        "AWSAccountId": "012345678910",
        "AWSContactTraceRecordFormatVersion": "2017-03-10",
        "Agent": set_agentName(),
        "AgentConnectionAttempts": 1,
        "Attributes": {"greetingPlayed": "true"},
        "Channel": "VOICE",
        "ConnectedToSystemTimestamp": myTime[0],
        "ContactId": str(uuid.uuid4()),
        "CustomerEndpoint": customerObj,
        "DisconnectTimestamp": myTime[1],
        "InitialContactId": None,
        "InitiationMethod": "INBOUND",
        "InitiationTimestamp": myTime[0],
        "InstanceARN": "arn:aws:connect:ap-southeast-2:708252083442:instance/8f1400f1-4492-46a2-85ac-90b2a7a5fdb8",
        "LastUpdateTimestamp": myTime[1],
        "MediaStreams": [{"Type": "AUDIO"}],
        "NextContactId": None,
        "PreviousContactId": None,
        "Queue": queueObj,
        "Recording": None,
        "Recordings": None,
        "SystemEndpoint": {"Address": "+611300395832", "Type": "TELEPHONE_NUMBER"},
        "TransferCompletedTimestamp": None,
        "TransferredToEndpoint": None
    }

    return (callData)


def main():
    data = generate_connectCallLog()
    print (data)
    data_str = json.dumps(data)

    print (">>>>> Generated data >>>>>")
    print ("")
    print (data_str)
    
    response = client.put_record(
        DeliveryStreamName = firehoseName,
        Record = {
            "Data": data_str
        }
    )
    print ("")
    print ("Pushing new record into Kinesis Firehose")
    print ("")
    print ("<<<<< KINESIS RESPONSE <<<<<")
    print (response)
    print ("")

if __name__ == "__main__":
    main()

