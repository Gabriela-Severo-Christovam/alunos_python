import pytest
from alunos.notas import resultado

def test_calcular_media_entrada_basica_sem_erro():
    #Definindo as entradas
    entrada = [5, 0, 7, 8, 6, 10, 9]

    #Executo o código
    resultado = resultado(entrada)

    #checo a saída
    assert resultado == 6.42