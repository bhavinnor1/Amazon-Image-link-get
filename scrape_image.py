from bs4 import BeautifulSoup
import requests

def img_link(name):
	url="https://www.amazon.in/s?k="+name.replace(' ','+')
	page=requests.get(url,timeout=10)
	htmltxt=page.text
	soup = BeautifulSoup(htmltxt, "lxml")
	linklist=[]
	dict={}
	for image in soup.select('img[class="s-image"]'):
		linklist.append(image.get('src'))
		dict[image.get('src')]=image.get('alt')
		img=dict[linklist[0]]
		if linklist[0]==None:
			continue
		return {'link':linklist[0],'name':img}
		break
	return img_link(name)

if __name__=="__main__":
	name=input('Enter Name: ')
	print(img_link(name))
