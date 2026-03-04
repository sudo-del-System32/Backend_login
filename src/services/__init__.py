import sqlite3 as sql
from fastapi import HTTPException, status

class SuperService():

    def find(self, 
            connection: sql.Connection, 
            campo: str = None, 
            dado: str = "TRUE",
            page: int = 1,
            rows_per_page: int = 1
        ):

        try:
            if not campo:
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