
def solve(data: list[dict[str, str]]) -> str:
    city_populations = {}  # Create a  to store the highest population for each city
    
    for row in data:  # Iterate through each row
        city_name = row['CityName'].strip()
        population = int(row['CityPopulation'])  
        
        # store only the highest population for each city, update if current population is higher
        if city_name not in city_populations or population > city_populations[city_name]:
            city_populations[city_name] = population
    
    # Sort cities by population 
    top_cities = sorted(city_populations.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Return just the top 5 city names
    return [city[0] for city in top_cities]
