#print("Hello World")

#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])

#temperature = int(input("What is the temperature outside?"))

#if temperature > 80:
#    print("Turn on the AC.")
#else: 
#    print("Open the windows.")

#counties =["Arapahoe","Denver","Jefferson"]
#if counties[1] =='Denver':
#    print(counties[1])

#score = int(input("What is your test score?"))
#if score>=90:
#    print("A")
#else:
#    if score>=80:
#        print("B")
#    else:
#        if score>=70:
#            print("C")
#        else:
#            if score >=60:
#                print("D")
#            else:
#                print("F")


#score = int(input("What is your score?"))

#if score>=90:
#    print("Your grade is A")
#elif score>=80:
#    print("Your grade is B")
#elif score>=70:
#    print("Your grade is C")
#elif score>=60:
#    print("Your grade is D")
#else:
#    print("Your grade is F")

#counties=["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not in the list of counties.")
#if "Arapahoe" in counties and "El Paso" in counties:
#    print("arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")


#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and Elpaso are not in the list of counties.")

#x = 0
#while x<=5:
#    print(x)
#    x=x+1

#for county in counties:
#    print(county)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
#for county in counties_dict.keys():
#for county in counties_dict.values():
#for county in counties_dict.keys():
#    print(county)

#gets the "key" in the dictionary
#for county in counties_dict:
#    print(counties_dict[county])

#also gets the key in the dictionary
#for county in counties_dict:
#    print(counties_dict.get(county))

#for key, value in counties_dict.items():
#    print(key, value)

#for county, voters in counties_dict.items():
#    print(county, voters)

#for county, voters in counties_dict.items():
#    print(f'{county} county has {voters} registered voters.')

#voting_data=[{"county":"Arapahoe", "registered_voters":422829},
#            {"county":"Denver","registered_voters":463353},
#            {"county":"Jefferson","registered_voters":432438}]
#for county_dict in voting_data:
#    #print(county_dict)
#    for key, value in county_dict.items():
#        print(key, value)


Name = "Harper"
Country = "Italy"
Age = 18
Hourly_Wage = 30
#Satisfied = True
#Daily_Wage = Hourly_Wage * 8
#print(Name+" "+Country+" "+str(Age)+" "+str(Hourly_Wage))
#print(f'{Daily_Wage} {Satisfied}')


#grocery_list = ["milk", "bread", "eggs", "peanut_butter", "jelly"]
#print(grocery_list)

#grocery_list.insert(3, "almond_butter")
#grocery_list.remove("peanut_butter")

#grocery_list.pop()
#grocery_list.append("coffee")
#grocery_list[3]="almond_butter"
#print(grocery_list)

pet = {"Cat":"Dottie","age":"seven","hobby":["nap","bird watching"], "wakeup":{"Mon":8, "Wed":7,"Fri":6}}
#print(len(pet["hobby"]))
#print(pet["Cat"],pet["age"])
#print(pet["hobby"][0])
#print(pet["wakeup")
#pet["wakeup"]["value"][0])

#for county in counties_dict:
#    print(counties_dict[county])
#print (pet['wakeup'])
for key, value in pet['wakeup'].items():
    if key == "Fri":
        print(value)
print(pet['wakeup']['Fri'])