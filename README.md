# 💘 Git Commit to Her

**Simulador interativo de conquista em Python · Terminal**

[![UNASP](https://img.shields.io/badge/UNASP-Experiências_pra_Vida-f5a623?style=for-the-badge)](https://unasp.br)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Status](https://img.shields.io/badge/Status-Em_desenvolvimento-2EC4B6?style=for-the-badge)]()

*Lógica de Programação — Centro Universitário Adventista de São Paulo*

---

## 🎯 Objetivo

O simulador coloca o jogador no papel de alguém tentando conquistar uma pessoa especial. A cada semana (ciclo), você toma uma decisão que afeta variáveis como interesse, confiança e humor. O objetivo é chegar ao **namoro** antes de acabar as 10 semanas — sem deixar o interesse cair a zero.

Cada jogo é diferente: o perfil da garota é **sorteado aleatoriamente** no início, e cada personalidade reage de forma distinta às mesmas ações.

---

## 👥 Equipe e Responsabilidades

| Integrante | Arquivo | Responsabilidade |
|---|---|---|
| 👨‍💻 **Guilherme** | `guilherme.py` | Lógica de decisões, consequências e condições de fim |
| 🧑‍💻 **Antonio** | `antonio.py` | Estado, progressão do relacionamento e limites |
| 🧑‍💻 **David** | `david.py` | Exibição, menus e interface no console |

---

## 📁 Estrutura do Projeto

```
git-commit-to-her/
└── src/
    ├── main.py        ← orquestra o jogo (sem lógica própria)
    ├── guilherme.py   ← decisões e consequências
    ├── antonio.py     ← estado e progressão
    ├── david.py       ← exibição e interface
    └── perfis.py      ← perfis das garotas (personalidades)
```

> `main.py` contém apenas importações, inicialização do estado e o loop principal. Toda a lógica fica nos arquivos individuais.

---

## 🧠 Variáveis de Estado

| Variável | Valor Inicial | Faixa | Descrição |
|---|---|---|---|
| `interesse` | `50` | 0–100 | Nível de interesse dela em você. **0 = fim de jogo** |
| `confianca` | `30` | 0–100 | Confiança que ela sente — afeta o sucesso de certas ações |
| `humor` | `50` | 0–100 | Estado de espírito atual — influencia as reações |
| `ciclo` | `1` | 1–10 | Semana atual |
| `relacao` | `"desconhecidos"` | — | Estágio: desconhecidos → amigos → pretendente → **namoro** |

---

## 🎮 Decisões por Ciclo

A cada semana, escolha uma de **6 ações**:

### A — 💬 Mandar uma mensagem fofa

- `interesse` **+10** se `humor > 50`, ou **+5** se `humor ≤ 50` (modulado pela personalidade)
- `confianca` **+5** · `humor` **+5**
- ⚠️ Usar 3 vezes seguidas: penalidade de interesse e humor (ela achou enjoativo)

### B — 📅 Marcar um encontro

- ✅ Sucesso se `confianca ≥ 50` **e** `humor > 40`: grandes bônus em interesse, confiança e humor
- ❌ Fracasso: penalidade em interesse e humor (muito cedo)
- Os valores são multiplicados pelo fator `encontro_interesse` da personalidade

### C — 🌿 Dar espaço

- `interesse` **-5** (afetado por `espaco_penalidade`)
- `humor` **+10** · `confianca` **+3**
- 💡 Recomendado quando `humor < 30` para evitar reações negativas

### D — 😂 Enviar um meme engraçado *(novo)*

- `humor > 60`: ela gargalha e compartilha com as amigas (+humor e +interesse)
- `humor ≤ 60`: ela solta um "kkk" (+humor menor)
- Efeitos modulados por `aprecia_humor` — algumas garotas não curtem tanto memes

### E — 💝 Fazer um elogio sincero *(novo)*

- `confianca < 30`: ela acha forçado e reage mal (−interesse, −confiança)
- `confianca ≥ 30`: elogio bem recebido (+interesse, +confiança)
- Amplificado por `impacto_elogio` da personalidade

### F — 🧠 Puxar um assunto profundo *(novo)*

- **Alto risco, alta recompensa**
- Funciona bem apenas se `confianca ≥ 60` **e** `interesse ≥ 70`
- Sucesso: os maiores bônus do jogo (+interesse, +confiança)
- Fracasso: penalidade pesada em interesse e humor
- Modulado por `gosta_de_profundidade`

---

## 👩 Perfis e Personalidades

Cada partida sorteia um perfil diferente. Cada garota tem multiplicadores únicos que afetam os resultados de cada ação:

| Multiplicador | O que faz |
|---|---|
| `msg_interesse` | Amplifica (ou reduz) o bônus de mandar mensagens |
| `encontro_interesse` | Amplifica o bônus de um encontro bem-sucedido |
| `erro_penalidade` | Multiplica as penalidades por erros |
| `aprecia_humor` | Afeta o efeito de enviar memes |
| `impacto_elogio` | Afeta o efeito de fazer elogios |
| `gosta_de_profundidade` | Afeta o efeito de conversas profundas |
| `espaco_penalidade` | Afeta a perda de interesse ao dar espaço |

---

## 🔄 Fluxo em Pseudocódigo

```
INÍCIO
  perfil ← sortear aleatoriamente de GIRLS_PROFILES
  estado ← {interesse=50, confianca=30, humor=50, ciclo=1,
             relacao='desconhecidos', historico=[], perfil=perfil}

  ENQUANTO ciclo ≤ 10 E interesse > 0:
    exibir_status(estado)
    pode_encontro ← checar_condicao_encontro(estado)
    opcao ← exibir_menu(pode_encontro)
    historico.append(opcao)

    estado ← aplicar_decisao(opcao, estado)      ← guilherme.py
    estado ← verificar_limites(estado)           ← antonio.py
    estado ← atualizar_relacao(estado)           ← antonio.py

    resultado ← verificar_vitoria_derrota(estado)
    SE resultado == 'vitoria': exibir_vitoria → ENCERRAR
    SE resultado == 'derrota': exibir_derrota → ENCERRAR

    ciclo ← ciclo + 1

  exibir_resultado_final(estado)   ← inclui histórico de ações
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

## 📋 Funções por Arquivo

### `guilherme.py`

| Função | Descrição |
|---|---|
| `aplicar_decisao(opcao, estado)` | Roteador: recebe A–F e chama a função correta |
| `decisao_mensagem(estado)` | Opção A — mensagem fofa |
| `decisao_encontro(estado)` | Opção B — marcar encontro |
| `decisao_espaco(estado)` | Opção C — dar espaço |
| `decisao_meme(estado)` | Opção D — enviar meme *(novo)* |
| `decisao_elogio(estado)` | Opção E — fazer elogio sincero *(novo)* |
| `decisao_conversa_profunda(estado)` | Opção F — conversa profunda *(novo)* |
| `verificar_vitoria_derrota(estado)` | Retorna `'vitoria'`, `'derrota'` ou `'continua'` |

### `antonio.py`

| Função | Descrição |
|---|---|
| `atualizar_relacao(estado)` | Evolui o estágio: desconhecidos → amigos → pretendente → namoro |
| `verificar_limites(estado)` | Mantém interesse, confiança e humor entre 0 e 100 |
| `checar_condicao_encontro(estado)` | Retorna `True` se o momento é bom para um encontro |

### `david.py`

| Função | Descrição |
|---|---|
| `exibir_status(estado)` | Mostra o painel de variáveis no início de cada semana |
| `exibir_menu(pode_encontro)` | Exibe as 6 opções e lê a escolha do jogador (com validação) |
| `exibir_resultado_final(estado)` | Mensagem de vitória, derrota ou tempo esgotado + histórico |

---

## ▶️ Como Executar

```bash
cd src
python main.py
```

> Requer **Python 3.10+** · Sem dependências externas

---

**UNASP · Experiências pra Vida**  
Guilherme · Antonio · David · 2026
