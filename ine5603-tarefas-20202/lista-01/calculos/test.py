import model.calculos as cal

try:
    print('\ntestando media_de_tres_numeros...')
    media_de_tres_numeros = cal.media_de_tres_numeros(1,2,3)
    assert media_de_tres_numeros == 2 , f'media_de_tres_numeros(1,2,3) deveria retornar 2 mas retornou {media_de_tres_numeros}' 
    media_de_tres_numeros = cal.media_de_tres_numeros(0,0,-3)
    assert media_de_tres_numeros == -1 , f'media_de_tres_numeros(0,0,-3) deveria retornar -1 mas retornou {media_de_tres_numeros}' 
    print('media_de_tres_numeros ok')
except Exception as e:
    print(e)

     
try:
    print('\ntestando soma_de_tres_numeros...')
    soma = cal.soma_de_tres_numeros(10, 20, 30)
    assert soma == 60 , f'soma_de_tres_numeros(10,20,30) deveria retornar 60 mas retornou {soma}'
    soma = cal.soma_de_tres_numeros(0, -20, 30)
    assert soma == 10 , f'soma_de_tres_numeros(0, -20, 30) deveria retornar 10 mas retornou {soma}'
    print('soma_de_tres_numeros ok')
except Exception as e:
    print(e)

     
try:
    print('\ntestando par...')
    par = cal.par(1)
    assert par == False , f'par(1) deveria retornar False mas retornou {par}'
    par = cal.par(2)
    assert par == True , f'par(2) deveria retornar True mas retornou {par}'  
    print('par ok')
except Exception as e:
    print(e)


try:
    print('\ntestando menor_de_tres_numeros...')
    menor_de_tres_numeros = cal.menor_de_tres_numeros(1, 2, 3)
    assert menor_de_tres_numeros == 1 , f'menor_de_tres_numeros(1,2,3) deveria retornar 1 mas retornou {menor_de_tres_numeros}' 
    menor_de_tres_numeros = cal.menor_de_tres_numeros(-10, -2, -30)
    assert menor_de_tres_numeros == -30 , f'menor_de_tres_numeros(-10, -2, -30) deveria retornar -30 mas retornou {menor_de_tres_numeros}' 
    print('menor_de_tres_numeros ok')
except Exception as e:
    print(e)


try:
    print('\ntestando maior_que...')
    maior_que = cal.maior_que(10, 20)
    assert maior_que == False , f'maior_que(10,20) deveria retornar False mas retornou {maior_que}' 
    maior_que = cal.maior_que(30, 20)
    assert maior_que == True , f'maior_que(30,20) deveria retornar True mas retornou {maior_que}' 
    print('maior_que ok')
except Exception as e:
    print(e)
     

try:
    print('\ntestando divisivel_por...')
    divisivel_por = cal.divisivel_por(12, 4)
    assert divisivel_por == True , f'divisivel_por(12, 4) deveria retornar True mas retornou {divisivel_por}' 
    divisivel_por = cal.divisivel_por(13, 4)
    assert divisivel_por == False , f'divisivel_por(13, 4) deveria retornar False mas retornou {divisivel_por}' 
    print('divisivel_por ok')
except Exception as e:
    print(e)


try:
    print('\ntestando multiplica...')
    multiplica = cal.multiplica(2, 5)
    assert multiplica == 10 , f'multiplica(2, 5) deveria retornar 10 mas retornou {multiplica}' 
    multiplica = cal.multiplica(25, 5)
    assert multiplica == 125 , f'multiplica(25, 5) deveria retornar 125 mas retornou {multiplica}' 
    print('multiplica ok')
except Exception as e:
    print(e)

     
try:
    print('\ntestando divide...')
    divide = cal.divide(8,5)
    assert divide == 1 , f'divide(8,5) deveria retornar 1 mas retornou {divide}' 
    divide = cal.divide(10,5)
    assert divide == 2 , f'divide(10,5) deveria retornar 2 mas retornou {divide}' 
    print('divide ok')
except Exception as e:
    print(e)

     
try:
    print('\ntestando bissexto...')
    bissexto = cal.bissexto(2016)
    assert bissexto == True , f'bissexto(2016) deveria retornar True mas retornou {bissexto}' 
    bissexto = cal.bissexto(2021)
    assert bissexto == False , f'bissexto(2021) deveria retornar False mas retornou {bissexto}' 
    print('bissexto ok')
except Exception as e:
    print(e)

     
try:
    print('\ntestando mdc...')
    mdc = cal.mdc(52, 24)
    assert mdc == 4 , f'mdc(52, 24) deveria retornar 4 mas retornou {mdc}' 
    mdc = cal.mdc(34, 82)
    assert mdc == 2 , f'mdc(34, 82) deveria retornar 2 mas retornou {mdc}' 
    print('mdc ok')
except Exception as e:
    print(e)
    

try:
    print('\ntestando soma_dos_divisores...')
    soma_dos_divisores = cal.soma_dos_divisores(6)
    assert soma_dos_divisores == 12 , f'soma_dos_divisores(6) deveria retornar 12 mas retornou {soma_dos_divisores}' 
    soma_dos_divisores = cal.soma_dos_divisores(7)
    assert soma_dos_divisores == 8 , f'soma_dos_divisores(7) deveria retornar 12 mas retornou {soma_dos_divisores}' 
    print('soma_dos_divisores ok')
except Exception as e:
    print(e)


try:
    print('\ntestando amigos...')
    amigos = cal.amigos(284,220)
    assert amigos == True , f'amigos(284,220) deveria retornar True mas retornou {amigos}' 
    amigos = cal.amigos(17296, 18416)
    assert amigos == True , f'amigos(17296, 18416) deveria retornar True mas retornou {amigos}' 
    amigos = cal.amigos(285, 220)
    assert amigos == False , f'amigos(285,220) deveria retornar False mas retornou {amigos}' 
    print('amigos ok')
except Exception as e:
    print(e)


try:
    print('\ntestando primo...')
    primo = cal.primo(7)
    assert primo == True , f'primo(7) deveria retornar True mas retornou {primo}' 
    primo = cal.primo(36)
    assert primo == False , f'primo(36) deveria retornar False mas retornou {primo}'
    print('primo ok')
except Exception as e:
    print(e)
  

try:
    print('\ntestando composto...')
    composto = cal.composto(49)
    assert composto == True , f'composto(49) deveria retornar True mas retornou {composto}' 
    composto = cal.composto(3)
    assert composto == False , f'composto(3) deveria retornar False mas retornou {composto}' 
    print('composto ok')
except Exception as e:
    print(e)

