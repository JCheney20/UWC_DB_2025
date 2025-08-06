# The Hitch Hackers 4323819 question_g.py DB Practical 1

# Reference:
# https://www.geeksforgeeks.org/python/python-increment-value-in-dictionary/

# Helper func to get Language of a city
def getLang(city):
    return city["Language"]


def solve(data: list[dict[str, str]]) -> str:
    answer = ""
    spokenLanguages = {}
    vistedCountryLang = []

# Calc num of cities that speak a language, inc if it is already there, add if not
    for city in data:
        countryLang = f"{city["CountryName"]}{city["Language"]}"
        if city["Language"] != "" and countryLang not in vistedCountryLang:
            pertSpoken = (int(city["CountryPopulation"]) * (float(city["Percentage"])/100))
            spokenLanguages[getLang(city)] = spokenLanguages.get(getLang(city), 0)+pertSpoken
            vistedCountryLang.append(countryLang)

    # Sort the list in descending order
    sortedLanguages = sorted(spokenLanguages.items(), reverse=True, key=lambda lang: lang[1])[:5]

    # Add the top 5 to the answer string
    for language in sortedLanguages:
        answer += f"{language[0]} - {language[1]}\n"

    return answer
