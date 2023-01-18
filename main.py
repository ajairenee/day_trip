import random

selected_day_trip = { 'city': 'greece', 'restaurant': 'cafe', 'transport': 'horseback', 'entertaiment': 'dancing'}

cities = ['paris','nice','greece']
fav_city = random.choice (cities)
yes_no = input (f'Do you want to stay here? {fav_city}')

while yes_no != 'yes':
    fav_city = random.choice (cities)
    yes_no = input (f'Do you want to stay here? {fav_city}')

selected_day_trip['city'] = fav_city

trip_food = ['cafe','vatican','beach']
good_restaurants = random.choice (trip_food)
yes_no = input (f'Would you like to dine here? {good_restaurants}')
while yes_no != 'yes':
    good_restaurants = random.choice (trip_food)
    yes_no = input (f'Would you like to dine here? {good_restaurants}')

selected_day_trip['restaurant'] = good_restaurants

transport_trip = ['bus','car','horseback']
get_around =random.choice(transport_trip)
yes_no = input (f'How will you get there? {get_around}')
while yes_no != 'yes':
    get_around = random.choice (transport_trip)
    yes_no = input (f'How will you get there? {get_around}')

selected_day_trip['transport'] = get_around

trip_entertainment = ['opera','museums','dancing']
fun_things = random.choice (trip_entertainment)
yes_no = input (f'What will you do? {fun_things}')
while yes_no != 'yes':
    fun_things = random.choice (trip_entertainment)
    yes_no = input (f'What should you do? {fun_things}')

selected_day_trip['entertaiment'] = fun_things

print('Enjoy your trip!')

    