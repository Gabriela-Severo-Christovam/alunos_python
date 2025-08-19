# def resultado(nota: float):


#     nota = [5, 0, 7, 8, 6, 10, 9]

#     media = sum(nota)/len(nota)
    
#     if media < 5 & media >= 0:
#         print("REPROVADO")

#     if media >= 5 & media < 7:
#         print("RECUPERAÇÃO")

#     if media >= 7 & media <= 10:
#         print("APROVADO")


 
   
#     return round(media,1)


def calcular_media(notas:list[float]) -> float:
    """ 
    Calcule a média de uma lista de notas
    
    Parâmetros:
    notas(list[float]): Lista de notas a serem calculadas 
    
    Retorna:
    float: A média das notas, arredondada para 1 casa decimal acima
    
    """
    if not isinstance(notas, int):
        raise TypeError("Nota invalida.")

    # verificando se é uma lista
    if not isinstance(notas,list[float]):
        raise ValueError("As notas não são uma lista.")
    
    # verificando novamente se é uma lista 
    if type(notas) != list:
        raise TypeError("Nota invalida.")
    
    # validandose é um número
    if not isinstance():
        raise TypeError("nota invalida")
    
    # validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("Não é permitido uma lista vazia.")
    
    # validando se todos elementos da lista são números 
    for nota in notas:
        if not type(nota) == int and not type(nota) == float:
            raise TypeError("Nota invalida.")
        if nota < 0 or nota > 10:
            raise ValueError("Nota invalida.")

    # media = sum(notas)/len(notas)
    # return round(media,1)
    
    total = sum(notas)  # soma
    quantidade = len(notas)  # numera quantas existem
    media = total / quantidade  # divide o total de notas
    return media

def aprovacao(media):
    if media < 5:
        print ("Aluno Reprovado")
    elif media >=5:
        print ("Aluno De recuperação")
    else:
        print("Aluno Aprovado ")