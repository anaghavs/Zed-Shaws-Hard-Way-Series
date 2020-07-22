def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!") 
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!") 
    print("Get a blanket.\n")
    
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10 
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def mydreams(musafir, khana):
    print(f"One of My dream places to visit are {musafir}")
    print(f"i love this place and befoe my death i just hope i get to visit this place atleast once in my life")
    print(f"I love eating {khana}")

print("""
I have so many dreams,and i live only for  my dreams and for my 
 brother who is my soul.I have so many things on my bucket list
 """ )

mydreams("Maldives", "Paneer")
mydreams("Darjeling", "Soup")
mydreams("Tigersnest_Tibet", "Pizza")
mydreams("HImalayas","Noodles")
mydreams("Japan", "Chikengheeroast")
mydreams("dubai", "evrything")