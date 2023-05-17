def enfeite():
    print('-'*250)


times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Cruzeiro',
         'Athletico-PR', 'Atlético-MG', 'Santos', 'Fortaleza',
         'Flamengo', 'São Paulo', 'Internacional', 'Bragantino',
         'Bahia', 'Goiás', 'Vasco da Gama', 'Corinthias', 'Cuiabá',
         'Coritiba', 'América-Mg')
enfeite()
print(f'Os times na ordem de colocação são \n {times}')
enfeite()
print(f"Os primeiros 5 colocados são {times[0:5]}")
enfeite()
print(f"Os últimos colocados são {times[15:19]}")
enfeite()
print(f'Em ordem alfabética: \n {sorted(times)}')
enfeite()
print(f"O time Vasco da gama está na {times.index('Vasco da Gama') + 1}ª posição.")
enfeite()