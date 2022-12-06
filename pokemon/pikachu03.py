#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return 1000
    # items in one response
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    # create a list to store items with the word searched on
    matchedwords = []

    # Loop through data, and print pokemon names
    # item.get("results") will return the list
    # mapped to the key "results"
    for item in items.get("results"):
        # check to see if the current item's VALUE mapped to item["name"]
        # contains the search word
        if args.searchword in item.get("name"):
            # if TRUE, add that item to the end of list matchedwords
            matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()
    ## map our matchedword list to a dict with a title
    matchedwords = {}
    matchedwords["matched"] = finishedlist

    ## list all words containing matched word
    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)

    ## export to excel with pandas
    # make a dataframe from our data
    itemsdf = pandas.DataFrame(matchedwords)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    itemsdf.to_excel("pokemonitems.xlsx", index=False)

    print("Gotta catch 'em all!")
    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()

    allpoke =[]
    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        print(poke.get("name"))
        allpoke.append(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")
    
    pokedf = pandas.DataFrame(allpoke)

    pokedf.to_csv("pokemonlist.csv")
    pokedf.to_json("pokemonlist.json")
    pokedf.to_excel("pokemonlist.xlsx", index=False)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search\
    the Pokemon item API")
    parser.add_argument('--searchword', metavar='SEARCHW',\
    type=str, default='ball', help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()

