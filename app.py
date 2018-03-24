import os
from flask import Flask
from flask_restful import Api
import pandas as pd
import numpy as np
#from utils.matrix_factorization_utilities import low_rank_matrix_factorization

from resources.recommend import RecommendedMovies
from resources.movies import Movies
from resources.movie import Movie

app = Flask(__name__)

# load configs
app.config.update(
    DEBUG=True
)

api = Api(app)

api.add_resource(RecommendedMovies, '/recommend/movies/<int:user_id>')
api.add_resource(Movies, '/movies')
api.add_resource(Movie, '/movie/<string:movie_name>')

if __name__ == '__main__':
    app.run(port=5000)
