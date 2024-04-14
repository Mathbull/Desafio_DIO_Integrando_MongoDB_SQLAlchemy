import Cliente_conta as cc
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy import select



print("\nTestanto...")
print(f"\n{cc.Cliente.__tablename__}")
print(f"{cc.Conta.__tablename__}")
print()


engine = create_engine("sqlite:///teste.db")

cc.Base.metadata.create_all(engine)

insp = inspect(engine)
print(insp.get_table_names())

print("Instanciando nossos elementos e obj")
with Session(engine) as connection:
    cli1 = cc.Cliente(
        nome = "Nick",
        cpf = "33333-11",
        endereco = "Rua: ze ramalho, 49, Silva-SP",
        conta = [(cc.Conta(
            tipo="Conta Poupança",
            agencia = "XXXX-YY",
            num = "777-99" ))])

    cli2 = cc.Cliente(nome = "Rafalei Dona",
        cpf = "333333-00",
        endereco = "Rua: buero limpo, 74, sargeta-SP",
        conta = [(cc.Conta(
            tipo="Conta corrente",
            agencia = "XXXX-YY",
            num = "888-33" ))])
    
    cli3 = cc.Cliente(nome = "Estomago sangrendo",
        cpf = "1111111-01",
        endereco = "Rua: pacreas, 95, orgao-SP",
        conta = [(cc.Conta(
            tipo="Conta Poupança",
            agencia = "XXXX-YY",
            num = "999-77" ))])

    connection.add_all([cli1, cli2, cli3])
    connection.commit()

    #connection.close()

connect = engine.connect()

sql = select(cc.Cliente)

table = connect.execute(sql).fetchall()
print("\nRecuperando dados\n")

for t in connection.scalars(sql):
    print(t)
  
