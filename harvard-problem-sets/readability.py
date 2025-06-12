def words(text) -> int:
    word = text.split()

    return len(word)

def sentences(text) -> int:
    
    sentence = text.split(".")
    return len(sentence)

def letters(text) -> int:
    
    striped_txt = text.replace(" ", "")
    pt = list(striped_txt)
    
    letters = [letter for letter in pt if letter != "."]

    return len(letters)

def cli(words, letters, sentences):
    L = float((letters / words) * 100)
    S = float((sentences / words) * 100)

    cli = 0.0588 * L - 0.296 * S - 15.8

    return int(cli)

def readability(text) -> int:
    word = words(text)
    letter = letters(text)
    sentence = sentences(text)

    grade = cli(word, letter, sentence)

    return int(grade) 


def main():
    text = input("Enter text: ")

    grade = readability(text)

    print(f"before grade: {grade}")

if __name__ == '__main__':
    main()
