import json
import re
import urllib.request
import fire

from pytube import YouTube

api_key = "ENTER_YOUR_API_KEY_HERE"
maxResults = 100 # the max is 100

# 
if maxResults > 100:
    maxResults = 100

dump = []

def getComments(vidID):
    video_id = vidID
    nextPageToken = ""
    stop = False
    count = 0

    while not stop:
        url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={api_key}&textFormat=plainText&part=snippet&videoId={video_id}&t&maxResults={maxResults}&pageToken={nextPageToken}"

        json_url = urllib.request.urlopen(url)
        data = json.loads(json_url.read())
        nPT = 'nextPageToken'

        # 
        if nPT in data:
            nextPageToken = data['nextPageToken']
        else:
            stop = True

        # 
        nComments = len(data['items'])

        # 
        for i in range(nComments):
            print(f'Grabbed comment #{i + (count*maxResults)}')
            put = f"{data['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName']}\t{data['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay']}".replace('\n'," ").replace('\r'," ")
            dump.append(put)

        # 
        count += 1

    # 
    with open("allComments.tsv", "w+", encoding='utf-8') as f:
        f.write("\n".join(dump))
        
def main():
    fire.Fire(getComments)
    
if __name__ == '__main__':
  main()