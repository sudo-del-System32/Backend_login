from pydantic import BaseModel, model_validator


class UserSchema(BaseModel):
    name: str
    email: str
    password: str

    @model_validator(mode="after")
    def check_name(self):
        if len(self.name) < 1:
            raise ValueError("User name can not be empty")
        return self
    
    @model_validator(mode="after")
    def check_email(self):
        if len(self.email) < 1:
            raise ValueError("User email can not be empty")
        return self
    
    @model_validator(mode="after")
    def check_password(self):
        if len(self.password) < 4:
            raise ValueError("User password needs to be bigger than 4 digis")
        return self

