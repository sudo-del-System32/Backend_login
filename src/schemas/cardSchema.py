from pydantic import BaseModel, model_validator
from typing import Optional


class CardSchema(BaseModel):
    name: str
    card_type: str #Ver objectId e falar com o pedro sobre essa verificaçao com json
    
    health: int
    attack_name: str
    attack_damage: int
    description: Optional[str]


    @model_validator
    def check_health(self):
        if not self.health:
            raise ValueError("Card health can not be empty")
       
        if type(self.health) is not int:
            raise TypeError("Card health needs to be an integer")
        
        if self.health < 1:
            raise ValueError("Card health can not be less than 1")
        return self

    @model_validator
    def check_attack_damage(self):
        if not self.attack_damage:
            raise ValueError("Card attack damage can not be empty")
        
        if type(self.attack_damage) is not int:
            raise TypeError("Card attack damage needs to be an integer")
        
        if self.attack_damage < 1:
            raise ValueError("Card health can not be less than 1")
        return self



    # String validators
    @model_validator(mode="after")
    def check_name(self):
        if len(self.name) < 1:
            raise ValueError("Card name can not be empty")
        return self
    
    @model_validator(mode="after")
    def check_attack_name(self):
        if len(self.attack_name) < 1:
            raise ValueError("Card attack name can not be empty")
        return self
    