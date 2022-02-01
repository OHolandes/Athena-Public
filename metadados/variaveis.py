import discord

atividaddes = {
    "jogando": [
        discord.Game(name="pão para pombos"),
        discord.Game(name="GTA VII"),
        discord.Game(name="minha preguiça pela janela")
    ]
}

CANAIS_ADM = {
    "diretoria": 441263190832185350,
    "secretaria": 731689039853518848
}

SAUDACOES = ["Olá!", "Oi!"]

msg_ajuda = "**.ola** | **.oi** | **.iai** | **.athena** : Mande um ola caloroso para mim, e responderei!\n" \
            "**.cool** TEXTO : Você pode me perguntar se algo é COOl(provavelmente sou eu).\n" \
            "**.soma** NUMEROS... : Somo uns números para você.\n" \
            "**.rola** | **.dado** NdN: Consigo rolar uns dados para você se for conveniente. " \
            "Use '.rola 1d1' = 1 dado de 1\n" \
            "**.escolha** | **.prefere** OPÇÕES... : Vou escolher a melhor opção entre algumas opções.\n" \
            "**.meuid** : Envio o seu ID de usuário.\n" \
	    "\n\n" \
            "ADM:\n" \
            "**.teste** REPETE PALAVRA: Repito uma mensagem para saber se estou 'di Boa'\n" \
            "**.ping** : Mando a minha latência (morar nos E.U.A não é para muitos).\n" \
            "**.idchn** : Mando o Id do canal atual.\n" \
            "**.relatorio** : Faço um relatório geral do servidor." \
            "(n de membros, n de boosts, nivel, n de canais, n de categorias, n de cargos...).\n" \
            "**.log** MEMBRO LIMITE AUDIT: Faço um pequeno histórico escolar de um membro especifico. " \
            "Ou o seu, caso não for especificado, " \
            "com o argumento AUDIT=True mostra as últimas LIMITE*2 ações administrativas do servidor. " \
            "Por padrão o limite é 10.\n" \
            "**.kick** MEMBRO: Kicka Algum membro...\n" \
            "**.ban** MEMBRO: Exclui um membro da sociedade.\n" \
            "**.desban** MEMBRO: Se caso você estiver arrependido de ter excluido alguem da sociedade.\n" \
            "**.ajuda** : Esse já é um pouco autoexplicativo não?"
