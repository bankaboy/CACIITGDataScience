from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
print(soup.find(text='bad'))
print(soup.i)
soup = BeautifulSoup("<tag1>Some</tag2>bad<tag3>XML",'xml')
print(soup.prettify())