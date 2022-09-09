Depeche_Mode_violator_songsdict ={'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.60,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68}

s= sum(Depeche_Mode_violator_songsdict.values())
print('Общее время звучания всех песен: ',s)

more_than_5_min=0
print('Песни, время звучания которых больше 5 мин: ')
for key, value in Depeche_Mode_violator_songsdict.items():
    if value>5:
        more_than_5_min+=1
        print(more_than_5_min, f'Песня: {key}, Время звучания: {value} ')

dict_new={s: Depeche_Mode_violator_songsdict[s]
          for s in Depeche_Mode_violator_songsdict.keys()
          if not ' ' in s}
print('Песни, название которых состоит из одного слова: ', dict_new)