import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.database import connect

def criar_tabela_ocorrencias():
    print("Conectando ao banco de dados...")
    conn = connect()
    cursor = conn.cursor()
    print("Conexão estabelecida. Criando tabela...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ocorrencias (
        id SERIAL PRIMARY KEY,
        tipo VARCHAR(50),
        descricao TEXT,
        cpf_email VARCHAR(100)
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabela 'ocorrencias' criada com sucesso.")

if __name__ == "__main__":
    criar_tabela_ocorrencias()
