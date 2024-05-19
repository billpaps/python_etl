from sqlalchemy.orm import Session
from sqlalchemy.dialects.sqlite import insert

class SQLite:

    def __init__(self, engine, batch_size = 50) -> None:
        self.engine = engine
        self.batch_size = batch_size

    def save(self, data):
        with Session(self.engine) as session:
            chunks = [data[i : i+ self.batch_size] for i in range(0, len(data), self.batch_size)]
            for chunk in chunks:
                print(f"Saving {len(chunk)} records")
                session.add_all(chunk)
                session.commit()