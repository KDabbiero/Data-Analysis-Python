import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix_titles.csv')

df_united_states = df.loc[df['country'] == 'United States']

user_input = int(input("What do you want to view?\n1. View average release year.\n2. View how many TV shows/ movies there are on Netflix\n3. What is the most popular rating on Netflix\n4. Stand-Up Comedy specials listed in the United States\n5. Release Year trends."))
#This is for all countries
if user_input == 1:
    #Average release year as a number
    print()
    avg_duration = np.mean(df["release_year"])
    print(avg_duration)
elif user_input == 2:
    #Print the number of Movies/TV Shows and display it in a graph
    netflix_total = df.value_counts("type")
    print(netflix_total) 
    print()
    sns.countplot(data=df, x="type")
    plt.show()
    plt.clf()
elif user_input == 3:
    #Display the most offered ratings 
    print()
    sns.countplot(data=df, x="rating")
    plt.show()
    plt.clf()
elif user_input == 4:
    #List all the stand up comedy specials in the US
    print()
    df_united_states_suc = df_united_states.loc[df_united_states['listed_in'] == 'Stand-Up Comedy']
    print(df_united_states_suc)
else:
    #See the average release year in a graph
    print()
    sns.boxenplot(data=df)
    plt.show()
    plt.clf()

user_input2 = int(input("Most popular genre by country: \n1. Brazil \n2. United Kingdom \n3. United States \n4. India \n5. China \n6. Japan"))

if user_input2 == 1:
# Tests to see the most popular category for each country
# Brazil
    df_brazil = df.loc[df['country'] == 'Brazil']
    print(df_brazil.value_counts('listed_in').head())
elif user_input2 == 2:
# United Kingdom
    df_united_kingdom = df.loc[df['country'] == 'United Kingdom']
    print(df_united_kingdom.value_counts('listed_in').head())
elif user_input2 == 3:
# United States
    df_united_states = df.loc[df['country'] == 'United States']
    print(df_united_states.value_counts('listed_in').head())
elif user_input2 == 4:
# India
    df_india = df.loc[df['country'] == 'India']
    print(df_india.value_counts('listed_in').head())
elif user_input2 == 5:
# China
    df_china = df.loc[df['country'] == 'China']
    print(df_china.value_counts('listed_in').head())
else:
# Japan
    df_japan = df.loc[df['country'] == 'Japan']
    print(df_japan.value_counts('listed_in').head())

user_input3 = int(input("View ratings by country: \n1. Brazil \n2. United Kingdom \n3. United States \n4. India \n5. China \n6. Japan"))

if user_input3 == 1:
    #View the most offered raitng by country
    #Brazil
    df_brazil = df.loc[df['country'] == 'Brazil']
    sns.countplot(data=df_brazil, x='rating', hue='type')
    plt.show()
    plt.clf()
elif user_input3 == 2:
    #United Kingdom
    df_united_kingdom = df.loc[df['country'] == 'United Kingdom']
    sns.countplot(data=df_united_kingdom, x='rating', hue='type')
    plt.show()
    plt.clf()
elif user_input3 == 3:
    #United States
    df_united_states = df.loc[df['country'] == 'United States']
    sns.countplot(data=df_united_states, x='rating', hue='type')
    plt.show()
    plt.clf()
elif user_input3 == 4:
    #India
    df_india = df.loc[df['country'] == 'India']
    sns.countplot(data=df_india, x='rating', hue='type')
    plt.show()
    plt.clf()
elif user_input3 == 5:
    #China
    df_china = df.loc[df['country'] == 'China']
    sns.countplot(data=df_china, x='rating', hue='type')
    plt.show()
    plt.clf()
else:
    #Japan
    df_japan = df.loc[df['country'] == 'Japan']
    sns.countplot(data=df_japan, x='rating', hue='type')
    plt.show()
    plt.clf()