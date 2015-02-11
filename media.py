# definition for class movie
class Movie:
	""" This class provides a way to store movie related information"""
	def __init__(self,title,poster_image_url,trailer_youtube_url):
		""" constructor with title,Box Art URL and YouTube URL"""
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def addActors(self,actors):
		"""adds a list of actors"""
		self.actors = actors

	def addReleaseDate(self,date):
		"""adds a release date"""
		self.releaseDate = date
