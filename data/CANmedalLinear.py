
import matplotlib.pyplot as plt
import numpy as np
input_values = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
squares = [9,17,20,13,20,17,19,22,7,20,1,3,2,4,6,36,40,48,75,68,81,90]

plt.plot(input_values,squares,linewidth=2)

x = np.array(input_values)
y = np.array(squares)

for a,b in zip(x,y):
    plt.annotate('(%s,%s)'%(a,b),xy=(a,b),xytext=(-10,20),
                 textcoords='offset points')

plt.title('CANADA each Winter Olympic Games performance from 1896-2014',fontsize=24)
plt.xlabel('year',fontsize=14)
plt.ylabel('Total medal',fontsize=14)

plt.tick_params(axis='both',labelsize=14)

plt.show()