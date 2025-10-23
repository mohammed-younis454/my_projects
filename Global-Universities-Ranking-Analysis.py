import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("universities_ranking.csv")


# the bar arrangements
top_countries = df[df["year"] == 2015]["country"].value_counts().nlargest(10)
top_countries.index=top_countries.index.to_series().replace({"United Kingdom":"GB","South Korea":"KR","USA":"US","Canada":"CA","Spain":"ES","Japan":"JP","China":"CN","Italy":"IT","France":"FR","Germany":"DE"})

# the pie arrangements
df_2015 = df[df["year"] == 2015]
c_europe=["Albania","Andorra","Austria","Belarus","Belgium","Bosnia and Herzegovina","Bulgaria","Croatia","Cyprus","Czechia","Denmark","Estonia","Finland","France","Germany","Greece","Hungary","Iceland","Ireland","Italy","Kosovo","Latvia","Liechtenstein","Lithuania","Luxembourg","Malta","Moldova","Monaco","Montenegro","Netherlands","North Macedonia","Norway",
"Poland","Portugal","Romania","San Marino","Serbia","Slovakia","Slovenia","Spain","Sweden","Switzerland","Ukraine","United Kingdom","Vatican City"]

c_africa=["Algeria","Angola","Benin","Botswana","Burkina Faso","Burundi","Cabo Verde","Cameroon","Central African Republic",
"Chad","Comoros","Democratic Republic of the Congo","Djibouti","Egypt","Equatorial Guinea","Eritrea","Eswatini","Ethiopia",
"Gabon","Gambia","Ghana","Guinea","Guinea-Bissau","Côte d’Ivoire","Kenya","Lesotho","Liberia","Libya","Madagascar","Malawi",
"Mali","Mauritania","Mauritius","Morocco","Mozambique","Namibia","Niger","Nigeria","Republic of the Congo","Rwanda",
"São Tomé and Príncipe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan","Sudan","Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe"]

c_n_america=["Antigua and Barbuda","Bahamas","Barbados","Belize","Canada","Costa Rica","Cuba","Dominica","Dominican Republic",
"El Salvador","Grenada","Guatemala","Haiti","Honduras","Jamaica","Mexico","Nicaragua","Panama","Saint Kitts and Nevis",
"Saint Lucia","Saint Vincent and the Grenadines","Trinidad and Tobago","USA"]

c_s_america=["Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador","Guyana","Paraguay","Peru","Suriname","Uruguay",
"Venezuela"]

c_asia=["Afghanistan","Armenia","Azerbaijan","Bahrain","Bangladesh","Bhutan","Brunei","Cambodia","China","Cyprus","Georgia",
"India","Indonesia","Iran","Iraq","Japan","Jordan","Kazakhstan","Kuwait","Kyrgyzstan","Laos","Lebanon","Malaysia","Maldives",
"Mongolia","Myanmar","Nepal","North Korea","Oman","Pakistan","Palestine","Philippines","Qatar","Russia","Saudi Arabia","Singapore","South Korea","Sri Lanka","Syria","Taiwan","Tajikistan","Thailand","Timor-Leste","Turkey","Turkmenistan","United Arab Emirates","Uzbekistan","Vietnam","Yemen"]

europe = len(df_2015[df_2015["country"].isin(c_europe)])
africa = len(df_2015[df_2015["country"].isin(c_africa)])
n_america = len(df_2015[df_2015["country"].isin(c_n_america)])
s_america = len(df_2015[df_2015["country"].isin(c_s_america)])
asia = len(df_2015[df_2015["country"].isin(c_asia)])
continent =[europe,africa,n_america,s_america,asia]

# the hist arrangments
bins = [10,20,30,40,50,60,70,80,90,100]

# the line arrangments
mean_score = df.groupby("year")["score"].mean().round(2)


colors = ['#002d00',"#014d01","#026d02","#038d03","#05ad05","#06cd06","#28d928","#55e055","#82e782",
"#aff0af"]

fig , ax = plt.subplots(nrows= 2 , ncols= 2 , figsize=(16,10))
fig.patch.set_facecolor('#F2F2F2')

ax[0,0].bar(top_countries.index,top_countries.values,color=colors)
ax[0,0].set_title("Tob 10 Countries By Number Of Ranked Universities",weight="semibold",fontname="DejaVu Sans",size=11)
ax[0,0].set_xlabel("Counries",weight="bold",fontname="DejaVu Sans",size=10)
ax[0,0].set_ylabel("Number of universities",weight='bold',fontname='DejaVu Sans',size=10)
ax[0,0].tick_params(axis='x', rotation=45)
ax[0,0].patch.set_facecolor('#F2F2F2')
ax[0,0].grid(color=colors[6],alpha=0.5,linestyle="--")
ax[0,0].spines["bottom"].set_color("black")
ax[0,0].spines["left"].set_color("black")
ax[0,0].spines["top"].set_visible(False)
ax[0,0].spines["right"].set_visible(False)

ax[0,1].hist(np.array(df_2015["score"].dropna(), dtype=float),bins=bins,edgecolor="black", color="#026d02")
ax[0,1].set_title("Distribution of Universities Score",weight="semibold",fontname="DejaVu Sans",size=11)
ax[0,1].set_xlabel("Score",weight='bold',fontname='DejaVu Sans',size=10)
ax[0,1].set_ylabel("Number",weight='bold',fontname='DejaVu Sans',size=10)
ax[0,1].patch.set_facecolor('#F2F2F2')
ax[0,1].grid(color=colors[6],alpha=0.5,linestyle="--")
ax[0,1].spines["bottom"].set_color("black")
ax[0,1].spines["left"].set_color("black")
ax[0,1].spines["top"].set_visible(False)
ax[0,1].spines["right"].set_visible(False)

ax[1,0].pie(continent,labels=["Europe","Africa","N_America","S_America","Asia"],colors=['#014d01', '#028d02', '#06cd06', '#55e055', '#aff0af'],autopct="%1.1f%%"
,explode=[0.02 for i in range(len(continent))])
ax[1,0].set_title("Distribution of continents according to the number of universities",weight="semibold",fontname="DejaVu Sans",size=11)
ax[1,0].legend(["Europe","Africa","N_America","S_America","Asia"], loc="upper left", bbox_to_anchor=(1, 0.8))

ax[1,1].plot(mean_score.index,mean_score.values,"g--o")
ax[1,1].set_title("Evolution of the average score over the years",weight="semibold",fontname="DejaVu Sans",size=11)
ax[1,1].set_xlabel("Year",weight="bold",fontname="DejaVu Sans",size=10)
ax[1,1].set_ylabel("Mean_Score",weight='bold',fontname='DejaVu Sans',size=10)
ax[1,1].set_xticks(mean_score.index)
ax[1,1].patch.set_facecolor('#F2F2F2')
ax[1,1].grid(color=colors[6],alpha=0.5,linestyle="--")
ax[1,1].spines["bottom"].set_color("black")
ax[1,1].spines["left"].set_color("black")
ax[1,1].spines["top"].set_visible(False)
ax[1,1].spines["right"].set_visible(False)

plt.suptitle('Global-Universities-Ranking-Analysis',fontname='DejaVu Sans',weight='bold',size=20)
plt.tight_layout(pad=5, w_pad=4, h_pad=5)
plt.subplots_adjust(top=0.88)
# plt.savefig("Global-Universities-Ranking-Analysis.png")
plt.show()

