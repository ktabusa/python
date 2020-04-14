# Started 04/13/20

import random

value = random.random()
print(value)
# this runs from 0 (inclusive) to 1 (non-inclusvie)

valu = random.uniform(1, 10)
print(valu)
# this provides a random float between 1 and 10

print('Test 6-sided')
rint = random.randint(1, 6)
print(rint)
# this is inclusive....

print(' ')
# choice method, ie pick a random greeting
# if multiple iterations, choices can pick the same value twice
greetings = ['Hi', 'Hello', 'Howdy', 'Bonjour']
testval = random.choice(greetings)
print(testval + ', Keenan!')


colors = ['Red', 'Black', 'Green']

results = random.choices(colors, k=10)
# what is k=10? this representations of the iterations for the method
print(results)

results = random.choices(colors, weights=[18, 18, 2], k=15)
# this weights red as 18, black as 18, green as 2, like a roulette wheel
print(results)


print('Deck of Cards')
deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)

# can't use choices method here bc it can pick the same number twice
hand = random.sample(deck, k=5)
print(hand)
# sample will pick unique numbers only


first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael',
               'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson',
              'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park',
                'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield',
               'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
          'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@bogusemail.com'
    print(f'{first} {last}\n{phone}\n{address}')
