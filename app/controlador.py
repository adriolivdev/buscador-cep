from app import servico_cep, interface

def iniciar_aplicacao():
    """
    Função principal que inicia a aplicação conectando interface e lógica.
    """
    # Esta função será chamada ao clicar no botão "Buscar"
    def buscar_cep(cep_digitado):
        dados = servico_cep.buscar_cep_api(cep_digitado)
        interface.atualizar_campos(dados)

    janela, interface.atualizar_campos = interface.criar_janela(buscar_cep)
    janela.mainloop()
