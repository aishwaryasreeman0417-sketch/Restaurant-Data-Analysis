#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")


# In[5]:


df = pd.read_csv("Dataset  (1).csv")
df.head()


# In[6]:


df.info()
df.describe()
df.shape
df.columns


# In[4]:


df.isnull().sum()


# In[5]:


df.drop_duplicates(inplace=True)


# In[6]:


top_cuisines = (
    df['Cuisines']
     .dropna()
    .str.split(', ')
    .explode()
    .value_counts()
    .head(3)
)
top_cuisines


# In[7]:


percentage = round((top_cuisines / len(df)) * 100, 2)
percentage


# In[8]:


plt.figure(figsize=(8,5))
top_cuisines.plot(kind='bar', color='skyblue')
plt.title("Top 3 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=0)
plt.show()


# ## Conclusion
# 
# North Indian is the most common cuisine in the dataset, followed by Chinese and Fast Food. These cuisines account for the largest share of restaurants, indicating their popularity among customers.

# In[9]:


city_count = df['City'].value_counts()
city_count.head()


# In[10]:


plt.figure(figsize=(10,6))
city_count.head(10).plot(kind='bar', color='orange')
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.show()


# In[11]:


avg_rating = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False)
avg_rating.head(10)


# ## Conclusion
# 
# New Delhi has the highest number of restaurants in the dataset. The average restaurant ratings vary across cities, highlighting differences in customer satisfaction.

# In[12]:


price = df['Price range'].value_counts().sort_index()
price


# In[13]:


price_percentage = round((price / len(df)) * 100, 2)
price_percentage


# In[14]:


plt.figure(figsize=(7,5))
price.plot(kind='bar', color='green')
plt.title("Distribution of Price Range")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=0)
plt.show()


# ## Conclusion
# 
# Most restaurants belong to Price Range 1, indicating that affordable dining options are more common than premium restaurants.

# In[15]:


online = df['Has Online delivery'].value_counts()
online


# In[16]:


delivery_percentage = round((online / len(df)) * 100, 2)
delivery_percentage


# In[17]:


avg_delivery = df.groupby('Has Online delivery')['Aggregate rating'].mean()
avg_delivery


# In[18]:


plt.figure(figsize=(6,5))
avg_delivery.plot(kind='bar', color=['red', 'blue'])
plt.title("Average Rating by Online Delivery")
plt.xlabel("Online Delivery")
plt.ylabel("Average Rating")
plt.xticks(rotation=0)
plt.show()


# ## Conclusion
# 
# Restaurants offering online delivery generally have higher average ratings than those without online delivery, suggesting that delivery services may contribute to better customer satisfaction.

# # Overall Conclusion
# 
# This project analyzed restaurant data using Python, Pandas, and Matplotlib. Exploratory Data Analysis (EDA) revealed key insights into cuisine popularity, city-wise restaurant distribution, pricing patterns, and online delivery services. The findings demonstrate how data analysis can support business decisions and improve understanding of customer preferences.

# # Level 2 - Task 1: Restaurant Ratings
# ### Objective
# Analyze the distribution of aggregate ratings, determine the most common rating range, and calculate the average number of votes received by restaurants.

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Dataset  (1).csv")   # Use your exact filename
plt.style.use("ggplot")


# In[12]:


