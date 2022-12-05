#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

#URL = "https://swapi.dev/luke/force"      # Comment out this line
URL= "https://swapi.dev/api/people/4/"     # Uncomment this line

def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    # check to see if the status is anything other than what we want, a 200 OK
    if resp.status_code == 200:
        # convert the JSON content of the response into a python dictionary
        vader= resp.json()
        pprint(vader)
        print(f"{vader['name']} was born in the year {vader['birth_year']}. His eyes are now {vader['eye_color']} and his hair color is {vader['hair_color']}") #C1
    else:
        print("That is not a valid URL.")


#C2
#resp = requests.get(vader['films'][0])
#first_movie = resp.json()

#resp = requests.get(vader['starships'][0])
#ship = resp.json()

#print(f"He first appeared in the movie {first_movie['title']} and could be found flying around in his {ship['name']}")



    resp = requests.get(vader['films'][0])
    first_movie = resp.json() # skip checking for the 200

    # pick up the name of his ship
    resp = requests.get(vader['starships'][0])
    ship = resp.json() 

    # this solution uses "f-strings" (string templates) to return the data
    print(f"He first appeared in the movie {first_movie['title']} and could be found flying around in his {ship['name']}.")

if __name__ == "__main__":
    main()

