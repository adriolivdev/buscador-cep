import tkinter as tk
from tkinter import messagebox

def criar_janela(buscar_callback):
    """
    Função que cria a interface gráfica.
    
    Parâmetros:
    buscar_callback (função): Função que será chamada quando o botão 'Buscar' for clicado.
    
    Retorna:
    None
    """
    janela = tk.Tk()
    janela.title("Buscador de CEP")
    janela.geometry("400x300")
    janela.resizable(False, False)

    tk.Label(janela, text="Digite o CEP:", font=("Arial", 12)).pack(pady=5)
    entrada_cep = tk.Entry(janela, font=("Arial", 12), width=20)
    entrada_cep.pack(pady=5)

    botao_buscar = tk.Button(janela, text="Buscar", font=("Arial", 12),
                             command=lambda: buscar_callback(entrada_cep.get()))
    botao_buscar.pack(pady=10)

    def criar_campo(titulo):
        tk.Label(janela, text=titulo, font=("Arial", 10)).pack()
        campo = tk.Entry(janela, font=("Arial", 10), width=40, state='readonly')
        campo.pack(pady=2)
        return campo

    campo_rua = criar_campo("Rua:")
    campo_bairro = criar_campo("Bairro:")
    campo_cidade = criar_campo("Cidade:")
    campo_estado = criar_campo("Estado:")

    # Função para atualizar os campos com dados do CEP
    def atualizar_campos(dados):
        def preencher_campo(campo, texto):
            campo.config(state='normal')
            campo.delete(0, tk.END)
            campo.insert(0, texto)
            campo.config(state='readonly')

        if dados:
            preencher_campo(campo_rua, dados.get("logradouro", ""))
            preencher_campo(campo_bairro, dados.get("bairro", ""))
            preencher_campo(campo_cidade, dados.get("localidade", ""))
            preencher_campo(campo_estado, dados.get("uf", ""))
        else:
            messagebox.showerror("Erro", "CEP inválido ou não encontrado.")
            preencher_campo(campo_rua, "")
            preencher_campo(campo_bairro, "")
            preencher_campo(campo_cidade, "")
            preencher_campo(campo_estado, "")

    # Devolve os elementos que serão usados pelo controlador
    return janela, atualizar_campos
