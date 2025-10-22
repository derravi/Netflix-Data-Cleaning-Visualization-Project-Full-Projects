import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read the csv file
print("Lets See some Data of Dataset.\n")
df = pd.read_csv("netflix.csv")
df.head()

#Find how many number of the Row and Columns are there.
print(f"The Total Columns is {df.shape[1]} and total rows is {df.shape[0]}.")

#See the data types of the DataFrame
print("Let see the Data Types of the all Columns.\n")
df.dtypes

#Let`s Describe and see the min,max,mean,std,...etc for this DataFrame
print("Lets Describe all the Columns of the Dataset.\n")
df.describe(include='all')

#Lets see how many Null values are present into this Dataframe.
print("Let see how many Null values is present into this dataset.\n")
df.isnull().sum()

#Lets Remove the Null Values from this DataFrames.
print("We are removing the null values\n")

#Remove the Null Values from the director Columns.
temp = ['director','cast','country','date_added','rating','duration']

for i in temp:
    df[i].fillna(df[i].mode()[0],inplace=True)

# df['director'].fillna(df['director'].mode()[0],inplace=True)
# df['cast'].fillna(df['cast'].mode()[0],inplace=True)
# df['country'].fillna(df['country'].mode()[0],inplace=True)
# df['date_added'].fillna(df['date_added'].mode()[0],inplace=True)
# df['rating'].fillna(df['rating'].mode()[0],inplace=True)
# df['duration'].fillna(df['duration'].mode()[0],inplace=True)

#Lets check any null values is present or not.
print("Lets Recheck the Null values is present or not.\n")
df.isnull().sum()

#Now we are Check theOutliers and remove the Outliers from this datasets.
#Using the IQR Methods.
import seaborn as sns

#let see the Outliers
print("Lets see the Outliers is present or not into release_year\n")
plt.figure(figsize=(15,5))
sns.boxplot(x="release_year", data=df)
plt.show()

#First we are see the how many rows and columns is there into this datasets.

df.shape

#Now we are use the IQR method for removing the Outliers.
print("Lets Apply the IQR Method for removing the Outliers.\n")
q1 = df['release_year'].quantile(0.25)
q3 = df['release_year'].quantile(0.75)


IQR = q3-q1

min_range = q1 - (IQR*1.5)
max_range = q3 - (IQR*1.5)

print("Minimum Range is:",min_range)
print("Maxximum Range is:",max_range)

new_dataset = df[df['release_year'] <= max_range]

print(f"Agter the Removing a OutLiers The Total Columns is {df.shape[1]} and total rows is {df.shape[0]}.")
new_dataset.shape
new_data = df.drop_duplicates()
new_data.head()
#Lets again check the how many data are cleaned.

df.shape

#Lets see the Differen different Diagrams for this Datasets

#Distribution of Movies and TV Shows on Netflix

type_count = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index, type_count.values, color =['Green','Yellow'], label=['Movie','Count'])
plt.title("Movie VS TV_Show Data")
plt.xlabel('Type')
plt.ylabel('Count')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('TV_Vs_Movie_Show.png',dpi=300, bbox_inches='tight')
plt.show()

#Pie Chart of the Rating Of the Movies.

rating_count = df['rating'].value_counts()

plt.figure(figsize=(8,6))
plt.pie(rating_count.values, labels=rating_count.index, autopct='%1.1f%%', startangle=90)
plt.title("Rating Count OF the Movie")
plt.tight_layout()
plt.savefig('Rating_of_Movies.png', dpi= 300, bbox_inches='tight')
plt.show()

#Release year Scatter plot diagrams

release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_count.index, release_count.values,color='purple',label='Release Year VS Movis Count')
plt.xlabel("Movie")
plt.ylabel("Cout")
plt.title("Release Year VS Movis Count")
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('Release_Year_VS_Movis.png', dpi=300, bbox_inches='tight')
plt.show()

#Top 10 Country by number of Movie (horizontal Bar graph)

country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index, country_count.values, color = 'skyblue', label='Top 10 country by number of Movies')
plt.xlabel("Number of shows")
plt.ylabel("Number of country")
plt.title("Top 10 country by number of Movies")
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('Top_10_country_by_number_of_Movies.png', dpi=300, bbox_inches='tight')
plt.show()

#Yearly Trend of Movies vs TV Shows Released


content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2, figsize=(12,5))

#Plot for the Movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='orange')
ax[0].set_title("Movies released per year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Movies")

#plot for thr TV Shows
ax[1].plot(content_by_year.index, content_by_year["TV Show"], color='brown')
ax[1].set_title("TV Show released per year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("TV Show")

plt.suptitle('Comparision TV Show vs Movie released per year.')
plt.tight_layout()
plt.savefig("Movie and TV show.png", dpi=300, bbox_inches='tight')
plt.show()