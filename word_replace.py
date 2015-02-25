words = open("wordlist.txt")
customwords = open('customtraining.txt')

dictionary = {}

def train(word_file):
    for line in word_file.readlines():
        line = line.strip()
        if len(line) > 0:
            line = line.split('-')
            dumbWord = line[0].lower().strip()
            smartWords = line[1].split(',')
            # print dumbWord, smartWords
            for word in smartWords:
                dictionary[word.strip()] = dumbWord

def stupify(sentence):
    finalSentence = ''
    for word in sentence.split():
        word = word.lower()
        if word in dictionary:
            finalSentence += dictionary[word] + ' '
        else:
            finalSentence += word + ' ' 

    return finalSentence

if __name__ == '__main__':
    train(words)
    train(customwords)

    print stupify("I was mistaken for a hazardous evil witch. You ain't got nothing on me.")

    print stupify("Boyfriend")