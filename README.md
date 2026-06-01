```markdown
# LabSec-PhishSim 🛡️ 🚀

Um ambiente de simulação controlada de Engenharia Social (Phishing) desenvolvido para fins estritamente educacionais, acadêmicos e de conscientização em Segurança da Informação. O projeto integra conceitos avançados de Redes, Sistemas Operacionais (Linux/Windows), Banco de Dados Distribuído (NewSQL) e Criptografia Aplicada.

O ecossistema simula a captura de requisições de um formulário web corporativo, intercepta as entradas em tempo real através de um motor de auditoria híbrido e armazena os metadados de forma segura utilizando funções de resumo criptográfico com persistência simultânea local e em nuvem.

---

## 🏗️ Arquitetura do Sistema e Fluxo de Dados

A infraestrutura é montada sobre uma arquitetura síncrona e resiliente em rede virtualizada via VMware, dividida em três camadas principais:

1. **Front-End (Cenário de Pretexting):** Interface HTML5/CSS3 que replica um portal de autenticação corporativo, distribuído na rede interna através do servidor web Nginx.
2. **Back-End (Motor de Auditoria):** Servidor Flask (Python) configurado no arquivo `capture_server.py` escutando requisições na porta `5000` em todas as interfaces de rede (`0.0.0.0`). O motor intercepta o payload, extrai os metadados do cliente (IP de Origem, User-Agent) e retorna um falso código HTTP `503` (Mecanismo de Pretexting para simular indisponibilidade técnica).
3. **Persistência Híbrida e Criptografia (*Security by Design*):**
   * **Tratamento de Dados:** Aplicação imediata do algoritmo de Hashing SHA-256 sobre as credenciais brutas, impossibilitando o vazamento ou armazenamento de senhas em texto claro.
   * **Persistência Local:** Gravação redundante e estruturada do evento em arquivo físico local (`tentativas_acesso.log`).
   * **Persistência em Nuvem:** Envio síncrono dos metadados estruturados via canal criptografado TLS para um Cluster Serverless **TiDB Cloud** (banco de dados NewSQL distribuído), garantindo integridade forense e centralização dos dados de auditoria.

---

## 🛠️ Tecnologias Utilizadas

* **Sistema Operacional:** Ubuntu Server / Desktop (VMware)
* **Banco de Dados em Nuvem:** TiDB Cloud Serverless (NewSQL Distribuído)
* **Back-End:** Python 3.x, Flask, PyMySQL (Ambiente Virtual `venv`)
* **Front-End:** HTML5, CSS3, Nginx Web Server
* **Segurança:** Criptografia de Fluxo TLS e Resumos Criptográficos SHA-256 (`hashlib`)
* **Versionamento & Deploy:** Git & GitHub

---

## 🗂️ Estrutura de Pastas do Projeto

```text
LabSec-PhishSim/
├── venv/                       # Ambiente virtual isolado do Python 3
├── src/
│   ├── frontend/
│   │   └── index.html          # Interface do formulário de simulação
│   └── backend/
│       ├── capture_server.py   # Motor Flask c/ persistência local + TiDB Cloud
│       └── logs/
│           └── tentativas_acesso.log  # Registro forense local (ignorado no Git)
├── .gitignore                  # Proteção de ambiente virtual e logs locais
└── README.md                   # Documentação técnica do projeto

```

---

## 🕵️‍♂️ Operação e Análise Forense de Logs

### 1. Monitoramento Local em Tempo Real

Para assistir a captura dos metadados entrando no servidor Linux à medida que os usuários interagem com o formulário no host externo (Windows), utilize o comando:

```bash
tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log

```

### 2. Estrutura do Log e Modelagem de Dados (SQL)

Os eventos disparados alimentam simultaneamente o arquivo local e a tabela `auditoria_acessos` no cluster TiDB Cloud. A modelagem segue a estrutura relacional abaixo:

| Campo | Tipo de Dado | Função Forense |
| --- | --- | --- |
| **`id`** | `INT AUTO_INCREMENT` | Chave primária de identificação exclusiva do evento gerenciada na nuvem. |
| **`timestamp`** | `VARCHAR(25)` | Registro cronológico preciso do momento do envio do formulário. |
| **`usuario_alvo`** | `VARCHAR(255)` | Identificador/E-mail submetido na simulação para análise de escopo. |
| **`credential_hash_sha256`** | `CHAR(64)` | Resumo criptográfico da credencial, assegurando a privacidade da informação. |
| **`ip_origem`** | `VARCHAR(45)` | Mapeamento do endereço IP de origem do cliente (vetor de rede). |
| **`user_agent`** | `TEXT` | Identificação de software e navegador utilizado para fingerprinting do host. |

---

## 🚀 Como Executar o Laboratório Localmente

### 1. Configurar o Ambiente Virtual e Dependências

Na pasta raiz do projeto (`~/LabSec-PhishSim`), inicialize o ecossistema Python isolado:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask pymysql

```

### 2. Iniciar o Motor de Captura

Certifique-se de estar com o ambiente virtual `(venv)` ativo, navegue até a pasta do back-end e execute o script principal:

```bash
cd src/backend
python3 capture_server.py

```

### 3. Executar e Testar o Front-End

1. Copie o arquivo `index.html` para a pasta pública do Nginx na sua máquina virtual:
```bash
sudo cp ~/LabSec-PhishSim/src/frontend/index.html /var/www/html/

```


2. Abra o navegador no seu sistema hospedeiro (Windows) e acesse o IP da VM Ubuntu (ex: `http://192.168.204.131`).
3. Preencha o formulário e clique em enviar para validar o fluxo híbrido de gravação local e persistência em nuvem.

---

## ⚖️ Aviso Legal (Disclaimer)

**Este projeto foi desenvolvido estritamente para fins de pesquisa acadêmica, testes de penetração autorizados e treinamento de conscientização de segurança corporativa.** O uso deste código contra sistemas sem consentimento explícito e por escrito dos proprietários é ilegal e passível de penalidades jurídicas. O desenvolvedor não se responsabiliza por eventuais danos causados pelo mau uso desta ferramenta.

---

Developed by [Marcio Souza](https://www.google.com/search?q=https://github.com/marciosouzagcm) 💻

```

```
