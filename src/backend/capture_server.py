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
