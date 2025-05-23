import pytest
from app.servico_cep import buscar_cep_api

def test_cep_valido():
    """
    Testa se a função retorna dados corretos para um CEP válido conhecido.
    Exemplo de CEP: 01001000 (Praça da Sé, SP)
    """
    cep = "01001000"
    resultado = buscar_cep_api(cep)
    
    assert resultado != {}, "Deve retornar dados para CEP válido"
    assert resultado.get("logradouro") == "Praça da Sé", "Logradouro deve ser Praça da Sé"
    assert resultado.get("uf") == "SP", "Estado deve ser SP"

def test_cep_invalido_formatacao():
    """
    Testa se a função retorna vazio para CEP com formato inválido (não numérico).
    """
    cep = "ABCDE123"
    resultado = buscar_cep_api(cep)
    assert resultado == {}, "Deve retornar vazio para CEP com formato inválido"

def test_cep_invalido_tamanho():
    """
    Testa se a função retorna vazio para CEP com tamanho diferente de 8 caracteres.
    """
    cep = "12345"
    resultado = buscar_cep_api(cep)
    assert resultado == {}, "Deve retornar vazio para CEP com tamanho inválido"

def test_cep_nao_encontrado():
    """
    Testa se a função retorna vazio para um CEP que não existe (erro na API).
    """
    cep = "00000000"
    resultado = buscar_cep_api(cep)
    assert resultado == {}, "Deve retornar vazio para CEP não encontrado"
