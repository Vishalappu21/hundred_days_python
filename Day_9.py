x = {"Name":"Vishal",
     "age":25,
     "Place":"Sangiruppu"}
print(type(x))
print(x["age"])
# Edit the dictionary..
x["age"]=50
print(x)
for i in x:
    print(i)
    print(x[i])

# Grading_Exercise..
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for student, score in student_scores.items():
    if score >= 91 and score <= 100:
        grade = "Outstanding"
    elif score >= 81 and score <= 90:
        grade = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[student] = grade
print(student_grades)

# Nested_Dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]['year'])

# List in a dict
country = "Afghanistan, Albania, Algeria, Andorra, Angola, Antigua and Barbuda, Argentina, Armenia, Australia, Austria, Azerbaijan, Bahamas, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Bhutan, Bolivia, Bosnia and Herzegovina, Botswana, Brazil, Brunei, Bulgaria, Cambodia, Canada, Central African Republic, Chile, China, Colombia, Costa Rica, Croatia, Cuba, Cyprus, Czechia, Denmark, Dominica, Dominican Republic, Ecuador, Egypt, El Salvador, Estonia, Finland, France, Georgia, Germany, Greece, Grenada, Guatemala,Guyana"
world_country = [i.strip() for i in country.split(",")]
print(world_country)

name_country= {
    'world':['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bhutan', 'Bolivia']
}
print(name_country["world"][0])

starting_dictionary = {
    "a": 9,
    "b": 8,
}
final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order['main'][2][0])
# Bid_auction Program
import os
print("Welcome to Secret Auction Program..")
bid_dict = {}
while True:
    user = input("Tell me Your Name: \n")
    price = int(input("how much is your Bid Price: \n"))
    bid_dict[user] = price
    any_other = input("are there any other bidders? type 'yes' or 'no': \n").lower()
    if any_other == 'no':
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
highest_bidder = max(bid_dict,key=bid_dict.get)
highest_bid = bid_dict[highest_bidder]
print(f"The winner is {highest_bidder} and the amount is {highest_bid} ")


