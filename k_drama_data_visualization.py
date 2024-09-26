# -*- coding: utf-8 -*-
"""K-Drama Data Visualization

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tSgmaYMpApZvY4ACx33wmDfwUrRatNB9

# **LATAR BELAKANG**

---
Drama Korea diterima dengan baik tidak hanya oleh orang Korea tetapi juga oleh orang-orang di seluruh dunia, berkat beragam tema dan elemen menarik yang dihadirkan. Selain konten drama itu sendiri, berbagai faktor seperti sutradara, penyiar, dan jadwal tayang juga memainkan peran penting dalam kesuksesan sebuah drama. Analisis ini menggunakan data dari berbagai drama Korea terkenal untuk melakukan eksplorasi elemen-elemen yang berkontribusi pada popularitas mereka. Seperti yang disebutkan sebelumnya, drama Korea menerima banyak perhatian dan cinta dari seluruh dunia. Mempertimbangkan hasil analisis data, lebih mudah untuk memahami karakteristik drama Korea, dan hasil yang lebih baik dapat diperoleh dengan merujuknya ke produksi drama.

# **Contents**

---
1. Released Year and Aired On
2. Number of Episode Distribution
3. Distribution of Korean Drama on different Networks
4. Kdrama Duration Distribution
5. Korean Drama relased by Year and Content Rating
6. Genre Distribution and Top 10 Cast Distribution
7. Drama Rating
8. Actors and Actresses in the Drama
9. Korean Drama Recommendation System

# **IMPORTING LIBRARIES**
"""

import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

"""# **Loading Dataset**"""

df = pd.read_csv('kdrama.csv', header=0)
df.head()

"""# **EXPLORATORY DATA ANALYSIS**"""

df.info()

df.shape

df.columns

df.isnull().sum()

"""# **Data Visualization**

**Released Year and Aired On**

---
"""

kdrama_grouped = df.groupby('Year of release').size().reset_index(name='Count')
plt.figure(figsize=(10, 5))
sns.set(style="whitegrid")
barplot = sns.barplot(data=kdrama_grouped, x='Year of release', y='Count', palette="summer_r")
for bar in barplot.patches:
    bar_height = bar.get_height()  # Get the height of the bar
    bar_x = bar.get_x() + bar.get_width() / 2  # Get the x position of the bar
    bar_y = bar_height  # y position to place the text
    plt.text(bar_x, bar_y, int(bar_height), ha='center', va='bottom', fontsize=10)
plt.title('Korean Drama Released by Year', fontsize=16, fontweight='bold')
plt.xlabel('Year of Release', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

import plotly.express as px
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objects as go
fig = px.bar(data_frame = df.groupby(['Year of release','Aired On']).size().reset_index().rename(columns = {0:'Count'}),
             x = 'Year of release',
             y = 'Count',
             color = 'Aired On',
             barmode = 'stack',
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_layout(title = {'text':'Korean Drama relased by Year and Aired On',
                           'y' : 0.95,
                           'x' : 0.45,
                           'xanchor' : 'center',
                           'yanchor' : 'top',
                           'font_family': 'Gravity One, monospace',
                           'font_color' :'black',
                           'font_size': 20},
                  legend_title = 'Aired On (day of week)',
                  font = dict(family = 'Courier New, monospace',
                              size = 15,
                              color = 'midnightblue'
                  ))

fig.show()

"""**Number of episodes**

---


"""

df['Number of Episodes'].value_counts()

episodes_count = df['Number of Episodes'].value_counts().sort_values(ascending=False)
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x=episodes_count.index, y=episodes_count.values, palette="winter")
plt.xticks(rotation=90)
plt.xlabel("Num Ep", fontsize=10)
plt.ylabel("Count", fontsize=10)
plt.title("Number of Episode Distribution", fontsize=14)
plt.tight_layout()
plt.show()

"""**Original Network**

---


"""

df['Original Network'].value_counts()

# Counting individual network
from collections import Counter

network_list = []
for networks in df['Original Network'] .to_list():
    networks = networks.strip().split(", ")
    for network in networks:
        network_list.append(network)

network_df = pd.DataFrame.from_dict(Counter(network_list),orient='index').rename(columns={0:'Count'})
network_df.sort_values(by='Count',ascending = False,inplace = True)
network_df

plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.barplot(x=network_df.index, y='Count', data=network_df)
plt.title("Distribution of Korean Drama on Different Networks", fontsize=16)
plt.xlabel("Network", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()

"""**Duration of each episode**

---


"""

duration_count = df['Duration'].value_counts().sort_values(ascending=False)
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x=duration_count.index, y=duration_count.values, palette="coolwarm")
plt.xticks(rotation=90)
plt.xlabel("Num Ep", fontsize=10)
plt.ylabel("Count", fontsize=10)
plt.title("Kdrama Duration Distribution", fontsize=14)
plt.tight_layout()
plt.show()

"""**Content Rating**

---


"""

content_rating = df['Content Rating'].value_counts().sort_values(ascending=False)
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x=content_rating .index, y=content_rating .values, palette="magma")
plt.xticks(rotation=45)
plt.xlabel("Con Rate", fontsize=10)
plt.ylabel("Count", fontsize=10)
plt.title("Content Rating", fontsize=14)
plt.tight_layout()
plt.show()

