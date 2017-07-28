import fresh_tomatoes
import media

#Create instances of Movie
star_wars_1 = media.Movie("Star Wars: Episode 1",
	"https://upload.wikimedia.org/wikipedia/en/thumb/4/40/Star_Wars_Phantom_Menace_poster.jpg/220px-Star_Wars_Phantom_Menace_poster.jpg",
	"https://www.youtube.com/watch?v=bD7bpG-zDJQ")

star_wars_2 = media.Movie("Star Wars: Episode 2",
	"https://upload.wikimedia.org/wikipedia/en/thumb/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg/220px-Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg",
	"https://www.youtube.com/watch?v=gYbW1F_c9eM")

star_wars_3 = media.Movie("Star Wars: Episode 3",
	"https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg/220px-Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
	"https://www.youtube.com/watch?v=5UnjrG_N8hU")

#Creat list with movie instances
list_of_movies = [star_wars_1, star_wars_2, star_wars_3]

#Run method from fresh_tomatoe package and pass the list of movies
fresh_tomatoes.open_movies_page(list_of_movies)
