from flask import Flask, render_template, request, jsonify
import json
from movie_recommender import MovieRecommender

app = Flask(__name__)
recommender = MovieRecommender()

@app.route('/')
def index():
    return render_template('index.html', moods=recommender.get_available_moods())

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get('mood', '')
    count = data.get('count', 3)
    
    recommendations = recommender.recommend_movies(mood, count)
    return jsonify(recommendations)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    title = data.get('title', '')
    movie = recommender.get_movie_by_title(title)
    return jsonify(movie)

if __name__ == '__main__':
    app.run(debug=True)