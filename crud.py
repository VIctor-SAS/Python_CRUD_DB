import sqlite3
from database import conectar_banco

def criar_usuario(nome, email, idade):
    """Insere um novo usuário. Retorna True se der certo, False se o email já existir."""
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO usuarios (nome, email, idade) 
            VALUES (?, ?, ?)
        """, (nome, email, idade))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()

def ler_usuarios():
    """Retorna a lista de todos os usuários."""
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

def atualizar_usuario(id_usuario, novo_nome, novo_email, nova_idade):
    """Atualiza o usuário. Retorna 'sucesso', 'nao_encontrado' ou 'email_duplicado'."""
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    # Verifica se o ID existe
    cursor.execute("SELECT id FROM usuarios WHERE id = ?", (id_usuario,))
    if not cursor.fetchone():
        conexao.close()
        return "nao_encontrado"

    try:
        cursor.execute("""
            UPDATE usuarios 
            SET nome = ?, email = ?, idade = ? 
            WHERE id = ?
        """, (novo_nome, novo_email, nova_idade, id_usuario))
        conexao.commit()
        return "sucesso"
    except sqlite3.IntegrityError:
        return "email_duplicado"
    finally:
        conexao.close()

def deletar_usuario(id_usuario):
    """Deleta um usuário pelo ID. Retorna True se deletou, False se não encontrou."""
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id FROM usuarios WHERE id = ?", (id_usuario,))
    if not cursor.fetchone():
        conexao.close()
        return False

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conexao.commit()
    conexao.close()
    return True