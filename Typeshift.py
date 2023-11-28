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
        else:
            # https://www.freecodecamp.org/news/python-string-to-array-how-to-convert-text-to-a-list/
            puzzle.rows[puzzle.index] = list(x)
            puzzle.rows.append([])
            puzzle.index += 1

    # call loadWords, which returns a list of words in wordlist that are the same length as puzzle.rows.length   
    words = loadWords(puzzle.index)

    # print(len(words))
    candidates = []
    for word in words:
        valid = True
        for i in range(puzzle.index):
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

def analyzeSolutions(candidates, puzzle):
    frequencies = [[0] * len(puzzle)]
    for c in range(len(puzzle)):
        tempDict = {}
        for let in puzzle[c]:
            tempDict[let] = 0
        frequencies[c] = tempDict

    print(frequencies)

    for word in candidates:
        letters = list(word)
        for i in range(len(letters)):
            letter = letters[i]
            # loc = puzzle.index(letter)
            frequencies[i][letter] += 1

    print(frequencies)


def main():
    game()

if __name__ == '__main__':
    main()