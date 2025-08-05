#The Hitch Hackers 4323284 question_d.py DB Practical 1

#references:
#https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
#https://www.studytonight.com/python-howtos/count-unique-values-in-python-list
#https://www.askpython.com/python/dictionary/filter-list-of-dictionaries-based-on-key-values


def solve(data: list[dict[str, str]]) -> str:
   
    # "set" prevents counting the same country many times 
    countries_60s80s = set()
    
    # goes over  each row in the data
    for row in data:
        indep_year = row['IndepYear']
        country_name = row['CountryName']
        
        # skips the rows where IndepYear is NULL/empty
        if indep_year == 'NULL' or indep_year == '':
            continue
            
        try:
            # converts the indep year to an integer
            year = int(indep_year)
            
            # checks if the year is between 1960 and 1980 
            if 1960 <= year <= 1980:
                countries_60s80s.add(country_name)

        # skip the rows where indep year can't be converted to an integer        
        except ValueError:
            continue
    
    # returns the string containing the count of countries
    return str(len(countries_60s80s))
