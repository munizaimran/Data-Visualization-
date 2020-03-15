#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("countries.csv")
plt.rcParams["figure.figsize"] = (10,5)

us = data[data.country == "United States"]
china = data[data.country == "China"]
afgha = data[data.country == "Afghanistan"]
alba = data[data.country == "Albania"]
belg = data[data.country == "Belgium"]
brazil = data[data.country == "Brazil"]
cana = data[data.country == "Canada"]
cuba = data[data.country == "Cuba"]
den = data[data.country == "Denmark"]
egypt = data[data.country == "Egypt"]

plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population/ china.population.iloc[0] * 100)
plt.plot(afgha.year, afgha.population/ afgha.population.iloc[0] * 100)
plt.plot(alba.year, alba.population/ alba.population.iloc[0] * 100)
plt.plot(belg.year, belg.population/belg.population.iloc[0] * 100)
plt.plot(brazil.year, brazil.population/brazil.population.iloc[0] * 100)
plt.plot(cana.year, cana.population/cana.population.iloc[0] * 100)
plt.plot(cuba.year, cuba.population/cuba.population.iloc[0] * 100)
plt.plot(den.year, den.population/den.population.iloc[0] * 100)
plt.plot(egypt.year, egypt.population/ egypt.population.iloc[0] * 100)

plt.title("Year/ Population Comparison of 10 Countries")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend(["US", "China", "Afghanistan", "Albania", "Belgium", "Brazil", "Canada", "Cuba", "Denmark", "Egypt"])
plt.show()


# In[ ]:




