import csv
import statistics


def extractFirstColor(c):
    for i in range(1, len(c)):
        if c[i].isupper():
            return c[0:i]


myStr = []
with open('bd.csv', 'r') as data:
    for line in csv.reader(data):
        myStr.append(str(line[0]).split(';'))

membersCount = len(myStr) - 1
print(len(myStr[0]))

envelopes = []

for e in myStr[1]:
    if (len(e) < 3):
        continue
    if e not in envelopes:
        envelopes.append(e)

members = []

for i in range(1, len(myStr)):
    newMember = {}

    for e in envelopes:
        newMember[e] = []

    for e in envelopes:
        for j in range(3, len(myStr[0])):
            if myStr[i][j] == e:
                newMember[e].append(int(myStr[i][j + 1]))

    for e in envelopes:
        newMember[e] = round(statistics.mean(newMember[e]), 1)

    members.append(newMember)

with open('out.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["User", "Scene", "Img", "Ans"])

    for i, member in enumerate(members):
        memberName = 'User' + str(i)

        for data in member.items():
            writer.writerow([memberName, extractFirstColor(data[0]), data[0], data[1]])

