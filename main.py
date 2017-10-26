# Author: Fernando Espinosa	
import webbrowser
import sys

youtube_main = 'https://www.youtube.com/results?search_query='

if len(sys.argv) > 1:
	webbrowser.open(youtube_main + str(sys.argv[1]))