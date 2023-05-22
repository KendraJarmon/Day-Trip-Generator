import random
import select

In_Town_Destinations = ['Houston Galleria','Houston Discovery Green','Houston Herman Park','Houston NRG Park']

In_Town_Restaurant = ['Turkey Leg Hut','Upper Kirby Bistro','Taste Bar + Kitchen','Twisted Grilled Cheese','Kulture','Phil & Dereks','Lucilles','ChopnBlok','Foodie Bar','Stuffd Wings']

Transportation_Options = ['Uber/Lift','Houston BCycle','Taxi','Metro Bus/Rail','Tunnels & SkyWalks','Own Vehicle']

Entertainment_options = ['Escape Room','Segway Tours','Canoe Tours','Color Factory','Downtown Aquarium','Houston Livestock Show and Rodeo','Houston Pedal Barge','Rental Scooters Downtown','Rooftop Cinama','Beyonce Concert']

yes_options = ['YES', 'Yes', 'yes', 'y']
no_option = ['NO', 'No', 'no', 'n']


def pick_random_item(list_of_items):
     selected_item = random.choice(list_of_items)
     return selected_item

def display_trip(dest, transp, rest, enter):
     print(f'DESTINATION:{dest}\nTRANSPORTATION:{transp}\nRESTAURANT:{rest}\nENTERTAINMENT:{enter}')
 
def day_trip_generator():
    day_trip_is_running = True
    while day_trip_is_running ==True:
        destination =pick_random_item(In_Town_Destinations)
        transportation = pick_random_item(Transportation_Options)
        restaurant = pick_random_item(In_Town_Restaurant)
        entertainment = pick_random_item(Entertainment_options)
        display_trip(destination, transportation, restaurant, entertainment)
        user_input = input('Would you like to confirm this trip?')
        if user_input in yes_options:
             print('Here is your trip!')
             display_trip(destination, transportation, restaurant, entertainment)
             day_trip_is_running = False
        elif user_input in no_option:
             print('We will regenerate a response')



day_trip_generator()








# My_Destination = pick_random_item(In_Town_Destinations)
# print('Your Destination is: ', My_Destination)

# def Display_options(In_Town_destinations):
#     print('option 0 - Exit')
#     option_number = 1
#     for item in (In_Town_Destinations):
#         print('Option',option_number,' ',item )
#         option_number += 1

# def prompt_input_numeric(prompt_string):
#     user_input_string = input(prompt_string)
#     num_choice = int(user_input_string)
#     return num_choice

# def validate_choice(In_Town_Destinations):
#     valid_choice = False
#     while (valid_choice == False):
#         Display_options(In_Town_Destinations)
#         user_item = prompt_input_numeric('Choose a Destination from this list above: ')
#         if user_item == 0:
#             valid_choice = True
#             choice = 'Nothing Selected'
#         elif (user_item >= 1 and user_item <= len(In_Town_Destinations)):
#             choice = In_Town_Destinations[user_item-1]
#             valid_choice = True
#         else:
#             print('\nThat is not valid choice. Please try again.')
#     print('Good choice!\n')
#     return choice


# My_Restaurant = pick_random_item(In_Town_Restaurant)
# print('Your Restuarant is: ', My_Restaurant)

# def Display_options(In_Town_Restaurant):
#     print('option 0 - Exit')
#     option_number = 2
#     for item in (In_Town_Restaurant):
#         print('Option',option_number,' ',item )
#         option_number += 2

# def validate_choice(In_Town_Restaurant):
#     valid_choice = False
#     while (valid_choice == False):
#         Display_options(In_Town_Restaurant)
#         user_item = prompt_input_numeric('Choose a Restaurant from this list above: ')
#         if user_item == 0:
#             valid_choice = True
#             choice = 'Nothing Selected'
#         elif (user_item >= 2 and user_item <= len(In_Town_Restaurant)):
#             choice = In_Town_Restaurant[user_item-2]
#             valid_choice = True
#         else:
#             print('\nThat is not valid choice. Please try again.')
#     print('Good choice!\n')
#     return choice         


# My_Transportation = pick_random_item(Transportation_Options)
# print('Your transportation is: ', My_Transportation)

# def Display_options(Transportation_Options):
#     print('option 0 - Exit')
#     option_number = 3
#     for item in (Transportation_Options):
#         print('Option',option_number,' ',item )
#         option_number += 3


# def validate_choice(Transportation_Options):
#     valid_choice = False
#     while (valid_choice == False):
#         Display_options(Transportation_Options)
#         user_item = prompt_input_numeric('Choose an option from the list above: ')
#         if user_item == 0:
#             valid_choice = True
#             choice = 'Nothing Selected'
#         elif (user_item >= 3 and user_item <= len(Transportation_Options)):
#             choice = Transportation_Options[user_item-3]
#             valid_choice = True
#         else:
#             print('\nThat is not valid choice. Please try again.')
#     print('Good choice!\n')
#     return choice  


# Entertainment_options = pick_random_item(Entertainment_options)
# print('Your Entertainment is: ', Entertainment_options)

# def Display_options(Entertainment_options):
#     print('option 0 - Exit')
#     option_number = 4
#     for item in (Entertainment_options):
#         print('Option',option_number,' ',item )
#         option_number += 4


# def validate_choice(Entertainment_options):
#     valid_choice = False
#     while (valid_choice == False):
#         Display_options(Entertainment_options)
#         user_item = prompt_input_numeric('Choose an option from the list above: ')
#         if user_item == 0:
#             valid_choice = True
#             choice = 'Nothing Selected'
#         elif (user_item >= 4 and user_item <= len(Entertainment_options)):
#             choice = Entertainment_options[user_item-4]
#             valid_choice = True
#         else:
#             print('\nThat is not valid choice. Please try again.')
#     print('Good choice!\n')
#     return choice  

# Yes_choice = ['yes']
# No_choice = ['No']

# while True:
#     user_input = input('are you satisfied with your trip? (Yes/No): ')


#     if user_input.lower() in Yes_choice:
#       print('user typed Yes')
#       break
#     elif user_input.lower() in No_choice:
#       print('user typed No')
#       break
#     else:
#       print('Yes')



