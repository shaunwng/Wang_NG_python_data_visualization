# import matplotlib.pyplot as plt
# import matplotlib as mpl

# mpl.rcParams["axes.unicode_minus"] = False

# x = [1]
# y = [2]
# y1 = [4]
# y2 = [9]

# plt.bar(x, y, align="center", color="#c05c00", tick_label=["CAN"], label="bronze")
# plt.bar(x, y1, align="center", bottom=y, color="#757171", label="silver")
# plt.bar(x, y2, align="center", bottom=y1, color="#f8c200", label="gold")

# plt.xlabel("1896-2014")
# plt.ylabel("times")

# plt.legend()

# plt.show()


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




# matplotlib.rcParams['axes.unicode_minus'] = False

# medal = [9,4,2]

# plt.barh(range(3), medal, height=0.7, color='steelblue', alpha=0.8)     
# plt.yticks(range(3), ['gold', 'silver', 'bronze'])
# plt.xlim(0,20)
# plt.xlabel("times")
# plt.title("How many times that Canada winning medal in Ice Hocky from 1896-2014 ")
# for x, y in enumerate(medal):
#     plt.text(y + 0.2, x - 0.1, '%s' % y)
# plt.show()
