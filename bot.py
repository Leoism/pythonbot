import requests

def cleanMarkup(text):
    markupList = ['[', ']']
    for markup in markupList:
        text = text.replace(markup, '')

    return text

def define(term):
    url    = 'https://api.urbandictionary.com/v0/define?term=' + term 
    final  = url.replace(' ', '%20')
    r      = requests.get(final)
    posDef = r.json()['list']
    index  = 0

    if len(posDef) >= 1:
        inc    = input('There are/is ' + str(len(posDef)) + ' definition(s)\nWhich number would you like to view: ')
        index  += inc - 1
        if inc > len(posDef):
            index = len(posDef) - 1
        definition = "\nHere's what " + term + " means:\n" + cleanMarkup(posDef[index]['definition']) + """\n
example: """ + cleanMarkup(posDef[index]['example'])
        return definition    

    elif len(posDef) == 0:
        return ('The word seems to not exist.')

while True:
    word = raw_input('What word would you like to look up on urbandictionary? \n')
    if len(word) > 0:
        print define(word)
    else:
        print ('Hey you did not give a word to define!')
