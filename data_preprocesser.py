
import re
import sys


def main():
    with open(sys.argv[1]) as f:
        with open("sample.tsv", "w+") as g:
            for line in f:
                if line[0] != '#':
                    thing = line.split()
                    if len(thing) > 0:
                        g.write("\t".join(thing[2:5]) + "\n")
    sequence_length = []
    flag = -1
    tagcount = {}
    totalcount = 0
    with open("sample.tsv") as f:
        for line in f:
            totalcount += 1
            number = int(line.split()[0])
            if int(flag) >= 0:
                if number == 0:
                    sequence_length.append(flag+1)
            flag = number
            tag = line.split()[2]
            if tag not in tagcount:
                tagcount[tag] = 1
            elif tag in tagcount:
                tagcount[tag] += 1
    maxi = max(sequence_length)
    mini = min(sequence_length)
    mean = sum(sequence_length)/(len(sequence_length)+1)
    infofile = open(sys.argv[2] , "w+")
    infofile.write("Max sequence length: " + str(maxi) + "\n")
    infofile.write("Min sequence length: " + str(mini) + "\n")
    infofile.write("Mean sequence length: " + str(mean) + "\n")
    infofile.write("Number of sequences: " + str(len(sequence_length)+1) + "\n" + "\n")
    infofile.write("Tags:" + "\n")
    for item in tagcount:
        prozentwert = tagcount[item]/totalcount
        prozentwert = round(prozentwert * 100,2)
        infofile.write(item + "\t" + str(prozentwert) + "%" + "\n")


if __name__ == "__main__":
    main()