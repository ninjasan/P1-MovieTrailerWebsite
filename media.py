"""
Movie Class definition
"""
__author__ = 'poojm'
import webbrowser


# Defining class Movie
class Movie:
    """Summary of Movie Class.

    Object that contains information relevant to movies.

    Attributes:
        title: A string representing the name of the Movie
        storyline: A string representing the synopsis of the Movie
        poster_image_url: A string representing the URL
                            of the movie poster image
        trailer_youtube_url: A string representing the URL of the
                            movie's trailer
        release_year: An integer representing the year the movie was released
        duration_in_minutes: An integer representing the length of the movie
                            in minutes
        mpaa_rating: A string representing the MPAA rating of the movie
    """
    def __init__(self, title, storyline, poster_image_url, trailer_url, release_year,
                 duration, mpaa_rating):
        """Inits MovieClass with a title, storyline, Poster URL, trailer URL,
        release year, duration, and the MPAA rating.
        :rtype : object
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url
        self.release_year = release_year
        self.duration_in_minutes = duration
        self.mpaa_rating = mpaa_rating

    def show_trailer(self):
        """Performs operation to view the trailer."""
        webbrowser.open(self.trailer_youtube_url)
