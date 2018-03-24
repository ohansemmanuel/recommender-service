from flask_restful import Resource


class RecommendedMovies(Resource):
    def get(self, user_id):
        return {'movies': 'These are the recommended movies for user, {}'.format(user_id)}, 200
