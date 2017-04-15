from collections import defaultdict
from collections import Counter

# generate stop words list from file
def genStopwordsList(filename):
    stopwordsList = []
    with open(filename) as infile:
        for line in infile:
            line.strip()
            stopwordsList.append(line)

    infile.close()
    return stopwordsList

# generate the list of names (second word of each line)
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

# generate sentences
# For each paragraph (contents between two neighbouring empty lines), get the first word.
# connect them to build the sentence
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

# generate a dictionary:
# key: name (second word in a line)
# value: labels list (all the labels in the file for the name)
# the labels are with prefix
def genNameDictionary(filename, stopwords):
    nameDict = defaultdict(list)
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
                    nameDict[words[1]].append(words[3])

    infile.close()
    return nameDict

# generate a dictionary:
# key: name (second word in a line)
# value: labels list (all the labels in the file for the name)
# the labels are without prefix
def genNameDictionaryWithPrefixRemoved(filename, stopwords):
    nameDict = defaultdict(list)
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
                    label = ""
                    if (words[3] == "O"):
                        label = words[3]
                    else:
                        tokens = words[3].split("-")
                        label = tokens[1]
                    nameDict[words[1]].append(label)

    infile.close()
    return nameDict

# generate a set for all labels (with prefix)
def genLabelSet(filename, stopwords):
    labelSet = set()
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
                    labelSet.add(words[3])

    infile.close()
    return labelSet

# remove the prefix of labels
def removeLabelPrefix(labelSet):
    newLabelSet = set()
    for label in labelSet:
        if label == "O":
            newLabelSet.add(label)
        else:
            tokens = label.split("-")
            newLabelSet.add(tokens[1])

    return newLabelSet


# find the most frequent element in a list
def mostFreqLabel(labelList):
    labelCounter = Counter(labelList)
    return labelCounter.most_common(1)[0][0]


if __name__ == "__main__":
    stopwords = genStopwordsList("data/stopwords.txt")
    #namelist = genNameList("data/conll03.eng.dev.gold.tsv", stopwords)
    namedict = genNameDictionaryWithPrefixRemoved("data/conll03.eng.trn.gold.tsv", stopwords)
    #labelSet = genLabelSet("data/conll03.eng.trn.gold.tsv", stopwords)

    print(namedict["south"])
    print(mostFreqLabel(namedict["south"]))

    #sentenceList = genSentenceList("data/conll03.eng.trn.gold.tsv")

    #outfile = open("data/sentences.txt", "w+")
    #for sentence in sentenceList:
    #    outfile.write(sentence + "\n")
    #outfile.close()
