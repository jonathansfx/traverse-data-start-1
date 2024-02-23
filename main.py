# opening files and stuff
age_data_file = open("age-data.txt","r")
number_data_file = open("number-data.txt", "r")
survey_results_file = open("survey-results.txt", "r")

# reading the file
age_data = age_data_file.read()
number_data = number_data_file.read()
survey_results = survey_results_file.read()

# age data
underage = 0
youngadult = 0
adult = 0
senior = 0
for x in age_data:
    print(x)