# Content Rating by year
fig = px.bar(data_frame = df.groupby(['Year of release','Content Rating']).size().reset_index().rename(columns = {0:'Count'}),
             x = 'Year of release',
             y = 'Count',
             color = 'Content Rating',
             barmode = 'stack',
             color_discrete_sequence=px.colors.qualitative.Pastel_r)

fig.update_layout(title = {'text':'Korean Drama relased by Year and Content Rating',
                           'y' : 0.95,
                           'x' : 0.45,
                           'xanchor' : 'center',
                           'yanchor' : 'top',
                           'font_family': 'Gravity One, monospace',
                           'font_color' :'black',
                           'font_size': 20},
                  legend_title = 'Content Rating 🤭🔥',
                  font = dict(family = 'Courier New, monospace',
                              size = 15,
                              color = 'midnightblue'
                  ))

fig.show()

"""**Genres**

---


"""

df['Genre'].value_counts()

# Counting individual genre
from collections import Counter

genre_list = []
for genre in df['Genre'] .to_list():
    genre = genre.strip().split(", ")
    for genre in genre:
        genre_list.append(genre)

genre_df = pd.DataFrame.from_dict(Counter(genre_list),orient='index').rename(columns={0:'Count'})
genre_df.sort_values(by='Count',ascending = False,inplace = True)
genre_df

plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")
barplot = sns.barplot(x=genre_df.index, y='Count', data=genre_df, palette="Set2")
plt.title('Genre Distribution', fontsize=20, fontweight='bold')
plt.xlabel('Genre', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Individuals Tags
tags_list = list()

for tags in df['Tags'].to_list():
    tags = tags.split(", ")
    for tag in tags:
        tags_list.append(tag)

tags_df = pd.DataFrame.from_dict(Counter(tags_list), orient = 'index').rename(columns = {0:'Count'})
tags_df.sort_values(by='Count',ascending = False, inplace = True)
tags_df.head()

# Ambil 10 baris pertama dari DataFrame
top_tags = tags_df.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_tags.index, top_tags['Count'])
plt.title('Top 10 Cast Distribution')
plt.xlabel('tags')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

"""**Drama Rating**

---


"""

# Max and Min Rating in the Top 100 Korean Drama
df['Rating'].max(), df['Rating'].min()

# Best Drama Rating
df[df['Rating'] == df['Rating'].max()]

df[df['Rating'] == df['Rating'].min()].head()

"""**Actors and Actresses in the Drama**

---


"""

cast_list = list()

for casts in df['Cast'].to_list():
    casts = casts.split(", ")
    for a in casts:
        cast_list.append(a)

cast_df = pd.DataFrame.from_dict(Counter(cast_list),orient = 'index').rename(columns = {0:'Appearance'})
cast_df.sort_values(by='Appearance',ascending = False,inplace = True)
cast_df.head()

# Ambil 10 baris pertama dari DataFrame
top_cast = cast_df.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_cast.index, top_cast['Appearance'])
plt.title('Top 10 Cast Distribution')
plt.xlabel('Cast')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

