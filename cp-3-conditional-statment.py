#conditional statement : When you want to do something based on event happen
# if,elif,else are main statement

# program defination : if warn have 10 rupees then buy butter

name = "warn"

rupees = 20

if rupees > 10 :
    rupees=rupees-10
    print("Warn have enough money to buy butter")


# check if warn have 20 rupees to buy bread consider this warn already purchase butter 
# if don't have 20 rupees then get double roti 


if rupees > 10 :
     print("Warn have enough money to buy bread")
elif rupees > 5 :
    print("Warn can buy double roti")
else:
     print("I don't have money to buy")

#check contain in string
sourceString = "This is vasim"
foundString = "This"

if foundString in sourceString:
    print("Found")
else:
    print("No Found")
    

    





