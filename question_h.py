#The Hitch Hackers
#4323399
#question_h
#DB_Practical 1

def solve(data: list[dict[str, str]]) -> str:
    countries_ending_with_a = set() #Created a variable set to place the country names ending with 'a' (set () ignores duplicate values)

    for row in data: #For loop to iterate through each row in the data
        country_name = row['CountryName'].strip().lower()  #Get the country names and removes any leading and trailing whitespaces

        if country_name.lower().endswith('a'): #Checks if the country name ends with 'a'
            countries_ending_with_a.add(country_name)  #Adds to set

    if not countries_ending_with_a:
        return "No countries found that end with 'a'."
    else:
        sorted_countries = sorted(countries_ending_with_a) #sorts the countries alphabetically
        countries_list = "\n".join(sorted_countries) #joins all items into one string
        return countries_list #returns list of country names ending with a

