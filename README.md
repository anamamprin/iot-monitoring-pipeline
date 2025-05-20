# 📡 Sistema de Monitoramento de Sensores IoT

Este projeto simula um sistema de monitoramento de sensores com foco em segurança doméstica. Ele usa Kafka para transporte de mensagens e MongoDB para persistência dos dados, com enriquecimento das informações recebidas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Apache Kafka
- MongoDB
- Faker
- Pytest

---

## 🧠 Regras de Enriquecimento/Processamento dos dados

Cada mensagem recebida do sensor é enriquecida com duas informações:

### 🔋 battery_status
| Nível de bateria (%) | Status       |
|----------------------|--------------|
| Abaixo de 20         | `CRITICAL`   |
| Entre 20 e 40        | `LOW`        |
| Acima de 40          | `OK`         |



### 🚨 risk_level – Níveis de risco com base em movimento, rostos e horário

| Movimento detectado | Rostos detectados | Faixa de horário | Nível de risco (`risk_level`)    |
|---------------------|-------------------|------------------|----------------------------------|
| `True`              | > 0               | 00h–06h          | `ALTISSIMO`                      |
| `True`              | > 0               | Fora de 00h–06h  | `ALTO`                           |
| `True`              | 0                 | Qualquer         | `MEDIO`                          |
| `False`             | 0                 | Qualquer         | `BAIXO`                          |
| *Qualquer*          | *Qualquer*        | Inválido         | `IMPRECISO` (timestamp inválido) |


## 🐳 Como executar com Docker

### 1. Utilizando o Docker compose

```bash
docker compose up -d --build
```

### 4. Executar os testes com **Pytest**

```bash
pytest -v 
```



## 🚫 Derrubando a aplicação

Para parar a aplicação e remover os containers, utilize:

```bash
docker compose down
```

---

## 👩‍💻 Autora

Ana Paula Mamprin  
Email: [ana.mamprin@hotmail.com](mailto:ana.mamprin@hotmail.com)


