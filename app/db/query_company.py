from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from app.models.organization import Organization

engine = create_engine(
    'mssql+pyodbc://DESKTOP-OE5G1EA\\SQLEXPRESS/ggs_stud?driver=SQL+Server+Native+Client+11.0', echo=True)

def query_organization_by_id(id: int):

    with Session(engine) as db:
        query = (select('*').where(Organization.id == id))
        result = db.execute(query).first()

        if not result:
            return None

        result_mapping = dict(result._mapping)
        return result_mapping