

def atualizar_relacao(estado):

    relacao_atual = estado["relacao"]

    if relacao_atual == "desconhecidos" and estado["interesse"] >= 60:
        estado["relacao"] = "amigos"
        print("\n💛 Você ainda é um beta!")

    elif relacao_atual == "amigos" and estado["interesse"] >= 75 and estado["confianca"] >= 50:
        estado["relacao"] = "Pretendente"
        print("\n🧡 Ela te vê como um pretendente agora! As coisas estão esquentando.")

    elif relacao_atual == "Pretedente" and estado["interesse"] >= 90 and estado["confianca"] >= 75:
        estado["relacao"] = "namoro"
        print("\n❤️  Ela aceitou namorar! Você conseguiu!")

    return estado

def verificar_limites(estado):
   
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


    confianca_ok = estado["confianca"] >= 50
    humor_ok = estado["humor"] > 40

    if confianca_ok and humor_ok:
        return True
    else:
        return False