import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import *
workbook  = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('Rotten Tomatoes')
table.write(0,0,'Index no.')
table.write(0,1,'URL')
table.write(0,2,'Movie Name')
table.write(0,4,'Introduction')
line = 1
url = 'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/'
f = requests.get(url)

soup = BeautifulSoup(f.content,'lxml')

# Extract Information
movies = soup.find('table',{'class':'table'}).find_all('a')
#print(len(movies))
count = 0

for anchor in movies:
	urls = 'https://www.rottentomatoes.com' + anchor['href']
	count+=1 
	movie_url = urls
	movie_f = requests.get(movie_url)
	movie_soup = BeautifulSoup(movie_f.content,'lxml')
	movie_content = movie_soup.find('div',{'class':'movie_synopsis clamp clamp-6 js-clamp'})
	#print(count, urls,'\n','Movie:'+anchor.string.strip())
	#print('Movie Info:' + movie_content.string.strip())
	table.write(line,0,count)
	table.write(line,1,urls)
	table.write(line,2,anchor.string.strip())
	table.write(line,3,movie_content.string.strip())
	line +=1
	print(count)

workbook.save('movies_top100.xls')

