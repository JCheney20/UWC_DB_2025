# https://realpython.com/sort-python-dictionary/
# https://www.w3schools.com/python/ref_list_sort.asp

def solve(data: list[dict[str, str]]) -> str:
    validData = []
    addedCountries = []
    answer = ""

    # Removing cities with NULL values for Life Expectancy; that aren't in Africa; that are in the same country as a city that was already added
    for city in data:
        if city["LifeExpectancy"] != "NULL" and city["Continent"] == "Africa" and city["CountryName"] not in addedCountries:
            validData.append(city)
            addedCountries.append(city["CountryName"])

    # Sort the list of African cities by the Life Expectancy
    sortedCities = sorted(validData, reverse=True, key=lambda city: float(city["LifeExpectancy"]))

    #Add the top 5 to a string to be returned
    for i in range(5):
        answer += f"\n{i+1}) {sortedCities[i]["CountryName"]}"

    return answer
