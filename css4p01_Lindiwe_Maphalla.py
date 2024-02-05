# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:39:42 2024

@author: lindiwe Maphalla
"""
# QUESTION 1 cleaning the data
import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df)
print(df.info())
df.dropna(inplace = True)
df = df.reset_index(drop=True)
print(df)
print(df.info())

movie_dataset = df
  
# This code filters the DataFrame to include only rows where the 'Rating' column is equal to the maximum rating in the dataset, and then it prints the title and rating of the highest-rated movie.

import pandas as pd

#Highest rated movie from the filtered data
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]

print("Highest-rated movie:")
print(highest_rated_movie[['Title', 'Rating']])

# df=DataFrame/movie_dataset


# QUESTION 2

average_revenue = df['Revenue (Millions)'].mean()

print("Average Revenue of All Movies: ${:,.2f}".format(average_revenue))


# QUESTION 3

# Convert the 'Year' column to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Filtering the DataFrame for movies released from 2015 to 2017
filtered_df = df[(df['Year'] >= '2015-01-01') & (df['Year'] <= '2017-12-31')]

# Calculating the average revenue of movies from 2015 to 2017
average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

print(f"The average revenue of movies from 2015 to 2017 is {average_revenue_2015_to_2017:.2f} million dollars.")


# QUESTION 4
import pandas as pd
#filtering the data of movies released in 2016

movies_2016 = (df['Year'] == 2016).sum()
print(movies_2016)


# QUESTION 5
import pandas as pd

#Filtering movies directed by Christopher Nolan
movies_by_Christopher_Nolan=(df['Director']== 'Christopher Nolan').sum()

#movies directed by Christopher Nolan
print(movies_by_Christopher_Nolan)

# QUESTION 6

import pandas as pd

# Filtering the dataFrame for movies with a rating of at least 8.0
movies_8= (df['Rating'] >= 8.0).sum()

#Movies with 8.0 rationg
print(movies_8)


# QUESTION 7

import pandas as pd

# Filtering the dataFrame for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()

print(f"The median rating of movies directed by Christopher Nolan is {median_rating_nolan_movies}.")

# QUESTION 8

import pandas as pd

# Calculating the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}.")

# QUESTION 9

import pandas as pd

# Filtering the dataFrame for movies made in 2006 and 2016
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

#the number of movies made in each year
count_2006 = len(movies_2006)
count_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((count_2016 - count_2006) / count_2006) * 100

print(f"The percentage increase in the number of movies made between 2006 and 2016 is {percentage_increase:.2f}%.")


# QUESTION 10

import pandas as pd


# Spliting the multiple actors in the "Actors" column and creating a new DataFrame
actors_df = df['Actors'].str.split(', ', expand=True)

# Restructuring the dataFrame to have one column for each actor
actors_list = actors_df.values.flatten()

#Count the occurrences of each actor
actors_count = pd.Series(actors_list).value_counts()

# Get the most common actor
most_common_actor = actors_count.idxmax()

print(f"The most common actor in all the movies is: {most_common_actor}")


# QUESTION 11

import pandas as pd

# Spliting the genres in the "Genre" column and create a new dataFrame
genres_df = df['Genre'].str.split(', ', expand=True)

# Restructuring the dataFrame to have one column for each genre
genres_list = genres_df.values.flatten()

# Get the number of unique genres
unique_genres_count = len(set(genres_list))

# Display the result
print(f"The number of unique genres in the dataset is: {unique_genres_count}")
















