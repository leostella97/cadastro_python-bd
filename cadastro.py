from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cria um mecanismo de banco de dados (usando SQLite
engine = create_engine('sqlite:///pessoas.db', echo=True)

# Cria uma classe de modelo
Base = declarative_base()

# Cria a base de dados 'pessoas'
class Pessoa(Base):
    __tablename__ = 'pessoas' # Nome da tabela
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True) # ID
    nome = Column(String(50)) # Nome
    idade = Column(Integer) # Idade
    email = Column(String(100)) # E-mail

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Solicita dados ao usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
email = input("Digite o e-mail: ")

# Cria uma instância do modelo com os dados inseridos
nova_pessoa = Pessoa(nome=nome, idade=idade, email=email)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Adiciona a pessoa na sessão e ao banco de dados
session.add(nova_pessoa)

# Commit para efetivar a transação
session.commit()

print("Dados da pessoa foram armazenados com sucesso no banco de dados.")
