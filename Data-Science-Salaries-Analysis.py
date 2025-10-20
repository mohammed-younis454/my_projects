import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ds_salaries.csv")

# the bar arrangments
h_j_s = df.groupby("job_title")["salary_in_usd"].mean().round().nlargest(10)
h_j_s.index = h_j_s.index.to_series().replace({
    "Data Analytics Lead": "D_A Lead",
    "Principal Data Engineer": "Principal D_E",
    "Financial Data Analyst": "Financial D_A",
    "Principal Data Scientist": "Principal D_S",
    "Director of Data Science": "Director of D_S",
    "Data Architect": "D_Architect",
    "Applied Data Scientist": "Applied D_S",
    "Analytics Engineer": "A_Engineer",
    "Data Specialist": "D_Specialist",
    "Head of Data": "Head_of_D"
})

# the hist arrangments
bins = [50000,100000,150000,200000,250000,300000,350000,400000,450000]

# the pie arrangments
df["company_size"] = df["company_size"].replace({"L":"Large","M":"Medium","S":"Small"})
large = df["company_size"].value_counts()["Large"]
medium = df["company_size"].value_counts()["Medium"]
small = df["company_size"].value_counts()["Small"]
com_size = [large,medium,small]

colors = [ '#2a0450', '#360664', '#420878', '#4e0b8c', '#5a0da0', '#6610b3', '#7b2bbf', '#9149cc', '#a667d9', '#bb85e6']

fig , (ax1,ax2,ax3) = plt.subplots(nrows= 1 , ncols= 3 , figsize=(14,5))
fig.patch.set_facecolor('#F2F2F2')

ax1.bar(h_j_s.index,h_j_s.values,color=colors)
ax1.set_title("Tob 10 Jobs By Average Salaries",weight="semibold",fontname="monospace",size=12)
ax1.set_xlabel("Jobs",weight="semibold",fontname="monospace",size=20)
ax1.set_ylabel("Salaries",weight='semibold',fontname='monospace',size=20)
ax1.set_xticklabels(h_j_s.index, rotation=45)
ax1.patch.set_facecolor('#F2F2F2')
ax1.grid(color=colors[6],alpha=0.5,linestyle="--")
ax1.spines["bottom"].set_color("black")
ax1.spines["left"].set_color("black")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

ax2.hist(np.array(df["salary_in_usd"].dropna(), dtype=float),bins=bins,edgecolor="black", color="#420878")
ax2.tick_params(axis='x', rotation=25, labelsize=10)
ax2.set_title("Salary Distribution In Dollars",weight="semibold",fontname="monospace",size=12)
ax2.set_xlabel("Salaris in dollars",weight='semibold',fontname='monospace',size=20)
ax2.set_ylabel("Count",weight='semibold',fontname='monospace',size=20)
ax2.patch.set_facecolor('#F2F2F2')
ax2.grid(color=colors[6],alpha=0.5,linestyle="--")
ax2.spines["bottom"].set_color("black")
ax2.spines["left"].set_color("black")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

ax3.pie(com_size,labels=["large","medium","small"],colors=["#4e0b8c","#7b2bbf","#bb85e6"],autopct="%1.1f%%"
,explode=[0.02 for i in range(len(com_size))])
ax3.set_title("Distribution of company sizes",weight="semibold",fontname="monospace",size=12)
ax3.legend(["large","medium","small"], loc="upper left", bbox_to_anchor=(1, 0.8))

plt.suptitle('Data-Science-Salaries-Analysis',fontname='monospace',weight='bold',size=30)
plt.tight_layout()
plt.subplots_adjust(bottom=0.35)
plt.show()