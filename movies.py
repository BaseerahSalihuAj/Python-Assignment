def count_by_genre (movies):
    genre_count = {}
    for movies in movies:
        genres = movies[3].split(",")
        # print(genres)
        for genres in genres:
            if genres in genre_count:
                genre_count[genres] += 1
            else:
                genre_count[genres] = 1
        return genre_count
    
    count_by_genre(movies)
    print(count_by_genre(movies))

    movies = [
    ["Casablanca", "Michael Curtiz", 1942, "Drama"],
    ["The Godfather", "Francis Ford Coppola", 1972, "Crime"],
    ["The Shawshank Redemption", "Frank Darabont", 1994, "Drama"],
    ["The Dark Knight", "Christopher Nolan", 2008, "Action, Thriller"],
    ["Living in Bondage", "Ola Balogun", 1992, "Drama"],
    ["Nneka the Pretty Serpent", "Christian Chukwu", 1994, "Drama, Thriller"],
    ["Rattlesnake", "Amaka Igwe", 1995, "Crime, Thriller"],
    ["Aki na Ukwa", "Chico Ejiro", 2002, "Comedy"],
    ["Saworo IDE", "unknown ", 1997,"Drama"] 
]


    # def find_movie_after_year(movies:list,year): 
    #     for movie in movies:

