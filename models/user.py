import os
from dotenv import load_dotenv
load_dotenv()

# The following assumes ONE user for this App.
app_user = {
    'id': os.getenv('USER_ID'),
    'username': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD')
}
username_mapping = {
    os.getenv('USERNAME'): app_user
}
userid_mapping = {
    os.getenv('USER_ID'): app_user
}


class UserModel(object):
    # def __init__(self, user_id, username, password):
    #     self._id = user_id
    #     self.username = username
    #     self.password = password

    # TODO: have user(s) pulled out from a DB
    def find_by_username(self, username):
        user = username_mapping.get(username, None)
        print(user)
        if user:
            return user

    def find_by_id(self, user_id):
        return userid_mapping.get(user_id, None)
