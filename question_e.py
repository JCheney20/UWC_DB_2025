#The Hitch Hackers 4323284 question_e.py DB Practical 1

#references:
#https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
#https://www.askpython.com/python/dictionary/filter-list-of-dictionaries-based-on-key-values
#https://www.w3schools.com/python/python_sets.asp
#https://docs.python.org/3/library/stdtypes.html#str.join
#https://realpython.com/python-list/


def solve(data: list[dict[str, str]]) -> str:
    
    # using "set" prevents listing the same country many times
    countries_30s50s = set()
    
    # goes over each row in the data
    for row in data:
        indep_year = row['IndepYear']
        country_name = row['CountryName']
        
        # skip the rows where IndepYear is NULL/empty
        if indep_year == 'NULL' or indep_year == '':
            continue
            
        try:
            # converts the indep year to integer
            year = int(indep_year)
            
            # checks if the year is between 1830 and 1850 
            if 1830 <= year <= 1850:
                countries_30s50s.add(country_name)

         # skips the rows where IndepYear can't be converted to integer        
        except ValueError:
            continue
    
    # converts set to a sorted list 
    countriesList = sorted(list(countries_30s50s))
    
    # joins the countries and return as a string
    if countriesList:
        return '\n'.join(countriesList)
    else:
        return "no countries found"
