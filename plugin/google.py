from googlesearch import search

def google(message):
        #query = message
        query = message.content[7:]
        #query = message[7:]
        url = search(query,num_results=10)
        #print(url)
        #for i in url:
        #        print(i)
        url_str = "🔰"+"\n 🔰".join(url)
        return url_str
        #for i in url:
        #        print(i)
#google('game')


