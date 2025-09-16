def greet():
    print("The Hello..")
    print("Hello World of Python..")
    print("The Hindu")
greet()

# Function with Inputs..
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"where are you working {name}?")
greet_with_name('vishal')

# exercise..
def life_in_weeks(age):
    years = 90-age
    forumla = years * 52
    print(years)
life_in_weeks(25)

def greet_with(name,age):
    print(f"what is your {name}")
    print(f"what's your {age}")
greet_with("Vishal",25)

def vishal(name,location):
    print(f"my name is {name} and i'm coming from {location}")
vishal(name="vishal",location="sangiruppu")

def calculate_love_score(name_1,name_2):
    combine_name = name_1+name_2
    lower_case_name = combine_name.lower()
    t = lower_case_name.count('t')
    r = lower_case_name.count('r')
    u = lower_case_name.count('u')
    e = lower_case_name.count('e')
    first_digit = t+r+u+e
    l = lower_case_name.count('l')
    o = lower_case_name.count('o')
    v = lower_case_name.count('v')
    e = lower_case_name.count('e')
    second_digit = l+o+v+e
    score = int(str(first_digit)+str(second_digit))
    print(score)
calculate_love_score("Vishal Prasanna","shruthi")

# Encode and Decode Project..
alphabets = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
alphabets_1 = [i.strip() for i in alphabets.split(",")]
print(alphabets_1)

print("Welcome to Encode and Decode Project..")
direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("type your message:\n").upper()
shift = int(input("Type your shift number:\n"))
def ceaser(original_text,shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1
    for i in original_text:
        if i not  in alphabets_1:
            output_text += i
        else:

            shift_position = alphabets_1.index(i) + shift_amount
            shift_position %= len(alphabets_1)
            output_text += alphabets_1[shift_position]
    print(f"{encode_or_decode}: {output_text}")
ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)
start_again = True
while start_again:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("type your message:\n").upper()
    shift = int(input("Type your shift number:\n"))

    once_again = input("type 'yes' for do again,type 'no' to stop\n").lower()
    if once_again == 'no':
        start_again = False
        print("Thank You Good Bye...")
ceaser(original_text=text,shift_amount=shift,encode_or_decode=direction)
