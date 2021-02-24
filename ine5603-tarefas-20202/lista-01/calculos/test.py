import model.calculos as cal

try:
    print('\nIniciando teste de media_de_tres_numeros...')
    media_de_tres_numeros = cal.media_de_tres_numeros(1,2,3)
    assert media_de_tres_numeros == 2 , f'media_de_tres_numeros(1,2,3) deveria retornar 2 mas retornou {media_de_tres_numeros}' 
    media_de_tres_numeros = cal.media_de_tres_numeros(0,0,-3)
    assert media_de_tres_numeros == -1 , f'media_de_tres_numeros(0,0,-3) deveria retornar -1 mas retornou {media_de_tres_numeros}' 
    print('media_de_tres_numeros ok')
except Exception as e:
    print(e)

     
try:
    print('\nIniciando teste de soma_de_tres_numeros...')
    soma = cal.soma_de_tres_numeros(10, 20, 30)
    assert soma == 60 , f'soma_de_tres_numeros(10,20,30) deveria retornar 60 mas retornou {soma}'
    soma = cal.soma_de_tres_numeros(0, -20, 30)
    assert soma == 10 , f'soma_de_tres_numeros(0, -20, 30) deveria retornar 10 mas retornou {soma}'
    print('soma_de_tres_numeros ok')
except Exception as e:
    print(e)

     
try:
    print('\nIniciando teste de par...')
    par = cal.par(1)
    assert par == False , f'par(1) deveria retornar False mas retornou {par}'
    par = cal.par(2)
    assert par == True , f'par(2) deveria retornar True mas retornou {par}' 
    par = cal.par(10)
    assert par == True , f'par(10) deveria retornar False mas retornou {par}' 
    par = cal.par(17)
    assert par == False , f'par(17) deveria retornar False mas retornou {par}'
    par = cal.par(0)
    assert par == True , f'par(0) deveria retornar False mas retornou {par}'
    print('par ok')
except Exception as e:
    print(e)


try:
    print('\nIniciando teste de menor_de_tres_numeros...')
    menor_de_tres_numeros = cal.menor_de_tres_numeros(1, 2, 3)
    assert menor_de_tres_numeros == 1 , f'menor_de_tres_numeros(1,2,3) deveria retornar 1 mas retornou {menor_de_tres_numeros}' 
    menor_de_tres_numeros = cal.menor_de_tres_numeros(-10, -2, -30)
    assert menor_de_tres_numeros == -30 , f'menor_de_tres_numeros(-10, -2, -30) deveria retornar -30 mas retornou {menor_de_tres_numeros}' 
    menor_de_tres_numeros = cal.menor_de_tres_numeros(8, 12, 76)
    assert menor_de_tres_numeros == 8 , f'menor_de_tres_numeros(8, 12, 76) deveria retornar -30 mas retornou {menor_de_tres_numeros}'
    menor_de_tres_numeros = cal.menor_de_tres_numeros(82, 12, 76)
    assert menor_de_tres_numeros == 12 , f'menor_de_tres_numeros(82, 12, 76) deveria retornar -30 mas retornou {menor_de_tres_numeros}'
    menor_de_tres_numeros = cal.menor_de_tres_numeros(182, 212, 76)
    assert menor_de_tres_numeros == 76 , f'menor_de_tres_numeros(182, 212, 76) deveria retornar -30 mas retornou {menor_de_tres_numeros}'
    menor_de_tres_numeros = cal.menor_de_tres_numeros(8, 8, 8)
    assert menor_de_tres_numeros == 8 , f'menor_de_tres_numeros(8, 8, 8) deveria retornar -30 mas retornou {menor_de_tres_numeros}'
    menor_de_tres_numeros = cal.menor_de_tres_numeros(0,0,0)
    assert menor_de_tres_numeros == 0 , f'menor_de_tres_numeros(0,0,0) deveria retornar -30 mas retornou {menor_de_tres_numeros}'
    menor_de_tres_numeros = cal.menor_de_tres_numeros(0,-5,0)
    assert menor_de_tres_numeros == -5 , f'menor_de_tres_numeros(0,-5,0) deveria retornar -30 mas retornou {menor_de_tres_numeros}'
    menor_de_tres_numeros = cal.menor_de_tres_numeros(-10,-5,-23)
    assert menor_de_tres_numeros == -23 , f'menor_de_tres_numeros(-10,-5,-23) deveria retornar -30 mas retornou {menor_de_tres_numeros}'
    print('menor_de_tres_numeros ok')
except Exception as e:
    print(e)


try:
    print('\nIniciando teste de maior_que...')
    maior_que = cal.maior_que(10, 20)
    assert maior_que == False , f'maior_que(10,20) deveria retornar False mas retornou {maior_que}' 
    maior_que = cal.maior_que(30, 20)
    assert maior_que == True , f'maior_que(30,20) deveria retornar True mas retornou {maior_que}' 
    maior_que = cal.maior_que(12, 8)
    assert maior_que == True , f'maior_que(12, 8) deveria retornar -30 mas retornou {maior_que}'
    maior_que = cal.maior_que(12, 83)
    assert maior_que == False , f'maior_que(12, 83) deveria retornar -30 mas retornou {maior_que}'
    maior_que = cal.maior_que(12, 12)
    assert maior_que == False , f'maior_que(12, 12) deveria retornar -30 mas retornou {maior_que}'
    print('maior_que ok')
except Exception as e:
    print(e)
     

try:
    print('\nIniciando teste de divisivel_por...')
    divisivel_por = cal.divisivel_por(12, 4)
    assert divisivel_por == True , f'divisivel_por(12, 4) deveria retornar True mas retornou {divisivel_por}' 
    divisivel_por = cal.divisivel_por(13, 4)
    assert divisivel_por == False , f'divisivel_por(13, 4) deveria retornar False mas retornou {divisivel_por}' 
    divisivel_por = cal.divisivel_por(12, 3)
    assert divisivel_por == True , f'divisivel_por(12, 3) deveria retornar False mas retornou {divisivel_por}' 
    divisivel_por = cal.divisivel_por(12, 5)
    assert divisivel_por == False , f'divisivel_por(12, 5) deveria retornar False mas retornou {divisivel_por}' 
    divisivel_por = cal.divisivel_por(12, 12)
    assert divisivel_por == True , f'divisivel_por(12, 12) deveria retornar False mas retornou {divisivel_por}' 
    divisivel_por = cal.divisivel_por(12, 24)
    assert divisivel_por == False , f'divisivel_por(12, 24) deveria retornar False mas retornou {divisivel_por}' 
    print('divisivel_por ok')
except Exception as e:
    print(e)


try:
    print('\nIniciando teste de multiplica...')
    multiplica = cal.multiplica(2, 5)
    assert multiplica == 10 , f'multiplica(2, 5) deveria retornar 10 mas retornou {multiplica}' 
    multiplica = cal.multiplica(25, 5)
    assert multiplica == 125 , f'multiplica(25, 5) deveria retornar 125 mas retornou {multiplica}' 
    print('multiplica ok')
except Exception as e:
    print(e)

     
try:
    print('\nIniciando teste de divide...')
    divide = cal.divide(8,5)
    assert divide == 1 , f'divide(8,5) deveria retornar 1 mas retornou {divide}' 
    divide = cal.divide(10,5)
    assert divide == 2 , f'divide(10,5) deveria retornar 2 mas retornou {divide}' 
    print('divide ok')
except Exception as e:
    print(e)

     
try:
    print('\nIniciando teste de bissexto...')
    bissexto = cal.bissexto(2016)
    assert bissexto == True , f'bissexto(2016) deveria retornar True mas retornou {bissexto}' 
    bissexto = cal.bissexto(2021)
    assert bissexto == False , f'bissexto(2021) deveria retornar False mas retornou {bissexto}' 
    print('bissexto ok')
except Exception as e:
    print(e)

     
