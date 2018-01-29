

# get weight from user
weight = int(input("Enter your weight: " ))

#get height from user
height = int(input("Enter your height in inches: " ))

#get age from user
age = int(input("Enter your age: "))

#get bodyfat percentage from user (asking for decimal form so 15% would be .15)
bfp = float(input("Enter your body fat percentage in decimal form (example: 15% would be .15): " ))
activity = input("Please enter activity level based on the following \n 1.2 = low/sedintary \n 1.375 = light activity (exercise 1-3 days a week) \n 1.55 = Moderate(3-5 days a week) \n 1.725 = Very Active(hard exercise 6-7 days a week) \n 1.9 = exta active(very hard exercise 6-7 days and physical job) \n Enter activity level: " )
aggressivity = float(input("Enter desired calorie deficit percentage as decimal (between .10 and .25 is advised) "))

#gender = input('Enter male or female: ')

fat = (float(weight) * bfp)

lbm = (weight - int(fat))

bmr = (370 + (21.6 * (lbm / 2.2)))

tdee = (float(bmr) * float(activity))
deficit = (tdee - (tdee * aggressivity))

protein_cal = round(deficit * 0.40)
carbs_cal = round(deficit * 0.40)
fat_cal = round(deficit * 0.20)

pro_gram = round(protein_cal / 4)
carb_gram = round(carbs_cal / 4)
fat_gram = round(fat_cal / 9)



#bmr = round(bmr)
#lean body mass print
print("\nYour Lean Body Mass is: ", round(lbm))
#body fat percentage print
print("\nYour total body fat in pounds is: ", round(fat))
#Basal Metabolic Rate print
print("\nYour BMR is: ", round(bmr))
#Total Daily Engergy Expenditure print
print("\nYour TDEE is: ", round(tdee))

print("\nAt your activity level, if you eat more than ", round(tdee), ", you'll gain weight. ")

print("If you eat less than ", round(tdee), ", you'll lose weight. ")

print("\nAt a calorie deficit of ", aggressivity, " you need to consume ", round(deficit), "calories \n")

print('What you really want to do is gain muscle and lose fat.')
print('In order to do that, you must properly measure and consume your macronutrients')

print('I recommend a breakdown of \n40 percent Protein \n40 percent Carbs \n20 percent fat.')
print('\n1 gram of protein = 4 calories')
print('1 gram of Carbs = 4 calories')
print('1 gram of fat = 9 calories')
print("\nYour calorie breakdown by macronutrient is as follows: \n")
print("PROTEIN \n", protein_cal, " Calories\n", pro_gram, "Grams \n")
print("CARBS \n", carbs_cal, " Calories\n", carb_gram, "Grams \n")
print("FAT \n", fat_cal, " Calories\n", fat_gram, "Grams \n")
