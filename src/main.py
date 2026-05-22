import random
from perfis import GIRLS_PROFILES
from guilherme import aplicar_decisao, verificar_vitoria_derrota
from antonio import atualizar_relacao, verificar_limites, checar_condicao_encontro
from david import exibir_status, exibir_menu, exibir_resultado_final

chave_perfil_sorteado = random.choice(list(GIRLS_PROFILES.keys()))
perfil_ativo = GIRLS_PROFILES[chave_perfil_sorteado]

estado = {
    "interesse": 50,
    "confianca": 30,
    "humor": 50,
    "ciclo": 1,
    "relacao": "desconhecidos",
    "mensagens_seguidas": 0,
    "perfil": perfil_ativo
}

print("\n Bem-vindo ao git-commit-to-her!")
print("Você tem 10 semanas para conquistar alguém especial.")
print("Tome boas decisões — cada escolha importa.\n")

print("=" * 40)
print("VOCÊ DEU MATCH COM:")
print(f"  Nome: {estado['perfil']['nome']}, {estado['perfil']['idade']} anos")
print(f"  Bio: {estado['perfil']['bio']}")
print("=" * 40)
input("Pressione Enter para começar a primeira semana...")

while estado["ciclo"] <= 10 and estado["interesse"] > 0:
    exibir_status(estado)
    pode_encontro = checar_condicao_encontro(estado)
    opcao = exibir_menu(pode_encontro)
    estado = aplicar_decisao(opcao, estado)
    estado = verificar_limites(estado)
    estado = atualizar_relacao(estado)
    resultado = verificar_vitoria_derrota(estado)
    if resultado != "continua":
        break
    estado["ciclo"] += 1

exibir_resultado_final(estado)