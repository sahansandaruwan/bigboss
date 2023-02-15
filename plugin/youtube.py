
from youtubesearchpython import VideosSearch
from pytube import YouTube

def ytsearch(message):
    quary = message.content[4:]
    #quary = message[4:]
    videosSearch = VideosSearch(quary, limit = 10)
    url = videosSearch.result()

    msg = ''
    for i in range(10):
        title = url['result'][i]['title']
        Channelname = url['result'][i]['channel']['name']
        duration = url['result'][i]['duration']
        link = url['result'][i]['link']
        publishedTime = url['result'][i]['publishedTime']
        ViweCount = url['result'][i]['viewCount']['short']
        VideoName = f'\n**Title:** {title}\n**Channel Name:** {Channelname}\n **Duration:** {duration}\n**ViweCount:** {ViweCount}\n**URL:** {link}\n'
        #print(VideoName)
        msg = VideoName + msg
    return msg
    
        #VideoName = JoinName.join(VideoName)
    #msg = VideoName +'\n'+ VideoName 
    #return msg
    #return msg

#ytsearch('.yt maniya')



