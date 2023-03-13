import csv
from sqlalchemy import Table, Column, MetaData, VARCHAR, Float, SmallInteger, Date, ForeignKey
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')

meta = MetaData()
conn = engine.connect()


def insert_from_csv(fileCsv: str, tablename):
    ins = tablename.insert()
    with open(fileCsv, 'r', newline='', encoding='UTF8') as csvf:
        temp_list = [line for line in csv.DictReader(csvf)]
        conn.execute(ins, temp_list)


stations = Table(
    'stations', meta,
    Column('station', VARCHAR(20), primary_key=True),
    Column('latitude', Float),
    Column('longitude', SmallInteger),
    Column('elevation', SmallInteger),
    Column('name', VARCHAR(50)),
    Column('country', VARCHAR(50)),
    Column('state', VARCHAR(50))
)

measure = Table(
    'measure', meta,
    Column('station', VARCHAR(20), ForeignKey('stations.station')),
    Column('date', VARCHAR(20)),
    Column('precip', Float),
    Column('tobs', SmallInteger)
)

meta.create_all(engine)

insert_from_csv('clean_stations.csv', stations)

insert_from_csv('clean_measure.csv', measure)
