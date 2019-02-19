import os
import matplotlib.pyplot as plt
import numpy as np
table = {}
average_values = {}

# to iterate over all subdirectories in keywords directory
for subdir in os.listdir('keywords'):

    # to iterate over all files in sub dir
    for filename in os.listdir("keywords\\"+subdir):
        count = 0
        file = open('keywords\\'+subdir+'\\'+filename, "r", encoding="latin-1")
        for line in file:
            count += line.lower().count(subdir)

        # insert filename and respective frequency count in table(dictionary)
        if filename != 'result.txt':
            table[filename] = count
            if filename in average_values:
                average_values[filename] = average_values.pop(filename) + count
            else:
                average_values[filename] = count

    # write table values in results.txt file
    fw = open('keywords\\'+subdir+'\\'+"result.txt", "w")
    for key, values in table.items():
        fw.write(key + "  : " + str(values) + "\n")

# to draw bar graph
pages = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
for k, v in average_values.items():
    average_values[k] = v/10
frequency = average_values.values()
y_pos = np.arange(len(pages))
plt.bar(y_pos, frequency, align='center')
plt.xticks(y_pos, pages)
plt.ylabel('Frequency')
plt.xlabel('Page No.')
plt.title('Frequency vs Pages')
plt.show()