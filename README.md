# 💘 Simulador de Conquista

> Simulador textual interativo em Python — trabalho de faculdade

---

## 🎯 Objetivo

Colocar o jogador no papel de alguém tentando conquistar uma pessoa especial. A cada rodada, você toma decisões que afetam diretamente o interesse, a confiança e o humor da outra pessoa. O objetivo é chegar ao namoro antes de acabar o tempo — sem deixar o interesse cair a zero.

---

## 📁 Estrutura do Projeto

```
projeto_simulador/
│
├── main.py          ← loop principal do jogo (sem lógica embutida)
├── guilherme.py     ← lógica de decisões e consequências
├── antonio.py       ← estado e progressão do relacionamento
└── david.py         ← exibição, menus e interface no console
```

---

## 👥 Divisão de Responsabilidades

| Integrante | Arquivo | Responsabilidade | Funções |
|---|---|---|---|
| Guilherme | `guilherme.py` | Decisões e lógica central | `aplicar_decisao()`, `calcular_consequencias()`, `verificar_vitoria_derrota()` |
| Antonio | `antonio.py` | Estado e progressão | `atualizar_relacao()`, `verificar_limites()`, `checar_condicao_encontro()` |
| David | `david.py` | Exibição e interface | `exibir_status()`, `exibir_menu()`, `exibir_resultado_final()` |

---

## 🧠 Variáveis de Estado

| Variável | Descrição | Valor Inicial | Faixa |
|---|---|---|---|
| `interesse` | O quanto a pessoa está interessada em você | 50 | 0–100 (0 = fim de jogo) |
| `confianca` | Nível de confiança que a pessoa sente | 30 | 0–100 |
| `humor` | Estado de espírito da pessoa no ciclo atual | 50 | 0–100 |
| `ciclo` | Número da rodada (semana do jogo) | 1 | 1–10 |
| `relacao` | Estágio do relacionamento | `"desconhecidos"` | desconhecidos → amigos → crush → namoro |

---

## 🎮 Decisões por Ciclo

A cada rodada, o jogador escolhe uma de 3 ações:

### A — Mandar mensagem fofa 💬
- `interesse` +10 se `humor > 50`, ou +5 se `humor ≤ 50`
- `confianca` +5
- `humor` +5
- ⚠️ Se usado 3 vezes seguidas: `interesse` -15 (enjoativo)

### B — Marcar um encontro 📅
- `interesse` +20 se `confianca ≥ 50`, ou -10 se `confianca < 50`
- `humor` +15 se der certo, -10 se der errado
- `confianca` +10 se o encontro for bem-sucedido
- ✅ Condição de sucesso: `confianca ≥ 50` e `humor > 40`

### C — Dar espaço 🌿
- `interesse` -5
- `humor` +10
- `confianca` +3
- 💡 Útil quando `humor < 30` para evitar reações negativas

---

## 🔄 Fluxo do Jogo

```
INÍCIO
  estado ← {interesse=50, confianca=30, humor=50, ciclo=1, relacao='desconhecidos'}

  ENQUANTO ciclo ≤ 10 E interesse > 0:
    exibir_status(estado)
    opcao ← exibir_menu_e_ler_escolha()
    estado ← aplicar_decisao(opcao, estado)
    estado ← atualizar_relacao(estado)

    SE interesse ≤ 0:
      exibir_derrota(estado)
      ENCERRAR

    SE relacao == 'namoro':
      exibir_vitoria(estado)
      ENCERRAR

    ciclo ← ciclo + 1

  SE ciclo > 10 E relacao != 'namoro':
    exibir_fim_de_tempo(estado)
FIM
```

---

## 🏁 Condições de Encerramento

| Condição | Resultado |
|---|---|
| `relacao == 'namoro'` | ✅ Vitória — você conquistou! |
| `interesse ≤ 0` | ❌ Derrota — ela perdeu o interesse |
| `ciclo > 10` | ⏰ Tempo esgotado — sem namoro |

---

## ▶️ Como Executar

```bash
python main.py
```

> Requer Python 3.8+. Sem dependências externas.
