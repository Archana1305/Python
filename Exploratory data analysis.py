#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


#loading the datasets

athletes = pd.read_csv('C:/Users/19808/Desktop/datasets/athlete_events.csv')
regions = pd.read_csv('C:/Users/19808/Desktop/datasets/noc_regions.csv')


# In[7]:


athletes.head()


# In[8]:


regions.head()


# In[11]:


#joining the dataframes

athletes_df = athletes.merge(regions, how = 'left', on = 'NOC')
athletes_df.head()


# In[13]:


#shape of the dataframe
athletes_df.shape


# In[15]:


# to make the column names consistent
athletes_df.rename(columns={'region':'Region','notes':'Notes'}, inplace=True)


# In[16]:


athletes_df.head()


# In[17]:


athletes_df.info()


# In[18]:


athletes_df.describe()


# In[19]:


#checking for null values
null_values=athletes_df.isnull()
null_columns=null_values.any()
null_columns


# In[20]:


athletes_df.isnull().sum()


# In[23]:


# competitors from India
athletes_df.query('Team=="India"').head(5)


# In[24]:


# competitors from Japan
athletes_df.query('Team=="Japan"').head(5)


# In[28]:


#Top 10 countries participating

top_10_countries = athletes_df.Team.value_counts().sort_values(ascending = False).head(10)
top_10_countries


# In[33]:


# Plot for the top 10 countries
#Set 2 is a coclor palatte
plt.figure(figsize=(12,6))
plt.title('Overall Participation by Country')
sns.barplot(x=top_10_countries.index, y=top_10_countries,palette = 'Set2');


# In[35]:


# Age distribution of the participants

plt.figure(figsize=(12,6))
plt.title("Age distribution of the Athletes")
plt.xlabel('Age')
plt.ylabel('Number of Participants')
plt.hist(athletes_df.Age, bins= np.arange(10,80,2), color='orange',edgecolor='white');


# In[36]:


#Winter sports
winter_sports = athletes_df[athletes_df.Season == 'Winter'].Sport.unique()
winter_sports


# In[37]:


#summer sports
summer_sports = athletes_df[athletes_df.Season == 'Summer'].Sport.unique()
summer_sports


# In[38]:


#gender of the participants from the beginning
gender_counts = athletes_df.Sex.value_counts()
gender_counts


# In[44]:


#pie plot for the gender distribution

plt.figure(figsize=(12,6))
plt.title('Gender Distribution')
plt.pie(gender_counts, labels= gender_counts.index, autopct='%1.1f%%', startangle=180)


# In[45]:


#Total number of medals for the athletes
athletes_df.Medal.value_counts()


# In[49]:


#Total number of women in each olympics
women_in_sports = athletes_df[(athletes_df.Sex=='F')&(athletes_df.Season=='Summer')][['Sex','Year']]
women_in_sports = women_in_sports.groupby('Year').count().reset_index()
women_in_sports.tail()


# In[50]:


womenOlympics = athletes_df[(athletes_df.Sex == 'F')&(athletes_df.Season=='Summer')]


# In[51]:


sns.set(style='darkgrid')
plt.figure(figsize=(20,10))
sns.countplot(x='Year',data=womenOlympics, palette="Spectral")
plt.title('Women Participation')


# In[52]:


part=womenOlympics.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(20,10))
part.loc[:,'F'].plot()
plt.title('Plot of Women Athletes over time')


# In[54]:


#Gold medal winners
goldMedals= athletes_df[(athletes_df.Medal=='Gold')]
goldMedals.head()


# In[55]:


goldMedals = goldMedals[np.isfinite(goldMedals['Age'])]


# In[58]:


goldMedals['ID'][goldMedals['Age']>60].count()


# In[61]:


sporting_event=goldMedals['Sport'][goldMedals['Age']>60]
sporting_event


# In[62]:


plt.figure(figsize=(10,5))
plt.tight_layout()
sns.countplot(sporting_event)
plt.title('Gold Medals for Athletes over 60 years')


# In[63]:


#Gold Medals for each country
goldMedals.Region.value_counts().reset_index(name='Medal').head(5)


# In[67]:


totalGoldMedals = goldMedals.Region.value_counts().reset_index(name='Medal').head(6)
g=sns.catplot(x='index', y='Medal', data=totalGoldMedals, height=5, kind='bar', palette='rocket')
g.despine(left=True)
g.set_xlabels("Top 5 countries")
g.set_ylabels("Number of Medals")
plt.title('Gold Medals per country')


# In[71]:


# Rio Olympics

max_year=athletes_df.Year.max()
print(max_year)

team_names=athletes_df[(athletes_df.Year == max_year) & (athletes_df.Medal == 'Gold')].Team
team_names.value_counts().head(10)


# In[74]:


sns.barplot(x=team_names.value_counts().head(20), y=team_names.value_counts().head(20).index)

plt.ylabel(None);
plt.xlabel('Countrywise Medals for the year 2016');


# In[75]:


not_null_medals=athletes_df[(athletes_df['Height'].notnull()) & (athletes_df['Weight'].notnull())]


# In[76]:


plt.figure(figsize = (12,10))
axis = sns.scatterplot(x='Height', y='Weight', data=not_null_medals, hue='Sex')
plt.title('Height vs Weight of Olympics Medalists')


# In[ ]:




