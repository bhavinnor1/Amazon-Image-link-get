from bs4 import BeautifulSoup
import requests

def img_link(name):
	url="https://www.amazon.in/s?k="+name.replace(' ','+')
	page=requests.get(url)
	htmltxt=page.text
	soup = BeautifulSoup(htmltxt, "lxml")
	for image in soup.select('img[class="s-image"]'):
		link=image.get('src'))
		name_in_alt=image.get('alt')
		if link==None:
			continue
		return {'link':link,'name':name_in_alt}
		break
	return img_link(name)

if __name__=="__main__":
	name=input('Enter Name: ')
	print(img_link(name))
