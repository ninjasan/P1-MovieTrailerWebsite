"""
Movie instance definitions
Movie metadata/synopses from IMDB
Trailers from YouTube
"""
__author__ = 'poojm'
import media
import fresh_tomatoes


# Creating Toy Story instance of Movie
TOY_STORY = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman " +
                        "figure supplants him as top toy in a boy's room.",
                        "http://ia.media-imdb.com/images/M/" +
                        "MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@." +
                        "_V1_SY317_CR12,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        1995,
                        81,
                        "G")

# Creating The Matrix instance of Movie
MATRIX = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of " +
                     "his reality and his role in the war against its controllers.",
                     "http://ia.media-imdb.com/images/M/" +
                     "MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@." +
                     "_V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=Q8g9zL-JL8E",
                     1999,
                     136,
                     "R")

# Creating Harry Potter instance of Movie
HARRY_POTTER_1 = media.Movie("Harry Potter and the Sorcerer's Stone",
                             "Rescued from the outrageous neglect of his aunt and uncle, a " +
                             "young boy with a great destiny proves his worth while attending " +
                             "Hogwarts School of Witchcraft and Wizardry.",
                             "http://ia.media-imdb.com/images/M/" +
                             "MV5BMTYwNTM5NDkzNV5BMl5BanBnXkFtZTYwODQ4MzY5." +
                             "_V1_SY317_CR8,0,214,317_AL_.jpg",
                             "https://www.youtube.com/watch?v=VyHV0BRtdxo",
                             2001,
                             152,
                             "PG")

# Creating Lord of the Rings instance of Movie
LORD_OF_THE_RINGS_1 = media.Movie("Lord of the Rings: The Fellowship of the Ring",
                                  "A meek hobbit of the Shire and eight companions set out on " +
                                  "a journey to Mount Doom to destroy the One Ring and the " +
                                  "dark lord Sauron.",
                                  "http://ia.media-imdb.com/images/M/" +
                                  "MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@." +
                                  "_V1_SY317_CR1,0,214,317_AL_.jpg",
                                  "https://www.youtube.com/watch?v=V75dMMIW2B4",
                                  2001,
                                  178,
                                  "PG-13")

# Creating Penelope instance of Movie
PENELOPE = media.Movie("Penelope",
                       "A modern romantic tale about a young aristocratic heiress born under a " +
                       "curse that can only be broken when she finds true love with \"one who " +
                       "will love her faithfully.\"",
                       "http://ia.media-imdb.com/images/M/" +
                       "MV5BMTc0MTYwNzQ5Nl5BMl5BanBnXkFtZTcwMjg2MzU1MQ@@." +
                       "_V1_SY317_CR2,0,214,317_AL_.jpg",
                       "https://www.youtube.com/watch?v=dLFuTrr4URM",
                       2006,
                       104,
                       "PG")

# Creating Wall-E instance of Movie
WALLE = media.Movie("WALL-E",
                    "In the distant future, a small waste collecting robot inadvertently " +
                    "embarks on a space journey that will ultimately decide the fate of mankind.",
                    "http://ia.media-imdb.com/images/M/" +
                    "MV5BMTczOTA3MzY2N15BMl5BanBnXkFtZTcwOTYwNjE2MQ@@." +
                    "_V1_SY317_CR0,0,214,317_AL_.jpg",
                    "https://www.youtube.com/watch?v=alIq_wG9FNk",
                    2008,
                    98,
                    "G")

# List of movie instances
MOVIES = [TOY_STORY, MATRIX, HARRY_POTTER_1, LORD_OF_THE_RINGS_1, PENELOPE, WALLE]
fresh_tomatoes.open_movies_page(MOVIES)
