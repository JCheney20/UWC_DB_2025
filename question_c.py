#The Hitch Hackers 4323072 question_c DB_Practical 1

def solve(data: list[dict[str, str]]) -> str:
    country_landmass = {}  # Create a variable set to store landmass for each country
    answer = ""
    
    for row in data:  # Iterate through each row in the data 
        country_name = row['CountryName'].strip() 
        landmass = float(row['LandMass']) #convert to float
        
        # Only store each country once 
        if country_name not in country_landmass:
            country_landmass[country_name] = landmass
    
    # Sort by landmass in descending order and get top 5
    countries = sorted(country_landmass.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Return top 5 country names 
    for country in countries:
        answer += f"{country[0]}\n"

    return answer
