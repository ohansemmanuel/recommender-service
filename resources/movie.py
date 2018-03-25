from flask_restful import Resource


class Movie(Resource):
    def get(self, movie_name):
        return {'message': 'A movie with name, {}'.format(movie_name)}, 200
