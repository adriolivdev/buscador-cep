# Buscador de CEP com Python e Tkinter

## Visão Geral

Este projeto é um aplicativo simples que permite ao usuário buscar informações de endereço a partir de um CEP (Código de Endereçamento Postal) brasileiro. Utiliza a API pública ViaCEP para consultar os dados e exibe-os em uma interface gráfica feita com Tkinter.

O objetivo é aplicar boas práticas de engenharia de software, como modularização do código, separação de responsabilidades e documentação clara, facilitando manutenção e evolução futura.

---

## Funcionalidades

- Entrada do CEP pelo usuário
- Validação simples do CEP (deve conter 8 dígitos numéricos)
- Consulta à API ViaCEP para obter dados de endereço (logradouro, bairro, cidade, estado)
- Exibição dos dados em uma interface gráfica amigável
- Tratamento de erros para CEP inválido ou não encontrado

---

## Estrutura do Projeto

buscador_cep/
│
├── app/
│ ├── interface.py # Interface gráfica com Tkinter
│ ├── servico_cep.py # Função que consulta a API ViaCEP
│ ├── controlador.py # Coordena a interação entre interface e serviço
│ └── init.py # Torna o app um pacote Python
│
├── tests/ #  Testes automatizados
│
├── main.py # Ponto de entrada da aplicação
├── requirements.txt # Lista de dependências
└── README.md # Documentação do projeto

## Tecnologias e Bibliotecas

- Python 3.x
- Tkinter (interface gráfica nativa do Python)
- requests (para requisições HTTP à API ViaCEP)

---

## Como Rodar o Projeto

1. Clone este repositório ou baixe os arquivos para seu computador.

2. Instale as dependências (requer `pip` instalado):
pip install -r requirements.txt

3. Execute a aplicação:
python main.py


4. Na janela que abrir, digite um CEP válido (8 dígitos) e clique em "Buscar".

---

## Próximos Passos / Melhorias Futuras

- Adicionar validação mais robusta na entrada do CEP
- Implementar testes automatizados para a função de busca
- Permitir buscas múltiplas sem reiniciar o programa
- Melhorar o design da interface gráfica
- Adicionar suporte a outras APIs ou fontes de dados

---

## Contato

Desenvolvido por Adriolidev
