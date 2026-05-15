<!-- UNASP · SISTEMAS DE INFORMAÇÃO -->

<div align="center">

# 💘 Git Commit to Her (Simulador de Conquista)

**Simulador interativo em Python**

![UNASP](https://img.shields.io/badge/UNASP-Experiências_pra_Vida-f5a623?style=for-the-badge)

*Lógica de Programação — Centro Universitário Adventista de São Paulo*

</div>

---

## 🎯 Objetivo

O simulador coloca o jogador no papel de um rapaz tentando conquistar a garota mais gata da faculdade. A cada rodada, você toma decisões que afetam o interesse, a confiança e o humor da outra pessoa. O objetivo é chegar ao **namoro** antes de acabar o tempo e não sobrar nada para o beta — sem deixar o interesse cair a zero.

---

## 👥 Equipe

| Integrante | Arquivo | Responsabilidade |
|---|---|---|
| 👨‍💻 **Guilherme** | `guilherme.py` | Lógica de decisões e consequências |
| 🧑‍💻 **Antonio** | `antonio.py` | Estado e progressão do relacionamento |
| 🧑‍💻 **David** | `david.py` | Exibição, menus e interface no console |

### Funções por arquivo

**`guilherme.py`**
```
aplicar_decisao()           → aplica a escolha do jogador no estado
calcular_consequencias()    → computa os efeitos em cada variável
verificar_vitoria_derrota() → checa condições de fim de jogo
```

**`antonio.py`**
```
atualizar_relacao()        → evolui o estágio do relacionamento
verificar_limites()        → mantém variáveis dentro de 0-100
checar_condicao_encontro() → valida se o encontro pode ocorrer
```

**`david.py`**
```
exibir_status()          → mostra o painel de variáveis atual
exibir_menu()            → exibe as opções de decisão
exibir_resultado_final() → mensagem de vitória, derrota ou tempo esgotado
```

---

## 📁 Estrutura do Projeto

```
projeto_simulador/
│
├── main.py          ← loop principal (sem lógica embutida)
├── guilherme.py     ← decisões e consequências
├── antonio.py       ← estado e progressão
└── david.py         ← exibição e interface
```

> `main.py` contém apenas importações, inicialização do estado e o loop principal.

---

## 🧠 Variáveis de Estado

| Variável | Valor Inicial | Faixa | Descrição |
|---|---|---|---|
| `interesse` | `50` | 0–100 | Nível de interesse da pessoa em você. **0 = fim de jogo** |
| `confianca` | `30` | 0–100 | Confiança que a pessoa sente — afeta o sucesso dos encontros |
| `humor` | `50` | 0–100 | Estado de espírito atual — influencia as reações |
| `ciclo` | `1` | 1–10 | Rodada atual (semana do jogo) |
| `relacao` | `"desconhecidos"` | — | Estágio: desconhecidos → amigos → ficantes → **namoro** |

---

## 🎮 Decisões por Ciclo

A cada rodada, escolha uma de 3 ações:

### A — 💬 Mandar flerte por mensagem (Pai tá chave) 
- `interesse` **+10** se `humor > 50`, ou **+5** se `humor ≤ 50`
- `confianca` **+5**
- `humor` **+5**
- ⚠️ Usado 3 vezes seguidas: `interesse` **-15** (enjoativo)

### B — 📅 Marcar um encontro (Sem pressa)
- `interesse` **+20** se `confianca ≥ 50`, ou **-10** se `confianca < 50`
- `confianca` **+10** e `humor` **+15** se o encontro for bem-sucedido
- ✅ Condição de sucesso: `confianca ≥ 50` **e** `humor > 40`

### C — 🌿 Dar espaço (Calma Moreno)
- `interesse` **-5**
- `humor` **+10**
- `confianca` **+3**
- 💡 Recomendado quando `humor < 30` para evitar reações negativas

---

## 🔄 Fluxo em Pseudocódigo

```
INÍCIO
  estado ← {interesse=50, confianca=30, humor=50, ciclo=1, relacao='desconhecidos'}

  ENQUANTO ciclo ≤ 10 E interesse > 0:
    exibir_status(estado)
    opcao ← exibir_menu_e_ler_escolha()
    estado ← aplicar_decisao(opcao, estado)
    estado ← atualizar_relacao(estado)

    SE interesse ≤ 0:
      exibir_derrota(estado)     → ENCERRAR
    SE relacao == 'namoro':
      exibir_vitoria(estado)     → ENCERRAR

    ciclo ← ciclo + 1

  SE ciclo > 10 E relacao != 'namoro':
    exibir_fim_de_tempo(estado)
FIM
```

---

## 🏁 Condições de Encerramento

| Condição | Resultado |
|---|---|
| `relacao == 'namoro'` | ✅ **Vitória** — você conquistou! |
| `interesse ≤ 0` | ❌ **Derrota** — ela perdeu o interesse |
| `ciclo > 10` | ⏰ **Tempo esgotado** — sem namoro no prazo |

---

## ▶️ Como Executar

```bash
python main.py
```

> Requer **Python (Versão a definir)+** · Sem dependências externas (AINDA!)

---

<div align="center">

**UNASP · Experiências pra Vida**
<br>
Guilherme · Antonio · David · 2026

</div>
