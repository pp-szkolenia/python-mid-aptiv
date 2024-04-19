import requests
from bs4 import BeautifulSoup


rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def scrape_single_book(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1").text
    price = float(soup.find("p", "price_color").text.replace("Â£", ""))
    upc = soup.find("table", "table-striped").find("tr").find("td").text
    rating_str = soup.find("p", "star-rating").attrs["class"][1]
    rating_int = rating_dict[rating_str]

    book_dict = {
        "title": title,
        "price": price,
        "rating": rating_int,
        "upc": upc
    }
    return book_dict


def scrape_single_category(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, "html.parser")

    all_books = soup.find_all("article", "product_pod")
    book_hrefs = []
    for book in all_books:
        book_href = book.find("a")["href"].replace("index.html", "")
        book_hrefs.append(book_href)

    all_books_data = []
    for href in book_hrefs:
        # try:
        book_data = scrape_single_book(category_url + href)
        all_books_data.append(book_data)
        # except Exception as e:
        #     pass

    return all_books_data


if __name__ == "__main__":
    url = "http://books.toscrape.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    categories_list = soup.find("ul", "nav").find("ul").find_all("li")

    result = {}
    for category in categories_list[:4]:
        category_name = category.text.strip()
        category_href = category.find("a")["href"].replace("index.html", "")

        category_data = scrape_single_category(url + category_href)
        rating_data = [book["rating"] for book in category_data]
        rating_mean = sum(rating_data) / len(rating_data)

        result[category_name] = round(rating_mean, 2)

    print(result)
