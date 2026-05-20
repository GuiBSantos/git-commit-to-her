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
    Se o humor dela estiver bom (acima de 50), ela responde melhor.
    Se o humor estiver ruim, o efeito é menor.
    Tem um risco: usar demais fica enjoativo.
    """
    print("\n💬 Você mandou uma mensagem fofa...")

    if estado["humor"] > 50:
        estado["interesse"] += 10
        print("   Ela amou! (+10 interesse)")
    else:
        estado["interesse"] += 5
        print("   Ela respondeu, mas tava quieta hoje. (+5 interesse)")

    estado["confianca"] += 5
    estado["humor"] += 5
    print("   (+5 confiança, +5 humor)")

    if estado.get("mensagens_seguidas", 0) >= 2:
        estado["interesse"] -= 15
        print("   Mas você mandou mensagem 3 vezes seguidas... ela achou enjoativo. (-15 interesse)")
        estado["mensagens_seguidas"] = 0
    else:
        estado["mensagens_seguidas"] = estado.get("mensagens_seguidas", 0) + 1

    return estado


def decisao_encontro(estado):
    """
    Opção B — Marcar um encontro.
    Só funciona bem se a confiança e o humor dela estiverem altos.
    Se for cedo demais, ela pode achar precipitado.
    """
    print("\n📅 Você tentou marcar um encontro...")

    encontro_deu_certo = estado["confianca"] >= 50 and estado["humor"] > 40

    if encontro_deu_certo:
        estado["interesse"] += 20
        estado["confianca"] += 10
        estado["humor"] += 15
        print("   Ela topou! Foi incrível. (+20 interesse, +10 confiança, +15 humor)")
    else:
        estado["interesse"] -= 10
        estado["humor"] -= 10
        print("   Ela achou precipitado... ainda não era hora. (-10 interesse, -10 humor)")

    estado["mensagens_seguidas"] = 0

    return estado


def decisao_espaco(estado):
    """
    Opção C — Dar espaço, não fazer nada por hoje.
    Perde um pouco de interesse, mas ela descansa e fica mais receptiva depois.
    Útil quando o humor dela está muito baixo.
    """
    print("\n🌿 Você decidiu dar um espaço hoje...")

    estado["interesse"] -= 5
    estado["humor"] += 10
    estado["confianca"] += 3
    print("   Ela ficou mais tranquila. (-5 interesse, +10 humor, +3 confiança)")

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