try:
    print('\nIniciando teste de mdc...')
    mdc = cal.mdc(52, 24)
    assert mdc == 4 , f'mdc(52, 24) deveria retornar 4 mas retornou {mdc}' 
    mdc = cal.mdc(34, 82)
    assert mdc == 2 , f'mdc(34, 82) deveria retornar 2 mas retornou {mdc}' 
    print('mdc ok')
except Exception as e:
    print(e)
    

try:
    print('\nIniciando teste de soma_dos_divisores...')
    soma_dos_divisores = cal.soma_dos_divisores(6)
    assert soma_dos_divisores == 12 , f'soma_dos_divisores(6) deveria retornar 12 mas retornou {soma_dos_divisores}' 
    soma_dos_divisores = cal.soma_dos_divisores(7)
    assert soma_dos_divisores == 8 , f'soma_dos_divisores(7) deveria retornar 8 mas retornou {soma_dos_divisores}' 
    soma_dos_divisores = cal.soma_dos_divisores(1)
    assert soma_dos_divisores == 1 , f'soma_dos_divisores(1) deveria retornar 1 mas retornou {soma_dos_divisores}' 
    print('soma_dos_divisores ok')
except Exception as e:
    print(e)


try:
    print('\nIniciando teste de amigos...')
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
    print('\nIniciando teste de primo...')
    primo = cal.primo(7)
    assert primo == True , f'primo(7) deveria retornar True mas retornou {primo}' 
    primo = cal.primo(36)
    assert primo == False , f'primo(36) deveria retornar False mas retornou {primo}'
    print('primo ok')
except Exception as e:
    print(e)
  

try:
    print('\nIniciando teste de composto...')
    composto = cal.composto(49)
    assert composto == True , f'composto(49) deveria retornar True mas retornou {composto}' 
    composto = cal.composto(3)
    assert composto == False , f'composto(3) deveria retornar False mas retornou {composto}' 
    print('composto ok')
