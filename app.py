from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def get_all_movies():
    return jsonify({
        'message': "at some point in the future, this will return the list of all movies"
    })


@app.route('/movies/recommend/<string:id>', methods=['GET'])
def get_recommended_movies(id):
    return jsonify({
        'message': 'at some point in the future, this will return the recommended movies for a particular user',
        'id': id
    })

app.run(port=5000)

