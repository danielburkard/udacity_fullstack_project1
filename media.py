# definition for class movie
class Movie:
	""" This class provides a way to store movie related information"""
	# constructor with title,Box Art URL and YouTube URL
	def __init__(self,title,poster_image_url,trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	# adds a list of actors
	def addActors(self,actors):
		self.actors = actors

	# adds a release date
	def addReleaseDate(self,date):
		self.releaseDate = date