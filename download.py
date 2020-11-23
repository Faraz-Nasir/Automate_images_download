import requests,bs4,os

url="https://xkcd.com"
while not url.endswith("#"):
    #Download The page
    print("Downloading Page "+url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    url=soup.select('#comic img')
    if(url==[]):
        print("Image Not Found")
    else:
        image_url=url[0].get("src")
        image_url=image_url.replace("//","https://")
        print("Downloading Image:  "+image_url)
        res=requests.get(image_url)
        res.raise_for_status()
        #SAVING THE IMAGE
        image_file=open(os.path.join('xkcd',os.path.basename(image_url)),'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

        #SETTING THE PREVIOUS URL BUTTON
        prevlink=soup.select('a[rel="prev"]')[0]
        url="https://xkcd.com"+prevlink.get('href')


print("DONE")