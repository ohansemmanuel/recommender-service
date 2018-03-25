from werkzeug.security import safe_str_cmp
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user import UserModel


class AccessToken(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help='Missing username parameter')
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='Missing password parameter')

        data = parser.parse_args()

        # check if username and password matches
        username_received = data.get('username', None)
        password_received = data.get('password', None)

        user = UserModel().find_by_username(username_received)

        if user and safe_str_cmp(user['password'], password_received):
            username = user['username']
            access_token = create_access_token(identity=username)
            return {
                "access_token": access_token
            }

        return {
            "message": "Unauthorized access. username or password is wrong"}, 401
