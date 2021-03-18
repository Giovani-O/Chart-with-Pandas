#!/usr/bin/env python
# coding: utf-8

# # Is Netflix increasingly focusing on TV rather than movies in recent years?

# #### Answer: No, according to the chart below, Netflix still focus more on movies rather than TV shows.

# In[17]:


import pandas as pd
import matplotlib.pyplot as plt

# Acessando o arquivo .csv e convertendo date_added para datetime
data = pd.read_csv('netflix_titles.csv', parse_dates=['date_added'])
# Obtendo apenas o ano da adição
data['year_added'] = data['date_added'].dt.year.astype('Int64')
# boolean indexing: me permitiu usar apenas dados de 2015 em diante
data = data[data['year_added'] >= 2015]

# Será utilizado para responder a segunda pergunta
data[['number_of_seasons', 'duration_type']] = data.duration.str.split(" ",expand=True)

# Separando TV Shows de Movies
group = data.groupby(data['type'])
tv_shows = group.get_group('TV Show')
movies = group.get_group('Movie')

# Gerando o gráfico
fig, axs = plt.subplots(figsize=(15, 5))
movies.groupby([movies["year_added"]])["year_added"].size().plot(kind='bar', rot=45, ax=axs, color='#ff3333', position=1, width=0.25)
tv_shows.groupby([tv_shows["year_added"]])["year_added"].size().plot(kind='bar', rot=45, ax=axs, color='#3333ff', position=0, width=0.25)
plt.title('Number of TV Shows/Movies added to Netflix each year')
plt.xlabel('Years')
plt.ylabel('Shows/movies added')
axs.legend(['Movies', 'TV Shows'])


# # What is the greatest number of seasons for a TV show on Netflix?

# #### Answer: According to the algorithm below, the greatest number of seasons for a TV show is 16, belonging to Grey's Anatomy.

# In[18]:


# Split para obter o número de temporadas
# data[['number_of_seasons','duration_type']] = data.duration.str.split(" ",expand=True)

seasons = []
titles = []
seasons = pd.to_numeric(tv_shows['number_of_seasons'])
titles = tv_shows['title']

# reset dos índices para facilitar o trabalho com as listas
seasons.reset_index(drop=True, inplace=True)
titles.reset_index(drop=True, inplace=True)

show_index = list(seasons).index(max(seasons))

print(f"The show on Netflix with the most seasons is {titles[show_index]} with {seasons[show_index]} seasons.")


# In[ ]:




