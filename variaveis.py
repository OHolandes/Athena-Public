CANAIS_ADM = {
    "diretoria": 441263190832185350,
    "secretaria": 731689039853518848
}

SAUDACOES = ["Olá!", "Oi!", "Iai!"]
GUIA_ANONIMA_ID = 956319073568976967

msg_ajuda = "**::ola** | **::oi** | **::iai** | **::athena**: Mande um ola caloroso para mim, e responderei!\n" \
            "**::cool** `texto`: Você pode me perguntar se algo é COOl (provavelmente sou eu).\n" \
            "**::soma** `números...`: Somo uns números para você.\n" \
            '**::rola** | **::dado** `NdN`: Consigo rolar uns dados para você se for conveniente.\n' \
            "**::escolha** | **::prefere** `opções...`: Vou escolher a melhor opção entre algumas opções.\n" \
            "**::stalk**: Envio algumas informações suas... Anda stalkeando você mesmo(a)!?.\n" \
            "**::privilegios**: Mostro suas permissões nesse canal.\n" \
            "**::convite**: Mando o convite do servidor.\n" \
            "**::chegamais** `menções...`: Separo um canal para você e mais pessoas ficarem a vontade.\n" \
            "**::ajuda** | **::comandos**: Esse já é um pouco autoexplicativo não?" \
            "\n\n" \
            "**Administração**:\n\n" \
            '**::teste** `repete` `palavra`: Repito uma mensagem para saber se estou "di Boa"\n' \
            '**::prompt**: Abro meu console para você interagir com meu código ||pervertido(a)!||.\n' \
            "**::ping**: Mando a minha latência (morar nos E.U.A é para poucos).\n" \
            "**::cep**: Mando o ID do canal atual.\n" \
            "**::relatorio**: Faço um relatório geral do servidor." \
            "(n de membros, n de boosts, nivel, n de canais, n de categorias, n de cargos...).\n" \
            "**::faxina** `limite`: Dou uma limpeza das últimas (100 por padrão) mensagens no canal atual.\n" \
            "\n" \
            "**::log** `membro`: Faço um pequeno histórico escolar de um membro especifico. " \
            "Ou o seu, caso não for especificado. Por padrão o limite é 15.\n" \
            "\n" \
            "**::basta**: Mando todas as pessoas **comuns** calarem a boca.\n" \
            "**::liberado**: Descalo a boca de todos (talvez não seja uma boa ideia).\n" \
            "**::aviso**: Muto alguém pelos seus crimes contra a nação.\n" \
            "\n" \
            "**::kick** `membro` `motivo`: Dou uma voadora em algum membro...\n" \
            "Você pode **kickar** sem um motivo especificado, porém isso seria abuso de autoridade...\n" \
            "**::ban** `membro` `motivo`: Excluo um membro da sociedade.\n" \
            "Você pode **banir** sem um motivo especificado, porém isso seria abuso de autoridade..." \
            "\n\n\n" \
            "Você ainda pode pedir uma explicação de alto calão de certos comandos usando **::ajuda** `comando`." \
            " Os que tenho alto conhecimento:" \
            "`cool`; `soma`; `rola`; `escolha`; `chegamais`; `basta`; `log`; `ban`/`kick`; `aviso`."


alta_ajuda = {
    "cool": "Digo se algo é _cool_, como por exemplo: ::cool athena",
    "soma": "Só somo uns números: ::soma 2 3 4 3 10",
    "rola": "Rolo um dado descompromissadamente: ::rola 1d20 = 1 dado de 20",
    "escolha": "Use para eu escolher coisas aleatórias, manda as opções em sequência: ::escolha loritta athena disboard",
    "chegamais": """Tenho um sistema de mensagens anônimas.
                    Entre em um desses canais para usufruir:
                    <#956301680679473253>
                    <#957638065596272680>
                    <#957638119560192090>

                    Use `::chegamais` `menções` (onde "menções" são as menções dos membros que queira convidar), o canal será fechado para todos com o cargo **everyone** com exceção de vocês (logicamente os outros como administradores e moderadores poderão ver as mensagens) e será aberto depois de _10 minutos_ de inatividade (fique tranquilo, antes disso eu vou apagar tudo).

                    Obs: Sendo que os de patente alta podem ver as mensagens, não passem os limites, olhem <#441263333807751178> para terem certeza.
                """,
    "basta": "Todos com somente o cargo **everyone** serão impedidos de falar no canal com o comando invocado.",
    "log": "Envio as últimas mensagens de alguém.",
    "aviso": "Dou o cargo @Avisado para um membro e ele não poderá mandar mensagens em qualquer canal, para descastiga-lo use o comando novamente.",
    "kick": "Use para por alguém nas rédias, use-o no canal em que o membro tenha acesso (para deixar as coisas um pouco mais democráticas).",
    "ban": "Use para por alguém nas rédias, use-o no canal em que o membro tenha acesso (para deixar as coisas um pouco mais democráticas)."
}