from flask_restful import Resource, reqparse
from utils.matrix_factorization_utilities import low_rank_matrix_factorization
from flask_jwt_extended import jwt_required
import pandas as pd
import numpy as np
import json
import ast


class RecommendMovies(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
                        required=True,
                        help="You must send the USER ID"
                        )
    parser.add_argument('movie_id',
                        required=True,
                        help="You must send the MOVIE ID"
                        )
    parser.add_argument('value',
                        required=True,
                        help="You must send the MOVIE RATING"
                        )

    @classmethod
    def get_raw_dataset_df(cls):
        # Load user ratings
        raw_dataset_df = pd.read_csv('data/movie_ratings_data_set.csv')
        return raw_dataset_df

    @classmethod
    def get_recommendations(cls, raw_dataset_df, user_id):
        # Load movie titles
        movies_df = pd.read_csv('data/movies.csv', index_col='movie_id')

        # Convert the running list of user ratings into a matrix
        ratings_df = pd.pivot_table(raw_dataset_df, index='user_id',
                                    columns='movie_id',
                                    aggfunc=np.max)

        # Apply matrix factorization to find the latent features
        U, M = low_rank_matrix_factorization(
            ratings_df.as_matrix(), num_features=15, regularization_amount=0.1)

        # Find all predicted ratings by multiplying U and M matrices
        predicted_ratings = np.matmul(U, M)

        reviewed_movies_df = raw_dataset_df[raw_dataset_df['user_id']
                                            == user_id]
        reviewed_movies_df = reviewed_movies_df.join(movies_df, on='movie_id')

        user_ratings = predicted_ratings[user_id - 1]
        movies_df['rating'] = user_ratings

        already_reviewed = reviewed_movies_df['movie_id']

        recommended_df = movies_df[movies_df.index.isin(
            already_reviewed) == False]

        recommended_df = recommended_df.sort_values(
            by=['rating'], ascending=False)

        return (
            reviewed_movies_df[[
                'title', 'genre', 'value']].to_json(),
            recommended_df[[
                'title', 'genre', 'rating']].head(5).to_json()
        )

    @jwt_required
    def get(self, user_id):
        raw_dataset_df = RecommendMovies.get_raw_dataset_df()
        recommendations = RecommendMovies.get_recommendations(
            raw_dataset_df, user_id)

        previously_recommended_movies = recommendations[0]
        recommended_movies = recommendations[0]

        return {
            'rated_movies': previously_recommended_movies,
            'movies': recommended_movies}, 200

    def post(self, user_id):
        data = RecommendMovies.parser.parse_args()
        raw_dataset_df = RecommendMovies.get_raw_dataset_df()

        data_formatted = {
            "user_id": ast.literal_eval(data['user_id']),
            "movie_id": ast.literal_eval(data['movie_id']),
            "value": ast.literal_eval(data['value'])
        }

        new_dataset_df = pd.DataFrame(data_formatted)

        combined_dataset = pd.concat([raw_dataset_df, new_dataset_df])

        recommendations = RecommendMovies.get_recommendations(
            combined_dataset, user_id)

        previously_recommended_movies = recommendations[0]
        recommended_movies = recommendations[1]

        return {
            'rated_movies': previously_recommended_movies,
            'movies': recommended_movies}, 200
