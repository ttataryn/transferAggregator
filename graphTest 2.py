import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from matplotlib.dates import date2num
import numpy as np


# Mark Ogden = 104 out of 1036
# Simon Stone = 106 out of 1857
# John Cross = 262 out of 1461
# David Ornstein = 87 out of 112
# John Percy = 57 out of 174
# Duncan Castles = 47 + out of 1231
# Ed Aarons = 109 out of 961
# Lyall Thomas = 88 out of 1417
# Paul Joyce = 30 out of 193
# James Ducker = 84 out of 561
# Keith Downie = 55out of 839

reporterNames = ['David Ornstein', 'John Percy', 'Paul Joyce','James Ducker']
width = 0.8
numTweets = [112, 174, 193, 561]
numRumors = [87, 57, 30, 84]
indices = np.arange(len(numTweets))

ax = plt.subplot()
rects= ax.bar(indices, numTweets, width=width, 
        color='b', label='Total Number of Tweets')
rects= ax.bar([i+.0001*width for i in indices], numRumors, 
        width=width, color='red', alpha=0.6, label='Number of Rumors')

labels = ['77.67%','32.76%','15.54%','14.97%']

plt.xticks(indices+width/5., 
           [reporterNames[i] for i in range(len(numTweets))], rotation = "vertical" )

for rect, label in zip(rects, labels):
	if label == '77.67%':
		height = rect.get_height()
		ax.text(rect.get_x() + rect.get_width() / 2, height - 25, label,
            ha='center', va='bottom', color="white")
	else:
		height = rect.get_height()
		ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom', color="white")
plt.legend()
plt.title("Number of Rumors vs Total Number of Tweets by Reporter")

plt.show()




#---------------------------- Days vs Num Transfers -----------------------------------------
# dayOfTransferDict = {"Tues": 28, "Thu": 18, "Fri": 32, "Sat":12,"Sun":7,"Wed":28,"Mon": 25}
# plt.bar(range(len(dayOfTransferDict)), dayOfTransferDict.values(), color ="blue")
# plt.xticks(range(len(dayOfTransferDict)), list(dayOfTransferDict.keys()))
# plt.xlabel("Day of Transfer", fontsize=16)  
# plt.ylabel("Count", fontsize=16)  
# plt.show()