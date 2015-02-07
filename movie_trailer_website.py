#!/usr/bin/python

import datetime
import fresh_tomatoes
import media

# main method
def main():
	# initiate movie instances
	# Herr Lehmann
	herrLehmann = media.Movie("Herr Lehmann",
		"http://www.cineasten.de/bilder/filme/herr-lehmann/l.jpg",
		"https://www.youtube.com/watch?v=NeS9aSYJcUM")
	herrLehmann.addActors(["Detlev Buck","Michael Gwisdek","Christian Ulmen",
		"Janek Rieke","Katja Danowski","Michael Beck","Margit Bendokat"])
	herrLehmann.addReleaseDate(datetime.date(2003,10,3))
	# Blade Runner
	bladeRunner = media.Movie("Blade Runner",
		"http://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
		"https://www.youtube.com/watch?v=eogpIG53Cis")
	bladeRunner.addActors(["Harrison Ford","Rutger Hauer","Sean Young","Edward James Olmos",
		"Daryl Hannah","M. Emmet Walsh","Joe Turkel","William Sanderson",
		"Brion James","Joanna Cassidy","Morgan Paull","James Hong"])
	# Whatever Works
	whateverWorks = media.Movie("Whatever Works",
		"http://upload.wikimedia.org/wikipedia/en/7/77/Whatever_works.jpg",
		"https://www.youtube.com/watch?v=7vvDhtfil3U")
	whateverWorks.addReleaseDate(datetime.date(2009,5,19))
	# movie 
	fightClub = media.Movie("Fight Club",
		"http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
		"https://www.youtube.com/watch?v=SUXWAEX2jlg")

	# put everything in a list
	movies = [herrLehmann,bladeRunner,whateverWorks,fightClub]

	# call function open_movies_page to creates an HTML file
	fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__': main()