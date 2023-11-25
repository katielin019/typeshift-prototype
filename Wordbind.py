def loadWords(puzzleLetters):
    words = []
    with open('dict.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) >= 5:
                letters = list(word)
                candidate = True

                for letter in letters:
                    if letter not in puzzleLetters:
                        candidate = False
                
                if candidate == True:
                    words.append(word)
    return words


def displaySolutions(arr):
    if len(arr) == 0:
        print("No solutions found :(")
    for elem in arr:
        print(elem)


def game():
    puzzle = input('Enter wordbind puzzle word: ')
    puzzleLetters = list(puzzle)

    words = loadWords(puzzleLetters)
    wordbinds = []

    for word in words:
        letters = list(word)
        indexes = []

        for letter in letters:
            currIndex = puzzleLetters.index(letter)
            indexes.append(currIndex)
        
        if sorted(indexes) == indexes:
            wordbinds.append(word)
    
    displaySolutions(wordbinds)    


def main():
    game()


if __name__ == '__main__':
    main()