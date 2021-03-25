
import pyshorteners as sh

link = 'https://www.youtube.com/channel/UCZQkssgRd4o2jcxT3c55bbg'

s = sh.Shortener()
x = (s.tinyurl.short(link))

print(x)
