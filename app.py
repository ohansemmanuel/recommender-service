import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import pandas as pd
import numpy as np

from security import authenticate, identity
from resources.recommend import RecommendedMovies
from resources.movies import Movies
from resources.movie import Movie
from dotenv import load_dotenv

load_dotenv(verbose=True)
app = Flask(__name__)
# load configs
app.config.update(
    DEBUG=True,
    SECRET_KEY=os.getenv('SECRET_KEY')
)

api = Api(app)

#auth
jwt = JWT(app, authenticate, identity)

api.add_resource(RecommendedMovies, '/recommend/movies/<int:user_id>')
api.add_resource(Movies, '/movies')
api.add_resource(Movie, '/movie/<string:movie_name>')

if __name__ == '__main__':
    app.run(port=5000)
