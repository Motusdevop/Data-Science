#место для твоего кода

import pandas as pd

import matplotlib.pyplot as plt

from pprint import pprint

df= pd.read_csv("IMDB-Movie-Data.csv")

#Изучение жанров
hashtable = dict()
def sort(Genres):
    if len(Genres) == 0:
        return hashtable
    else:
        Genre = Genres[0]
        if Genre in hashtable:
            hashtable[Genre] += 1
            return sort(Genres[1:])
        else:
            hashtable[Genre] = 1
            return sort(Genres[1:])
        




df["Revenue (Millions)"].fillna(-1, inplace=True)

df["Metascore"].fillna(-1, inplace=True)

Genre_list = list(df["Genre"].head(150))

Genre_list = ",".join(Genre_list).split(",")

Genre_dict = sort(Genre_list)

df2 = pd.DataFrame(Genre_dict.items(), columns=['Genre', 'Count'])
print(df2)
table = df2.pivot_table(
    index = "Genre",
    values = "Count"
)
print(table)
table.plot(kind = "barh", figsize=(10,12))

table2 = df.pivot_table(
    index = "Rating",
    values = "Revenue (Millions)"
)
print(table2)
table2.plot(kind="barh", figsize= (10,20))




plt.show()

print("Самые популярные жанры у лучших фильмов по оценки: Drama, Adventure, Action, Comedy")








