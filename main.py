import csv
import question_a
import question_b
import question_c
import question_d
import question_e
import question_f
import question_g
import question_h

# read the csv file, converting the rows to dictionaries
# returns a list of dictionaries
def parse_csv(file_name: str) -> list[dict[str, str]]:
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        keys = next(reader)
        data = list()
        for row in reader:
            data.append(dict(zip(keys, row)))

    return data

def main():
    # keys are
    # CityName, CityPopulation, CountryName,
    # Continent, Region, LandMass, IndepYear,
    # CountryPopulation, LifeExpectancy, GNP,
    # GovernmentForm, HeadOfState, Capital,
    # Language, Percentage
    data = parse_csv("file.txt")
    text = "Question a:\n" + question_a.solve(data) + "\n\n"
    text += "Question b:\n" + question_b.solve(data) + "\n\n"
    text += "Question c:\n" + question_c.solve(data) + "\n\n"
    text += "Question d:\n" + question_d.solve(data) + "\n\n"
    text += "Question e:\n" + question_e.solve(data) + "\n\n"
    text += "Question f:\n" + question_f.solve(data) + "\n\n"
    text += "Question g:\n" + question_g.solve(data) + "\n\n"
    text += "Question h:\n" + question_h.solve(data) + "\n\n"

    print(text)
    with open("file2.txt", "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()
