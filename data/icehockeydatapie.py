


from matplotlib import pyplot as plt

plt.figure(figsize=(6,9)) 
labels = [u'bronze',u'silver',u'gold',u'lose']
sizes = [2,4,9,7] 
colors = ['brown','grey','gold','#d3d3d3'] 
explode = (0,0,0.02,0) 
patches,text1,text2 = plt.pie(sizes,
								explode=explode,
								labels=labels,
								colors=colors,
								labeldistance = 0.8,
								autopct = '%3.2f%%', 
								shadow = False, 
								startangle =90, 
								pctdistance = 0.6) 
plt.axis('equal')
plt.title("How many times that Canada winning medal in Ice Hocky from 1896-2014")
plt.legend()
plt.show()





