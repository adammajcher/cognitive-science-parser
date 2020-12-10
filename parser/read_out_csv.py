import csv

from scipy import stats

myStr = []
with open('out.csv', 'r') as data:
    for line in csv.reader(data):
        myStr.append(str(line[0]).split(';'))

colors = ['Green', 'Orange', 'Red', 'Yellow', 'Gray', 'Blue', 'Violet', 'White', 'Black']
colors_value = [[] for i in range(len(colors))]

for i in range(1, len(myStr)):
    index = colors.index(myStr[i][1])
    colors_value[index].append(myStr[i][3])

for color in colors_value:
    color = list(map(float, color))

for i in range(len(colors)):
    for j in range(len(colors)):
        if (j is not i):
            print("--- " + colors[i] + " with " + colors[j] + ": " + "---")
            statistic, pvalue = stats.mannwhitneyu(colors_value[i], colors_value[j])
            print(stats.mannwhitneyu(colors_value[i], colors_value[j]))
            print()

t = colors_value
print(stats.kruskal(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8]))
