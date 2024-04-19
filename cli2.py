import argparse
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def scrape_n_quotes(n, verbose):
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    if verbose:
        print(f"Response code: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    result = [quote.text for quote in soup.find_all('span', "text")][:n]
    return result


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", metavar="number", type=int, help="Number of quotes to scrape",
                    required=True, choices=[1, 2, 3])
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()
print(args)

if __name__ == "__main__":
    result = scrape_n_quotes(args.number, args.verbose)
    pprint(result)
