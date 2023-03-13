from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')

conn = engine.connect()

print(conn.execute("SELECT * FROM stations LIMIT 5").fetchall())