plt.figure(figsize=(8,5))
sns.histplot(df['Aggregate rating'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.show()


# In[13]:


rating_range = pd.cut(
    df['Aggregate rating'],
    bins=[0,1,2,3,4,5],
    labels=["0-1","1-2","2-3","3-4","4-5"],
    include_lowest=True
)
common_rating = rating_range.value_counts().sort_index()
print(common_rating)


# In[14]:


average_votes = df["Votes"].mean()
print(f"Average Number of Votes: {average_votes:.2f}")


# In[15]:


top_votes = df.sort_values(by="Votes", ascending=False)[
    ["Restaurant Name", "Votes", "Aggregate rating"]
].head(10)

top_votes


# ## Conclusion
# The distribution of aggregate ratings indicates that most restaurants have moderate to high ratings. The average number of votes provides an overview of customer engagement, while the most-voted restaurants generally represent well-known and popular dining establishments.

# # Task 2: Cuisine Combination
# ### Objective
# Identify the most common combinations of cuisines and analyze whether certain cuisine combinations receive higher ratings.

# In[16]:


cuisine_combination = df["Cuisines"].value_counts().head(10)
print(cuisine_combination)


# In[17]:


plt.figure(figsize=(12,6))

cuisine_combination.plot(kind="bar", color="teal")

plt.title("Top 10 Most Common Cuisine Combinations")
plt.xlabel("Cuisine Combination")
plt.ylabel("Number of Restaurants")

plt.xticks(rotation=45, ha="right")

plt.show()


# In[18]:


average_rating = (
    df.groupby("Cuisines")["Aggregate rating"]
      .mean()
      .sort_values(ascending=False)
)

average_rating.head(10)


# In[19]:


top_rated = average_rating.head(10)

print(top_rated)


# In[20]:


plt.figure(figsize=(12,6))

top_rated.sort_values().plot(kind="barh", color="orange")

plt.title("Top 10 Highest Rated Cuisine Combinations")
plt.xlabel("Average Rating")
plt.ylabel("Cuisine Combination")

plt.show()


# ## Conclusion
# 
# The analysis identified the most popular cuisine combinations served by restaurants. It also showed that some cuisine combinations consistently receive higher customer ratings, indicating stronger customer preference and satisfaction for those combinations.

# In[21]:


pip install folium


# In[22]:


import folium


# In[23]:


restaurant_map = folium.Map(
    location=[df["Latitude"].mean(), df["Longitude"].mean()],
    zoom_start=5
)
restaurant_map


# In[24]:


for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=2,
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.5
    ).add_to(restaurant_map)

restaurant_map


# In[25]:


restaurant_map.save("Restaurant_Locations_Map.html")
print("Map saved successfully!")


# ## Conclusion
# The geographic analysis visualizes restaurant locations using latitude and longitude coordinates. The map shows that restaurants are concentrated in major cities, forming dense clusters in urban areas, while rural and less populated regions have fewer restaurants. This indicates that restaurant businesses are more prevalent in areas with higher population density and customer demand.

# # Task 4: Restaurant Chains
# ### Objective
# Identify restaurant chains in the dataset and analyze their popularity based on the number of outlets, average ratings, and customer votes.

# In[26]:


restaurant_count = df["Restaurant Name"].value_counts()
chains = restaurant_count[restaurant_count > 1]
print("Number of Restaurant Chains:", len(chains))
chains.head(10)


# In[27]:


plt.figure(figsize=(12,6))

chains.head(10).plot(kind="bar", color="steelblue")

plt.title("Top 10 Restaurant Chains by Number of Outlets")
plt.xlabel("Restaurant Chain")
plt.ylabel("Number of Outlets")

plt.xticks(rotation=45, ha="right")

plt.show()


# In[28]:


chain_rating = (
    df.groupby("Restaurant Name")["Aggregate rating"]
      .mean()
)

top_chain_rating = chain_rating.loc[chains.index].sort_values(ascending=False)

top_chain_rating.head(10)


# In[29]:


plt.figure(figsize=(12,6))

top_chain_rating.head(10).sort_values().plot(
    kind="barh",
    color="green"
)

plt.title("Top 10 Highest Rated Restaurant Chains")
plt.xlabel("Average Rating")
plt.ylabel("Restaurant Chain")

plt.show()


# In[30]:


chain_votes = (
    df.groupby("Restaurant Name")["Votes"]
      .mean()
)

top_chain_votes = chain_votes.loc[chains.index].sort_values(ascending=False)

top_chain_votes.head(10)


# In[31]:


plt.figure(figsize=(12,6))

top_chain_votes.head(10).sort_values().plot(
    kind="barh",
    color="orange"
)

plt.title("Top 10 Most Popular Restaurant Chains (Average Votes)")
plt.xlabel("Average Votes")
plt.ylabel("Restaurant Chain")

plt.show()


# ## Conclusion
# The analysis identified several restaurant chains with multiple outlets in the dataset. By comparing their average ratings and customer votes, we observed that some chains maintain consistently high ratings and receive greater customer engagement. This analysis helps identify popular and well-performing restaurant brands.

# In[ ]:




