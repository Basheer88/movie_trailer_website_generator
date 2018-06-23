import fresh_tomatoes
import media

# Add Movies
# variable = media.Movie(movie name, story line, poster image, trialer url)
black_panther = media.Movie("Black Panther",
                            "T'Challa is crowned king of Wakanda following his father's death, but his sovereignty is soon challenged by a new adversary who plans to abandon the country's isolationist policies and begin a global revolution.",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=x02xX2dv6bQ")

thor_ragnarok = media.Movie("Thor Ragnarok",
                            "Thor must escape the alien planet Sakaar in time to save Asgard from Hela and the impending Ragnarok",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")

pacific_rim_u = media.Movie("Pacific Rim Uprising",
                            "In 2035, the plot follows humanity again fighting Kaiju, the giant monsters set on destroying the world.",
                            "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",
                            "https://www.youtube.com/watch?v=kbYkQmt0b7s")

gringo = media.Movie("Gringo",
                     "a mild-mannered businessman sent to Mexico to deliver an experimental marijuana pill. When he is kidnapped by the drug cartel he must escape alongside a hired mercenary.",
                     "https://upload.wikimedia.org/wikipedia/en/e/e3/GringoPoster.jpeg",
                     "https://www.youtube.com/watch?v=6lKqPuO6N2U")

bumblebee = media.Movie("Bumblebee",
                        "In 1987, Bumblebee takes refuge in a small California beach town junkyard, where a teenage girl named Charlie Watson takes him in. However, the two of them soon find themselves hunted by a government agency known as Sector 7, led by Agent Burns. As they run from society, the two learn that Bee isn't the only Transformer on Earth, and that the others might not be as friendly.",
                        "https://upload.wikimedia.org/wikipedia/en/0/04/Bumblebee_teaser_poster.jpg",
                        "https://www.youtube.com/watch?v=fAIX12F6958")

terminator_6 = media.Movie("Terminator 6",
                           " I will be back. he said, and so he will, for the sixth time. The timey-wimey cyborg franchise is marching off into the future with no signs of slowing down",
                           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfcot1qdimyd7y81xODCLdr9aL5hH7aOAS1LejnbeaB3ZF3LcP",
                           "https://www.youtube.com/watch?v=jLCiy3zOQaE")

#collect movies on a single list
movies = [black_panther, thor_ragnarok, pacific_rim_u, gringo, bumblebee, terminator_6]

#creat webpage using open_movies_page(movies list)
fresh_tomatoes.open_movies_page(movies)
