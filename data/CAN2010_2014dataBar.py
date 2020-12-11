

import numpy as np
import matplotlib.pyplot as plt


medal_names = ['bronze','silver', 'gold']
amount = {
	'2010': [8, 15, 68],
	'2014': [5, 22, 63],

}


def survey(amount, medal_names):
    labels = list(amount.keys())

    data = np.array(list(amount.values()))

    data_cum = data.cumsum(axis=1)

    medal_colors = plt.get_cmap('RdYlGn')(np.linspace(0.15, 0.85, data.shape[1]))




    print(medal_colors)

    fig, ax = plt.subplots(figsize=(5, 9))

    ax.yaxis.set_visible(False)
    ax.set_xticklabels(labels=labels, rotation=90)


    ax.set_ylim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(medal_names, medal_colors)):
        heights = data[:, i]
 
        starts = data_cum[:, i] - heights

        ax.bar(labels, heights, bottom=starts, width=0.5,
                label=colname, color=color)
        xcenters = starts + heights / 2
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, heights)):
            ax.text(y, x, str(int(c)), ha='center', va='center',
                    color=text_color, rotation = 90)
    ax.legend()
    return fig, ax


survey(amount, medal_names)
plt.title("Medal earned by Canada in 2010 and 2014") 
plt.xlabel("year")
plt.ylabel("amount") 
plt.show()




