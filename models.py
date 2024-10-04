import sqlalchemy as sql
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
#criando a tabela
#cursor.execute("""
#    create table tbl_pessoal(
#        id integer primary key autoincrement,
#        nome text,
#        idade integer
#    )
#""")

class db():
    def __init__(self) -> None:
        conexao_db = os.getenv("URL_CONEXAO")
        self.__engine = sql.create_engine(conexao_db, echo = True)
        self.__conn = self.__engine.connect()

    def inserir(self, nome:str, email:str):
        self.__conn.execute(sql.sql.text(""" 
            INSERT INTO teste_user (name,email)
            VALUES(
                :nome, :email
            )
        """), {"nome":nome, "email":email})
        self.__conn.commit()

    def consulta_unico(self, id:int):
        result = self.__conn.execute(sql.sql.text("""
            SELECT * FROM teste_user WHERE ID = :id
        """),{"id": id}).fetchall()
        return [e for e in result]

    def consulta_geral(self):
        result = self.__conn.execute(sql.sql.text("""
            SELECT * FROM teste_user 
        """)).fetchall()
        if result == []:
            return []
        else:
            return [e for e in result]

    def alterar(self, id:int, nome:str, email:str):
        query = sql.sql.text("""
            UPDATE teste_user
            SET
                name = :nome ,
                email = :email
            WHERE
                id = :id
        """)
        self.__conn.execute(query, {"nome":nome, "email":email, "id":id})
        self.__conn.commit()

    def excluir(self, id:int):
        query = sql.sql.text(""" 
            DELETE FROM teste_user
            WHERE id = :id
        """)
        self.__conn.execute(query, {'id': id})
        self.__conn.commit()

#listando os índices de uma tupla => ()
#print([list(enumerate(e)) for e in cursor.execute("select * from tbl_pessoal")])

#exemplo de dicionário
#e = cursor.execute("select * from tbl_pessoal").fetchall()
#print(dict({'id':e[0][0], 'nome': e[0][1], 'idade': e[0][2]}))

#print(db.consulta_geral()) 
#print(db.consulta_unico(2))