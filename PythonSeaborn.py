import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()

sns.scatterplot(data=tips,x='total_bill',y='tip')

sns.countplot(data=tips,x="size")

sns.barplot(data=tips,x="total_bill",y='smoker')

sns.displot(data=tips,x='smoker')

data = np.random.randint(low=10,high=100,size=(10,10))
hm = sns.heatmap(data,vmin=30,vmax=80)
plt.show()

