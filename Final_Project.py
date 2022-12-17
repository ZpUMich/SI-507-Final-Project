##############
# NPS and Twitter keys will need to be entered for the code to function completely
##############
NPSkey=               # SET KEY
Twitterbearer_token=  # SET TOKEN
import requests
import json
import webbrowser
from twarc import Twarc2, expansions
import datetime

#0-50
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?parkCode&api_key='+NPSkey)
Data = json.loads(jsondata.text)
NPSAll=Data["data"]
#50-100
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?start=50" -H%20 "accept: &api_key='+NPSkey)
Data = json.loads(jsondata.text)
for i in Data["data"]:
    NPSAll.append(i)
#100-150
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?start=100" -H%20 "accept: &api_key='+NPSkey)
Data = json.loads(jsondata.text)
for i in Data["data"]:
    NPSAll.append(i)
#150-200
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?start=150" -H%20 "accept: &api_key='+NPSkey)
Data = json.loads(jsondata.text)
for i in Data["data"]:
    NPSAll.append(i)
#200-250
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?start=200" -H%20 "accept: &api_key='+NPSkey)
Data = json.loads(jsondata.text)
for i in Data["data"]:
    NPSAll.append(i)
#250-300
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?start=250" -H%20 "accept: &api_key='+NPSkey)
Data = json.loads(jsondata.text)
for i in Data["data"]:
    NPSAll.append(i)
#300-350
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?start=300" -H%20 "accept: &api_key='+NPSkey)
Data = json.loads(jsondata.text)
for i in Data["data"]:
    NPSAll.append(i)
#350-400
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?start=350" -H%20 "accept: &api_key='+NPSkey)
Data = json.loads(jsondata.text)
for i in Data["data"]:
    NPSAll.append(i)
#400-450
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?start=400" -H%20 "accept: &api_key='+NPSkey)
Data = json.loads(jsondata.text)
for i in Data["data"]:
    NPSAll.append(i)
#450-467
jsondata = requests.get('https://developer.nps.gov/api/v1/parks?start=450" -H%20 "accept: &api_key='+NPSkey)
Data = json.loads(jsondata.text)
for i in Data["data"]:
    NPSAll.append(i)
    
with open("NPSAll.json", "w") as write_file:
    json.dump(NPSAll, write_file, indent=1)


fullName_NPS=[]
len(NPSAll)
for i in range(len(NPSAll)):
    fullName_NPS.append(NPSAll[i]['fullName'])
len(fullName_NPS)

#Replace with your own file location
with open('C:/Users/zacha/Desktop/SI 507/Final Project/NPSAll.json') as f:
    NPSAll = json.load(f)
fullName_NPS=[]

for i in range(len(NPSAll)):
    fullName_NPS.append(NPSAll[i]['fullName'])

class Park:
    def __init__(self, fullname, name, latLong, url= "No URL"):
        self.fullName = fullname
        self.url=url
        self.latLong=latLong
        self.Nicknames=name
        self.hashtag='#'+name.replace(" ", "")
    def OtherNames(self,name2):
        if name2 not in self.Nicknames:
            self.Nicknames.append(name2)
for i in range(len(NPSAll)):
    fullName_NPS[i]=Park(NPSAll[i]['fullName'],NPSAll[i]['name'],NPSAll[i]['latLong'],NPSAll[i]['url'])

client = Twarc2(bearer_token=Twitterbearer_token)

ParkDict = {}
for i in range(len(NPSAll)):
    ParkDict[fullName_NPS[i].fullName]=[]
    # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2021, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)
    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2022, 11, 30, 0, 0, 0, 0, datetime.timezone.utc)
    # This is where we specify our query as discussed in module 5
    query = '"'+fullName_NPS[i].fullName+'"'+' or '+'"'+fullName_NPS[i].Nicknames+'"'+' or '+'"'+fullName_NPS[i].hashtag+'"'
    # The search_all method call the full-archive search endpoint to get Tweets based on the query, start and end times
    search_results = client.search_all(query=query, start_time=start_time, end_time=end_time, max_results=1000)
    # Twarc returns all Tweets for the criteria set above, so we page through the results
    for page in search_results:
        # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
        # so we use expansions.flatten to get all the information in a single JSON
        result = expansions.flatten(page)
        for tweet in result:
            # Here we are printing the full Tweet object JSON to the console
            ParkDict[fullName_NPS[i].fullName].append(tweet)

with open("NPSTweets.json", "w") as write_file:
    json.dump(ParkDict, write_file, indent=1)