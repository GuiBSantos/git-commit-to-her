# Responsável pelo estado e progressão do relacionamento

def atualizar_relacao(estado):
    """
    Verifica se o relacionamento subiu de nível
    com base nos valores atuais de interesse e confiança.
    Os estágios são: desconhecidos → amigos → crush → namoro
    """

    relacao_atual = estado["relacao"]

    if relacao_atual == "desconhecidos" and estado["interesse"] >= 60:
        estado["relacao"] = "amigos"
        print("\n💛 Vocês viraram amigos! O relacionamento evoluiu.")

    elif relacao_atual == "amigos" and estado["interesse"] >= 75 and estado["confianca"] >= 50:
        estado["relacao"] = "crush"
        print("\n🧡 Ela te vê como um crush agora! As coisas estão esquentando.")

    elif relacao_atual == "crush" and estado["interesse"] >= 90 and estado["confianca"] >= 75:
        estado["relacao"] = "namoro"
        print("\n❤️  Ela aceitou namorar! Você conseguiu!")

    return estado

def verificar_limites(estado):
    """
    Garante que nenhuma variável passe dos limites permitidos.
    Interesse e confiança ficam entre 0 e 100.
    Humor também fica entre 0 e 100.
    Isso evita que os números fiquem impossíveis (tipo interesse = 150).
    """

    if estado["interesse"] > 100:
        estado["interesse"] = 100

    if estado["confianca"] > 100:
        estado["confianca"] = 100

    if estado["humor"] > 100:
        estado["humor"] = 100

    if estado["interesse"] < 0:
        estado["interesse"] = 0

    if estado["confianca"] < 0:
        estado["confianca"] = 0

    if estado["humor"] < 0:
        estado["humor"] = 0

    return estado


def checar_condicao_encontro(estado):
    """
    Diz se as condições para marcar um encontro estão boas.
    Útil para dar uma dica ao jogador antes de ele escolher.
    Retorna True se for um bom momento, False se não for.
    """

    confianca_ok = estado["confianca"] >= 50
    humor_ok = estado["humor"] > 40

    if confianca_ok and humor_ok:
        return True
    else:
        return False