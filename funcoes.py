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
        func="Confira a programação completa: https://www.cisco.com/c/pt_br/training-events/connect.html  \nNeste link você também faz o seu registro para os dias 1 e 2.  \n"

    elif codigo==20:
        # dia 1
        func="A senha para acessar o evento do dia 1 é: Cisco2020  \n"
        
    elif codigo==30:
        # dia 2
        func="Para acessar as sessões de Breakout do dia 2: https://collabpartner.webex.com/collabpartner/onstage/g.php?PRID=65fd67c8ba3d603fc53c57fc5be661ab  \nLembre-se que você precisa estar registrado para participar.  \n"

    elif codigo==40:
        # gravação
        func="As sessões serão gravadas e disponibilizadas na nossa plataforma Cisco Sales Connect.  \nTodos os participantes receberão o link para as grações e as apresentações.  \n"

    #elif codigo==30:
    #    func="Vou pedir para um atendente conversar com você. Aguarde ser chamado aqui no Webex Teams.  \n"
    #    #envia msg para teams
    #    webexmsgRoom(admins_room,f"Usuário {usermail} pediu ajuda.")

        
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
