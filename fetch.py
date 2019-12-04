import urllib
import urllib2
import re

page = urllib.urlopen("https://www.facebook.com/profile.php?id=100009757061339", 'r')
content = page.read()

soup = BeautifulSoup(page)

links = soup.findAll("a")

test = open('test.txt', 'w')

for line in page:
    #word = line.split()
    re.findall('happy birthday', line, re.IGNORECASE)
    test.write(line)