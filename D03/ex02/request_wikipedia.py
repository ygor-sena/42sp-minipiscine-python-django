import dewiki
import requests
import sys

def request_wiki_search():
	subject = sys.argv[1]
	url = 'https://en.wikipedia.org/w/api.php'
	params = {
            'action': 'parse',
            'page': subject,
            'format': 'json',
            'prop': 'wikitext',
            'redirects':'true'
		}
	try:
		response = requests.get(url, params)
		response.raise_for_status()
	except requests.HTTPError:
		print("Could not connect to the given URL.")
	try:
		data = response.json()
		print(data)
	except Exception:
		print("Could not write in JSON format.")
	try:
		return dewiki.from_string(data["parse"]["wikitext"]["*"])
	except Exception:
		print("Wikipedia doesn't have a page about '{}'.".format(sys.argv[1]))

def main():
	if (len(sys.argv) != 2):
		sys.exit("Usage: <request_wikipedia.py> <\"string to be searched\">")
	result = request_wiki_search()
	if result is not None:
		filename = "".join([sys.argv[1].replace(' ', "_"), ".wiki"])
		with open(filename, "w") as file:
			file.write(result)

if __name__ == '__main__':
	main()
