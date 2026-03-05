from src.models.userModel import User
from src.schemas.userSchema import UserSchema, UserEditSchema
from src.services.userService import UserService

class UserAdapter:

    def read_all_users_controller(self):
        return UserService().read_all_users()

    def read_user_by_id_controller(self, id: int):
        return UserService().read_user_by_id(id)

    def read_user_by_email_controller(self, email: str):
        return UserService().read_user_by_email(email)

    def read_user_by_name_controller(self, name: str):
        return UserService().read_user_by_name(name)

    def add_user_controller(self, schema: UserSchema):

        newUser = User(
            id=None, 
            name=schema.name, 
            email=schema.email, 
            password=schema.password, 
            card_id=None
        )

        UserService().add_user(new_user=newUser)
        return {"Mensagem" : "User Added Sucessfull"}

    def update_user_controller(self, id: int, user_to_update: UserEditSchema):
        return UserService().update_user(id, user_to_update)

    def kill_yourself_controller(self, id: int):
    # def delete_user_controller(self, id: int):
        # return UserService().delete_user(id=id)
        return UserService().kill_yourself(id=id)