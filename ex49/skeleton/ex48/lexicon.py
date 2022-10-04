"""
def scan(input):
    words = input.split()
    # split the input based on spaces
    #return a tuple called ('direction', input)
    operation = ''
    sentence = []

    for word in words:
        if word in directions:
            operation = 'direction'
        elif word in verb:
            operation = 'verb'
        elif word in stop_words:
            operation = 'stop'
        elif word in nouns:
            operation = 'noun'
        elif convert_number(word):
            operation = 'number'
            word = convert_number(word)
        else:
            operation = 'error'
        sentence.append((operation, word))
    return sentence

def covert_number(word):
    try:
        return int(word)
    except ValueError:
        return None
"""


# another way of how to handle it

def scan(input):
    lexicon = {'north': 'direction',
               'south': 'direction',
               'east': 'direction',
               'west': 'direction',
               'down': 'direction',
               'up': 'direction',
               'left': 'direction',
               'right': 'direction',
               'back': 'direction',
               'go': 'verb',
               'stop': 'verb',
               'kill': 'verb',
               'eat': 'verb',
               'the': 'stop',
               'in': 'stop',
               'of': 'stop',
               'from': 'stop',
               'at': 'stop',
               'it': 'stop',
               'bear': 'noun',
               'princess': 'noun',
               'cabinet': 'noun',
               'space': 'noun'
               }

    sentence = []
    words = input.split()

    for word in words:
        if word.isdigit():
            word = int(word)
            sentence.append(('number', word))
        elif word in lexicon.keys():
            sentence.append((lexicon[word], word))
        else:
            sentence.append(('error', word))
    return sentence
