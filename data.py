import urllib.request

name = input('OSRS Name ')

url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
visit_url = urllib.request.urlopen(url)
information = visit_url.read()
levels = information.split(b'\n')

print(levels[:])
