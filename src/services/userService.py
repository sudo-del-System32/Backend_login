import sqlite3 as sql
from fastapi import HTTPException, status
from src import database
from src.models.userModel import User # Talvez não
from src.schemas.userSchema import UserReturnSchema, UserSchema
from . import SuperService

class UserService:

    def __init__(self):
        self.connect = sql.connect("databases/dataBank.db")
        self.cursor = self.connect.cursor()

    def read_all_users(self):

        #Verifying if the bank is empty
        
        user_found = SuperService().find(self.connect)

        if not user_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        users = SuperService().find(connection=self.connect, page=1, rows_per_page=10)

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

        user_found = SuperService().find(connection=self.connect, campo="id", dado=id)
        
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

    def read_user_by_email(self, email: str):

        user_found = SuperService().find(self.connect,  campo="email", dado=email)
        
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
    
    def read_user_by_name(self, name: str):

        user_found = SuperService().find(self.connect, campo="name", dado=name, page=1, rows_per_page=10)

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

    def update_user(self, id: int, user_to_update: UserSchema):

        dados = tuple(user_to_update.__dict__.values())

        user_found = SuperService().find(self.connect, "id", id)

        if not user_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        user_found = SuperService().find(self.connect, "email", user_to_update.email)
        
        if user_found and user_found[0][0] != id: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is already in use")

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

        user_found = SuperService().find(self.connect, "id", id)

        if not user_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        self.cursor.execute("""
            DELETE 
            FROM users
            WHERE id = ?    
            """,
            (id, )
        )
        self.connect.commit()
        self.connect.close()
        
        return {"mensagem": f"User with id {id} was deleted"}
