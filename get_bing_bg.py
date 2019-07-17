from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import win32api, win32gui, win32con

today = date.today().strftime('%y%m%d')
file_path = r'C:\Users\Ridoukei\Pictures\必应' + '\\' + today + '.jpg'

# 获取必应搜索背景图的地址
def getUrl():
    html = urlopen('https://cn.bing.com')
    soup = BeautifulSoup(html, 'html.parser')
    url = soup.find('link', {'as':'image'})['href']
    url = 'https://cn.bing.com' + url
    return url

# 按照file_path路径存储图片
def savePic(file_path):
    url = getUrl()
    picbyte = urlopen(url).read()   #read() transform data into bits
    with open(file_path, 'wb') as f:
        f.write(picbyte)

# set wallpaper according to file_path
def setWallPaper(file_path):
    # open register
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,file_path, win32con.SPIF_SENDWININICHANGE)

getUrl()
savePic(file_path)
setWallPaper(file_path)
