# Responsável pela exibição e interface no console

def exibir_status(estado):
    """
    Mostra na tela como estão todas as variáveis do jogo.
    É chamada no início de cada rodada para o jogador saber
    como as coisas estão antes de tomar uma decisão.
    """

    print("\n" + "=" * 40)
    print(f"  💘 git-commit-to-her  |  Semana {estado['ciclo']}")
    print("=" * 40)
    print(f"  Relacionamento: {estado['relacao'].upper()}")
    print(f"  Interesse:  {estado['interesse']}/100")
    print(f"  Confiança:  {estado['confianca']}/100")
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

    print("\n" + "=" * 40)

    if estado["relacao"] == "namoro":
        print("    VOCÊ CONSEGUIU! ELA ACEITOU NAMORAR!")
        print(f"  Durou {estado['ciclo']} semanas de conquista.")

    elif estado["interesse"] <= 0:
        print("   DERROTA — ela perdeu o interesse.")
        print("  Talvez da próxima vez com mais calma...")

    else:
        print("   TEMPO ESGOTADO — 10 semanas se passaram.")
        print(f"  Vocês ficaram em: {estado['relacao']}")
        print("  Quase lá... tente de novo!")

    print("=" * 40)
