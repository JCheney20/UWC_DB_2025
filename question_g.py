# The-Hitch-Hackers 4323819 question_g.py DB Practical 1

# Reference:
# https://www.geeksforgeeks.org/python/python-increment-value-in-dictionary/

# Helper func to get Language of a city
def get_Lang(city):
    return city["Language"]


def solve(data: list[dict[str, str]]) -> str:
    answer = ""
    spokenLanguages = {}

# Calc num of cities that speak a language, inc if it is already there, add if not
    for city in data:
        spokenLanguages[get_Lang(city)] = spokenLanguages.get(get_Lang(city), 0)+1

    # Sort the list in descending order
    sortedLanguages = sorted(spokenLanguages.items(), reverse=True, key=lambda lang: lang[1])

    # Add the top 5 to the answer string
    for i in range(5):
        answer += f"\n{i+1}) {sortedLanguages[i][0]}"

    return answer
