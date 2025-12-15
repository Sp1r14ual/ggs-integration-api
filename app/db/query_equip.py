from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session
from app.db.engine import engine
from app.models.equip import Equip
from app.models.type_packing import TypePacking
from app.models.type_pipe_material import TypePipeMaterial
from app.models.type_diameter import TypeDiameter


def query_equip_by_id(id: int):

    with Session(engine) as db:
        query = (
            select(
                Equip.id,
                TypePacking.name.label('packing_name'),
                Equip.diameter,
                TypeDiameter.name.label('diameter_type_name'),
                Equip.length,
                TypePipeMaterial.name.label('pipe_material_name'),
                Equip.amount,
                Equip.num
            )
            .outerjoin(TypePacking, Equip.id_type_packing == TypePacking.id)
            .outerjoin(TypeDiameter, Equip.id_type_diameter == TypeDiameter.id)
            .outerjoin(TypePipeMaterial, Equip.id_type_pipe_material == TypePipeMaterial.id)
            .where(Equip.id == 1195)
        )

        result = db.execute(query).first()

        if not result:
            return None

        result_mapping = dict(result._mapping)

        return result_mapping

    