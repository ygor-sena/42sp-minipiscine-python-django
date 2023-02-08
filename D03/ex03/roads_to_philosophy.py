from bs4 import BeautifulSoup
import sys
import requests

class SearchWiki:
	def __init__(self):
		self.history = []

	def road_to_philosophy(self, arg):
		while not 'Philosophy' in self.history:
			topic =  arg
			url = "".join(["https://en.wikipedia.org", topic])

			try:
				response = requests.get(url)
				response.raise_for_status()
			except requests.HTTPError:
				raise
			
			soup = BeautifulSoup(response.text,'html.parser')
			title = soup.find(id="firstHeading").text

			if title in self.history:
				return print("It leads to an infinite loop !")
			self.history.append(title)

			article = soup.find(id="mw-content-text")
			for i in self.history:
				print (i)
			
			content = article.select('p > a')
			for link in content:
				if link.get('href') != None and link['href'].startswith('/wiki/') \
						and not link['href'].startswith('/wiki/wikipedia:') \
						and not link['href'].startswith('/wiki/Help:'):
					return self.road_to_philosophy(link['href'])
			return print("It leads to a dead end !")
		return print("{} roads {} from to philosophy !".format(len(self.history), self.history[0]))

def main():
	if len(sys.argv) != 2:
		sys.exit("Usage: <roads_to_philosophy.py> <string to search>")
	log = SearchWiki()
	try:
		log.road_to_philosophy("/wiki/" + sys.argv[1].replace(" ", "_"))
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()
