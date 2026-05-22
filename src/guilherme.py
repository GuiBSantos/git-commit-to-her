# Lógica de decisões e consequência

def aplicar_decisao(opcao, estado):
    """
    Recebe a opção escolhida pelo jogador (A, B ou C)
    e o estado atual do jogo, e chama a função certa.
    Retorna o estado atualizado.
    """
    opcao = opcao.upper()

    if opcao == "A":
        estado = decisao_mensagem(estado)
    elif opcao == "B":
        estado = decisao_encontro(estado)
    elif opcao == "C":
        estado = decisao_espaco(estado)
    else:
        print("Opção inválida. Nenhuma ação foi tomada.")

    return estado

def decisao_mensagem(estado):
    """
    Opção A — Mandar uma mensagem fofa.
    O efeito varia conforme a personalidade da garota.
    """
    print("\n💬 Você mandou uma mensagem fofa...")
    personalidade = estado["perfil"]["personalidade"]

    if estado.get("mensagens_seguidas", 0) >= 2:
        penalidade_interesse = int(15 * personalidade["erro_penalidade"])
        penalidade_humor = int(10 * personalidade["erro_penalidade"])
        
        estado["interesse"] -= penalidade_interesse
        estado["humor"] -= penalidade_humor
        print(f"   Mas você mandou mensagem 3 vezes seguidas... ela achou enjoativo. (-{penalidade_interesse} interesse, -{penalidade_humor} humor)")
        estado["mensagens_seguidas"] = 0
    else:
        multiplicador = personalidade["msg_interesse"]
        bonus_interesse = 0
        
        if estado["humor"] > 50:
            bonus_interesse = int(10 * multiplicador)
            print(f"   Ela amou! (+{bonus_interesse} interesse)")
        else:
            bonus_interesse = int(5 * multiplicador)
            print(f"   Ela respondeu, mas tava quieta hoje. (+{bonus_interesse} interesse)")

        estado["interesse"] += bonus_interesse
        estado["confianca"] += 5  # Confiança e humor podem ter bônus base
        estado["humor"] += 5
        print("   (+5 confiança, +5 humor)")
        
        estado["mensagens_seguidas"] = estado.get("mensagens_seguidas", 0) + 1

    return estado


def decisao_encontro(estado):
    """
    Opção B — Marcar um encontro.
    O sucesso e a penalidade são afetados pela personalidade.
    """
    print("\n📅 Você tentou marcar um encontro...")
    personalidade = estado["perfil"]["personalidade"]
    
    encontro_deu_certo = estado["confianca"] >= 50 and estado["humor"] > 40

    if encontro_deu_certo:
        bonus_interesse = int(20 * personalidade["encontro_interesse"])
        bonus_confianca = int(10 * personalidade["encontro_interesse"])
        bonus_humor = int(15 * personalidade["encontro_interesse"])
        
        estado["interesse"] += bonus_interesse
        estado["confianca"] += bonus_confianca
        estado["humor"] += bonus_humor
        print(f"   Ela topou! Foi incrível. (+{bonus_interesse} interesse, +{bonus_confianca} confiança, +{bonus_humor} humor)")
    else:
        penalidade_interesse = int(10 * personalidade["erro_penalidade"])
        penalidade_humor = int(10 * personalidade["erro_penalidade"])
        
        estado["interesse"] -= penalidade_interesse
        estado["humor"] -= penalidade_humor
        print(f"   Ela achou precipitado... ainda não era hora. (-{penalidade_interesse} interesse, -{penalidade_humor} humor)")

    estado["mensagens_seguidas"] = 0

    return estado


def decisao_espaco(estado):
    """
    Opção C — Dar espaço.
    A penalidade por dar espaço é afetada pela personalidade.
    """
    print("\n🌿 Você decidiu dar um espaço hoje...")
    personalidade = estado["perfil"]["personalidade"]
    
    penalidade_interesse = int(5 * personalidade["espaco_penalidade"])
    
    estado["interesse"] -= penalidade_interesse
    estado["humor"] += 10
    estado["confianca"] += 3

    print(f"   Ela ficou mais tranquila. (-{penalidade_interesse} interesse, +10 humor, +3 confiança)")

    estado["mensagens_seguidas"] = 0

    return estado


def verificar_vitoria_derrota(estado):
    """
    Verifica se o jogo acabou.
    Retorna "vitoria", "derrota" ou "continua".
    """
    if estado["relacao"] == "namoro":
        return "vitoria"
    elif estado["interesse"] <= 0:
        return "derrota"
    else:
        return "continua"