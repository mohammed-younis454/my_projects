import pandas as pd
import matplotlib.pyplot as plt

dfs = pd.read_csv("Kaggle.csv")

# the bar arrangments
dfs=dfs.fillna('None')
dfs.drop(index=0,inplace=True)

q7 = dfs.columns[dfs.columns.str.contains("Q7")]
dic7 = dict()

for col in q7:
    dic7.update(dfs[col].value_counts().to_dict())

df_bar = pd.Series(dic7)
df_bar.drop("None",inplace=True)
df_bar = df_bar.sort_values(ascending=False)

# the pie arrangments
man = dfs["Q2"].value_counts()["Man"]
woman = dfs["Q2"].value_counts()["Woman"]
pie = [man,woman]

# the hist arrangments
dfs["Q6"].replace({"I have never written code" : "never"},inplace=True)

bluec=['#6ee1fa','#65d4ee','#5cc6e3','#54b9d7','#4caccb','#449fbf','#3c93b3','#3586a7','#2d7a96','#266e8f','#1f6282','#175776']

fig , (ax1,ax2,ax3) = plt.subplots(nrows= 1 , ncols= 3 , figsize=(14,5))
fig.patch.set_facecolor('#F2F2F2')

ax1.bar(df_bar.index,df_bar.values,color=bluec)
ax1.set_ylabel("Count",weight='semibold',fontname='monospace',size=20)
ax1.set_xlabel("Programming Languages",weight='semibold',fontname='monospace',size=20)
ax1.tick_params(labelrotation=70,labelsize=15)
ax1.patch.set_facecolor('#F2F2F2')
ax1.grid(color=bluec[3],alpha=0.5,linestyle="--")
ax1.spines["bottom"].set_color("black")
ax1.spines["left"].set_color("black")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

ax2.hist(dfs["Q6"],edgecolor="black", color="#003653")
ax2.tick_params(labelrotation=25,labelsize=10)
ax2.set_ylabel("Count",weight='semibold',fontname='monospace',size=20)
ax2.set_xlabel("Years Of Coding",weight='semibold',fontname='monospace',size=20)
ax2.patch.set_facecolor('#F2F2F2')
ax2.grid(color=bluec[3],alpha=0.5,linestyle="--")
ax2.spines["bottom"].set_color("black")
ax2.spines["left"].set_color("black")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

ax3.pie(pie,labels=["man","woman"],colors=["#1f6282","#4caccb"],autopct="%1.1f%%",explode=[0.04 for i in range(len(pie))])
ax3.legend(["man","woman"], loc="upper left", bbox_to_anchor=(1, 0.8))


plt.suptitle('Information About Kaggle Users',fontname='monospace',weight='bold',size=30)
plt.subplots_adjust(bottom=0.35)

plt.show()