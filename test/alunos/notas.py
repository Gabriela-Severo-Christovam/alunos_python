def resultado(nota: float):


    nota = [5, 0, 7, 8, 6, 10, 9]

    media = sum(nota)/len(nota)
    
    if media < 5 & media >= 0:
        print("REPROVADO")

    if media >= 5 & media < 7:
        print("RECUPERAÇÃO")

    if media >= 7 & media <= 10:
        print("APROVADO")


 
   
    return round(media,1)
