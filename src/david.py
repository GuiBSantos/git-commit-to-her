# Responsável pela exibição e interface no console

def exibir_status(estado):
    """
    Mostra na tela como estão todas as variáveis do jogo.
    É chamada no início de cada rodada para o jogador saber
    como as coisas estão antes de tomar uma decisão.
    """
    nome_garota = estado["perfil"]["nome"]

    print("\n" + "=" * 40)
    print(f"  💘 Conquistando {nome_garota}  |  Semana {estado['ciclo']}")
    print("=" * 40)
    print(f"  Relacionamento: {estado['relacao'].upper()}")
    print(f"  Interesse de {nome_garota}: {estado['interesse']}/100")
    print(f"  Confiança dela: {estado['confianca']}/100")
    print(f"  Humor dela: {estado['humor']}/100")
    print("=" * 40)


def exibir_menu(pode_encontro):
    """
    Mostra as opções de ação disponíveis para o jogador.
    Recebe um True ou False para avisar se o encontro é uma boa ideia.
    Retorna a opção que o jogador digitou.
    """

    print("\nO que você vai fazer hoje?")
    print("  [A] Mandar uma mensagem fofa")

    if pode_encontro:
        print("  [B] Marcar um encontro  ✅ (bom momento!)")
    else:
        print("  [B] Marcar um encontro  ⚠️  (pode ser cedo demais)")

    print("  [C] Dar espaço hoje")

    opcao = input("\nDigite A, B ou C: ")
    return opcao


def exibir_resultado_final(estado):
    """
    Mostra a mensagem de fim de jogo.
    Pode ser vitória, derrota ou tempo esgotado.
    """
    nome_garota = estado["perfil"]["nome"]

    print("\n" + "=" * 40)

    if estado["relacao"] == "namoro":
        print(f"    VOCÊ CONSEGUIU! {nome_garota.upper()} ACEITOU NAMORAR!")
        print(f"  Durou {estado['ciclo']} semanas de conquista.")

    elif estado["interesse"] <= 0:
        print(f"   DERROTA — {nome_garota} perdeu o interesse.")
        print("  Talvez da próxima vez com mais calma...")

    else:
        print("   TEMPO ESGOTADO — 10 semanas se passaram.")
        print(f"  Vocês e {nome_garota} ficaram em: {estado['relacao']}")
        print("  Quase lá... tente de novo!")

    print("=" * 40)
