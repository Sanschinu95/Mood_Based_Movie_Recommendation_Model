# Mood-Based Movie Recommendation System

A Python-based movie recommendation system that suggests movies based on your current mood! Includes both a command-line interface (CLI) and a web interface built with Flask.

## Features

- **Mood-based Recommendations**: Get movie suggestions based on 7 different moods
- **Interactive CLI**: Easy-to-use command-line interface
- **Web Interface**: User-friendly web app using Flask
- **Movie Search**: Find specific movies in the database
- **Add Movies**: Expand the database with your own movie entries (CLI)
- **Persistent Storage**: Save and load your movie database (CLI)
- **Customizable**: Easily add new moods or movies

## Available Moods

- **Happy** - Feel-good movies to boost your spirits
- **Sad** - Emotional movies for when you need a good cry
- **Excited** - Action-packed thrillers and adventures
- **Romantic** - Love stories and romantic comedies
- **Scared** - Horror and thriller movies
- **Thoughtful** - Mind-bending sci-fi and philosophical films
- **Nostalgic** - Classic movies that bring back memories

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Command-Line Interface (CLI)

Run the script directly to use the interactive CLI:
```bash
python movie_recommender.py
```

Follow the on-screen prompts to:
- Get mood-based recommendations
- Search for specific movies
- Add new movies to the database
- Save your database to a file

### 2. Web Interface (Flask)

Start the Flask app:
```bash
python app.py
```
Then open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

#### API Endpoints

- `GET /` — Home page with mood selection
- `POST /recommend` — Get movie recommendations (JSON: `{ "mood": "happy", "count": 3 }`)
- `POST /search` — Search for a movie by title (JSON: `{ "title": "Inception" }`)

## Example: Using the Python Class

```python
from movie_recommender import MovieRecommender

# Create recommender instance
recommender = MovieRecommender()

# Get 3 movie recommendations for happy mood
movies = recommender.recommend_movies("happy", 3)

for movie in movies:
    print(f"{movie['title']} ({movie['year']}) - {movie['rating']}/10")
```

## File Structure
```
Mood_Based_Movie_Recommendation_Model/
│
├── app.py                  # Flask web application
├── movie_recommender.py    # Main recommendation logic and CLI
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── templates/
│   └── index.html          # Web interface template
└── __pycache__/            # Python cache files
```

## Customization

### Adding New Moods
```python
recommender.movies_by_mood["adventurous"] = [
    {"title": "Indiana Jones", "year": 1981, "genre": "Adventure", "rating": 8.4}
]
```

### Adding Movies to Existing Moods
```python
new_movie = {
    "title": "Your Movie",
    "year": 2023,
    "genre": "Drama",
    "rating": 8.0
}
recommender.add_movie("happy", new_movie)
```

## Future Enhancements

- [ ] Integration with movie APIs (TMDb, OMDb)
- [ ] Machine learning-based recommendations
- [ ] User rating system
- [ ] Movie poster integration
- [ ] Recommendation history
- [ ] Social features (sharing recommendations)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Created by [Your Name] - feel free to contact me!

---

**Happy movie watching! 🍿**