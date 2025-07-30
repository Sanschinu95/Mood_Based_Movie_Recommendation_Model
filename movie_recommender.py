import random
import json
from typing import List, Dict

class MovieRecommender:
    def __init__(self):
        # Movie database organized by mood
        self.movies_by_mood = {
            "happy": [
                {"title": "The Pursuit of Happyness", "year": 2006, "genre": "Drama", "rating": 8.0},
                {"title": "Forrest Gump", "year": 1994, "genre": "Drama/Comedy", "rating": 8.8},
                {"title": "The Grand Budapest Hotel", "year": 2014, "genre": "Comedy", "rating": 8.1},
                {"title": "Paddington", "year": 2014, "genre": "Family/Comedy", "rating": 7.3},
                {"title": "La La Land", "year": 2016, "genre": "Musical/Romance", "rating": 8.0},
                {"title": "School of Rock", "year": 2003, "genre": "Comedy", "rating": 7.1},
                {"title": "Chef", "year": 2014, "genre": "Comedy/Drama", "rating": 7.3}
            ],
            "sad": [
                {"title": "Inside Out", "year": 2015, "genre": "Animation/Drama", "rating": 8.1},
                {"title": "Her", "year": 2013, "genre": "Drama/Romance", "rating": 8.0},
                {"title": "Manchester by the Sea", "year": 2016, "genre": "Drama", "rating": 7.8},
                {"title": "The Fault in Our Stars", "year": 2014, "genre": "Drama/Romance", "rating": 7.7},
                {"title": "A Monster Calls", "year": 2016, "genre": "Drama/Fantasy", "rating": 7.5},
                {"title": "Up", "year": 2009, "genre": "Animation/Drama", "rating": 8.2}
            ],
            "excited": [
                {"title": "Mad Max: Fury Road", "year": 2015, "genre": "Action", "rating": 8.1},
                {"title": "John Wick", "year": 2014, "genre": "Action/Thriller", "rating": 7.4},
                {"title": "Mission: Impossible - Fallout", "year": 2018, "genre": "Action", "rating": 7.7},
                {"title": "Spider-Man: Into the Spider-Verse", "year": 2018, "genre": "Animation/Action", "rating": 8.4},
                {"title": "Top Gun: Maverick", "year": 2022, "genre": "Action/Drama", "rating": 8.3},
                {"title": "Baby Driver", "year": 2017, "genre": "Action/Crime", "rating": 7.6}
            ],
            "romantic": [
                {"title": "The Notebook", "year": 2004, "genre": "Romance/Drama", "rating": 7.8},
                {"title": "Eternal Sunshine of the Spotless Mind", "year": 2004, "genre": "Romance/Sci-Fi", "rating": 8.3},
                {"title": "Before Sunrise", "year": 1995, "genre": "Romance/Drama", "rating": 8.1},
                {"title": "Casablanca", "year": 1942, "genre": "Romance/Drama", "rating": 8.5},
                {"title": "Pride and Prejudice", "year": 2005, "genre": "Romance/Drama", "rating": 7.8},
                {"title": "When Harry Met Sally", "year": 1989, "genre": "Romance/Comedy", "rating": 7.7}
            ],
            "scared": [
                {"title": "Get Out", "year": 2017, "genre": "Horror/Thriller", "rating": 7.7},
                {"title": "A Quiet Place", "year": 2018, "genre": "Horror/Thriller", "rating": 7.5},
                {"title": "Hereditary", "year": 2018, "genre": "Horror", "rating": 7.3},
                {"title": "The Conjuring", "year": 2013, "genre": "Horror", "rating": 7.5},
                {"title": "Midsommar", "year": 2019, "genre": "Horror/Drama", "rating": 7.0},
                {"title": "The Babadook", "year": 2014, "genre": "Horror/Drama", "rating": 6.8}
            ],
            "thoughtful": [
                {"title": "Inception", "year": 2010, "genre": "Sci-Fi/Thriller", "rating": 8.8},
                {"title": "Interstellar", "year": 2014, "genre": "Sci-Fi/Drama", "rating": 8.6},
                {"title": "Blade Runner 2049", "year": 2017, "genre": "Sci-Fi", "rating": 8.0},
                {"title": "Ex Machina", "year": 2014, "genre": "Sci-Fi/Thriller", "rating": 7.7},
                {"title": "Arrival", "year": 2016, "genre": "Sci-Fi/Drama", "rating": 7.9},
                {"title": "The Matrix", "year": 1999, "genre": "Sci-Fi/Action", "rating": 8.7}
            ],
            "nostalgic": [
                {"title": "Stand by Me", "year": 1986, "genre": "Drama/Adventure", "rating": 8.1},
                {"title": "The Sandlot", "year": 1993, "genre": "Comedy/Family", "rating": 7.8},
                {"title": "E.T. the Extra-Terrestrial", "year": 1982, "genre": "Sci-Fi/Family", "rating": 7.9},
                {"title": "Back to the Future", "year": 1985, "genre": "Sci-Fi/Comedy", "rating": 8.5},
                {"title": "The Breakfast Club", "year": 1985, "genre": "Comedy/Drama", "rating": 7.8},
                {"title": "Ferris Bueller's Day Off", "year": 1986, "genre": "Comedy", "rating": 7.8}
            ]
        }
    
    def get_available_moods(self) -> List[str]:
        """Return list of available moods"""
        return list(self.movies_by_mood.keys())
    
    def recommend_movies(self, mood: str, count: int = 3) -> List[Dict]:
        """Recommend movies based on mood"""
        mood = mood.lower().strip()
        
        if mood not in self.movies_by_mood:
            return []
        
        movies = self.movies_by_mood[mood].copy()
        random.shuffle(movies)
        
        return movies[:count]
    
    def get_movie_by_title(self, title: str) -> Dict:
        """Find a specific movie by title"""
        title = title.lower().strip()
        for mood_movies in self.movies_by_mood.values():
            for movie in mood_movies:
                if title in movie['title'].lower():
                    return movie
        return {}
    
    def add_movie(self, mood: str, movie: Dict) -> bool:
        """Add a new movie to a mood category"""
        mood = mood.lower().strip()
        if mood in self.movies_by_mood:
            self.movies_by_mood[mood].append(movie)
            return True
        return False
    
    def save_to_file(self, filename: str = "movies_database.json"):
        """Save movie database to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.movies_by_mood, f, indent=2)
    
    def load_from_file(self, filename: str = "movies_database.json"):
        """Load movie database from JSON file"""
        try:
            with open(filename, 'r') as f:
                self.movies_by_mood = json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found. Using default database.")

def main():
    recommender = MovieRecommender()
    
    print(" Welcome to the Movie Recommendation System!")
    print("=" * 50)
    
    while True:
        print(f"\nAvailable moods: {', '.join(recommender.get_available_moods())}")
        print("\nOptions:")
        print("1. Get movie recommendations")
        print("2. Search for a specific movie")
        print("3. Add a new movie")
        print("4. Save database")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            mood = input("\nWhat's your current mood? ").strip()
            try:
                count = int(input("How many recommendations do you want? (default: 3): ") or "3")
            except ValueError:
                count = 3
            
            recommendations = recommender.recommend_movies(mood, count)
            
            if recommendations:
                print(f"\n Here are {len(recommendations)} movie recommendations for your '{mood}' mood:")
                print("-" * 60)
                for i, movie in enumerate(recommendations, 1):
                    print(f"{i}. {movie['title']} ({movie['year']})")
                    print(f"   Genre: {movie['genre']} | Rating: {movie['rating']}/10")
                    print()
            else:
                print(f" Sorry, mood '{mood}' not found. Please try one of the available moods.")
        
        elif choice == '2':
            title = input("\nEnter movie title to search: ").strip()
            movie = recommender.get_movie_by_title(title)
            
            if movie:
                print(f"\n Found: {movie['title']} ({movie['year']})")
                print(f"Genre: {movie['genre']} | Rating: {movie['rating']}/10")
            else:
                print(" Movie not found in database.")
        
        elif choice == '3':
            print(f"\nAvailable moods: {', '.join(recommender.get_available_moods())}")
            mood = input("Enter mood category: ").strip()
            title = input("Enter movie title: ").strip()
            try:
                year = int(input("Enter release year: "))
                rating = float(input("Enter rating (0-10): "))
            except ValueError:
                print(" Invalid year or rating format.")
                continue
            
            genre = input("Enter genre: ").strip()
            
            new_movie = {
                "title": title,
                "year": year,
                "genre": genre,
                "rating": rating
            }
            
            if recommender.add_movie(mood, new_movie):
                print(" Movie added successfully!")
            else:
                print(" Invalid mood category.")
        
        elif choice == '4':
            filename = input("Enter filename (default: movies_database.json): ").strip() or "movies_database.json"
            recommender.save_to_file(filename)
            print(f" Database saved to {filename}")
        
        elif choice == '5':
            print("\n Thanks for using the Movie Recommendation System!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()