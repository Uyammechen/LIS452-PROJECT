def genStopwordsList(filename):
    stopwordsList = []
    with open(filename) as infile:
        for line in infile:
            line.strip()
            stopwordsList.append(line)

    infile.close()
    return stopwordsList

def genNameList(filename, stopwords):
    nameList = []
    with open(filename) as infile:
        for line in infile:
            line = line.strip()
            if (line == ""):
                continue
            else:
                words = line.split("\t")
                if (words[1] in stopwords):
                    continue
                else:
                    nameList.append(words[1])

    infile.close()
    return nameList

def genSentenceList(filename):
    sentenceList = []
    sentence = ""

    with open(filename) as infile:
        for line in infile:
            line  = line.rstrip("\n")
            line.strip()
            words = line.split("\t")
            if (line.find("-docstart-") != -1):
                continue
            else:
                if (line == ""):
                    if (sentence == ""):
                        continue
                    else:
                        sentenceList.append(sentence)
                        sentence = ""
                else:
                    sentence = sentence + " " + words[0]

        sentenceList.append(sentence)

    infile.close()
    return sentenceList


if __name__ == "__main__":
    #stopwords = genStopwordsList("data/stopwords.txt")
    #namelist = genNameList("data/conll03.eng.dev.gold.tsv", stopwords)
    sentenceList = genSentenceList("data/conll03.eng.trn.gold.tsv")

    outfile = open("data/sentences.txt", "w+")
    for sentence in sentenceList:
        outfile.write(sentence + "\n")
    outfile.close()
