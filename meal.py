# Python Project: meal helper game
#by Ponpen WOngkaseam
# This game is using if else statement

print("Hello, How are you doing? I hope you have a fabulous day.  ")
user_reply = input("Would you like some help for dinner tonight? ")
if user_reply != "yes":
    quit()
print("Wonderful!! Let's get started ")

ingredient = input("Do you have eggs or chicken? ")
if ingredient == "eggs":
    print("ingredient is ", ingredient)
elif ingredient == "chicken":
    print("Chicken! It' is")
else:
    print("Sorry! I can only help with either eggs or chicken at the moment")
# if I want to use the code below how should I do? Think!!
# user_reply = input("Do you want to change your mind? ")
# if user_reply != "yes":
#         quit()
print("Great!! It is going to be an easy meal today")
ingredient = input("Do you have rice or noodle? ")
if ingredient == "rice":
    print("Rice is perfect!!")
    print("Let's make fried rice")
elif ingredient == "noodle":
    print("Noodle is fun")
    print("Noodle soup sounds good to me!")
else:
    print("Sorry! I can only help with rice or noodle")



