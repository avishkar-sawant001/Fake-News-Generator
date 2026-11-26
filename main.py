#import random module

import random

#creat lists:
#subject

subjects = ["Nana Pateker",
           "Rotit Sharma",
           "Narendra Modi",
           "Akshay kumar",
           "Dogesh Bhai",
           "Babu Rao",
           "Darmendra bahubali",
           "Jonhy liver",
           "Dilwala Raj"]
#Action
actions = ["with Dance",
           "fighting with karan",
           "eating vadapav",
           "running on street",
           "orderd parsaled samosa",
           "painting burj khalipha",
           "avoiding media",
           "creating body",
           "singing songs",
          "traveling",
          "eating mangoes"]
#Places or things
place_things = ["at mumbai beech",
           "on terace",
           "at balcony",
           "inside Home",
           "at garden",
           "or stand on car",
           "on marindrive",
           "in pune",
           "in Kokan"]

#while loop
while True :
    
    #randomly select each subject,action,place
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_thing = random.choice(place_things)

    #combin throw string formating
    headline = f"BREAKING NEWS :{subject} {action} {place_thing}"

    #print headline
    print("\n" + headline)

    #ask to generate another
    user_input = input("Do you want to generate another Headline(yes/no) :").strip().lower()

    if user_input == "no" :
        break
    elif user_input == "yes" :
        continue
    else:
        print("\nYou Entered Invalid Input \nEnter Only Yes/No !!!...")
    
#print Good Bye!
print("Thank you for using Fake news generator, have a fun day !!!...")
