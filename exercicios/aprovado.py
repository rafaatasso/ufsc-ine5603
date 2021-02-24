def aprovado(nota1, nota2, nota3):
    menor = nota1 if nota1 < nota2 else nota2
    menor = nota3 if nota3 < menor else menor
    media = (nota1 + nota2 + nota3 - menor)/2
    return media >= 5.75
