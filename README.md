# Movie Recommendation System Based on Mood

A Python-based movie recommendation system that suggests movies based on your current mood!

## Features

- **Mood-based Recommendations**: Get movie suggestions based on 7 different moods
- **Interactive CLI**: Easy-to-use command-line interface
- **Movie Search**: Find specific movies in the database
- **Add Movies**: Expand the database with your own movie entries
- **Persistent Storage**: Save and load your movie database
- **No External Dependencies**: Built using only Python standard library

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

2. Run the program:
```bash
python movie_recommender.py
```

## Usage

### Basic Usage
```python
from movie_recommender import MovieRecommender

# Create recommender instance
recommender = MovieRecommender()

# Get 3 movie recommendations for happy mood
movies = recommender.recommend_movies("happy", 3)

# Print recommendations
for movie in movies:
    print(f"{movie['title']} ({movie['year']}) - {movie['rating']}/10")
```

### Interactive Mode
Run the script directly to use the interactive CLI:
```bash
python movie_recommender.py
```

Follow the on-screen prompts to:
- Get mood-based recommendations
- Search for specific movies
- Add new movies to the database
- Save your database to a file

## Database Structure

Movies are stored with the following information:
- **Title**: Movie name
- **Year**: Release year
- **Genre**: Movie genre(s)
- **Rating**: IMDb-style rating (0-10)

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

## File Structure
```
movie-recommendation-system/
│
├── movie_recommender.py    # Main application file
├── requirements.txt        # Dependencies (currently none)
├── README.md              # This file
└── movies_database.json   # Saved database (created when you save)
```

## Future Enhancements

- [ ] Web interface using Flask/FastAPI
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