"""**Korean Drama Recommendation System**

---


"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

features = ['Duration','Synopsis','Cast','Genre','Tags']
df['Number of Episodes'] = df['Number of Episodes'].astype(str)

df['combined_features'] = df['Synopsis'] + " " + df['Genre'] + " " + df['Tags']

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(count_matrix)

# Function for movie recommendation
def df_recommendation(mov,sim_num = 5):

    user_choice = mov

    try:
        ref_index = df[df['Name'].str.contains(user_choice, case = False)].index[0]

        similar_movies = list(enumerate(cosine_sim[ref_index]))

        sorted_simmilar_movies = sorted(similar_movies, key = lambda x: x[1], reverse = True)[1:]

        print('\nRecomended K Drama for [{}]'.format(user_choice))
        print('-'*(24 + len(user_choice)))

        for i, element in enumerate(sorted_simmilar_movies):
            similar_movie_id = element[0]
            similar_movie_title = df['Name'].iloc[similar_movie_id]
            s_score = element[1]
            print('{:40} -> {:.3f}'.format(similar_movie_title, s_score))

            if i > sim_num:
                break
    except IndexError:
        print("\n[{}] is not in our database!".format(user_choice))
        print("We couldn't recommend anyting...Sorry...")

# Search for movie with the keyword
def df_available(key):

    keyword = key

    print("Movie with keyword: [{}]".format(keyword))

    for i, mov in enumerate(df[df['Name'].str.contains(keyword)]['Name'].to_list()):
        print("{}) {} ".format(i+1,mov))

df_available('It')

df_recommendation("It's Okay to Not Be Okay")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

tfdif_vector = TfidfVectorizer(stop_words = 'english')

tfidf_matrix = tfdif_vector.fit_transform(df['Synopsis'])

sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

indicies = pd.Series(df.index, index = df['Name']).drop_duplicates()

def content_based_recommender(title, sim_scores = sim_matrix):
    idx = indicies[title]

    sim_scores = list(enumerate(sim_matrix[idx]))

    sim_scores = sorted(sim_scores, key = lambda x : x[1], reverse = True)

    sim_scores = sim_scores[1:11]

    drama_score = list()
    for score in sim_scores:
        drama_score.append(score[1])

    kdrama_indices = [i[0] for i in sim_scores]

    kdrama_name = df['Name'].iloc[kdrama_indices]

    print('\nRecomended KDrama for [{}]'.format(title))
    print('-'*(24 + len(title)))
    for score,name in list(zip(drama_score,kdrama_name)):
        print("{:30} -> {:.3f}".format(name,score))

content_based_recommender("It's Okay to Not Be Okay")

# nltk
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

VERB_CODES = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

def preprocess_sentences(text):
    text = text.lower()
    temp_sent =[]
    words = nltk.word_tokenize(text)
    tags = nltk.pos_tag(words)
    for i, word in enumerate(words):
        if tags[i][1] in VERB_CODES:
              lemmatized = lemmatizer.lemmatize(word, 'v')
        else:
              lemmatized = lemmatizer.lemmatize(word)
        if lemmatized not in stop_words and lemmatized.isalpha():
              temp_sent.append(lemmatized)

    finalsent = ' '.join(temp_sent)
    finalsent = finalsent.replace("n't", " not")
    finalsent = finalsent.replace("'m", " am")
    finalsent = finalsent.replace("'s", " is")
    finalsent = finalsent.replace("'re", " are")
    finalsent = finalsent.replace("'ll", " will")
    finalsent = finalsent.replace("'ve", " have")
    finalsent = finalsent.replace("'d", " would")
    return finalsent

df_copy = df.copy()
df_copy['synopsis_processed'] = df_copy['Synopsis'].apply(preprocess_sentences)
df_copy['synopsis_processed'].head()

tfdifvec = TfidfVectorizer()
tfdif_drama_processed = tfdifvec.fit_transform((df_copy['synopsis_processed']))

co_sin_drama = cosine_similarity(tfdif_drama_processed,tfdif_drama_processed)

# Storing indices of the data
indices = pd.Series(df_copy['Name'])

def recommendations(title, cosine_sim = co_sin_drama):
    recommended_movies = []
    index = indices[indices == title].index[0]
    similarity_scores = pd.Series(cosine_sim[index]).sort_values(ascending = False)
    top_10_movies = list(similarity_scores.iloc[1:11].index)
    for i in top_10_movies:
        recommended_movies.append(list(df_copy['Name'].index)[i])

    for index in recommended_movies:
        print(df_copy.iloc[index]['Name'])

recommendations("It's Okay to Not Be Okay")

"""# **Results and Conclusions**

---

**Results:**

- Drama Korea dengan jumlah rilis terbanyak di tahun 2021.
- Jumlah episode terbanyak pada drama Korea umumnya adalah 16 episode.
- Distribusi Drama Korea di berbagai jaringan televisi paling dominan ada di TVN.
- Durasi episode drama Korea yang paling umum adalah 1 jam 10 menit.
- Genre yang paling populer adalah romance.
- Drama dengan rating tertinggi adalah **Move to Heaven** dengan nilai 9,2.

**Conclusions:**

Dari hasil rekomendasi di atas, diketahui bahwa **"It's Okay to Not Be Okay"** memiliki kesamaan dalam kategori Sinopsis, Genre, dan Tags. Dari 7 item yang direkomendasikan, semuanya memiliki kesamaan dalam kategori tersebut. Selain itu, terdapat 10 rekomendasi yang memiliki sinopsis serupa.
"""