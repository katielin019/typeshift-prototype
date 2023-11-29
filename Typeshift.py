# var_in = input("Please enter something: ")
# print("You entered: " + var_in)

class Typeshift(object):
    def __init__(self):
        self.rows = [[]]
        self.index = 0

    # def addColumn(letters):
    #     self.rows[index] = letters
    #     self.index += 1


def game():
    # wordLen = input('How long is each typeshift word?')
    puzzle = Typeshift()
    initialized = False

    while (not initialized):
        x = input('Enter the letters (no spaces between) in column ' + str(puzzle.index) + ' or press enter/return to finish: ')
        if len(x) == 0:
            # https://stackoverflow.com/questions/52231554/blank-input-in-python
            initialized = True
        elif puzzle.index == 0:
            # https://www.freecodecamp.org/news/python-string-to-array-how-to-convert-text-to-a-list/
            puzzle.rows[puzzle.index] = list(x)
            puzzle.index += 1
        else:
            puzzle.rows.append([])
            puzzle.rows[puzzle.index] = list(x)
            puzzle.index += 1

    # call loadWords, which returns a list of words in wordlist that are the same length as puzzle.rows.length   
    words = loadWords(puzzle.index)

    # print(len(words))
    candidates = []
    for word in words:
        valid = True
        # for i in range(puzzle.index):
        for i in range(len(puzzle.rows)):
            if word[i] not in puzzle.rows[i]:
                valid = False
        if valid == True:
            candidates.append(word)
    
    # print(candidates)
    analyzeSolutions(candidates, puzzle.rows)
    # displaySolutions(candidates)
    

def loadWords(target):
    words = []
    # https://stackoverflow.com/questions/70426424/convert-text-file-into-array
    with open('dict.txt', 'r') as f:
        for line in f:
            # word = line[1:-1].upper()
            word = line.strip()
            if len(word) == target:
                words.append(word)
    return words

def displaySolutions(arr):
    if len(arr) == 0:
        print("No solutions found :(")
    for elem in arr:
        print(elem)

def analyzeSolutions(candidates, keys):
    frequencies = [{}]
    vals = [[]]

    # Initialize data structures for frequency analysis (1)
    for i in range(len(keys)):
        tmp = [0] * len(keys[i])
        vals[i] = tmp
        if not i == len(keys) - 1:
            vals.append([])
            frequencies.append({})

    # Initialize data structures for frequency analysis (2)
    for j in range(len(vals)):
        tmpDict = dict(zip(keys[j], vals[j]))
        frequencies[j] = tmpDict

    for word in candidates:
        print(word)
        letters = list(word)
        for k in range(len(letters)):
            currLetter = letters[k]
            print(str(k) + ": " + currLetter)
            # letterIndex = keys[k].index(currLetter)
            # print("letter index: " + str(letterIndex))
            frequencies[k][currLetter] += 1

    print(frequencies)


def main():
    game()

if __name__ == '__main__':
    main()