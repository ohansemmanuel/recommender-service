import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
import pandas as pd
import numpy as np

from resources.access import AccessToken
from resources.recommend import RecommendMovies
from resources.movies import Movies
from resources.movie import Movie
from dotenv import load_dotenv

load_dotenv(verbose=True)
app = Flask(__name__)
CORS(app)

# load configs
app.config.update(
    DEBUG=True,
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
)

api = Api(app)

# auth
jwt = JWTManager(app)

api.add_resource(AccessToken, '/auth')
api.add_resource(RecommendMovies, '/recommend/movies/<int:user_id>')
api.add_resource(Movies, '/movies')
api.add_resource(Movie, '/movie/<string:movie_name>')

if __name__ == '__main__':
    app.run(port=5000)
