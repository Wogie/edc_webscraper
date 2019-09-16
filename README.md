# EDC webscraper
This script downloads all addresses, prices and price/m2 of apartments from edc with given zip-code interval

Example use:\
`git clone https://github.com/Wogie/edc_webscraper`\
`cd edc_webscraper`\
`python edc_webscraping.py 1000-3000  # Scrapes properties in zip code interval 1000-3000`

Results can be found in `boligliste.csv` and looks like this:

|                                              |          |                        | 
|----------------------------------------------|----------|------------------------| 
| Addresses                                    | Prices   | Price per square meter | 
| Laksegade 20D 1 tv, 1063 København K         | 3245000  | 55948                  | 
| Boldhusgade 4 st., 1062 København K          | 3795000  | 41250                  | 
| Dybensgade 21 3, 1071 København K            | 4995000  | 57414                  | 
| Laksegade 20B 1 mf, 1063 København K         | 2995000  | 55463                  | 
| Peder Skrams Gade 28 1 tv, 1054 København K  | 4495000  | 59145                  | 
| Laksegade 20E 2, 1063 København K            | 3550000  | 47333                  | 
| Havnegade 35 4 th, 1058 København K          | 9500000  | 77869                  | 
| Boldhusgade 2 2, 1062 København K            | 7695000  | 53438                  | 
| Nyhavn 38, st. Dør/lejl. 4, 1051 København K | 10500000 | 126506                 | 

