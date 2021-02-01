import requests

list = open('list.txt', 'r').read().split('\n')

for animal in list:
  check_result = requests.get('https://api.urbandictionary.com/v0/define?term=' + animal + 'shit')

  definition = 'None'

  try:
    definition = check_result.json()['list'][0]['definition'].replace('\r\n\r\n',' ').replace('[','').replace(']','')
  except Exception as e:
    pass

  print(f'{animal}shit: {definition}')
