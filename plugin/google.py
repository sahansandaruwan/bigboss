from googlesearch import search

def google(message):
        query = message.content[7:]
        urls = search(query, num_results=10)
        url_str = "🔰"+"\n 🔰".join(urls)
        return url_str
