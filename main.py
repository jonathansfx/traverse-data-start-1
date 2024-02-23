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
    elif age_data[x] > 18 and age_data[x] < 36:
        young_adult += 1
    elif age_data[x] > 35 and age_data[x] < 66:
        adult += 1

print(underage"," young_adult)

# number data
with open ('number-data.txt', 'r') as number_data_file:
    number_data = number_data_file.read().split('\n')

