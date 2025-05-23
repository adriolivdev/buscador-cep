import requests

def buscar_cep_api(cep: str) -> dict:
    """
    Função que chama a API ViaCEP e retorna os dados do CEP.
    
    Parâmetros:
    cep (str): CEP com 8 dígitos (exemplo: '01001000')
    
    Retorna:
    dict: Dados do endereço (rua, bairro, cidade, estado) ou vazio se erro.
    """
    if not cep.isdigit() or len(cep) != 8:
        return {}

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        if "erro" in dados:
            return {}
        return dados
    except requests.exceptions.RequestException:
        return {}
