# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Definição das funções que realizam cálculos diversos.


def media_de_tres_numeros(n1, n2, n3):
    """Calcula a média de três números."""

    return (n1 + n2 + n3)/3


def soma_de_tres_numeros(n1, n2, n3):
    """Calcula a soma de três números."""

    return n1 + n2 + n3


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
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3

    return menor


def maior_que(n1, n2):
    """Verifica se o primeiro número é maior que segundo número.

    Retorna True se n1 for maior que n2 ou False caso contrário.
    """
    if n1 > n2:
        return True
    else:
        return False


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
    return True if ano % 4 == 0 and ano % 100 != 0 else False


def mdc(n1, n2):
    """Calcula o Máximo Divisor Comum entre dois números inteiros positivos.

    Dica: Utilize o Método das Divisões Sucessivas. Veja o método em
    http://www.mundoeducacao.com/matematica/mdc-divisoes-sucessivas.htm
    """
    numerador = n1 if n1 > n2 else n2
    denominador = n1 if n1 < n2 else n2
    resto = numerador % denominador

    while resto > 0:
        numerador = denominador
        denominador = resto
        resto = numerador % denominador

    return denominador


def soma_dos_divisores(n):
    """Calcula a soma dos divisores de um número inteiro maior que zero.

    Dica: a metade de n é n // 2.
    """
    para_somar = [1, n]
    i = 2

    while i <= n//2:
        if n % i == 0:
            para_somar.append(i)
        i += 1
        
    soma = sum(para_somar)

    return soma


def amigos(n1, n2):
    """Verifica se dois números inteiros positivos são amigos.

    Retorna True se números são amigos ou False caso contrário.
    Dica: Números Amigos: http://www.matematica.br/historia/namigos.html
    """
    soma1 = soma_dos_divisores(n1)
    soma2 = soma_dos_divisores(n2)
    return True if soma1 == soma2 else False


def primo(n):
    """Verifica se número é primo.
    
    Considera que n sempre é maior que 1.
    Retorna True se n for primo ou False caso contrário.
    """
    soma = soma_dos_divisores(n)
    return True if soma == n + 1 else False


def composto(n):
    """Verifica se um número é composto.

    Considera que n sempre é maior que 1.
    Retorna True se n for número composto ou False caso contrário.
    Definição: um número é composto se possui mais de dois divisores.
    Conclusão (regra): Todo o número inteiro não-primo e diferente de 1 é composto.
    """
    e_primo = primo(n)
    return True if e_primo == False and n != 1 else False

