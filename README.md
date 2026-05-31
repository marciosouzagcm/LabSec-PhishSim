# LabSec-PhishSim 🛡️ 🚀

Um ambiente de simulação controlada de Engenharia Social (Phishing) desenvolvido para fins estritamente educacionais, acadêmicos e de conscientização em Segurança da Informação. O projeto integra conceitos de Redes, Sistemas Operacionais (Linux/Windows) e Criptografia Aplicada.

O ecossistema simula a captura de requisições de um formulário web corporativo, processa as entradas em tempo real e armazena os metadados de forma segura utilizando funções de resumo criptográfico.

---

## 🏗️ Arquitetura do Sistema e Fluxo de Dados

A infraestrutura foi montada utilizando uma arquitetura híbrida de rede virtualizada via VMware, dividida em três camadas principais:

1. **Front-End (Cenário de Pretexting):** Interface HTML/CSS que replica um portal de autenticação corporativo, servido localmente.
2. **Back-End (Motor de Auditoria):** Servidor Flask (Python) configurado para escutar requisições de rede de forma síncrona, interceptar os dados de formulários e processar metadados do cliente (IP de Origem, User-Agent).
3. **Camada de Criptografia e Log:** Aplicação de algoritmos de Hashing (SHA-256) sobre as credenciais recebidas, garantindo a privacidade dos dados nos arquivos de log (`tentativas_acesso.log`) conforme boas práticas de Segurança Defensiva.

---

## 🛠️ Tecnologias Utilizadas

* **Sistema Operacional:** Ubuntu Server / Desktop (VMware)
* **Back-End:** Python 3.x, Flask (Ambiente Virtual `venv`)
* **Front-End:** HTML5, CSS3
* **Segurança:** Hash SHA-256 (Biblioteca Nativa `hashlib`)
* **Versionamento:** Git & GitHub CLI (`gh`)

---

## 🗂️ Estrutura de Pastas

```text
LabSec-PhishSim/
├── src/
│   ├── frontend/
│   │   └── index.html          # Interface do formulário de simulação
│   └── backend/
│       ├── app.py              # Servidor Flask e motor de processamento
│       └── logs/
│           └── tentativas_acesso.log  # Registro forense estruturado (ignorado no Git)
├── .gitignore                  # Proteção de ambiente virtual e logs locais
└── README.md                   # Documentação do projeto

---

##🕵️‍♂️ Formato do Log Gerado (Análise Forense)

Quando uma requisição é capturada, o motor gera uma entrada estruturada e anonimizada no arquivo de log:
Plaintext

[2026-05-30 23:41:32] IP_ORIGEM: 192.168.204.1 | USUARIO_ALVO: marcio.souza@globalcorp.com | CREDENTIAL_HASH(SHA256): 33a5dc2f4c65ed3f7155af1f9e15b30e2ff796433392a348275f579222d0a677 | NAV_INFO: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...

---

##🚀 Como Executar o Laboratório Localmente
Pró-requisitos

    Python 3 instalado

    Ambiente Linux/Ubuntu (ou Windows com WSL)

1. Clonar o repositório
Bash

git clone [https://github.com/marciosouzagcm/LabSec-PhishSim.git](https://github.com/marciosouzagcm/LabSec-PhishSim.git)
cd LabSec-PhishSim

2. Configurar o Ambiente Virtual do Python
Bash

python3 -m venv venv
source venv/bin/activate
pip install flask

3. Iniciar o Servidor de Auditoria
Bash

cd src/backend
python3 app.py


---


##⚖️ Aviso Legal (Disclaimer)

Este projeto foi desenvolvido estritamente para fins de pesquisa acadêmica, testes de penetração autorizados e treinamento de conscientização de usuários. O uso deste código contra sistemas sem consentimento explícito e por escrito dos proprietários é ilegal e passível de penalidades jurídicas. O desenvolvedor não se responsabiliza pelo mau uso desta ferramenta.
---
Developed by Marcio Souza 💻

