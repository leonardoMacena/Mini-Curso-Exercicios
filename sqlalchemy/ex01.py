#!/usr/bin/env python
#-*- coding: utf-8 -*-

m = raw_input("Visualizar o sql gerado?[s/n] ")
mostrarSql = [True, False][m.lower() == 'n']
visualizar = mostrarSql
    
############# PASSO 1 - CRIAR UMA CONEXÃO COM O BANCO DE DADOS. ################

# O sqlalchemy usa um objeto 'engine' para se conectar ao banco de dados.
from sqlalchemy import create_engine

#O parametro 'echo = True' faz com que o sql gerado seja mostrado na tela.
engine = create_engine('sqlite:///fatec.db', echo = visualizar) 

########### PASSO 2 - CRIAR AS TABELAS QUE SERÃO USADAS. #######################

#Uma tabela no sqlalchemy é um objeto do tipo Table. 
#objetos do tipo Column são usados para definir os campos da tabela.
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData

# MetaData é o objeto responsável pelas queries.
metadata = MetaData()

tabela_alunos = Table('alunos', metadata,
    Column('id', Integer, primary_key = True),
    Column('nome', String),
    Column('ra', String)
)

tabela_materias = Table('materias', metadata,
    Column('id', Integer, primary_key = True),
    Column('nome', String)
)

tabela_materias_alunos = Table('materias_alunos', metadata,
    Column('id', Integer, primary_key = True),
    Column('id_materia', Integer, ForeignKey('materias.id')),
    Column('id_aluno', Integer, ForeignKey('alunos.id')),
    Column('ano', Integer),
    Column('semestre', Integer)
)

#realizando alterações no banco e criando tabelas
metadata.create_all(engine)

if visualizar:
    raw_input("\nO SQL gerado foi a criação das tabelas.")

####### PASSO 3 - CRIAR AS CLASSES E MAPEÁ-LAS COM AS TABELAS CRIADAS. #########

from sqlalchemy.orm import mapper, relation

class aluno(object):
    def __repr__(self):
        nome = self.nome or ''
        ra = self.ra or ''
        return """nome: %s, r.a: %s""" %(nome, ra)

#mapeando aluno com tabela de alunos.
mapper(aluno, tabela_alunos)

class materia(object):
    def __repr__(self):
        nome = self.nome or ''
        return """nome: %s""" %(nome)
        
mapper(materia, tabela_materias)


###################### BRINCANDO COM OS NOSSOS OBJETOS  ########################


novo_aluno = aluno()
novo_aluno.nome = "Tankard"
novo_aluno.ra = "49794564654"
 
#Para salvar no banco usaremos um objeto 'session' que será criado com sessionmaker
#Nossa 'session' será associada à nossa 'engine'.
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

#Agora, com a session criada, é só adicionar nosso objeto a session...
session.add(novo_aluno)
session.commit()

um_aluno = session.query(aluno).filter(aluno.nome == "Tankard").first()

#Bom, vamos criar um disco.
nova_materia = materia()
nova_materia.nome = "Pitao"
session.add(nova_materia)
session.commit()
            
        