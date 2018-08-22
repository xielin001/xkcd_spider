import os,urllib,bs4
from urllib import request
url = 'https://xkcd.com/'
os.makedirs('xkcd',exist_ok=True)


while not url.endswith('#'):
    html = urllib.request.urlopen(url).read()
    # html.raise_for_status()
    soup = bs4.BeautifulSoup(html)
    htmlurl = soup.select('#comic img')
    if len(htmlurl) == 0:
        print("Could not find comic image")
    else:
        # img={'src': '//imgs.xkcd.com/comics/driving_cars.png', 'alt': 'Driving Cars', 'srcset': '//imgs.xkcd.com/comics/driving_cars_2x.png 2x', 'title': "It's probably just me. If driving were as dangerous as it seems, hundreds of people would be dying every day!"}
        downloadurl = 'https:' + htmlurl[0].get('src')
        comicname = os.path.basename(downloadurl)
        print("Downloading image %s...." % downloadurl)
        img = urllib.request.urlopen(downloadurl).read()
        file = os.path.join('xkcd', comicname)
        with open(file, 'wb') as f:
            f.write(img)
        f.close()
        prevlink = soup.select('a[rel="prev"]')
        preimg = prevlink[0].get('href')
        url = 'https://xkcd.com/' + preimg