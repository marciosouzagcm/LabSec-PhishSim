```markdown
# LabSec-PhishSim 🛡️ 🚀

Um ambiente de simulação controlada de Engenharia Social (Phishing) desenvolvido para fins estritamente educacionais, acadêmicos e de conscientização em Segurança da Informação. O projeto integra conceitos de Redes, Sistemas Operacionais (Linux/Windows) e Criptografia Aplicada.

O ecossistema simula a captura de requisições de um formulário web corporativo, processa as entradas em tempo real através de um motor de auditoria e armazena os metadados de forma segura utilizando funções de resumo criptográfico.

---

## 🏗️ Arquitetura do Sistema e Fluxo de Dados

A infraestrutura é montada utilizando uma arquitetura híbrida de rede virtualizada via VMware, dividida em três camadas principais:

1. **Front-End (Cenário de Pretexting):** Interface HTML/CSS que replica um portal de autenticação corporativo, servido localmente ou via Nginx.
2. **Back-End (Motor de Auditoria):** Servidor Flask (Python) configurado no arquivo `capture_server.py` para escutar requisições de rede de forma síncrona na porta `5000`, interceptar dados de formulários e processar metadados do cliente (IP de Origem, User-Agent).
3. **Camada de Persistência e Criptografia:** Aplicação de algoritmos de Hashing (SHA-256) sobre as credenciais recebidas, garantindo a privacidade dos dados antes do armazenamento nos logs locais (`tentativas_acesso.log`).

### 🗺️ Próxima Fase: Expansão para a Nuvem
O projeto prevê a migração do armazenamento local para um modelo centralizado, onde o `capture_server.py` enviará os payloads anonimizados via TLS para um Banco de Dados na Nuvem (**MongoDB Atlas** ou **PostgreSQL**), aumentando a resiliência forense do ambiente.

---

## 🛠️ Tecnologias Utilizadas

* **Sistema Operacional:** Ubuntu Server / Desktop (VMware)
* **Back-End:** Python 3.x, Flask (Ambiente Virtual `venv`)
* **Front-End:** HTML5, CSS3
* **Segurança:** Hash SHA-256 (Biblioteca Nativa `hashlib`)
* **Versionamento & Deploy:** Git & GitHub CLI (`gh`)

---

## 🗂️ Estrutura de Pastas Atualizada

```text
LabSec-PhishSim/
├── venv/                       # Ambiente virtual isolado do Python 3
├── src/
│   ├── frontend/
│   │   └── index.html          # Interface do formulário de simulação
│   └── backend/
│       ├── capture_server.py   # Motor Flask e processamento de requisições
│       └── logs/
│           └── tentativas_acesso.log  # Registro forense local (ignorado no Git)
├── .gitignore                  # Proteção de ambiente virtual e logs locais
└── README.md                   # Documentação técnica do projeto

```

---

## 🕵️‍♂️ Operação e Análise Forense de Logs

### 1. Monitoramento em Tempo Real

Para assistir as tentativas de acesso e capturas entrando no servidor Linux à medida que ocorrem no navegador, utilize o comando:

```bash
tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log

```

### 2. Anatomia do Log Estruturado

Cada entrada capturada gera um registro anonimizado conforme o padrão abaixo:

```text
[2026-05-31 15:56:31] IP_ORIGEM: 192.168.204.1 | USUARIO_ALVO: teste@email.com | CREDENTIAL_HASH(SHA256): e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | NAV_INFO: Mozilla/5.0...

```

* **`IP_ORIGEM`**: Identifica a máquina host (Windows) de onde partiu o clique.
* **`CREDENTIAL_HASH(SHA256)`**: Garante que a senha digitada nunca fique exposta em texto claro no servidor, aplicando os princípios de *Security by Design*.

---

## 🚀 Como Executar o Laboratório Localmente

### 1. Configurar o Ambiente Virtual e Dependências

Na pasta raiz do projeto (`~/LabSec-PhishSim`), inicialize o ambiente:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask

```

### 2. Iniciar o Servidor de Captura

Entre na pasta do back-end e execute o motor:

```bash
cd src/backend
python3 capture_server.py

```

*Nota: O servidor responderá com um erro HTTP `503` simulado para o cliente após a coleta, agindo como um mecanismo de pretexting técnico.*

### 3. Testar o Front-End

Abra o arquivo `src/frontend/index.html` no navegador do sistema hospedeiro (Windows) e certifique-se de que a tag `<form action="...">` aponta para o IP correto da sua máquina virtual Ubuntu na porta `5000`.

---

## ⚖️ Aviso Legal (Disclaimer)

**Este projeto foi desenvolvido estritamente para fins de pesquisa acadêmica, testes de penetração autorizados e treinamento de conscientização de usuários.** O uso deste código contra sistemas sem consentimento explícito e por escrito dos proprietários é ilegal e passível de penalidades jurídicas. O desenvolvedor não se responsabiliza pelo mau uso desta ferramenta.

---

Developed by [Marcio Souza](https://www.google.com/search?q=https://github.com/marciosouzagcm) 💻

```

```
