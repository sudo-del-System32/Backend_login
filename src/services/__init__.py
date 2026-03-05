import sqlite3 as sql
from fastapi import HTTPException, status

class SuperService():

    def find(self, 
            connection: sql.Connection, 
            campo: str = " ", 
            dado: str = "TRUE",
            page: int = 1,
            rows_per_page: int = 1
        ):

        try:
            if campo == " ":
                query = "TRUE"
            else:
                query = f"{campo} = '{dado}'"

            cursor = connection.execute(f"""
                    SELECT * 
                    FROM users
                    WHERE {query}
                    LIMIT ?
                    OFFSET ?
                """,
                (rows_per_page*page, rows_per_page*(1-page))
            )
    
            return cursor.fetchall()
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def find_like(self, 
            connection: sql.Connection, 
            campo: str, 
            dado: str,
            page: int = 1,
            rows_per_page: int = 1
        ):

        try:
            cursor = connection.execute(f"""
                    SELECT * 
                    FROM users
                    WHERE {campo} LIKE '%{dado}%'
                    LIMIT ?
                    OFFSET ?
                """,
                (rows_per_page*page, rows_per_page*(1-page))
            )
    
            return cursor.fetchall()
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))