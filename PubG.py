#!/usr/bin/env python
# coding: utf-8

# In[14]:


## Importing all the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


## Importing Data and creating a dataframe
df = pd.read_csv(r"C:\Users\pxj190011\Desktop\Projects\pubg-match-deaths\aggregate\agg_match_stats_0.csv")


# In[3]:


## Head of the dataset
df.head


# In[5]:


## Variable names
df.info()


# In[6]:


## Summary Statistic of the dataset
df.describe()


# In[7]:


#Assigning Values
df.loc[df['player_dist_ride'] == 0, 'Walk&Ride'] = 0
df.loc[df['player_dist_ride'] > 0, 'Walk&Ride'] = 1
df.loc[df['game_size'] <33, 'Match_duration'] = 1
df.loc[df['game_size'] >=33, 'Match_duration'] = 2
df.loc[df['game_size'] >66, 'Match_duration'] = 3
df.loc[df['player_survive_time'] >1000, 'churn'] = 0
df.loc[df['player_survive_time'] <=1000, 'churn'] = 1
df.player_survive_time = df.player_survive_time.round()
    


# In[8]:


#Bar graph for Walk and Walk&Ride
df['Walk&Ride'].value_counts()[:20].plot(kind='bar', color='red')
plt.xlabel('Walk and Walk and Ride')


# In[9]:


#Bar graph for Small, Medium, Large
df['Match_duration'].value_counts()[:20].plot(kind='bar', color='blue')
plt.xlabel('Small, Medium, Large')


# In[10]:


#Bar graph for no. in squads
df['party_size'].value_counts()[:20].plot(kind='bar', color='blue')

