from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from app.bitrix.object_ks import add_item as object_ks_add_util
from app.db.query_object_ks_gs import query_house_by_id
from app.enums.db_to_bitrix_fields import HouseToObjectKSFields, HouseToGasificationStageFields
from app.enums.object_ks import ObjectKSFields, ClientType, GasificationType, District

router = APIRouter(prefix="/sync_with_db", tags=["db"])

def build_payloads(house):
    object_ks_payload = dict()
    gasification_stage_payload = dict()

    #object_ks_payload
    for key, value in house.items():

        # pydantic_schema_field_name = HouseToObjectKSFields[key].value
        # bitrix_field_name = ObjectKSFields[pydantic_schema_field_name].value

        if key in ("is_to_from_sibgs", "is_double_adress", "is_ods"):
            pydantic_schema_field_name = HouseToObjectKSFields[key].value
            print(pydantic_schema_field_name)
            bitrix_field_name = ObjectKSFields[pydantic_schema_field_name].value
            print(bitrix_field_name)
            object_ks_payload[bitrix_field_name] = bool(value)

        elif key == "type_client":
            pydantic_schema_field_name = HouseToObjectKSFields[key].value
            bitrix_field_name = ObjectKSFields[pydantic_schema_field_name].value
            object_ks_payload[bitrix_field_name] = ClientType(value).value

        elif key == "type_house_gazification":
            pydantic_schema_field_name = HouseToObjectKSFields[key].value
            bitrix_field_name = ObjectKSFields[pydantic_schema_field_name].value
            object_ks_payload[bitrix_field_name] = GasificationType(value).value

        elif key == "district":
            pydantic_schema_field_name = HouseToObjectKSFields[key].value
            bitrix_field_name = ObjectKSFields[pydantic_schema_field_name].value
            object_ks_payload[bitrix_field_name] = District(value).value

        elif key in ("cadastr_number", "cadastr_number_oks", "address"):
            pydantic_schema_field_name = HouseToObjectKSFields[key].value
            bitrix_field_name = ObjectKSFields[pydantic_schema_field_name].value
            object_ks_payload[bitrix_field_name] = value
    
    return object_ks_payload
    


@router.get("/house/{id}")
def sync_with_db_house_endpoint(id: int):
    house = query_house_by_id(id)
    object_ks_payload = build_payloads(house)
    # return object_ks_payload
    return object_ks_add_util(object_ks_payload)
