#  Input needs from the user
# total rent
# total food ordered for anscking
# electricity bill unit spend
# charge per unit


# output
# total amount you've to pay is

# ------------- i want to calculate rent permonth-----------
total_person = int(input("please Enter the number of total person : "))
room_rent=int(input("please enter the room rent : "))
food_amount = int(input("Please Enter the total food amount :"))
electrict_unit=int(input("please enter bijli unit :"))
per_unit_charge= int(input("Please enter the bijli charge perunit:"))

total_bijli_bil = electrict_unit * per_unit_charge
total_rent_per_month = (room_rent+food_amount+total_bijli_bil)/total_person

print("------------------------------------")
print("per hed rent amount in month : ",  total_rent_per_month)