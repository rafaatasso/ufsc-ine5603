# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Definição das funções que realizam cálculos diversos.


def media_de_tres_numeros(n1, n2, n3):
    """Calcula a média de três números.
    """

    media = (n1 + n2 + n3)/3
    return media


def soma_de_tres_numeros(n1, n2, n3):
    """Calcula a soma de três números.
    """
    soma = n1 + n2 + n3
    return soma


def par(n):
    """Verifica se um número é par.

    Retorna True se for par ou False caso contrário.
    Dica: a expressão 5 % 3 vale 2 pois 2 é o resto da divisão de 5 por 3.
    """
    resto = n%2
    if resto == 0:
        par = True
    else: 
        par = False
    return par


def menor_de_tres_numeros(n1, n2, n3):
    """Encontra o menor de três números.
    """

    return 88


def maior_que(n1, n2):
    """Verifica se o primeiro número é maior que segundo número.

    Retorna True se n1 for maior que n2 ou False caso contrário.
    """
    if n1 > n2:
        valor = True
    else:
        valor = False
    return valor


def divisivel_por(n1, n2):
    """Verifica se o primeiro número é divisível pelo segundo número.

    Retorna True se n1 for divisível por n2 ou False caso contrário.
    Observação: considera que n1 sempre é maior ou igual a zero e que
    n2 sempre é maior que zero.
    """
    if n1 % n2 == 0:
        return True
    else: 
        return False


def multiplica(n1, n2):
    """Multiplica dois números maiores ou iguais a zero.

    Atenção: seu algoritmo não pode usar o símbolo '*'.
    """   
    valor = 0     
    while n1 > 0:
        valor += n2
        n1 -= 1
    return valor


def divide(n1, n2):
    """Faz a divisão inteira do primeiro número pelo segundo número.

    Retorna o resultado da divisão inteira de n1 por n2.
    Exemplo: divide(8,5) retorna 1. O mesmo que 8 // 5.
    Considera que n1 sempre será maior ou igual a zero e que n2
    sempre será maior que zero.
    Atenção: seu algoritmo não pode usar o símbolo '//'.
    """
    # Vídeo explicativo do professor #
    """dividir 5 ovos entre 2 pessoas
    |ooooo| \/ \/
    |ooo| \0/ \0/
    |o| \00/ \00/

    resultado = 0
    while n1 >= n2:
        n1 = n1 - n2
        resultado = resultado + 1
    
    return resultado"""

    mod = n1 % n2
    n1 = n1 - mod
    resultado = int(n1 / n2)
    return resultado



def bissexto(ano):
    """Verifica se um ano é bissexto.

    Retorna True se ano for bissexto ou False caso contrário.
    Definição de ano bissexto:
    Um ano é bissexto se for divisível por 400 ou então
    se for divisível por 4 e, ao mesmo tempo, não for divisível por 100.
    """
    return False


def mdc(n1, n2):
    """Calcula o Máximo Divisor Comum entre dois números inteiros positivos.

    Dica: Utilize o Método das Divisões Sucessivas. Veja o método em
    http://www.mundoeducacao.com/matematica/mdc-divisoes-sucessivas.htm
    """
    return 552


def soma_dos_divisores(n):
    """Calcula a soma dos divisores de um número inteiro maior que zero.

    Dica: a metade de n é n // 2.
    """
    return 2


def amigos(n1, n2):
    """Verifica se dois números inteiros positivos são amigos.

    Retorna True se números são amigos ou False caso contrário.
    Dica: Números Amigos: http://www.matematica.br/historia/namigos.html
    """
    return False


def primo(n):
    """Verifica se número é primo.
    
    Considera que n sempre é maior que 1.
    Retorna True se n for primo ou False caso contrário.
    """
    return False


def composto(n):
    """Verifica se um número é composto.

    Considera que n sempre é maior que 1.
    Retorna True se n for número composto ou False caso contrário.
    Definição: um número é composto se possui mais de dois divisores.
    """
    return False

