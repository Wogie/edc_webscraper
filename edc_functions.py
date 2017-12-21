import requests
from bs4 import BeautifulSoup


def test_for_max_func(soup):
    for i in soup.findAll('li'):
        try:
            if "searchwarning__text" in i['class']:
                print("Warning:\nmore than 1000 results")
                return True
        except KeyError:
            return False


def zip_iterations(list_of_minima, stepsize):
    addresses = []
    prices = []
    extramin = []
    prices_per_square = []
    i = 0

    for my_minimum in list_of_minima:
        i += 1
        print("%i out of %i iterations" % (i, len(list_of_minima)))

        if my_minimum == list_of_minima[-1]:
            last = 1
        else:
            last = 0

        url_to_scrape = \
            'https://www.edc.dk/sog/?postnr=%i-%i&sort=liggetid&antal=1000&side=1#lstsort' \
            % (my_minimum, my_minimum + stepsize - 1 + last)

        r = requests.get(url_to_scrape)

        soup = BeautifulSoup(r.text, 'lxml')

        if test_for_max_func(soup):
            print("Zip code: %i-%i" % (my_minimum, my_minimum + stepsize - 1 + last))
            print("Tries in smaller bites after current loop")
            extramin.extend((my_minimum, my_minimum + 50))
            continue

        selection = soup.select("[class$=propertyitem--list]")

        for element in selection:
            price = element.findAll('strong')
            price = "%r" % price
            price = price.split(">")[1].split("<")[0].split()[1]
            price = int("".join(price.split(".")))

            prices.append(price)

            info = element.find('a')
            address = info['title']

            addresses.append(address)

            try:
                p_per_square = element.findAll('td')[6].string
                prices_per_square.append(p_per_square)
            except IndexError:
                prices_per_square.append("N/A")

        print("\nAccumulative results: %i\n" % len(prices))

    return addresses, prices, extramin, prices_per_square
