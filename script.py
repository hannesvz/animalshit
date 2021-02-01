from wiktionaryparser import WiktionaryParser

parser = WiktionaryParser()

list = open('list.txt', 'r').read().split('\n')

for animal in list:
  check_result = parser.fetch(animal + 'shit')

  definitions = 'None'

  try:
    definitions = ', '.join(check_result[0]['definitions'][0]['text'])
  except Exception as e:
    pass

  print(f'{animal}: {definitions}')
