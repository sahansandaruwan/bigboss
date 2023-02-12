import requests

def quote():

  
  url = 'https://zenquotes.io/api/random'
  response = requests.get(url)
  if response.status_code == 200:
    quote = response.json()
    print('')
    quote = quote[0]['q'] + '\n \n' + 'Author : ' +quote[0]['a']
    return quote
  else:
    return 'Bot Have a problem..please contact developer'

