class Movie:
	""" This class allows you to create new instances of a Movie with a title, poster and trailer """

	def __init__(self,title, poster_image_url, trailer_youtube_url):
		"""
		The inputs are the follwing:
	    title - movi title
	    poster_image_url - URL of the image for the poster
	    trailer_youtube_url - Youtub URL from the movie trailer
	    """
		self.title = title
		self.poster_image_url = poster_image_url		
		self.trailer_youtube_url = trailer_youtube_url
