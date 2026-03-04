from fastapi import APIRouter, Request
from src.schemas.userSchema import UserSchema
from src.adapters.userAdapter import UserAdapter

router = APIRouter(prefix="/user") 


@router.get("/")
async def read_all_users(request: Request):
    # djeizu: dict = await request.json() # await utiliza junto de async function
    # if djeizu.get("email") is None:
    return UserAdapter().read_all_users_controller()

@router.get("/search/id/{id}")
async def read_user_by_id(id: int):
    return UserAdapter().read_user_by_id_controller(id)

@router.get("/search/email/{email}")
async def read_user_by_email(email: str):
    return UserAdapter().read_user_by_email_controller(email)

@router.get("/search/name/{name}")
async def read_user_by_name(name: str):
    return UserAdapter().read_user_by_name_controller(name)

@router.post("/")
async def add_user(schema: UserSchema):
    return UserAdapter().add_user_controller(schema)

@router.put("/")
async def update_user(id: int, user_to_update: UserSchema):
    return UserAdapter().update_user_controller(id=id, user_to_update=user_to_update)


@router.delete("/")
async def kill_yourself(id: int):
# async def delete_user(id: int):
    # return UserAdapter().delete_user_controller(id=id)
    return UserAdapter().kill_yourself_controller(id=id)