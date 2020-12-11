import matplotlib.pyplot as plt


values = [44,37] 
labels = ['Women','Men'] 
colors = ['green', 'gold']
explode=(0.05,0.05)

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.pie(values, labels=labels, autopct=make_autopct(values),colors=colors,explode=explode,
	wedgeprops = {'linewidth': 1.5, 'edgecolor':'orange'})
plt.title('The proportion of medal won between Men and Women in 2010')
plt.show()
