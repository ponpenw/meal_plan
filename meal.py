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

def display_recipe(menu, r):

    display_infos(menu, r)

def display_ingr(ingr, i):

    display_infos(ingr, i)

def main():
    file = "ingre.csv"
    r, i = get_infos(file)
    print("Hello, How are you doing? ")
    user_reply = input("Would you like some help for dinner tonight? ")
    if user_reply != "yes":
        quit()
    print("Great!! Let's get started ")
    user_reply = input("Would you like to go with recipe or ingredient? ")
    if user_reply == "recipe":
        #call function
        menu = input("What would you like \n "
                     "fried rice \n noodle soup \n panang curry \n "
                      "tom yum soup \n basil stirfried \n  ")
        display_recipe(menu, r)
    elif user_reply == "ingredient":
        #call another function
         ingr = input("What ingredient do you have? \n "
                        "eeg \n chicken \n coocked_rice \n noodle \n spinach \n mushroom \n ")
         display_ingr(ingr, i)
    else:
        quit()

#    for recipe in r:
#        display_infos(recipe, r)
        #print(recipe, end=": ")
        #for ingredients in r[recipe]:
             #print(ingredients, end=", ")
        #print(", ".join(r[recipe])) # join list ", ".join()
    #print()

#    for ingredients in i:
#        display_infos(ans_protein, i)
        #display_infos(ingredients, i)
        #print(ingredients, end=": ")
        #print(", ".join(i[ingredients]))
    #print()

#    display_infos("noodle_soup", r)
#    display_infos("panang_curry", r)
#    display_infos("cooked noodle", i)
#    display_infos("egg", i)


main()













