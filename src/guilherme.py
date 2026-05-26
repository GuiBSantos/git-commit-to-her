# Lógica de decisões e consequência

def aplicar_decisao(opcao, estado):
    """
    Recebe a opção escolhida pelo jogador (A, B, C, D, E ou F)
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
    elif opcao == "D":
        estado = decisao_meme(estado)
    elif opcao == "E":
        estado = decisao_elogio(estado)
    elif opcao == "F":
        estado = decisao_conversa_profunda(estado)
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
        penalidade_interesse = int(15 * personalidade.get("erro_penalidade", 1))
        penalidade_humor = int(10 * personalidade.get("erro_penalidade", 1))
        
        estado["interesse"] -= penalidade_interesse
        estado["humor"] -= penalidade_humor
        print(f"   Mas você mandou mensagem 3 vezes seguidas... ela achou enjoativo. (-{penalidade_interesse} interesse, -{penalidade_humor} humor)")
        estado["mensagens_seguidas"] = 0
    else:
        multiplicador = personalidade.get("msg_interesse", 1)
        bonus_interesse = 0
        
        if estado["humor"] > 50:
            bonus_interesse = int(10 * multiplicador)
            print(f"   Ela amou! (+{bonus_interesse} interesse)")
        else:
            bonus_interesse = int(5 * multiplicador)
            print(f"   Ela respondeu, mas tava quieta hoje. (+{bonus_interesse} interesse)")

        estado["interesse"] += bonus_interesse
        estado["confianca"] += 5
        estado["humor"] += 5
        print("   (+5 confiança, +5 humor)")
        
        estado["mensagens_seguidas"] = estado.get("mensagens_seguidas", 0) + 1

    return estado


def decisao_encontro(estado):
    """
    Opção B — Marcar um encontro.
    O sucesso e a penalidade são afetados pela personalidade.
    """
    print("\n Você tentou marcar um encontro...")
    personalidade = estado["perfil"]["personalidade"]
    
    encontro_deu_certo = estado["confianca"] >= 50 and estado["humor"] > 40

    if encontro_deu_certo:
        multiplicador = personalidade.get("encontro_interesse", 1)
        bonus_interesse = int(20 * multiplicador)
        bonus_confianca = int(10 * multiplicador)
        bonus_humor = int(15 * multiplicador)
        
        estado["interesse"] += bonus_interesse
        estado["confianca"] += bonus_confianca
        estado["humor"] += bonus_humor
        print(f"   Ela topou! Foi incrível. (+{bonus_interesse} interesse, +{bonus_confianca} confiança, +{bonus_humor} humor)")
    else:
        penalidade = int(10 * personalidade.get("erro_penalidade", 1))
        
        estado["interesse"] -= penalidade
        estado["humor"] -= penalidade
        print(f"   Ela achou precipitado... ainda não era hora. (-{penalidade} interesse, -{penalidade} humor)")

    estado["mensagens_seguidas"] = 0

    return estado


def decisao_espaco(estado):
    """
    Opção C — Dar espaço.
    A penalidade por dar espaço é afetada pela personalidade.
    """
    print("\n🌿 Você decidiu dar um espaço hoje...")
    personalidade = estado["perfil"]["personalidade"]
    
    penalidade_interesse = int(5 * personalidade.get("espaco_penalidade", 1))
    
    estado["interesse"] -= penalidade_interesse
    estado["humor"] += 10
    estado["confianca"] += 3

    print(f"   Ela ficou mais tranquila. (-{penalidade_interesse} interesse, +10 humor, +3 confiança)")

    estado["mensagens_seguidas"] = 0

    return estado

def decisao_meme(estado):
    """
    Opção D — Enviar um meme engraçado.
    O efeito depende do humor dela e da sua personalidade.
    """
    print("\n Você enviou um meme que achou a cara dela...")
    personalidade = estado["perfil"]["personalidade"]
    multiplicador = personalidade.get("aprecia_humor", 1.0)

    if estado["humor"] > 60:
        bonus_humor = int(15 * multiplicador)
        bonus_interesse = int(5 * multiplicador)
        estado["humor"] += bonus_humor
        estado["interesse"] += bonus_interesse
        print(f"   Ela gargalhou e compartilhou com as amigas! (+{bonus_humor} humor, +{bonus_interesse} interesse)")
    else:
        bonus_humor = int(10 * multiplicador)
        estado["humor"] += bonus_humor
        print(f"   Ela soltou um 'kkk'. Pelo menos um sorriso você tirou. (+{bonus_humor} humor)")

    if multiplicador < 0.9:
        print("   (Ela não é muito de memes, mas valeu a tentativa)")

    estado["mensagens_seguidas"] = 0
    return estado

def decisao_elogio(estado):
    """
    Opção E — Elogiar algo específico nela.
    Requer um mínimo de confiança para não soar forçado.
    """
    print("\n Você fez um elogio sincero sobre algo que admira nela...")
    personalidade = estado["perfil"]["personalidade"]
    multiplicador = personalidade.get("impacto_elogio", 1.0)

    if estado["confianca"] < 30:
        estado["interesse"] -= 10
        estado["confianca"] -= 5
        print("   Ela achou meio forçado e ficou desconfortável. (-10 interesse, -5 confiança)")
    else:
        bonus_interesse = int(10 * multiplicador)
        bonus_confianca = int(15 * multiplicador)
        estado["interesse"] += bonus_interesse
        estado["confianca"] += bonus_confianca
        print(f"   Ela ficou super sem graça e adorou! (+{bonus_interesse} interesse, +{bonus_confianca} confiança)")

    estado["mensagens_seguidas"] = 0
    return estado

def decisao_conversa_profunda(estado):
    """
    Opção F — Puxar um assunto profundo.
    Ação de alto risco e alta recompensa.
    """
    print("\n Você iniciou uma conversa sobre um assunto mais profundo...")
    personalidade = estado["perfil"]["personalidade"]
    multiplicador = personalidade.get("gosta_de_profundidade", 1.0)

    if estado["confianca"] < 60 or estado["interesse"] < 70:
        penalidade_interesse = int(15 * personalidade.get("erro_penalidade", 1))
        penalidade_humor = int(10 * personalidade.get("erro_penalidade", 1))
        estado["interesse"] -= penalidade_interesse
        estado["humor"] -= penalidade_humor
        print(f"   Ela não estava no clima... a conversa morreu. (-{penalidade_interesse} interesse, -{penalidade_humor} humor)")
    else:
        bonus_interesse = int(25 * multiplicador)
        bonus_confianca = int(20 * multiplicador)
        estado["interesse"] += bonus_interesse
        estado["confianca"] += bonus_confianca
        print(f"   A conversa fluiu por horas e vocês se conectaram muito. (+{bonus_interesse} interesse, +{bonus_confianca} confiança)")

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