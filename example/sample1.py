from IMDB import IMDB
def main():
    while 1:
        imdb = IMDB()
        movie = input("Enter a movie: ").strip();
        if movie == 'quit':
            break
        if movie:
            print("Movie Rated: "+imdb.getRating(movie)+" out Of 10")
        else:
            print("enter a valid movie name")
main()