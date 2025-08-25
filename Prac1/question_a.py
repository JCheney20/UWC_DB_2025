# The Hitch Hackers 4323399 question_a DB_Practical 1

def solve(data: list[dict[str, str]]) -> str:
    countries_end_with_a = set() # Created a variable set to place the country names ending with 'a' (set () ignores duplicate values)

    for row in data: # For loop to iterate through each row in the data
        country_name = row['CountryName'].strip().lower()  # Get the country names and removes any leading and trailing whitespaces

        if country_name.lower().endswith('a'): # Checks if the country name ends with 'a'
            countries_end_with_a.add(country_name)  # Adds to the set

    return f"{len(countries_end_with_a)}" # Returns number of items
