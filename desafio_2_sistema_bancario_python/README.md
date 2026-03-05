# 💰 Sistema Bancário em Python

Este projeto foi desenvolvido como parte de um desafio prático de programação em **Python**, com apoio do professor durante o Bootcamp.

O objetivo foi criar um **sistema bancário simples no terminal**, capaz de simular operações básicas realizadas por clientes de um banco.

O sistema permite realizar depósitos, saques e consultar o extrato da conta, aplicando regras de negócio comuns em instituições financeiras.

---

# 📌 Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

```
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
```

### 💵 Depósito
Permite adicionar valores ao saldo da conta.

Regras:
- O valor precisa ser **maior que zero**
- O valor **não pode ser negativo**
- O valor é armazenado no saldo
- A operação é registrada no **extrato**

---

### 💸 Saque
Permite retirar valores do saldo disponível.

Regras implementadas:

- Máximo de **3 saques por dia**
- Valor máximo por saque: **R$ 500**
- O saque **não pode ultrapassar o saldo disponível**
- O valor precisa ser **maior que zero**
- O valor **não pode ser negativo**
- Cada saque realizado é registrado no **extrato**

---

### 📄 Extrato

Exibe todas as movimentações realizadas na conta.

O extrato mostra:

- Histórico de **depósitos**
- Histórico de **saques**
- **Saldo atual da conta**

Caso nenhuma movimentação tenha sido realizada, o sistema informa que não há registros.

---

# 🧠 Conceitos de Python aplicados

Durante o desenvolvimento deste projeto, foram utilizados diversos conceitos fundamentais da linguagem:

- Estruturas condicionais (`if`, `elif`, `else`)
- Estrutura de repetição (`while`)
- Variáveis e controle de estado
- Operações matemáticas
- Manipulação de **strings**
- **f-strings** para formatação de valores monetários
- **Operador ternário** para simplificar condições
- Controle de fluxo do programa
- Interação com o usuário via `input()`

---

# 🧾 Estrutura do Código

O sistema utiliza algumas variáveis principais para controlar as operações:

| Variável | Função |
|--------|--------|
| `saldo` | Armazena o valor disponível na conta |
| `limite` | Define o valor máximo permitido por saque |
| `extrato` | Guarda o histórico de movimentações |
| `numero_saques` | Conta quantos saques foram realizados |
| `LIMITE_SAQUES` | Define o número máximo de saques permitidos |

---

# 📊 Registro das movimentações

Todas as operações são armazenadas na variável `extrato`, funcionando como um **histórico de transações**.


---

# 🖥️ Exemplo de uso

```
[d] Depósito
[s] Saque   
[e] Extrato 
[q] Sair    

=>d
Informe o valor do depósito: 1000

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=>s
Informe o valor do saque: 200

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=>d
Informe o valor do depósito: 100

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=>s
Informe o valor do saque: 500

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=>e

================ EXTRATO ================
Depósito: R$ 1000.00
Saque: R$ 200.00
Depósito: R$ 100.00
Saque: R$ 500.00


Saldo: R$ 400.00
==========================================

```

---

# 🛠️ Tecnologias utilizadas

- Python 3

---

# 🎯 Objetivo do projeto

Este projeto teve como objetivo praticar **lógica de programação e fundamentos da linguagem Python**, simulando um sistema bancário simples baseado em regras de negócio.

Além disso, o desafio ajudou a desenvolver habilidades como:

- organização de código
- controle de fluxo
- validação de operações
- registro de histórico de transações

---

⭐ Projeto desenvolvido para fins de estudo durante o Bootcamp.
