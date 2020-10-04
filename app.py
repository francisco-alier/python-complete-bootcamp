# Decide where to store movies in code
# store in list!
# movies = []
# Decide what data we want to store for each movie
# use dicts or tuples, make decision! Lets use dictionary: title, director, year
# Show the user a menu and let them pick an option
# Run a loop to get their input at the begining and at the end!

# Implement each requirement in turn, each as a seperate function
# Stop running the program when they type 'q in the menu


MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []
title = "The matrix"


# function fo adding movies by input from user
def add_movies():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    new_movie = {
        'title': title,
        'director': director,
        'year': year
    }

    movies.append(new_movie)


def print_movies(movie):
    print(f"The name of the movie is: {movie['title']}")
    print(f"The director of the movie is: {movie['director']}")
    print(f"The year of release of the movie is: {movie['year']}")


# Function for listing movies
def list_movies():
    for movie in movies:
        print_movies(movie)


def find_movie():
    user_question = input("Which title are you searching?")
    for movie in movies:
        if title == movie['title']:
            print_movies(movie)


user_options = {
    "a": add_movies,
    "l": list_movies,
    "f": find_movie
}


# Actual App
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':

        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

# Remember to run the user menu function at the end!
menu()