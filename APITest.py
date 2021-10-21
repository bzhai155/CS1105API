from googleapiclient.discovery import build
#I deleted the key after posting on github
api_key = "AIzaSyDpVpRpjnXf7y6yQriufXpA_XRmIl5IJGY"
channelID = "UC9qkQ1s5iWY6PzYZ5BiD-tQ"

yt = build("youtube", "v3", developerKey= api_key)
rq = yt.channels().list(
    part = "statistics",
    id= channelID
)

response = rq.execute()
#print(response)
print("CS1105 stats: ")
print("View Count: " + response['items'][0]['statistics']['viewCount'])
print("Amount of subscribers: " + response['items'][0]['statistics']['subscriberCount'])
print("Amount of videos: " + response['items'][0]['statistics']['videoCount'])

#testing out on a friends yt channel
yt1 = build("youtube", "v3", developerKey= api_key)
rq1 = yt.channels().list(
    part = "statistics",
    id= "UC6Z9TKs52ILYmeTkx1gTDHg"
)

response1 = rq1.execute()
print("Magenta Cobra stats: ")
print("View Count: " + response1['items'][0]['statistics']['viewCount'])
print("Amount of subscribers: " + response1['items'][0]['statistics']['subscriberCount'])
print("Amount of videos: " + response1['items'][0]['statistics']['videoCount'])