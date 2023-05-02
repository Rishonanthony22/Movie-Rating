class MovieReview:
    def __init__(self, movie_name, story_rating, actor_rating, music_rating):
        self.movie_name = movie_name
        self.story_rating = story_rating
        self.actor_rating = actor_rating
        self.music_rating = music_rating
        self.avg = int((story_rating + actor_rating + music_rating) / 3)
        self.myrating = {"Story": story_rating, "Actors": actor_rating, "Music": music_rating}
    
    def add_movie_ratings(self, movie_list):
        movie_list.append(self.myrating)
        
    def get_star(self, movie_list):
        for rating in movie_list:
            avg_rating = int((rating["Story"] + rating["Actors"] + rating["Music"]) / 3)
            stars = "*" * avg_rating
            print(stars + " " + self.movie_name)

# Create a global list variable moviereviews = []
moviereviews = []

# Create an object of the class MovieReview
movie1 = MovieReview("Titanic", 5, 4, 5)

# Add the movie ratings to the movie list
movie1.add_movie_ratings(moviereviews)

# Get the star rating for each movie in the list
movie1.get_star(moviereviews)
