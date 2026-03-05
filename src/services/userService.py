import sqlite3 as sql
from fastapi import HTTPException, status
from src import database
from src.models.userModel import User
from src.schemas.userSchema import UserReturnSchema, UserSchema, UserEditSchema
from . import SuperService

class UserService:

    def __init__(self):
        self.connect = sql.connect("databases/dataBank.db")
        self.cursor = self.connect.cursor()

    def read_all_users(self, page: int=1, rows_per_page: int=10):

        #Verifying if the bank is empty
        
        user_found = SuperService().find(self.connect)

        if not user_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no users")
        
        users = SuperService().find(connection=self.connect, page=page, rows_per_page=rows_per_page)

        found_users: list[UserReturnSchema] = []

        for user in users: 
            
            found_users.append(UserReturnSchema(
                id=user[0],
                name=user[1],
                email=user[2],
                card_id=user[4]
                ))
        
        self.connect.close()
        return found_users

    def read_user_by_id(self, id: int):

        user_found = SuperService().find(connection=self.connect, campo="id", dado=str(id))
        
        if not user_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        user_found = user_found[0]

        found_users = UserReturnSchema(
            id=user_found[0],
            name=user_found[1],
            email=user_found[2],
            card_id=user_found[4]
        )

        self.connect.close()
        return found_users

    def read_user_by_email(self, email: str, page: int=1, rows_per_page: int=10):

        user_found = SuperService().find_like(self.connect, campo="email", dado=email, page=page, rows_per_page=rows_per_page)
        
        if not user_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        found_users: list[UserReturnSchema] = []

        for user in user_found:
            found_users.append(UserReturnSchema(
                id=user[0],
                name=user[1],
                email=user[2],
                card_id=user[4]
                ))

        self.connect.close()
        return found_users
    
    def read_user_by_name(self, name: str, page: int=1, rows_per_page: int=10):

        user_found = SuperService().find_like(self.connect, campo="name", dado=name, page=page, rows_per_page=rows_per_page)

        if not user_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        found_users: list[UserReturnSchema] = []

        for user in user_found:
            found_users.append(UserReturnSchema(
                id=user[0],
                name=user[1],
                email=user[2],
                card_id=user[4]
                ))
        
        self.connect.close()
        return found_users

    def add_user(self, new_user : User):
        
        user_found = SuperService().find(connection=self.connect, campo="email", dado=new_user.email)

        if user_found:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is already in use")

        data = tuple(new_user.__dict__.values())
        
        self.cursor.execute("""
                INSERT INTO users
                (id, name, email, password, card_id)
                VALUES
                (?, ?, ?, ?, ?)
            """,
            (data)
        )
        self.connect.commit()
        self.connect.close()

    def update_user(self, id: int, user_to_update: UserEditSchema):

        user_found = SuperService().find(self.connect, "id", str(id))
        
        if not user_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        if user_to_update.email:
            user_found = SuperService().find(self.connect, "email", user_to_update.email)
            
            if user_found and user_found[0][0] != id: 
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is already in use")
            elif not user_found:
                user_found = SuperService().find(self.connect, "id", str(id))


        user_found = user_found[0]
        user_found = User(
            id=user_found[0],
            name=user_found[1],
            email=user_found[2],
            password=user_found[3],
            card_id=user_found[4]
            )

        # Casos de alteraçao de uma unica informaçao do banco
        if not user_to_update.name:
            user_to_update.name = user_found.name
        if not user_to_update.email:
            user_to_update.email = user_found.email
        if not user_to_update.password:
            user_to_update.password = user_found.password

        dados = tuple(user_to_update.__dict__.values())

        self.cursor.execute(f"""
            UPDATE users
            SET 
            name = ?,
            email = ?, 
            password = ?
                            
            WHERE id = ?
            """,
            dados.__add__((id, ))
        )
        self.connect.commit()
        self.connect.close()

        return {"mensagem": f"User with id {id} was edit"}


    def kill_yourself(self, id: int):
    # def delete_user(self, id: int):

        user_found = SuperService().find(self.connect, "id", str(id))

        if not user_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        self.cursor.execute("""
            DELETE 
            FROM users
            WHERE id = '?'    
            """,
            (id, )
        )
        self.connect.commit()
        self.connect.close()
        
        return {"mensagem": f"User with id {id} was deleted"}
