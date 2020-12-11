import numpy as np
import matplotlib.pyplot as plt



plt.rcParams['axes.unicode_minus'] = False  
barWidth = 0.25

bronze = [167,107,127,93,221]
silver = [319,203,171,97,147]
gold = [167,315,159,250,66]


r1 = np.arange(len(bronze))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]



plt.bar(r1, bronze, color='#c05c00', width=barWidth, edgecolor='white', label='bronze')
plt.bar(r2, silver, color='#757171', width=barWidth, edgecolor='white', label='silver')
plt.bar(r3, gold, color='#f8c200', width=barWidth, edgecolor='white', label='gold')


plt.xticks([r + barWidth for r in range(len(bronze))], ['USA','CAN','NOR','URS','FIN'])
plt.title(' Winter Olympic Games all-time medal table Top 5 countries from 1896 to 2014')




plt.legend()

plt.show()

