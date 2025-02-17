# age data
with open('age-data.txt','r') as age_data_file:
    age_data = age_data_file.read().split('\n')
    
underage = 0
young_adult = 0
adult = 0
senior = 0
for x in range(0, len(age_data)):
    age_data[x] = int(age_data[x])
    if age_data[x] < 18:
        underage += 1
    elif age_data[x] >= 18 and age_data[x] <= 35:
        young_adult += 1
    elif age_data[x] >= 36 and age_data[x] <= 65:
        adult += 1
    else:
        senior += 1

# number data
with open('number-data.txt', 'r') as number_data_file:
    number_data = number_data_file.read().split('\n')

even_numbers = 0
odd_numbers = 0

for x in range(0, len(number_data)):
    number_data[x] = int(number_data[x])
    if number_data[x] % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

# survey data
with open('survey-results.txt', 'r') as survey_results_file:
    survey_results = survey_results_file.read().split('\n')

yes_response = 0
no_response = 0
maybe_response = 0

for x in range(0, len(survey_results)):
    if survey_results[x] == "Yes":
        yes_response += 1
    elif survey_results[x] == "No":
        no_response += 1
    elif survey_results[x] == "Maybe":
        maybe_response += 1

print(f"Age Distribution: Under 18 ({underage}), 18 to 35 ({young_adult}), 36 to 65 ({adult}), Above 65 ({senior})")
print(f"Number Analysis: Even ({even_numbers}), Odd ({odd_numbers})")
print(f"Survey Results: Yes ({yes_response}), No ({no_response}), Maybe ({maybe_response})")
