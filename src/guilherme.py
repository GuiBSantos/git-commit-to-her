
def alterar_status(estado, interesse=0, confianca=0, humor=0):
    estado["interesse"] += interesse
    estado["confianca"] += confianca
    estado["humor"] += humor

def resetar_mensagens(estado):
    estado["mensagens_seguidas"] = 0

def aplicar_decisao(opcao, estado):

    opcao = opcao.upper()

    if opcao not in ACOES:
        print("Opção inválida. Nenhuma ação foi tomada.")
        return estado

    return ACOES[opcao](estado)

def decisao_mensagem(estado):

    print("\n💬 Você mandou uma mensagem fofa...")

    personalidade = estado["perfil"]["personalidade"]

    if estado.get("mensagens_seguidas", 0) >= 2:

        penalidade_interesse = int(
            15 * personalidade.get("erro_penalidade", 1)
        )

        penalidade_humor = int(
            10 * personalidade.get("erro_penalidade", 1)
        )

        alterar_status(
            estado,
            interesse=-penalidade_interesse,
            humor=-penalidade_humor
        )

        print(
            f"   Mas você mandou mensagem 3 vezes seguidas..."
            f" (-{penalidade_interesse} interesse,"
            f" -{penalidade_humor} humor)"
        )

        resetar_mensagens(estado)

    else:

        multiplicador = personalidade.get("msg_interesse", 1)

        if estado["humor"] > 50:
            bonus_interesse = int(10 * multiplicador)
            print(f"   Ela amou! (+{bonus_interesse} interesse)")
        else:
            bonus_interesse = int(5 * multiplicador)
            print(
                f"   Ela respondeu, mas tava quieta hoje."
                f" (+{bonus_interesse} interesse)"
            )

        alterar_status(
            estado,
            interesse=bonus_interesse,
            confianca=5,
            humor=5
        )

        print("   (+5 confiança, +5 humor)")

        estado["mensagens_seguidas"] = (
            estado.get("mensagens_seguidas", 0) + 1
        )

    return estado

def decisao_encontro(estado):

    print("\n Você tentou marcar um encontro...")

    personalidade = estado["perfil"]["personalidade"]

    encontro_deu_certo = (
        estado["confianca"] >= 50
        and estado["humor"] > 40
    )

    if encontro_deu_certo:

        multiplicador = personalidade.get(
            "encontro_interesse", 1
        )

        bonus_interesse = int(20 * multiplicador)
        bonus_confianca = int(10 * multiplicador)
        bonus_humor = int(15 * multiplicador)

        alterar_status(
            estado,
            interesse=bonus_interesse,
            confianca=bonus_confianca,
            humor=bonus_humor
        )

        print(
            f"   Ela topou! Foi incrível."
            f" (+{bonus_interesse} interesse,"
            f" +{bonus_confianca} confiança,"
            f" +{bonus_humor} humor)"
        )

    else:

        penalidade = int(
            10 * personalidade.get("erro_penalidade", 1)
        )

        alterar_status(
            estado,
            interesse=-penalidade,
            humor=-penalidade
        )

        print(
            f"   Ela achou precipitado..."
            f" (-{penalidade} interesse,"
            f" -{penalidade} humor)"
        )

    resetar_mensagens(estado)

    return estado

def decisao_espaco(estado):

    print("\n🌿 Você decidiu dar um espaço hoje...")

    personalidade = estado["perfil"]["personalidade"]

    penalidade_interesse = int(
        5 * personalidade.get("espaco_penalidade", 1)
    )

    alterar_status(
        estado,
        interesse=-penalidade_interesse,
        confianca=3,
        humor=10
    )

    print(
        f"   Ela ficou mais tranquila."
        f" (-{penalidade_interesse} interesse,"
        f" +10 humor, +3 confiança)"
    )

    resetar_mensagens(estado)

    return estado

def decisao_meme(estado):

    print("\n Você enviou um meme que achou a cara dela...")

    personalidade = estado["perfil"]["personalidade"]

    multiplicador = personalidade.get(
        "aprecia_humor", 1.0
    )

    if estado["humor"] > 60:

        bonus_humor = int(15 * multiplicador)
        bonus_interesse = int(5 * multiplicador)

        alterar_status(
            estado,
            humor=bonus_humor,
            interesse=bonus_interesse
        )

        print(
            f"   Ela gargalhou!"
            f" (+{bonus_humor} humor,"
            f" +{bonus_interesse} interesse)"
        )

    else:

        bonus_humor = int(10 * multiplicador)

        alterar_status(
            estado,
            humor=bonus_humor
        )

        print(
            f"   Ela soltou um 'kkk'."
            f" (+{bonus_humor} humor)"
        )

    if multiplicador < 0.9:
        print(
            "   (Ela não é muito de memes,"
            " mas valeu a tentativa)"
        )

    resetar_mensagens(estado)

    return estado

def decisao_elogio(estado):

    print(
        "\n Você fez um elogio sincero "
        "sobre algo que admira nela..."
    )

    personalidade = estado["perfil"]["personalidade"]

    multiplicador = personalidade.get(
        "impacto_elogio", 1.0
    )

    if estado["confianca"] < 30:

        alterar_status(
            estado,
            interesse=-10,
            confianca=-5
        )

        print(
            "   Ela achou meio forçado."
            " (-10 interesse, -5 confiança)"
        )

    else:

        bonus_interesse = int(10 * multiplicador)
        bonus_confianca = int(15 * multiplicador)

        alterar_status(
            estado,
            interesse=bonus_interesse,
            confianca=bonus_confianca
        )

        print(
            f"   Ela adorou!"
            f" (+{bonus_interesse} interesse,"
            f" +{bonus_confianca} confiança)"
        )

    resetar_mensagens(estado)

    return estado

def decisao_conversa_profunda(estado):

    print(
        "\n Você iniciou uma conversa "
        "sobre um assunto mais profundo..."
    )

    personalidade = estado["perfil"]["personalidade"]

    multiplicador = personalidade.get(
        "gosta_de_profundidade", 1.0
    )

    if (
        estado["confianca"] < 60
        or estado["interesse"] < 70
    ):

        penalidade_interesse = int(
            15 * personalidade.get(
                "erro_penalidade", 1
            )
        )

        penalidade_humor = int(
            10 * personalidade.get(
                "erro_penalidade", 1
            )
        )

        alterar_status(
            estado,
            interesse=-penalidade_interesse,
            humor=-penalidade_humor
        )

        print(
            f"   Ela não estava no clima."
            f" (-{penalidade_interesse} interesse,"
            f" -{penalidade_humor} humor)"
        )

    else:

        bonus_interesse = int(
            25 * multiplicador
        )

        bonus_confianca = int(
            20 * multiplicador
        )

        alterar_status(
            estado,
            interesse=bonus_interesse,
            confianca=bonus_confianca
        )

        print(
            f"   A conversa fluiu."
            f" (+{bonus_interesse} interesse,"
            f" +{bonus_confianca} confiança)"
        )

    resetar_mensagens(estado)

    return estado

def verificar_vitoria_derrota(estado):

    if estado["relacao"] == "namoro":
        return "vitoria"

    if estado["interesse"] <= 0:
        return "derrota"

    return "continua"

ACOES = {
    "A": decisao_mensagem,
    "B": decisao_encontro,
    "C": decisao_espaco,
    "D": decisao_meme,
    "E": decisao_elogio,
    "F": decisao_conversa_profunda
}