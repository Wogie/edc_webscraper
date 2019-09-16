import edc_functions as edc
import sys

try:
    postnumre = sys.argv[1]
except IndexError:
    postnumre = "1000-3000"

postnumre = postnumre.split("-")
mins = list(range(int(postnumre[0]), int(postnumre[1]), 100))

addresses, prices, extramin, prices_per_square = \
    edc.zip_iterations(mins, stepsize=100)

if len(extramin) > 0:
    print("\nIterations with smaller intervals:")
    addresses2, prices2, extramin2, prices_per_square2 = \
        edc.zip_iterations(extramin, stepsize=50)
    addresses.extend(addresses2)
    prices.extend(prices2)
    prices_per_square.extend(prices_per_square2)

    if len(extramin2) > 0:
        addresses3, prices3, extramin3, prices_per_square3 = \
            edc.zip_iterations(extramin, stepsize=25)
        addresses.extend(addresses3)
        prices.extend(prices3)
        prices_per_square.extend(prices_per_square3)

print("Total results: %i" % len(prices))

string_to_print = "Addresses;Prices;Price per square meter"

to_print_list = []

for i in range(len(prices)):
    element = "%s;%i;%s" % (addresses[i], prices[i], prices_per_square[i])
    to_print_list.append(element)

to_print_list = "\n".join(to_print_list)

string_to_print = "\n".join((string_to_print, to_print_list))

boligliste = open("boligliste.csv", "w", encoding='utf8')
boligliste.write(string_to_print)
boligliste.close()
