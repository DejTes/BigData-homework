'''
1) Create a Python program to output the following basic JSON notation.
Output:
{
"donut_name":"Vanilla Donut",
"quantity_purchased":"10",
"price":2.5
} 
'''
# Solution
json_data = '''{
    "donut_name":"Vanilla Donut",
    "quantity_purchased":"10",
    "price":2.5
}'''
print(json_data)




'''
2)Create a Python program to prompt customers for their name and age. The format for the name and age labels should be in bold. And, the name literal should be underlined.
'''
# Answere
from termcolor import colored
def main():
    name = input("Enter your name: ")
    age = input("enter your age:")
    print(colored(name, attrs=['bold', 'underline']))

    print(colored(age, attrs=['bold']))

if __name__ == "__main__":
    main()



'''
3)Create a Python program to find the 8th character in the String: "http://allaboutscala".
'''
# Solution

str = "http://allaboutscala"
print(str[7])




'''4)Create a Python program to calculate the total cost for a customer who is buying 10 Glazed donuts. You can assume that the price of each Glazed donut item is at $2.50. Notice the format of the $25.00 total cost literal, which is essentially at 2 decimal places
'''
# Solution
quantity = 10
price = 2.5 
total_cost = quantity * price
print(f"${total_cost:.2f}")



'''5)Create a Python program that will ask the following question to a customer: "What is your favorite movie of all times?".
'''
# Solution
movie = input("What is your favorite movie of all times?")
print(movie)


'''6)Create a Python program to output your name and favorite movie.
Output:
First Name: Nadim
Last Name: Bahadoor
Favorite Movie: The Matrix'''


# Solution
FirstName = "Dejen"
LastName = "Tesfa"
FavoriteMovie = "Shooter"
print(f"First Name: {FirstName}")
print(f"Last Name: {LastName}")
print(f"Favorite Movie: {FavoriteMovie}")



'''7) Create a Python program to parse the corresponding values from the given String "Vanilla Donut 10 2.25", where the literal Vanilla Donut is a particular donut, the 10 literal is the quantity purchased, and 2.25 is the unit price of each Vanilla Donut. You further need to cast each token from the input String to their corresponding types, such as, an Int, Double or String.
'''

'''8)Create a Python program and use an appropriate data structure to present the following key and value pairs of children and their ages: Bill is 9 years old, Jonny is 8 years old, Tommy is 11 years old, and Cindy is 13 years old. Sort out the corresponding child to age in reverse alphabet order.
'''

'''9) Let us assume that you two shopping baskets with a bunch of items in each one. The first contains elements: "Cake", "Milk", "Cheese", "Toilet Paper", and the second one has the following items: "Bread", "Water", "Juice", "Milk", "Cheese". Write a Python program to find the common items between the two shopping baskets. You can use whichever data structure that you feel is appropriate for this particular problem.
'''

'''10)Create a Python program that defines a sequence of numbers from 100 to 110. The sequence should include the 100 starting number literal, and ends with the 110 number literal.'''