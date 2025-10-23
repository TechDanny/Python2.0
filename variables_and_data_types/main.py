# Profile card

name = input("Please enter your full names: ")
age = int(input("What is your age? "))
country = input("Please enter your nationality: ")
fav_color = input("What is your favorite color? ")
hobby = input("What is your hobby? ")
dream_job = input("What is your dream job? ")

# year of birth
current_year = 2025
year_of_birth = current_year - age

# Age in 10yrs
age_in_10yrs = age + 10

print("")
print("--------------------PROFILE CARD------------------")
print(f"Name: {name}\t\t\tAge: {age}")
print(f"Country: {country}\t\t\tFavorite color: {fav_color}")
print(f"Hobby: {hobby}\t\t\tDream job: {dream_job}")
print("")
print("--------------------CALCULATIONS--------------------")
print(f"Year of birth: {year_of_birth}")
print("")
print(f"Age in 10yrs: {age_in_10yrs}")
print("")