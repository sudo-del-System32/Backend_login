from src.models.userModel import User


class UserAdapter:

    def __init__(self, currUser: User):
        self.currUser = currUser

    def read_all_users_controller(self):
        pass