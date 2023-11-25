def loadWords():
    words = []
    with open('dict.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) > 5:
                words.append(word)
    return words


def game():
    words = loadWords()

    puzzle = input('Enter wordbind puzzle word: ')
    puzzleLetters = list(puzzle)
        


def main():
    game()


if __name__ == '__main__':
    main()