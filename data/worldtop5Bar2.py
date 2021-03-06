
import matplotlib.pyplot as plt
import numpy as np



name_list = ['USA','CAN','NOR','URS','FIN']
num_list = [653,625,457,440,434]
x = np.array(name_list)
y = np.array(num_list)
plt.bar(x,y,width=0.5,align='center',color='c')
plt.xlabel('Top 5 Country',fontsize=14)
plt.ylabel('Number of Medal',fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.axis([-1,5,-1,700])
for a,b in zip(x,y):
    plt.text(a,b+0.1,'%.0f'%b,ha = 'center',va = 'bottom',fontsize=7)
plt.show()