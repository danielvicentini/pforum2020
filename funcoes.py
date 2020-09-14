# -*- coding: utf-8 -*-


# custom comands function for this bot
from config import le_config
from config import admins_room

from webexteams import webexmsgRoom

# Parte 1
# Defina aqui suas funções


# Parte 2
# Trate aqui seus comandos
# identifique o que foi pedido pela variável codigo
# os parametros digitados estao em formato de lista na variável lista_parametros

def executa(usermail, codigo, lista_parametros):

    # deve retornar em formato de texto + arquivo com msg e arquivo

    # Variáveis que podem ser retornadas
    # MSG = O texto que é Obrigatório
    # Arquivo = Um arquivo que é anexado a mensagem no Teams
    # CARD = um Card do Webex no formato JSON (FUTURO)

    func=""
    #para msg
    msg=""
    #para arquivo
    arquivo=""
    # card (FUTURO)
    # card é um json
    

    # a Partir daqui trata suas funções conforme código

    if codigo==10:
        # função sem parâmetro
        func="O site do evento é ***http://partnerforum.cisco.com.br***  \n"
        
    elif codigo==20:
        func="Os contatos da Ingrm Micro: ***fulano@ingrammicro.com***, telefone: ***11 4000-4000***  \n"
        
    elif codigo==30:
        func="Vou pedir para um atendente conversar com você. Aguarde ser chamado aqui no Webex Teams.  \n"
        #envia msg para teams
        webexmsgRoom(admins_room,f"Usuário {usermail} pediu ajuda.")

        
    # monta mensagem para retornar
    msg=msg+func
        
    return msg,arquivo

def executa_puro(comando, usermail):

    # usar esta funcão para definir sua própria lógica
    # retornar msg e arquivo para webex teams apresentar na mensagem

    msg=""
    arquivo=""

    msg=f"comando digitado: {comando}. Digitado por {usermail}"

    return msg,arquivo
