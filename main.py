
from jikanpy import Jikan
import pandas as pd
from random import choice
import numpy as np

jikan = Jikan()
tipos = ['anime','manga']
print("\n==============================")
print("====Recomendador de Animes====")
print("==============================\n")

while True:
    try:
        tipo = str(input("->Você deseja recomendação de Mangás ou Anime? Digite(manga ou anime)>> "))
        # se o usuario não escolher anime ou manga eh necessario gerar uma excecao de tipo
        tipo = tipo.lower()
        if tipo not in tipos:
            raise TypeError
        # realizando busca
        search = jikan.genre(tipo,np.random.randint(0,18))
        results = search[tipo] # pesquisamos pelo tipo
        animes_search_df = pd.DataFrame(results) # colocamos em um dataframe
        # realizando a escolha
        animes = np.array(animes_search_df['title'])
        print("\n\nEncontramos o ",tipo," perfeito para você!")
        print(">>Nossa recomendação é:",choice(animes),"<<")
        break
    except TypeError:
        print("\nOps... Este não é possível recomendar!\nEscolha 'manga' ou 'anime'.")
