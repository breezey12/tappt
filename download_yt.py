import sh
import sys


url = sys.argv[1]
sh.youtube_dl(url)
print "does this print after downloading"
