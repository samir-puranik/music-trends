# Billboard API Docs: https://github.com/guoguo12/billboard-charts

import billboard

old = "2019-01-04"

chart = billboard.ChartData('billboard-200', date=old)

song = chart[0]

print(song.title)
print(song.artist)
