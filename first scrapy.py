from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_doubanmovie(url):
    doubanmovie = urlopen(url)
    doubanmovie_bs = BeautifulSoup(doubanmovie,"html.parser")
    on_screening = doubanmovie_bs.find("div",{"class":"screening-bd"})
    while 1:
        try:
            on_screening = on_screening.find('li',class_='ui-slide-item s')
        except:
            print('there is no more movies')
        else:
            print(on_screening['data-title']+'/rate:'+on_screening['data-rate'])
        # screen_follow = on_screening.find_all('li',class_='ui-slide-item',recursive = False)
        # print(screen_follow)


html = urlopen('http://movie.douban.com')
soup = BeautifulSoup(html,'html.parser')
billboard = soup.find('div',{'id':'billboard'}).find('table').find_all('a')
print('豆瓣电影一周口碑榜')
for i in range(len(billboard)):
    print(str(i+1) + ':' + billboard[i].get_text())

