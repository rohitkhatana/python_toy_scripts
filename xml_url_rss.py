from xml.dom import minidom
import urllib2

p = urllib2.urlopen('http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml').read()

x = minidom.parseString(p)

len(x.getElementsByTagName('item') )
