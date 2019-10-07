"""
infantmortality.py

NYC infant mortality rate from 2007-2016 

"""
#import
import sys
import io
import csv
import urllib.request
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/jhjhjhsu/InfantMortality/master/InfantMortality.csv"

#access data

try:
    fileFromUrl = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error, file = sys.stderr)
    sys.exit(1)

sequenceOfBytes = fileFromUrl.read() #Read whole file into one big sequenceOfBytes.
fileFromUrl.close()

try:
    s = sequenceOfBytes.decode("utf-8")    #s is a string, decoding
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

fileFromString = io.StringIO(s)
lines = csv.reader(s.splitlines())
lines = [line for line in lines]
fileFromString.close()


#modeled after https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
#sort,trim for year, ethnicity and infant mortality rate
lines.sort()
labels = [line[0] for line in lines[1:]] #create years, remove duplicates
labels = list(set(labels))
label.sort()
#men_means = [20, 34, 30, 35, 27] # need for five ethnicities
asian = []
black =
otherHispanic =


#graph

x = np.arange(len(year))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()


#for loop
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Infant Mortality Rate per 1000 Live Births')
ax.set_title('Infant Morality Rate in NYC 2007-2016')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()

