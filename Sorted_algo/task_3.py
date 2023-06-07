def sort_movies(movies):
    sorted_movies = sorted(movies, key=lambda movie: (movie['rating'], movie['genre'], movie['year']), reverse=True)
    return sorted_movies


movies = [
    {'title': 'Aboba', 'rating': 8.5, 'genre': 'Drama', 'year': 2010},
    {'title': 'Boba', 'rating': 7.8, 'genre': 'Action', 'year': 2015},
    {'title': 'Biba', 'rating': 9.2, 'genre': 'Comedy', 'year': 2012},
    {'title': 'HSE', 'rating': 8.0, 'genre': 'Drama', 'year': 2010}
]

sorted_movies = sort_movies(movies)
for movie in sorted_movies:
    print(movie['title'], movie['rating'], movie['genre'], movie['year'])