except Exception as e:
    print(e)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                     TESTES DOS COLEGAS                     """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


##################################################################
##################################################################
######################    Vinícius Antunes    ####################
##################################################################
##################################################################


print('Início dos teste da Vinícius')


try:
    print('\nIniciando teste composto')
    numero_composto = cal.composto(2)
    assert numero_composto == False, f'composto(2) deveria retornar False, mas retornou {numero_composto}'
    numero_composto == True, f'composto(4) deveria retornar True, mas retornou {numero_composto}'
    print('composto: ok')
except Exception as e:
    print(e)


# Testando primo
try:
    print('\nIniciando teste primo')
    numero_primo = cal.primo(5)
    assert numero_primo == True, f'primo(5) deveria retornar True, mas retornou {numero_primo}'
    numero_primo = cal.primo(4)
    assert numero_primo == False, f'primo(4) deveria retornar False, mas retornou {numero_primo}'
    print('primo: ok')
except Exception as e:
    print(e)


# Testando amigos
try:
    print('\nIniciando teste amigos')
    numeros_amigos = cal.amigos(220, 284)
    assert numeros_amigos == True, f'amigos(220, 284) deveria retornar True, mas retornou {numeros_amigos}'
    numeros_amigos = cal.amigos(456, 780)
    assert numeros_amigos == False, f'amigos(456, 780) deveria retornar False, mas retornou {numeros_amigos}'
    print('amigos: ok')
except Exception as e:
    print(e)


# Testando soma_divisores
try:
    print('\nIniciando teste soma_divisores')
    soma = cal.soma_dos_divisores(4)
    assert soma == 7, f'soma_divisores(4) deveria retornar 7, mas retornou {soma}'
    soma = cal.soma_dos_divisores(5)
    assert soma == 6, f'soma_divisores(5) deveria retornar 6, mas retornou {soma}'
    print('soma_divisores: ok')
except Exception as e:
    print(e)


# Testando mdc
try:
    print('\nIniciando teste mdc')
    gcd = cal.mdc(8, 12)
    assert gcd == 4, f'mdc(8, 12) deveria retornar 4, mas retornou {gcd}'
    print('mdc: ok')
except Exception as e:
    print(e)


# Testando divide
try:
    print('\nIniciando teste divide')
    resultado = cal.divide(10, 2)
    assert resultado == 5, f'divide(10, 2) deveria retornar 5, mas retornou {resultado}'
    print('divide: ok')
except Exception as e:
    print(e)


# Testando multiplica
try:
    print('\nIniciando teste multiplica')
    result = cal.multiplica(3, 2)
    assert result == 6, f'multiplica(3, 2) deveria retornar 6, mas retornou {result}'
    print('multiplica: ok')
except Exception as e:
    print(e)


# Testando bissexto
try:
    print('\nIniciando teste bissexto')
    ano = cal.bissexto(1904)
    assert ano == True, f'bissexto(1904) deveria retornar True, mas retornou {ano}'
    ano = cal.bissexto(1905)
    assert ano == False, f'bissexto(1905), deveria retornar False, mas retornou {ano}'
    print('bissexto: ok')
except Exception as e:
    print(e)

# Testando divisivel_por
try:
    print('\nIniciando teste divisivel_por')
    divisivel = cal.divisivel_por(10, 5)
    assert divisivel == True, f'divisivel_por(10, 5) deveria retornar True, mas retornou {divisivel}'
    divisivel = cal.divisivel_por(10, 6)
    assert divisivel == False, f'divisivel_por(10, 6) deveria retornar False, mas retornou {divisivel}'
    print('is_divisivel: ok')
except Exception as e:
    print(e)


# Testando menor_de_tres_numeros
try:
    print('\nIniciando teste menor_de_tres_numeros')
    menor = cal.menor_de_tres_numeros(4, -1, 60)
    assert menor == -1, f'menor_de_tres_numeros(4, -1 60) deveria retornar -1, mas retornou {menor}'
    print('menor_de_tres_numeros: ok')
except Exception as e:
    print(e)


# Testando maior_que
try:
    print('\nIniciando teste maior_que')
    maior = cal.maior_que(-1, 0)
    assert maior == 0, f'maior_que(-1, 0) deveria retornar 0, mas retornou {maior}'
    print('maior_que: ok')
except Exception as e:
    print(e)


# Testando par
try:
    print('\nIniciando teste par')
    par = cal.par(200)
    assert par == True, f'par(200) deveria retornar True, mas retornou {par}'
    par = cal.par(7)
    assert par == False, f'par(7) deveria retornar Fasle, mas retornou {par}'
    print('par: ok')
except Exception as e:
    print(e)

print('----------------------------------')
print('Final dos teste da Vinícius')
print('----------------------------------')

#################################################################################
#################################################################################
############################            Rebeca          #########################
#################################################################################
#################################################################################


print('Início dos teste da Rebeca')


from model.calculos import media_de_tres_numeros
from model.calculos import soma_de_tres_numeros
from model.calculos import par, menor_de_tres_numeros
from model.calculos import maior_que
from model.calculos import multiplica
from model.calculos import divide
from model.calculos import bissexto
from model.calculos import divisivel_por
from model.calculos import mdc
from model.calculos import soma_dos_divisores
from model.calculos import amigos
from model.calculos import primo
from model.calculos import composto

# media_de_tres_numeros

try:
    print('\nIniciando teste em media_de_tres_numeros...')
    media = media_de_tres_numeros(1, 2, 3)
    assert media == 2, f'media_de_tres_numeros(1, 2, 3) deveria retornar 2 mas retornou {media}'
    print('media_de_tres_numeros ...ok...')
except Exception as e:
    print(e)


# soma_de_tres_numeros

try:
    print('\nIniciando teste em soma_de_tres_numeros...')
    soma = soma_de_tres_numeros(1, 2, 3)
    assert soma == 6, f'soma_de_tres_numeros(1, 2, 3) deveria retornar 6 mas retornou {soma}'
    print('soma_de_tres_numeros ...ok...')
except Exception as e:
    print(e)


# par - True

try:
    print('\nIniciando teste em par com número par...')
    ehPar = par(2)
    assert ehPar == True, f'par(2) deveria retornar True mas retornou {ehPar}'
    print('par ...ok...')
except Exception as e:
    print(e)

# par - Fakse

try:
    print('\nIniciando teste em par com número ímpar...')
    ehPar = par(3)
    assert ehPar == False, f'par(3) deveria retornar False mas retornou {ehPar}'
    print('par ...ok...')
except Exception as e:
    print(e)


# menor_de_tres_numeros(2, 1, 4)

try:
    print('\nIniciando teste em menor_de_tres_numeros(2, 1, 4)...')
    menorNumero = menor_de_tres_numeros(2, 1, 4)
    assert menorNumero == 1, f'menor_de_tres_numeros(2, 1, 4) deveria retornar 1 mas retornou {menorNumero}'
    print('menor_de_tres_numeros ...ok...')
except Exception as e:
    print(e)


# menor_de_tres_numeros(7, 5, 3)

try:
    print('\nIniciando teste em menor_de_tres_numeros(7, 5, 3)...')
    menorNumero = menor_de_tres_numeros(7, 5, 3)
    assert menorNumero == 3, f'menor_de_tres_numeros(7, 3, 5) deveria retornar 3 mas retornou {menorNumero}'
    print('menor_de_tres_numeros ...ok...')
except Exception as e:
    print(e)


# maior_que(2, 5)

try:
    print('\nIniciando teste em maior_que(2, 5)...')
    ehMaior = maior_que(2, 5)
    assert ehMaior == False, f'maior_que(2, 5) deveria retornar 3 mas retornou {ehMaior}'
    print('maior_que ...ok...')
except Exception as e:
    print(e)


# maior_que(7, 6)

try:
    print('\nIniciando teste em maior_que(7, 6)...')
    ehMaior = maior_que(7, 6)
    assert ehMaior == True, f'maior_que(7, 6) deveria retornar 3 mas retornou {ehMaior}'
    print('maior_que ...ok...')
except Exception as e:
    print(e)


# multiplica

try:
    print('\nIniciando teste em multiplica(5, 6)...')
    multiplicacao = multiplica(5, 6)
    assert multiplicacao == 30, f'multiplica(5, 6) deveria retornar 30 mas retornou {multiplicacao}'
    print('multiplica ...ok...')
except Exception as e:
    print(e)


# divide

try:
    print('\nIniciando teste em divide(20, 5)...')
    divisao = divide(20, 5)
    assert divisao == 4, f'divide(20, 5) deveria retornar 4 mas retornou {divisao}'
    print('divide ...ok...')
except Exception as e:
    print(e)



# bissexto ano 2004

try:
    print('\nIniciando teste em bissexto(2004)...')
    bissexto1 = bissexto(2004)
    assert bissexto1 == True, f'bissexto(2004) deveria retornar True mas retornou {bissexto1}'
    print('bissexto ...ok...')
except Exception as e:
    print(e)

# bissexto ano 2000

try:
    print('\nIniciando teste em bissexto(2000)...')
    bissexto2 = bissexto(2000)
    assert bissexto2 == True, f'bissexto(2000) deveria retornar True mas retornou {bissexto2}'
    print('bissexto ...ok...')
except Exception as e:
    print(e)


# bissexto ano 2005

try:
    print('\nIniciando teste em bissexto(2005)...')
    bissexto3 = bissexto(2005)
    assert bissexto3 == False, f'bissexto(2005) deveria retornar False mas retornou {bissexto3}'
    print('bissexto ...ok...')
except Exception as e:
    print(e)



# divisivel_por (4, 2)

try:
    print('\nIniciando teste em divisivel_por(4, 2)...')
    divisivel1 = divisivel_por(4, 2)
    assert divisivel1 == True, f'divisivel_por(4, 2) deveria retornar True mas retornou {divisivel1}'
    print('divisivel_por ...ok...')
except Exception as e:
    print(e)


# divisivel_por (5, 2)

try:
    print('\nIniciando teste em divisivel_por(5, 2)...')
    divisivel2 = divisivel_por(5, 2)
    assert divisivel2 == False, f'divisivel_por(5, 2) deveria retornar True mas retornou {divisivel2}'
    print('divisivel_por ...ok...')
except Exception as e:
    print(e)


# mdc (52, 24)

try:
    print('\nIniciando teste em mdc(52, 24)...')
    mdc1 = mdc(52, 24)
    assert mdc1 == 4, f'mdc(52, 24) deveria retornar 4 mas retornou {mdc1}'
    print('mdc ...ok...')
except Exception as e:
    print(e)


# mdc (82, 64)

try:
    print('\nIniciando teste em mdc(82, 64)...')
    mdc2 = mdc(82, 64)
    assert mdc2 == 2, f'mdc(82, 64) deveria retornar 2 mas retornou {mdc2}'
    print('mdc ...ok...')
except Exception as e:
    print(e)


# soma_dos_divisores (4)

try:
    print('\nIniciando teste em soma_dos_divisores(4)...')
    somaDivisores = soma_dos_divisores(4)
    assert somaDivisores == 7, f'soma_dos_divisores(4) deveria retornar 7 mas retornou {somaDivisores}'
    print('soma_dos_divisores ...ok...')
except Exception as e:
    print(e)


# soma_dos_divisores (10)

try:
    print('\nIniciando teste em soma_dos_divisores(10)...')
    somaDivisores2 = soma_dos_divisores(10)
    assert somaDivisores2 == 18, f'soma_dos_divisores(10) deveria retornar 18 mas retornou {somaDivisores2}'
    print('soma_dos_divisores ...ok...')
except Exception as e:
    print(e)


# amigos (284, 220)

try:
    print('\nIniciando teste em amigos(284, 220)...')
    numerosAmigos = amigos(284, 220)
    assert numerosAmigos == True, f'amigos(284, 220) deveria retornar True mas retornou {numerosAmigos}'
    print('amigos ...ok...')
except Exception as e:
    print(e)


# primo (3)

try:
    print('\nIniciando teste em primo(3)...')
    numeroPrimo = primo(3)
    assert numeroPrimo == True, f'primo(3) deveria retornar True mas retornou {numeroPrimo}'
    print('primo ...ok...')
except Exception as e:
    print(e)


# primo (4)

try:
    print('\nIniciando teste em primo(4)...')
    numeroPrimo2 = primo(4)
    assert numeroPrimo2 == False, f'primo(4) deveria retornar False mas retornou {numeroPrimo2}'
    print('primo ...ok...')
except Exception as e:
    print(e)
    

# composto(4)

try:
    print('\nIniciando teste em composto(4)...')
    numComposto = composto(4)
    assert numComposto == True, f'composto(4) deveria retornar True mas retornou {numComposto}'
    print('composto ...ok...')
except Exception as e:
    print(e)


print('----------------------------------')
print('Final dos teste da Rebeca')
print('----------------------------------')


#################################################################################
#################################################################################
########################            Pedro Pereira          ######################
#################################################################################
#################################################################################


print('Início dos teste da Pedro Pereira')


from model.calculos import media_de_tres_numeros
from model.calculos import soma_de_tres_numeros
from model.calculos import par
from model.calculos import menor_de_tres_numeros
from model.calculos import maior_que
from model.calculos import divisivel_por
from model.calculos import multiplica
from model.calculos import divide
from model.calculos import bissexto
from model.calculos import mdc
from model.calculos import soma_dos_divisores
from model.calculos import amigos
from model.calculos import primo
from model.calculos import composto

#testando media_de_tres_numeros
try:
    print('\nIniciando teste media_de_tres_numeros...')
    media = media_de_tres_numeros(1, 1, 1)
    assert media == 1.0 , f'media_de_tres_numeros(1,1,1) deveria retornar 1.0 mas retornou {media}'
    print('media_de_tres_numeros ok')
except Exception as e:
    print(e)
#fim do teste

#testando soma_de_tres_numeros
try:
    print('\nIniciando teste soma_de_tres_numeros...')
    soma = soma_de_tres_numeros(1, 1, 1)
    assert soma == 3, f'soma_de_tres_numeros(1,1,1) deveria retornar 3 mas retornou {soma}'
    soma = soma_de_tres_numeros(0, 0, 0)
    assert soma == 0, f'soma_de_tres_numeros(0,0,0) deveria retornar 0 mas retornou {soma}'
    soma = soma_de_tres_numeros(-9, -1, -10)
    assert soma == -20, f'soma_de_tres_numeros(-9,-1,-10) deveria retornar -20 mas retornou {soma}'
    print('soma_de_tres_numeros ok')
except Exception as e:
    print(e)
#fim de teste


#testando par
try:
    print('\nIniciando teste par...')
    eh_par = par(10)
    assert eh_par == True, f'par(10) deveria retornar True mas retornou {eh_par}'
    eh_par = par(17)
    assert eh_par == False, f'par(17) deveria retornar False mas retornou {eh_par}'
    eh_par = par(0)
    assert eh_par == True, f'par(0) deveria retornar True mas retornou {eh_par}'
    eh_par = par(1)
    assert eh_par == False, f'par(1) deveria retornar False mas retornou {eh_par}'
    print('par ok')
except Exception as e:
    print(e)
#fim de teste

#testando menor_de_tres_numeros
try:
    print('\nIniciando teste menor_de_tres_numeros...')
    menor = menor_de_tres_numeros(8, 12, 76)
    assert menor == 8, f'menor_de_tres_numeros(8,12,76) deveria retornar 8 mas retornou{menor}'
    menor = menor_de_tres_numeros(82, 12, 76)
    assert menor == 12, f'menor_de_tres_numeros(82,12,76) deveria retornar 12 mas retornou{menor}'
    menor = menor_de_tres_numeros(182, 212, 76)
    assert menor == 76, f'menor_de_tres_numeros(182,212,76) deveria retornar 76 mas retornou{menor}'
    menor = menor_de_tres_numeros(8, 8, 8)
    assert menor == 8, f'menor_de_tres_numeros(8,8,8) deveria retornar 8 mas retornou{menor}'
    menor = menor_de_tres_numeros(0, 0, 0)
    assert menor == 0, f'menor_de_tres_numeros(0,0,0) deveria retornar 0 mas retornou{menor}'
    menor = menor_de_tres_numeros(0, -5, 0)
    assert menor == -5, f'menor_de_tres_numeros(0,-5,0) deveria retornar -5 mas retornou{menor}'
    menor = menor_de_tres_numeros(-10, -5, -23)
    assert menor == -23, f'menor_de_tres_numeros(-10,-5,-23) deveria retornar -23 mas retornou{menor}'
    print('menor_de_tres_numeros ok')
except Exception as e:
    print(e)
#fim de teste

#testando maior_que
try:
    print('\nIniciando teste maior_que...')
    eh_maior = maior_que(12,8)
    assert eh_maior == True, f'maior_que(12,8) deveria retornar True mas retornou{eh_maior}'
    eh_maior = maior_que(8, 12)
    assert eh_maior == False, f'maior_que(8, 12) deveria retornar Fa;se mas retornou{eh_maior}'
    eh_maior = maior_que(12, 12)
    assert eh_maior == False, f'maior_que(8, 12) deveria retornar Fa;se mas retornou{eh_maior}'
    print('maior_que ok')
except Exception as e:
    print(e)
#fim de teste

#testando divisivel_por
try:
    print('\nIniciando teste divisivel_por...')
    eh_divisivel = divisivel_por(12,3)
    assert eh_divisivel == True, f'divisivel_por(12,3) deveria retornar True mas retornou{eh_divisivel}'
    eh_divisivel = divisivel_por(12,5)
    assert eh_divisivel == False, f'divisivel_por(12,5) deveria retornar False mas retornou{eh_divisivel}'
    eh_divisivel = divisivel_por(12,12)
    assert eh_divisivel == True, f'divisivel_por(12,12) deveria retornar True mas retornou{eh_divisivel}'
    eh_divisivel = divisivel_por(12,24)
    assert eh_divisivel == False, f'divisivel_por(12,24) deveria retornar False mas retornou{eh_divisivel}'
    
    print('divisivel_por ok')
except Exception as e:
    print(e)
#fim de teste


#testando multiplica
try:
    print('\nIniciando teste multiplica...')
    eh_multiplicavel = multiplica(12,3)
    assert eh_multiplicavel == 36, f'multiplica(12,3) deveria retornar 36 mas retornou{multiplica}'   
    eh_multiplicavel = multiplica(2,5)
    assert eh_multiplicavel == 10, f'multiplica(2, 5) deveria retornar 10 mas retornou{multiplica}' 
    eh_multiplicavel = multiplica(2,2)
    assert eh_multiplicavel == 4, f'multiplica(2, 2) deveria retornar 4 mas retornou{multiplica}' 
    eh_multiplicavel = multiplica(2,0)
    assert eh_multiplicavel == 0, f'multiplica(2, 0) deveria retornar 0 mas retornou{multiplica}' 
    eh_multiplicavel = multiplica(0,2)
    assert eh_multiplicavel == 0, f'multiplica(0, 2) deveria retornar 0 mas retornou{multiplica}' 
    eh_multiplicavel = multiplica(0,0)
    assert eh_multiplicavel == 0, f'multiplica(0, 0) deveria retornar 0 mas retornou{multiplica}' 
    print('multiplica ok')
except Exception as e:
    print(e)
#fim de teste


#testando divide
try:
    print('\nIniciando teste divide...')
    divisor = divide(12,3)
    assert divisor == 4, f'divide(12,3) deveria retornar 4 mas retornou{divide}'   
    divisor = divide(8,5)
    assert divisor == 1, f'divide(8,5) deveria retornar 1 mas retornou{divide}'
    divisor = divide(3,12)
    assert divisor == 0, f'divide(3,12) deveria retornar 0 mas retornou{divide}'  
    divisor = divide(0,3)
    assert divisor == 0, f'divide(0,3) deveria retornar 0 mas retornou{divide}' 
    divisor = divide(12,12)
    assert divisor == 1, f'divide(12,12) deveria retornar 1 mas retornou{divide}' 
    print('divide ok')
except Exception as e:
    print(e)
#fim de teste


#testando bissexto
try:
    print('\nIniciando teste bissexto...')
    eh_bissexto = bissexto(400)
    assert eh_bissexto == True, f'bissexto(400) deveria retornar True mas retornou{bissexto}'   
    eh_bissexto = bissexto(500)
    assert eh_bissexto == False, f'bissexto(500) deveria retornar False mas retornou{bissexto}'   
    eh_bissexto = bissexto(2020)
    assert eh_bissexto == True, f'bissexto(2020) deveria retornar True mas retornou{bissexto}'  
    eh_bissexto = bissexto(0)
    assert eh_bissexto == True, f'bissexto(0) deveria retornar True mas retornou{bissexto}'    
    print('bissexto ok')
except Exception as e:
    print(e)
#fim de teste


#testando mdc
try:
    print('\nIniciando teste MDC...')
    eh_mdc = mdc(52, 24)
    assert eh_mdc == 4, f'mdc(52, 24) deveria retornar 4 mas retornou{mdc}'   
    eh_mdc = mdc(82, 34)
    assert eh_mdc == 2, f'mdc(82, 34) deveria retornar 2 mas retornou{mdc}' 
    eh_mdc = mdc(144, 92)
    assert eh_mdc == 4, f'mdc(144, 92) deveria retornar 4 mas retornou{mdc}' 
    print('mdc ok')
except Exception as e:
    print(e)
#fim de teste


#testando soma_dos_divisores
try:
    print('\nIniciando teste soma_dos_divisores...')
    eh_somadivid = soma_dos_divisores(7)
    assert eh_somadivid == 8, f'soma_dos_divisores(7) deveria retornar 8 mas retornou{soma_dos_divisores}'
    eh_somadivid = soma_dos_divisores(2)
    assert eh_somadivid == 3, f'soma_dos_divisores(2) deveria retornar 3 mas retornou{soma_dos_divisores}'  
    eh_somadivid = soma_dos_divisores(14)
    assert eh_somadivid == 24, f'soma_dos_divisores(14) deveria retornar 24 mas retornou{soma_dos_divisores}' 
    eh_somadivid = soma_dos_divisores(32)
    assert eh_somadivid == 63, f'soma_dos_divisores(32) deveria retornar 63 mas retornou{soma_dos_divisores}'
    eh_somadivid = soma_dos_divisores(10)
    assert eh_somadivid == 18, f'soma_dos_divisores(10) deveria retornar 18 mas retornou{soma_dos_divisores}'
    print('soma_dos_divisores ok')
except Exception as e:
    print(e)
#fim de teste


#testando amigos
try:
    print('\nIniciando teste amigos...')
    eh_amigo = amigos(284, 220)
    assert eh_amigo == True, f'soma_dos_divisores(284,220) deveria retornar True mas retornou{amigos}'
    eh_amigo = amigos(283, 220)
    assert eh_amigo == False, f'soma_dos_divisores(283,220) deveria retornar False mas retornou{amigos}'
    print('amigos ok')
except Exception as e:
    print(e)
#fim de teste


#testando primo
try:
    print('\nIniciando teste primo...')
    eh_primo = primo(7)
    assert eh_primo == True, f'primo(7) deveria retornar True mas retornou{primo}'
    eh_primo = primo(2)
    assert eh_primo == True, f'primo(2) deveria retornar True mas retornou{primo}'
    eh_primo = primo(14)
    assert eh_primo == False, f'primo(14) deveria retornar False mas retornou{primo}'
    eh_primo = primo(32)
    assert eh_primo == False, f'primo(32) deveria retornar False mas retornou{primo}'
    print('primo ok')
except Exception as e:
    print(e)
#fim de teste


#testando composto
try:
    print('\nIniciando teste composto...')
    eh_composto = composto(7)
    assert eh_composto == False, f'composto(7) deveria retornar False mas retornou{composto}'
    eh_composto = composto(2)
    assert eh_composto == False, f'composto(2) deveria retornar False mas retornou{composto}'
    eh_composto = composto(14)
    assert eh_composto == True, f'composto(14) deveria retornar True mas retornou{composto}'
    eh_composto = composto(32)
    assert eh_composto == True, f'composto(32) deveria retornar True mas retornou{composto}'
    print('composto ok')
except Exception as e:
    print(e)
#fim de teste

print('----------------------------------')
print('Final dos teste do Pedro Pereira')
print('----------------------------------')

#################################################################################
#################################################################################
##########################            Victória          #########################
#################################################################################
#################################################################################

print('Início dos teste do Victória')

from model.calculos import *

# testando media_de_tres_numeros
try:
    print('\nIniciando teste media_de_tres_numeros...')
    media = media_de_tres_numeros(10,20,30)
    assert media == 20, f'media_de_tres_numeros(10,20,30) deveria retornar 20 mas retornou {media}'
    media = media_de_tres_numeros(10,10,10)
    assert media == 10, f'media_de_tres_numeros(10,10,10) deveria retornar 10 mas retornou {media}'
    media = media_de_tres_numeros(0,0,0)
    assert media == 0, f'media_de_tres_numeros(0,0,0) deveria retornar 0 mas retornou {media}'
    print('media_de_tres_numeros ok')
except Exception as e:
    print(e)
# fim de teste

# testando soma_de_tres_numeros
try:
    print('\nIniciando teste soma_de_tres_numeros...')
    soma = soma_de_tres_numeros(10,20,30)
    assert soma == 60, f'soma_de_tres_numero(10,20,30) deveria retornar 60 mas retornou {soma}'
    soma = soma_de_tres_numeros(0,0,0)
    assert soma == 0, f'soma_de_tres_numero(0,0,0) deveria retornar 0 mas retornou {soma}'
    print('soma_de_tres_numeros ok')
except Exception as e:
    print(e)
# fim de teste

# testando par
try:
    print('\nIniciando teste par...')
    eh_par = par(8)
    assert eh_par == True, f'par(8) deveria retornar True mas retornou {eh_par}'
    eh_par = par(23)
    assert eh_par == False, f'par(23) deveria retornar False mas retornou {eh_par}'
    eh_par = par(0)
    assert eh_par == True, f'par(0) deveria retornar True mas retornou {eh_par}'
    eh_par = par(1)
    assert eh_par == False, f'par(1) deveria retornar False mas retornou {eh_par}'
    print('par ok')
except Exception as e:
    print(e)
# fim de teste

# testando menor_de_tres_numeros
try:
    print('\nIniciando teste menor_de_tres_numeros...')
    menor = menor_de_tres_numeros(5,9,14)
    assert menor == 5, f'menor_de_tres_numeros(5,9,14) deveria retornar 5 mas retornou {menor}'
    menor = menor_de_tres_numeros(20,9,14)
    assert menor == 9, f'menor_de_tres_numeros(20,9,14) deveria retornar 9 mas retornou {menor}'
    menor = menor_de_tres_numeros(14,9,5)
    assert menor == 5, f'menor_de_tres_numeros(14,9,5) deveria retornar 5 mas retornou {menor}'
    menor = menor_de_tres_numeros(8,8,8)
    assert menor == 8, f'menor_de_tres_numeros(8,8,8) deveria retornar 8 mas retornou {menor}'
    menor = menor_de_tres_numeros(0,0,0)
    assert menor == 0, f'menor_de_tres_numeros(0,0,0) deveria retornar 0 mas retornou {menor}'
    menor = menor_de_tres_numeros(0,-5,0)
    assert menor == -5, f'menor_de_tres_numeros(0,-5,0) deveria retornar -5 mas retornou {menor}'
    menor = menor_de_tres_numeros(-10,-5,-23)
    assert menor == -23, f'menor_de_tres_numeros(-10,-5,-23) deveria retornar -23 mas retornou {menor}'
    print('menor_de_tres_numeros ok')
except Exception as e:
    print(e)
# fim de teste

# testando maior_que
try:
    print('\nIniciando teste maior_que...')
    eh_maior = maior_que(15,8)
    assert eh_maior == True, f'maior_que(15,8) deveria retornar True mas retornou {eh_maior}'
    eh_maior = maior_que(4,8)
    assert eh_maior == False, f'maior_que(4,8) deveria retornar False mas retornou {eh_maior}'
    eh_maior = maior_que(8,8)
    assert eh_maior == False, f'maior_que(8,8) deveria retornar False mas retornou {eh_maior}'
    eh_maior = maior_que(-8,8)
    assert eh_maior == False, f'maior_que(-8,8) deveria retornar False mas retornou {eh_maior}'
    eh_maior = maior_que(1,-8)
    assert eh_maior == True, f'maior_que(1,-1) deveria retornar True mas retornou {eh_maior}'
    print('maior_que ok')
except Exception as e:
    print(e)
# fim de teste

# testando divisivel_por
try:
    print('\nIniciando teste divisivel_por...')
    eh_divisivel = divisivel_por(16,8)
    assert eh_divisivel == True, f'divisivel_por(16,8) deveria retornar True mas retornou {eh_divisivel}'
    eh_divisivel = divisivel_por(16,5)
    assert eh_divisivel == False, f'divisivel_por(16,5) deveria retornar False mas retornou {eh_divisivel}'
    eh_divisivel = divisivel_por(16,16)
    assert eh_divisivel == True, f'divisivel_por(16,16) deveria retornar True mas retornou {eh_divisivel}'
    eh_divisivel = divisivel_por(16,16)
    assert eh_divisivel == True, f'divisivel_por(16,16) deveria retornar True mas retornou {eh_divisivel}'
    eh_divisivel = divisivel_por(12,24)
    assert eh_divisivel == False, f'divisivel_por(12,24) deveria retornar False mas retornou {eh_divisivel}'
    print('divisivel_por ok')
except Exception as e:
    print(e)
# fim de teste

# testando multiplica
try:
    print('\nIniciando teste multiplica...')
    produto = multiplica(2,8)
    assert produto == 16, f'multiplica(2,8) deveria retornar 16 mas retornou {produto}'
    produto = multiplica(7,7)
    assert produto == 49, f'multiplica(7,7) deveria retornar 49 mas retornou {produto}'
    produto = multiplica(0,0)
    assert produto == 0, f'multiplica(0,0) deveria retornar 0 mas retornou {produto}'
    produto = multiplica(-8,5)
    assert produto == -40, f'multiplica(-8,5) deveria retornar -40 mas retornou {produto}'
    produto = multiplica(-8,-5)
    assert produto == 40, f'multiplica(-8,-5) deveria retornar 40 mas retornou {produto}'
    print('multiplica ok')
except Exception as e:
    print(e)
# fim de teste

# testando divide
try:
    print('\nIniciando teste divide...')
    divisao = divide(8,2)
    assert divisao == 4, f'divide(8,2) deveria retornar 4 mas retornou {divisao}'
    divisao = divide(8,5)
    assert divisao == 1, f'divide(8,5) deveria retornar 1 mas retornou {divisao}'
    divisao = divide(10,4)
    assert divisao == 2, f'divide(10,4) deveria retornar 2 mas retornou {divisao}'
    print('divide ok')
except Exception as e:
    print(e)
# fim de teste

# testando bissexto
try:
    print('\nIniciando teste bissexto...')
    eh_bissexto = bissexto(1948)
    assert eh_bissexto == True, f'bissexto(1948) deveria retornar True mas retornou {eh_bissexto}'
    eh_bissexto = bissexto(2024)
    assert eh_bissexto == True, f'bissexto(2024) deveria retornar True mas retornou {eh_bissexto}'
    eh_bissexto = bissexto(2021)
    assert eh_bissexto == False, f'bissexto(2021) deveria retornar False mas retornou {eh_bissexto}'
    print('bissexto ok')
except Exception as e:
    print(e)
# fim de teste

# testando mdc
try:
    print('\nIniciando teste mdc...')
    maior_div_comum = mdc(8,7)
    assert maior_div_comum == 1, f'mdc(8,7) deveria retornar 1 mas retornou {maior_div_comum}'
    maior_div_comum = mdc(9,12)
    assert maior_div_comum == 3, f'mdc(9,12) deveria retornar 3 mas retornou {maior_div_comum}'
    maior_div_comum = mdc(12,9)
    assert maior_div_comum == 3, f'mdc(12,9) deveria retornar 3 mas retornou {maior_div_comum}'
    print('mdc ok')
except Exception as e:
    print(e)
# fim de teste

# testando soma_dos_divisores
try:
    print('\nIniciando teste soma_dos_divisores...')
    soma = soma_dos_divisores(2)
    assert soma == 3, f'soma_dos_divisores(2) deveria retornar 3 mas retornou {soma}'
    soma = soma_dos_divisores(25)
    assert soma == 31, f'soma_dos_divisores(25) deveria retornar 31 mas retornou {soma}'
    soma = soma_dos_divisores(36)
    assert soma == 91, f'soma_dos_divisores(36) deveria retornar 91 mas retornou {soma}'
    print('soma_dos_divisores ok')
except Exception as e:
    print(e)
# fim de teste

# testando amigos
try:
    print('\nIniciando teste amigos...')
    sao_amigos = amigos(284,220)
    assert sao_amigos == True, f'amigos(284,220) deveria retornar True mas retornou {sao_amigos}'
    sao_amigos = amigos(1184,1210)
    assert sao_amigos == True, f'amigos(1184,1210) deveria retornar True mas retornou {sao_amigos}'
    sao_amigos = amigos(100,200)
    assert sao_amigos == False, f'amigos(100,200) deveria retornar False mas retornou {sao_amigos}'
    print('amigos ok')
except Exception as e:
    print(e)
# fim de teste

# testando primo
try:
    print('\nIniciando teste primo...')
    eh_primo = primo(2)
    assert eh_primo == True, f'primo(2) deveria retornar True mas retornou {eh_primo}'
    eh_primo = primo(11)
    assert eh_primo == True, f'primo(11) deveria retornar True mas retornou {eh_primo}'
    eh_primo = primo(4)
    assert eh_primo == False, f'primo(4) deveria retornar False mas retornou {eh_primo}'
    print('primo ok')
except Exception as e:
    print(e)
# fim de teste

# testando composto
try:
    print('\nIniciando teste composto...')
    eh_composto = composto(2)
    assert eh_composto == False, f'composto(2) deveria retornar False mas retornou {eh_composto}'
    eh_composto = composto(11)
    assert eh_composto == False, f'composto(11) deveria retornar False mas retornou {eh_composto}'
    eh_composto = composto(4)
    assert eh_composto == True, f'composto(4) deveria retornar True mas retornou {eh_composto}'
    print('composto ok')
except Exception as e:
    print(e)
# fim de teste

print('----------------------------------')
print('Final dos teste do Victória')
print('----------------------------------')


#################################################################################
#################################################################################
#####################            Vitor Schweighofer          ####################
#################################################################################
#################################################################################

print('Início dos teste do Vitor Schweighofer')

from model.calculos import *

try:
    print('\nIniciando teste media_de_tres_numeros...')
    media = media_de_tres_numeros(10,20,30)
    assert media == 20, f'media_de_tres_numeros(10,20,30), deveria retornar 20 mas retornou {media}'
    print('media_de_tres_numeros OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando soma_de_tres_numeros...')
    soma = soma_de_tres_numeros(10,20,30)
    assert soma == 60, f'soma_de_tres_numeros(10,20,30), deveria retornar 60 mas retornou {soma}'
    print('soma_de_tres_numeros OK')
except Exception as e:
    print(e)

try:
    print('\nIniciando par...')
    testePar = par(3)
    assert testePar==False, f'par(3) deveria retornar False mas retornou {testePar}'
    testePar = par(4)
    assert testePar==True, f'par(4) deveria retornar True mas retornou {testePar}'
    print('par OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando menor_de_tres_numeros...')
    menor = menor_de_tres_numeros(10,20,30)
    assert menor == 10, f'menor_de_tres_numeros(10,20,30), deveria retornar 10 mas retornou {menor}'
    print('menor_de_tres_numeros OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando maior_que...')
    maior = maior_que(20,10)
    assert maior == True, f'maior_que(20,10), deveria retornar True mas retornou {maior}'
    maior = maior_que(10,20)
    assert maior == False, f'maior_que(10,20), deveria retornar False mas retornou {maior}'
    print('maior_que OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando divisivel_por...')
    divisivel = divisivel_por(4,2)
    assert divisivel == True, f'divisivel_por(4,2), deveria retornar True mas retornou {divisivel}'
    divisivel = divisivel_por(5,2)
    assert divisivel == False, f'divisivel_por(5,2), deveria retornar False mas retornou {divisivel}'
    print('divisivel_por OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando multiplica...')
    multiplicar = multiplica(4,2)
    assert multiplicar == 8, f'multiplica(4,2), deveria retornar 8 mas retornou {multiplicar}'
    print('multiplica OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando divide...')
    dividir = divide(4,2)
    assert dividir == 2, f'divide(4,2), deveria retornar 2 mas retornou {dividir}'
    print('divide OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando bissexto...')
    ano_bissexto = bissexto(2020)
    assert ano_bissexto == True, f'bissexto(2020), deveria retornar True mas retornou {ano_bissexto}'
    ano_bissexto = bissexto(2019)
    assert ano_bissexto == False, f'bissexto(2019), deveria retornar False mas retornou {ano_bissexto}'
    print('bissexto OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando mdc...')
    max_dc = mdc(3,6)
    assert max_dc == 3, f'mdc(3,6), deveria retornar 3 mas retornou {max_dc}'
    print('mdc OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando soma_dos_divisores...')
    soma_div = soma_dos_divisores(8)
    assert soma_div == 15, f'soma_dos_divisores(8), deveria retornar 7 mas retornou {soma_div}'
    print('soma_dos_divisores OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando amigos...')
    num_amigos = amigos(220,284)
    assert num_amigos == True, f'num_amigos(220,284), deveria retornar True mas retornou {num_amigos}'
    num_amigos = amigos(221,284)
    assert num_amigos == False, f'num_amigos(221,284), deveria retornar False mas retornou {num_amigos}'
    print('amigos OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando primo...')
    num_primo = primo(7)
    assert num_primo == True, f'num_primo(7), deveria retornar True mas retornou {num_primo}'
    num_primo = primo(8)
    assert num_primo == False, f'num_primo(8), deveria retornar False mas retornou {num_primo}'
    print('primo OK')
except Exception as e:
    print(e)


try:
    print('\nIniciando composto...')
    num_composto = composto(8)
    assert num_composto == True, f'num_composto(8), deveria retornar True mas retornou {num_composto}'
    num_composto = composto(7)
    assert num_composto == False, f'num_composto(7), deveria retornar False mas retornou {num_composto}'
    print('composto OK')
except Exception as e:
    print(e)

print('----------------------------------')
print('Final dos teste do Vitor Schweighofer')
print('----------------------------------')

#################################################################################
#################################################################################
#####################            Guilherme          ####################
#################################################################################
#################################################################################

print('Início dos teste do Guilherme')

from model.calculos import media_de_tres_numeros
from model.calculos import soma_de_tres_numeros
from model.calculos import par
from model.calculos import menor_de_tres_numeros
from model.calculos import maior_que
from model.calculos import divisivel_por
from model.calculos import multiplica
from model.calculos import divide
from model.calculos import bissexto
from model.calculos import mdc
from model.calculos import soma_dos_divisores
from model.calculos import amigos
from model.calculos import primo
from model.calculos import composto

# testando media_de_tres_numeros
try:
    print('\niniciando teste media_de_tres_numeros')
    media = media_de_tres_numeros(1, 1, 1)
    assert media == 1.0 , f'media_de_tres_numero(1, 1, 1) deveria retornar 1.0 mas retornou {media}'
    media = media_de_tres_numeros(3, 1, 2)
    assert media == 2 , f'media_de_tres_numero(3, 1, 2) deveria retornar 2 mas retornou {media}'
    print('media_de_tres_numeros ok')
except Exception as e:
    print(e)    
#fim do teste

# testando soma_de_tres_numeros
try:
    print('\niniciando teste soma_de_tres_numeros')
    soma = soma_de_tres_numeros(1, 1, 1)
    assert soma == 3 , f'soma_de_tres_numero(1, 1, 1) deveria retornar 3 mas retornou {soma}'
    soma = soma_de_tres_numeros(3, 5, 1)
    assert soma == 9 , f'soma_de_tres_numero(3, 5, 1) deveria retornar 9 mas retornou {soma}'
    print('soma_de_tres_numeros ok')
except Exception as e:
    print(e)    
#fim do teste

# testando par
try:
    print('\niniciando teste par')
    resposta = par(2)
    assert resposta == True , f'par(2) deveria retornar True mas retornou {resposta}'
    resposta = par(3)
    assert resposta == False , f'par(3) deveria retornar False mas retornou {resposta}'
    print('par ok')
except Exception as e:
    print(e)    
#fim do teste

# testando menor_de_tres_numeros
try:
    print('\niniciando teste menor_de_tres_numeros')
    menor = menor_de_tres_numeros(1, 2, 3)
    assert menor == 1 , f'menor_de_tres_numero(1, 2, 3) deveria retornar 1 mas retornou {menor}'
    menor = menor_de_tres_numeros(3, 2, 6)
    assert menor == 2 , f'menor_de_tres_numero(3, 2, 6) deveria retornar 2 mas retornou {menor}'
    menor = menor_de_tres_numeros(9, 4, 3)
    assert menor == 3 , f'menor_de_tres_numero(9, 4, 3) deveria retornar 3 mas retornou {menor}'
    print('menor_de_tres_numeros ok')
except Exception as e:
    print(e)    
#fim do teste

# testando maior_que
try:
    print('\niniciando teste maior_que')
    maior = maior_que(1, 2)
    assert maior == False , f'maior_que(1, 2) deveria retornar False mas retornou {maior}'
    maior = maior_que(5, 3)
    assert maior == True , f'maior_que(5, 3) deveria retornar True mas retornou {maior}'
    print('maior_que ok')
except Exception as e:
    print(e)    
#fim do teste

# testando divisivel_por
try:
    print('\niniciando teste divisivel_por')
    divisivel = divisivel_por(10, 5)
    assert divisivel == True , f'divisivel_por(10, 5) deveria retornar True mas retornou {divisivel}'
    divisivel = divisivel_por(13, 2)
    assert divisivel == False , f'divisivel_por(13, 2) deveria retornar False mas retornou {divisivel}'
    print('divisivel_por ok')
except Exception as e:
    print(e)    
#fim do teste

# testando divisivel_por
try:
    print('\niniciando teste multiplica')
    produto = multiplica(2, 5)
    assert produto == 10 , f'multiplica(2, 5) deveria retornar 10 mas retornou {produto}'
    produto = multiplica(5, 6)
    assert produto == 30 , f'multiplica(5, 6) deveria retornar 30 mas retornou {produto}'
    print('multiplica ok')
except Exception as e:
    print(e)    
#fim do teste

# testando divide
try:
    print('\niniciando teste divide')
    quociente = divide(11, 2)
    assert quociente == 5 , f'divide(11, 2) deveria retornar 5 mas retornou {quociente}'
    quociente = divide(13, 4)
    assert quociente == 3 , f'divide(13, 6) deveria retornar 3 mas retornou {quociente}'
    print('quociente ok')
except Exception as e:
    print(e)    
#fim do teste

#testando bissexto
try:
    print('\niniciando teste bissexto')
    ano = bissexto(2024)
    assert ano == True , f'bissexto(2024) deveria retornar True mas retornou {ano}'
    ano = bissexto(2025)
    assert ano == False, f'bissexto(2025) deveria retornar False mas retornou {ano}'
    print('ano ok')
except Exception as e:
    print(e)    
#fim do teste

#testando mdc
try:
    print('\niniciando teste mdc')
    solucao = mdc(82, 34)
    assert solucao == 2 , f'mdc(82, 34) deveria retornar 2 mas retornou {solucao}'
    solucao = mdc(34, 82)
    assert solucao == 2 , f'mdc(34, 82) deveria retornar 2 mas retornou {solucao}'
    solucao = mdc(18, 60)
    assert solucao == 6 , f'mdc(18, 60) deveria retornar 6 mas retornou {solucao}'
    print('solucao ok')
except Exception as e:
    print(e)    
#fim do teste

#testando soma_dos_divisores

try:
    print('\niniciando teste soma_dos_divisores')
    soma = soma_dos_divisores(4)
    assert soma == 7 , f'soma_dos_divisores(4) deveria retornar 7 mas retornou {soma}'
    soma = soma_dos_divisores(20)
    assert soma == 42 , f'soma_dos_divisores(20) deveria retornar 42 mas retornou {soma}'
    print('soma ok')
except Exception as e:
    print(e)
#fim de teste

#testando numeros amigos

try:
    print('\niniciando teste amigos')
    conclusao = amigos(284, 220 )
    assert conclusao == True , f'amigos(284, 220) deveria retornar True mas retornou {conclusao}'
    conclusao = amigos(220, 284 )
    assert conclusao == True , f'amigos(284, 220) deveria retornar True mas retornou {conclusao}'
    conclusao = amigos(300, 229 )
    assert conclusao == False , f'amigos(300, 229) deveria retornar False mas retornou {conclusao}'
    print('conclusao ok')
except Exception as e:
    print(e)

#fim do teste

#testando numeros amigos

try:
    print('\niniciando teste primo')
    verificacao = primo(13)
    assert verificacao == True , f'primo(13) deveria retornar True mas retornou {verificacao}'
    verificacao = primo(2)
    assert verificacao == True , f'amigos(2) deveria retornar True mas retornou {verificacao}'
    verificacao = primo(12)
    assert verificacao == False , f'amigos(12) deveria retornar False mas retornou {verificacao}'
    print('verificacao ok')
except Exception as e:
    print(e)

#fim do teste

#inicio do teste
try:
    print('\niniciando teste primo')
    verificacao = primo(13)
    assert verificacao == True , f'primo(13) deveria retornar True mas retornou {verificacao}'
    verificacao = primo(2)
    assert verificacao == True , f'primo(2) deveria retornar True mas retornou {verificacao}'
    verificacao = primo(12)
    assert verificacao == False , f'primo(12) deveria retornar False mas retornou {verificacao}'
    print('verificacao ok')
except Exception as e:
    print(e)

#fim do teste

#inicio do teste
try:
    print('\niniciando teste composto')
    verificacao = composto(13)
    assert verificacao == False , f'composto(13) deveria retornar False mas retornou {verificacao}'
    verificacao = composto(2)
    assert verificacao == False , f'composto(2) deveria False True mas retornou {verificacao}'
    verificacao = composto(12)
    assert verificacao == True , f'composto(12) deveria retornar True mas retornou {verificacao}'
    print('verificacao ok')
except Exception as e:
    print(e)

#fim do teste

print('----------------------------------')
print('Final dos teste do Guilherme')
print('----------------------------------')

#################################################################################
#################################################################################
#####################            Roger          ####################
#################################################################################
#################################################################################

print('Início dos teste do Roger')

import model.calculos as calculos

try:
    print('teste de media_de_tres_numeros')
    resultado = calculos.media_de_tres_numeros(5,5,5)
    assert resultado == 5 , f'media_de_tres_numeros(5,5,5) deveria retornar 5 mas retornou {resultado}' 
    resultado = calculos.media_de_tres_numeros(0,0,-15)
    assert resultado == -5 , f'media_de_tres_numeros(0,0,-15) deveria retornar -5 mas retornou {resultado}' 
    print('media_de_tres_numeros passou')
except Exception as err:
    print(err)


try:
    print('teste de soma_de_tres_numeros')
    resultado = calculos.soma_de_tres_numeros(10, 10, 10)
    assert resultado == 30 , f'soma_de_tres_numeros(10,10,10) deveria retornar 30 mas retornou {resultado}'
    resultado = calculos.soma_de_tres_numeros(0, -5, 20)
    assert resultado == 15 , f'soma_de_tres_numeros(0, -5, 20) deveria retornar 15 mas retornou {resultado}'
    print('soma_de_tres_numeros passou')
except Exception as err:
    print(err)

     
try:
    print('teste de par')
    resultado = calculos.par(0)
    assert resultado == True , f'par(0) deveria retornar True mas retornou {resultado}'
    resultado = calculos.par(1)
    assert resultado == False , f'par(1) deveria retornar False mas retornou {resultado}'
    resultado = calculos.par(2)
    assert resultado == True , f'par(2) deveria retornar True mas retornou {resultado}' 
    resultado = calculos.par(10)
    assert resultado == True , f'par(10) deveria retornar False mas retornou {resultado}' 
    resultado = calculos.par(11)
    assert resultado == False , f'par(17) deveria retornar False mas retornou {resultado}'
    print('par passou')
except Exception as err:
    print(err)


try:
    print('teste de menor_de_tres_numeros')
    resultado = calculos.menor_de_tres_numeros(1, 2, 3)
    assert resultado == 1 , f'menor_de_tres_numeros(1,2,3) deveria retornar 1 mas retornou {resultado}' 
    resultado = calculos.menor_de_tres_numeros(-1, -2, -3)
    assert resultado == -3 , f'menor_de_tres_numeros(-1, -2, -3) deveria retornar -3 mas retornou {resultado}' 
    print('menor_de_tres_numeros passou')
except Exception as err:
    print(err)


try:
    print('teste de maior_que')
    resultado = calculos.maior_que(1, 2)
    assert resultado == False , f'maior_que(1,2) deveria retornar False mas retornou {resultado}' 
    resultado = calculos.maior_que(3, 2)
    assert resultado == True , f'maior_que(3,2) deveria retornar True mas retornou {resultado}' 
    print('maior_que passou')
except Exception as err:
    print(err)
     

try:
    print('teste de divisivel_por')
    resultado = calculos.divisivel_por(4, 2)
    assert resultado == True , f'divisivel_por(4, 2) deveria retornar True mas retornou {resultado}' 
    resultado = calculos.divisivel_por(15, 2)
    assert resultado == False , f'divisivel_por(15, 2) deveria retornar False mas retornou {resultado}' 
    print('divisivel_por passou')
except Exception as err:
    print(err)


try:
    print('teste de multiplica')
    resultado = calculos.multiplica(3, 10)
    assert resultado == 30 , f'multiplica(3, 10) deveria retornar 30 mas retornou {resultado}' 
    resultado = calculos.multiplica(5, 5)
    assert resultado == 25 , f'multiplica(5, 5) deveria retornar 25 mas retornou {resultado}' 
    print('multiplica passou')
except Exception as err:
    print(err)

     
try:
    print('teste de divide')
    resultado = calculos.divide(6,5)
    assert resultado == 1 , f'divide(6,5) deveria retornar 1 mas retornou {resultado}' 
    resultado = calculos.divide(10,5)
    assert resultado == 2 , f'divide(10,5) deveria retornar 2 mas retornou {resultado}' 
    print('divide passou')
except Exception as err:
    print(err)

     
try:
    print('teste de bissexto')
    resultado = calculos.bissexto(2020)
    assert resultado == True , f'bissexto(2020) deveria retornar True mas retornou {resultado}' 
    resultado = calculos.bissexto(2021)
    assert resultado == False , f'bissexto(2021) deveria retornar False mas retornou {resultado}' 
    print('bissexto passou')
except Exception as err:
    print(err)

     
try:
    print('teste de mdc')
    resultado = calculos.mdc(52, 24)
    assert resultado == 4 , f'mdc(52, 24) deveria retornar 4 mas retornou {resultado}' 
    resultado = calculos.mdc(34, 82)
    assert resultado == 2 , f'mdc(34, 82) deveria retornar 2 mas retornou {resultado}' 
    print('mdc passou')
except Exception as err:
    print(err)
    

try:
    print('teste de soma_dos_divisores')
    resultado = calculos.soma_dos_divisores(5)
    assert resultado == 6 , f'soma_dos_divisores(5) deveria retornar 6 mas retornou {resultado}' 
    resultado = calculos.soma_dos_divisores(2)
    assert resultado == 3 , f'soma_dos_divisores(2) deveria retornar 3 mas retornou {resultado}' 
    print('soma_dos_divisores passou')
except Exception as err:
    print(err)


try:
    print('teste de amigos')
    resultado = calculos.amigos(284,220)
    assert resultado == True , f'amigos(284,220) deveria retornar True mas retornou {resultado}' 
    resultado = calculos.amigos(285, 220)
    assert resultado == False , f'amigos(285,220) deveria retornar False mas retornou {resultado}' 
    print('amigos passou')
except Exception as err:
    print(err)


try:
    print('teste de primo')
    resultado = calculos.primo(11)
    assert resultado == True , f'primo(11) deveria retornar True mas retornou {resultado}' 
    resultado = calculos.primo(4)
    assert resultado == False , f'primo(4) deveria retornar False mas retornou {resultado}'
    print('primo passou')
except Exception as err:
    print(err)
  

try:
    print('teste de composto')
    resultado = calculos.composto(4)
    assert resultado == True , f'composto(4) deveria retornar True mas retornou {resultado}' 
    resultado = calculos.composto(5)
    assert resultado == False , f'composto(5) deveria retornar False mas retornou {resultado}' 
    print('composto passou')
except Exception as err:
    print(err)



print('----------------------------------')
print('Final dos teste do Roger')
print('----------------------------------')

#################################################################################
#################################################################################
#####################            ???          ####################
#################################################################################
#################################################################################

print('Início dos teste do ???')
print('----------------------------------')
print('Final dos teste do ???')
print('----------------------------------')