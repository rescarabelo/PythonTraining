from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:postgres@localhost:5432/training', echo=True)
base = declarative_base()


class Training(base):
    __tablename__ = 'training'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    year = Column(Text)


if __name__ == "__main__":
    # Método ORM/Mais pŕatico:

    Session = sessionmaker(engine)
    session = Session()

    base.metadata.create_all(engine)

    test1 = Training(id=10, name='test1', year='2022')
    session.add(test1)
    session.commit()

    rs = session.query(Training)
    for i in rs:
        print(i.name)

    # Método mais rústico:

    # engine.execute('CREATE TABLE IF NOT EXISTS testing (id int primary key, name text, year text)')
    # engine.execute("INSERT INTO testing (id, name, year) VALUES (1, 'test1', '2022')")
    #
    # result_set = engine.execute("SELECT * FROM testing")
    # for r in result_set:
    #     print(r)

    # Método "meio-termo":

    # meta = MetaData(engine)
    # training_table = Table('testing', meta,
    #                        Column('id', Integer, primary_key=True),
    #                        Column('name', Text),
    #                        Column('year', Text),
    #                        )
    #
    # with engine.connect() as conn:
    #     training_table.create()
    #     insert = training_table.insert().values(
    #         id=1,
    #         name='test1',
    #         year='2022'
    #     )
    #     conn.execute(insert)
    #
    #     select = training_table.select()
    #     rs = conn.execute(select)
    #     for i in rs:
    #         print(i)
