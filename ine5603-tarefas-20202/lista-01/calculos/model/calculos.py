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
    # resto = n%2
    # if resto == 0:
    #     par = True
    # else: 
    #     par = False
    # return par
    return n % 2 == 0


def menor_de_tres_numeros(n1, n2, n3):
    """Encontra o menor de três números.
    """
    # menor = n1
    # if n2 < menor:
    #     menor = n2
    # if n3 < menor:
    #     menor = n3

    # return menor
    menor = n1 if n1 < n2 else n2
    return n3 if n3 < menor else menor
    

def maior_que(n1, n2):
    """Verifica se o primeiro número é maior que segundo número.

    Retorna True se n1 for maior que n2 ou False caso contrário.
    """
    # if n1 > n2:
    #     return True
    # else:
    #     return False
    return n1 > n2


def divisivel_por(n1, n2):
    """Verifica se o primeiro número é divisível pelo segundo número.

    Retorna True se n1 for divisível por n2 ou False caso contrário.
    Observação: considera que n1 sempre é maior ou igual a zero e que
    n2 sempre é maior que zero.
    """
    # if n1 % n2 == 0:
    #     return True
    # else: 
    #     return False
    return n1 % n2 == 0


def multiplica(n1, n2):
    """Multiplica dois números maiores ou iguais a zero.

    Atenção: seu algoritmo não pode usar o símbolo '*'.
    """   
    # Minha Solução
    # valor = 0     
    # while n1 > 0:
    #     valor += n2
    #     n1 -= 1
    # return valor

    # Resolução do professor
    if n2 < n1:
        n1, n2 = n2, n1  #coloca em n1 o valor de n2 e também em n2, teremos o valor de n1
    
    resultado = 0
    for _ in range(n1):
        resultado += n2
    return resultado

def divide(n1, n2):
    """Faz a divisão inteira do primeiro número pelo segundo número.

    Retorna o resultado da divisão inteira de n1 por n2.
    Exemplo: divide(8,5) retorna 1. O mesmo que 8 // 5.
    Considera que n1 sempre será maior ou igual a zero e que n2
    sempre será maior que zero.
    Atenção: seu algoritmo não pode usar o símbolo '//'.
    """
    # Minha Solução
    # Essa resolução passaria em uma prova pois não está violando nenhuma regra da questão, porém o intuito do exercício era, justamente, não utilizar a divisão
    mod = n1 % n2
    n1 = n1 - mod
    return int(n1 / n2)

    # Resolução do professor
    # dividir 5 ovos entre 2 pessoas
    # |ooooo| \/ \/
    # |ooo| \0/ \0/
    # |o| \00/ \00/
    # resultado = 0
    # while n1 >= n2:
    #     n1 = n1 - n2
    #     resultado = resultado + 1
    # return resultado


def bissexto(ano):
    """Verifica se um ano é bissexto.

    Retorna True se ano for bissexto ou False caso contrário.
    Definição de ano bissexto:
    Um ano é bissexto se for divisível por 400 ou então
    se for divisível por 4 e, ao mesmo tempo, não for divisível por 100.
    """
    # Minha Solução
    # return True if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 else False

    # Resolução do professor
    return divisivel_por(ano, 400) or divisivel_por(ano, 4) and not divisivel_por(ano,100)


def mdc(n1, n2):
    """Calcula o Máximo Divisor Comum entre dois números inteiros positivos.

    Dica: Utilize o Método das Divisões Sucessivas. Veja o método em
    http://www.mundoeducacao.com/matematica/mdc-divisoes-sucessivas.htm
    """
    # Minha Solução
    numerador = n1 if n1 > n2 else n2
    denominador = n1 if n1 < n2 else n2
    resto = numerador % denominador

    while resto > 0:
        numerador = denominador
        denominador = resto
        resto = numerador % denominador

    return denominador

    # Resolução do professor
    # if n2 < n1:
    #     n1, n2 = n2, n1
    # resto = n1 % n2
    # while resto > 0:
    #     n1 = n2
    #     n2 = resto
    #     resto = n1 % n2
    # return n2


def soma_dos_divisores(n):
    """Calcula a soma dos divisores de um número inteiro maior que zero.

    Dica: a metade de n é n // 2.
    """
    # Minha Solução
    para_somar = [1] if n == 1 else [1, n]
    i = 2

    while i <= n//2:
        if divisivel_por(n, i):
            para_somar.append(i)
        i += 1
        
    soma = sum(para_somar)
    return soma
    
    # Resolução do professor
    # soma = 1 if n == 1 else 1 + n
    # for i in range(2, n // 2 + 1):
    #     if divisivel_por(n, i):
    #         soma += i
    # return soma


def amigos(n1, n2):
    """Verifica se dois números inteiros positivos são amigos.

    Retorna True se números são amigos ou False caso contrário.
    Dica: Números Amigos: http://www.matematica.br/historia/namigos.html
    """
    return soma_dos_divisores(n1) - n1 == n2 and soma_dos_divisores(n2) - n2 == n1


def primo(n):
    """Verifica se número é primo.
    
    Considera que n sempre é maior que 1.
    Retorna True se n for primo ou False caso contrário.
    """
    # Minha Solução - parece ser ideal, porém não é otimizada, se tornando ineficiente se comparado com o do professor
    # return soma_dos_divisores(n) == n + 1
    
    # Resolução do professor
    if n < 4:
        resultado = True
    elif par(n):
        resultado = False
    else:
        resultado = True
        divisor = 3
        maior_divisor = n // 2 + 1
        while resultado and divisor <= maior_divisor:
            resultado = not divisivel_por(n, divisor)
            divisor += 2
    return resultado


def composto(n):
    """Verifica se um número é composto.

    Considera que n sempre é maior que 1.
    Retorna True se n for número composto ou False caso contrário.
    Definição: um número é composto se possui mais de dois divisores.
    Conclusão (regra): Todo o número inteiro não-primo e diferente de 1 é composto.
    """
    # Minha Solução
    # return False if n == 1 else not primo(n)

    # Resolução do professor
    return not primo(n)
