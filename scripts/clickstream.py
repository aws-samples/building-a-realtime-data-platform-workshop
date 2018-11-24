import uuid
import random
import socket
import struct
import datetime
import time


def set_sourceIp():
    sourceIp = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    # checking if 0.0.0.0 or 255.255.255.255. Still allows private IP addresses
    if sourceIp == "0.0.0.0" or sourceIp == "255.255.255.255":
        set_sourceIp()
    return (sourceIp)

def set_requestTime():
    timeNow = datetime.datetime.now()
    # changing to CLR format like '24/Jul/2018:17:17:13'
    timestampFormat = "%d/%b/%Y:%H:%M:%S"
    timezone = "+0000"
    return ("[{} {}]".format(timeNow.strftime(timestampFormat),timezone))

# randomizer
def set_randomWeighting(**kwargs): # pass dict values like this set_randomWeighting(foo=3,bar=6)
    myList = []
    for key, value in kwargs.items():
        myList += [str(key)] * int(value) # creates a list with weighted/quantity of values to random choose
    return (random.choice(myList))

def set_method():
    return (set_randomWeighting(GET=6, POST=3, OPTIONS=1))

def set_uriPath():
    rootPath = set_randomWeighting(home=13, products=5, categories=4, signup=1, signin=2)
    if rootPath == "home" or rootPath == "signup" or rootPath == "signin":
        secondPath = ""
    elif rootPath == "products":
        secondPath = set_randomWeighting(**({"":3}), Porcubbuks=1, Armawoo=1, Leopowwi=1, Serpaaslem=1, Glorsibou=1, Cuksing=1, Foxboon=1, Blactile=1, Meeqeos=1, Claassoukse=1) + "/"
    elif rootPath == "categories":
        secondPath = set_randomWeighting(**({"":3}) , smallUnicorns=1, mediumUnicorns=1, bigunicorns=1) + "/"
    return (rootPath + "/" + secondPath)

def set_statusCode():
    statusCodes = {
        "200" : "25",
        "301" : '3',
        "401" : "1",
        "403" : "3",
        "500" : "1",
        "503" : "1"
    }
    return (set_randomWeighting(**statusCodes))

def set_byteSize():
    return (str(random.randint(1000,50000)))

def set_host():
    return ("www.unicornshop.io")

def set_referer():
    return (set_host() + "/" + set_uriPath())

def set_userAgent():
    # user-agents
    userAgent = {
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" : "1",
        "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)" : "1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36" : "3",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36" : "3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36": "3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15" : "3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134" : "3",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1" : "3",
        "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36" : "2",
        "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4" : "2",
        "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36" : "2",
        "Mozilla/5.0 (Linux; Android 7.0; HTC 10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36" : "2",
        "Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7" : "2"
    }
    return (set_randomWeighting(**userAgent))

def set_cookies():
    userName = {
        "anonymous": "100",
        "architectjobless" : "1",
        "mongoosespots" : "1",
        "typepads" : "1",
        "purrsmunch" : "1",
        "dankishyear" : "1",
        "monstummy" : "1",
        "admiredcrocodiles" : "1",
        "silicajointed" : "1",
        "radiantscold" : "1",
        "approvefeminine" : "1",
        "grunchymole" : "1",
        "ointmentdangly" : "1",
        "paltedquantock" : "1",
        "bashfulpeas" : "1",
        "filletingtekton" : "1",
        "lymphstripey" : "1",
        "industryimmaterial" : "1",
        "comicsynonymous" : "1",
        "chippingrejoice" : "1",
        "ticketpedant" : "1",
        "apricotsflandy" : "1",
        "grainhysterical" : "1",
        "quinoacinnamon" : "1",
        "effectivemixed" : "1",
        "enquiryinventory" : "1",
        "complainoffended" : "1",
        "gustyeland" : "1",
        "rylonkookaburra" : "1",
        "softballpleasant" : "1",
        "serviceeritrean" : "1",
        "ruffbreads" : "1",
        "thoroughdrouse" : "1",
        "rockytaxonomy" : "1",
        "boastbroker" : "1",
        "uranusvapid" : "1",
        "siskinstemson" : "1",
        "nunchingburberry" : "1",
        "henastonished" : "1",
        "tackyspecific" : "1",
        "hearjaundice" : "1",
        "rejectcrucket" : "1",
        "seagullpatches" : "1",
        "immaculateobedient" : "1",
        "hicnicmanager" : "1",
        "anguisheddufus" : "1",
        "pradanonchalant" : "1",
        "vomergills" : "1",
        "viceplaintive" : "1",
        "eyepouldy" : "1",
        "fearattached" : "1",
        "defendedmother" : "1",
        "sneakypale" : "1",
        "snictorwhy" : "1",
        "refereemiscuits" : "1",
        "welcomema" : "1",
        "spongeslide" : "1",
        "pardensneering" : "1",
        "cinemaabnormal" : "1",
        "brooklyncriminal" : "1",
        "boldlateral" : "1",
        "whairhonorable" : "1",
        "needyguilty" : "1",
        "preacherbutterfly" : "1",
        "mouldythine" : "1",
        "knockroasted" : "1",
        "splittingliteral" : "1",
        "yieldclang" : "1",
        "beachsmoker" : "1",
        "slidethinking" : "1",
        "gemboar" : "1",
        "slooktaekwondo" : "1",
        "congolesebuttery" : "1",
        "rosinsaber" : "1",
        "popdiffidence" : "1",
        "movementmoneybag" : "1",
        "prestosoluble" : "1",
        "coinagecomponents" : "1",
        "mimosafilter" : "1",
        "excitingempathic" : "1",
        "invitegumps" : "1",
        "pasternsitemap" : "1"
    }
    
    sessionId = uuid.uuid4().hex

    return ("user = {}; PHPSESSID={}".format(set_randomWeighting(**userName),sessionId))

def generate_clickstreamRow():
    row = (
        set_sourceIp() +
        " " + "-" + 
        " " + "-" + 
        " " + set_requestTime() + 
        " " + "\"" + set_method() + " " + set_uriPath() + " " + "HTTP/1.1" + "\"" +
        " " + set_statusCode() +
        " " + set_byteSize() + 
        " " + "\"" + set_referer() + "\"" + 
        " " + "\"" + set_userAgent() + "\"" + 
        " " + "\"" + set_cookies() + "\""
    )
    return (row)


def main():
    logPath = "/var/log/httpd/access_log"
    #logPath = "/tmp/access_log"
    
    with open(logPath, "a") as f:
        print ("Generating new clickstream log at {}".format(logPath))
        f.write(generate_clickstreamRow())
        f.write("\n")
        time.sleep(1)

if __name__ == '__main__':
    main()
