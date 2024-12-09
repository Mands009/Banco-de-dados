import sqlite3

# Função para conectar ao banco de dados SQLite
def conectar_bd():
    conn = sqlite3.connect('imc_db.db')
    cursor = conn.cursor()
    # Criação da tabela de pacientes se não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        endereco TEXT,
        peso REAL,
        altura REAL
    )
    ''')
    conn.commit()
    return conn, cursor

# Função para salvar os dados do paciente no banco de dados
def salvar_dados(nome, endereco, peso, altura):
    conn, cursor = conectar_bd()
    cursor.execute('''
    INSERT INTO pacientes (nome, endereco, peso, altura)
    VALUES (?, ?, ?, ?)
    ''', (nome, endereco, peso, altura))
    conn.commit()
    conn.close()

# Função principal para interação com o usuário
def main():
    print("Armazenamento de Dados do Paciente")

    # Coletando os dados do paciente
    nome = input("\nDigite o nome do paciente: ")
    endereco = input("Digite o endereço do paciente: ")
    peso = float(input("Digite o peso do paciente (em kg): "))
    altura = float(input("Digite a altura do paciente (em metros): "))

    # Salvando os dados no banco de dados
    salvar_dados(nome, endereco, peso, altura)

    # Confirmando que os dados foram salvos
    print("\nDados do paciente foram salvos no banco de dados.")

# Executando o programa
if __name__ == "__main__":
    main()