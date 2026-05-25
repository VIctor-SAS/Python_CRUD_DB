import sqlite3

DB_NAME = "sistema.db"

def conectar_banco():
    """Conecta ao banco de dados SQLite."""
    return sqlite3.connect(DB_NAME)

def inicializar_banco():
    """Cria a tabela se ela não existir."""
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            idade INTEGER
        )
    """)
    conexao.commit()
    conexao.close()