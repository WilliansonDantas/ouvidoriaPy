from dotenv import load_dotenv
from database.database import connect
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'src', '.env'))

def criar_ocorrencia(tipo, descricao, cpf_email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ocorrencias (tipo, descricao, cpf_email) VALUES (%s, %s, %s)",
        (tipo, descricao, cpf_email)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Ocorrência criada com sucesso.")

def listar_ocorrencias():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ocorrencias")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

def atualizar_ocorrencia(id, nova_descricao):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE ocorrencias SET descricao = %s WHERE id = %s",
        (nova_descricao, id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Ocorrência atualizada com sucesso.")

def deletar_ocorrencia(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ocorrencias WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Ocorrência deletada com sucesso.")

def menu():
    while True:
        print("Menu de Interação do Usuário:")
        print("1. Criar Ocorrência")
        print("2. Listar Ocorrências")
        print("3. Atualizar Ocorrência")
        print("4. Deletar Ocorrência")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            tipo = input("Digite o tipo (crítica, elogio, sugestão): ")
            descricao = input("Digite a descrição: ")
            cpf_email = input("Digite o CPF ou email: ")
            criar_ocorrencia(tipo, descricao, cpf_email)
        elif choice == '2':
            listar_ocorrencias()
        elif choice == '3':
            id = input("Digite o ID da ocorrência: ")
            nova_descricao = input("Digite a nova descrição: ")
            atualizar_ocorrencia(id, nova_descricao)
        elif choice == '4':
            id = input("Digite o ID da ocorrência: ")
            deletar_ocorrencia(id)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
