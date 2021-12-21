# Python Project: meal helper game
#by Ponpen Wongkaseam
# This game is using if else statement
import csv
def display_infos(recipe, r):
    print(recipe, end=": ")
    print(", ".join(r[recipe]))

def get_infos(file):
    r = {}
    i = {}

    # open csv file to "r"ead or "w"rite
    with open(file, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting through first row
        ingredients = next(csvreader)[1:]

        #extracting each data row one by one
        for row in csvreader:
            #print(row)
            quant = row[1:]
            #print("value of quant is",quant)
            recipe = row[0]
            #print(recipe)#getting element 0 from row
            r[recipe] = []
            for q in range(len(quant)):
                #getting q from quant
                #print("inside loop",q)
                if quant[q] == "x":
                    r[recipe].append(ingredients[q])
                    #print(r[recipe])
                    if ingredients[q] not in i:
                        i[ingredients[q]] = []
                    i[ingredients[q]].append(recipe)
                    #print(i[ingredients[q]])
    return r,i

def main():
    file = "ingre.csv"
    r,i = get_infos(file)
    for recipe in r:
        display_infos(recipe, r)
        #print(recipe, end=": ")
        # for ingredients in r[recipe]:
        #     print(ingredients, end=", ")
        #print(", ".join(r[recipe])) # join list ", ".join()
    print()

    for ingredients in i:
        display_infos(ingredients, i)
        #print(ingredients, end=": ")
        #print(", ".join(i[ingredients]))
    print()

    display_infos("noodle_soup", r)
    display_infos("panang_curry", r)
    display_infos("cooked noodle", i)


main()

exit()


print("Hello, How are you doing? ")
user_reply = input("Would you like some help for dinner tonight? ")
if user_reply != "yes":
    quit()
print("Wonderful!! Let's get started ")

answer1 = input("Do you have eggs or chicken? ")
if answer1 == "eggs":
    print("ingredient is ", answer1)
elif answer1 == "chicken":
    print("Chicken! It' is")
else:
    print("Sorry! I can only help with either eggs or chicken at the moment")

print("Great!! It is going to be an easy meal today")
answer1 = input("Do you have rice or noodle? ")
if answer1 == "rice":
     print("Rice is perfect!!")
     print("Let's make fried rice")
     #recipe = "fried_rice"
     display_infos("fried_rice", r)
     # print(recipe, end=": ")
     # print(", ".join(r[recipe]))#how can I specify to print out just one recipe with ingredients
elif answer1 == "noodle":
     print("Noodle is fun")
     print("Noodle soup sounds good to me!") #code to get recipe for noodle soup
else:
     print("Sorry! I can only help with rice or noodle")



