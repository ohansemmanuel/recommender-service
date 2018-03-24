from flask_restful import Resource
from utils.matrix_factorization_utilities import low_rank_matrix_factorization
import pandas as pd
import numpy as np


class RecommendedMovies(Resource):

    def get(self, user_id):
        # Load user ratings
        raw_dataset_df = pd.read_csv('data/movie_ratings_data_set.csv')

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

        previously_recommended_movies = reviewed_movies_df[[
            'title', 'genre', 'value']].to_json()
        recommended_movies = recommended_df[[
            'title', 'genre', 'rating']].head(5).to_json()

        return {
            'rated_movies': previously_recommended_movies,
            'movies': recommended_movies}, 200
