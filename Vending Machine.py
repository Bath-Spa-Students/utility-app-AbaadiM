#creating a vending machine

print("Hello")
print("______________________________")
print("WELCOME TO VENDING MACHINE")
print("......................................................................................")
print("[Languages= English / Arabic]")
print("______________________________")

#Select a language
Language = {
    '1' : 'English' , 
    '2' : 'Arabic'
}
Language_code=input('please select the Language:')
if Language_code== 'English' :
    print("You have selected English")
elif Language_code=='Arabic' :
 print("You have selected Arabic")


#Codes of the Items in the shop
items={
   '1111' : 'water' , 
   '2222' : 'C4' , 
   '3333' : 'PREWORKOUT' , 
   '4444' : 'PROTIEN BAR' , 
   '5555' : 'ORGANIC CHIPS' , 
   '6666' : 'BANANA' , 
   '7777' : '0 CARB SANDWICH' , 
   '8888' : 'MOUNTAIN DEW' , 
   '9999' : '100G BOILED CHKN' ,
   '1122' : 'GATORADE' , 
   '1133' : 'REDBULL' , 
   '1144' : 'TOWEL' , 
   '1155' : 'HEADSET' ,
   '1166' : 'PROTIEN SHAKE' ,
   '1177' : 'STERIODS' , 


}

print("MENU OF GYMSHACK")
print("...........................................................................")
print("1. water                   AED 5 ,      Code: 1111 ,         Stock:200")
print("2. C4                        AED 20 ,      Code: 2222 ,         Stock:300")
print("3. PREWORKOUT                    AED 20 ,      Code: 3333 ,         Stock:50 ")
print("4. PROTIEN BAR                        AED 15 ,      Code: 4444 ,         Stock:150")
print("5. ORGANIC CHIPS                    AED 10 ,      Code: 5555 ,         Stock:300")
print("6. BANANA                      AED 5 ,      Code: 6666 ,         Stock:80")
print("7. 0 CARB SANDWICH                     AED 15 ,      Code: 7777 ,         Stock:120")
print("8. Mountain Dew                AED 4 ,      Code: 8888 ,         Stock:110")
print("9. 100G BOILED CHKN                       AED 25 ,      Code: 9999 ,         Stock:220")
print("10. Gatorade                   AED 20 ,      Code: 1122 ,         Stock:60")
print("11. Redbull                    AED 20 ,      Code: 1133 ,         Stock:80")
print("12. TOWEL                      AED 10 ,      Code: 1144 ,         Stock:140")
print("13. HEADSET                   AED 20 ,      Code: 1155 ,         Stock:85")
print("14. PROTIEN SHAKE                      AED 25 ,      Code: 1166 ,         Stock:45")
print("15. STERIODS                     AED 200 ,      Code: 1177 ,         Stock:195")   
print("............................................................................")

#Price of items in the shop
WATER=5
C4=20
PREWORKOUT=20
PROTIENBAR=15
ORGANICCHIPS=10
BANANA=5
CARBSSANDWICH=15
MountainDew=4
BOILEDCHKN=25
GATORADE=20
REDBULL=20
TOWEL=10
HEADSET=20
PROTIENSHAKE=25
STERIODS=200

# check stock
stock=3000
if stock > 0:
    print("________________________")
    print("We have snacks and beverages in stock. Please make your selection.")
    print("_______________________")


#This is for Entering The Product Code      
items_code=input('Please enter the Product Code you would like to buy:')

# Enter the Amount of Money
money=int(input("Thankyou for your selection .Please insert the money"))



#Choice for Additional Item
choice = {
   '1': 'yes' ,
   '2': 'no'
}
choice=input('Snackers and Drinkers would like to suggest you to have some chocolate? (yes/no):')
if choice== 'yes':
   print("...............................")
   print("Thankyou for your Selection")
elif choice== 'no':
   print("Thankyou for your Selection")

   #Calculating and Returning the Correct Change Of WATER
   if items_code=='1111':
      if money >= WATER:
         money=money-WATER

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of C4
   if items_code=='2222':
      if money >= C4:
         money=money-C4

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of PREWORKOUT
   if items_code=='3333':
      if money >= PREWORKOUT:
         money=money-PREWORKOUT

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of PROTIENBAR
   if items_code=='4444':
      if money >= PROTIENBAR:
         money=money-PROTIENBAR

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of ORGANICCHIPS
   if items_code=='5555':
      if money >= ORGANICCHIPS:
         money=money-ORGANICCHIPS

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of BANANA
   if items_code=='6666':
      if money >= BANANA:
         money=money-BANANA

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of 0CARBSSANDWICH
   if items_code=='7777':
      if money >= CARBSSANDWICH:
         money=money-CARBSSANDWICH

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Mountain Dew
   if items_code=='8888':
      if money >= MountainDew:
         money=money-MountainDew

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of BOILEDCHKN
   if items_code=='9999':
      if money >= BOILEDCHKN:
         money=money-BOILEDCHKN

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Gatorade
   if items_code=='1122':
      if money >= GATORADE:
         money=money-GATORADE

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of Redbull
   if items_code=='1133':
      if money >= REDBULL:
         money=money-REDBULL

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of TOWEL
   if items_code=='1144':
      if money >= TOWEL:
         money=money-TOWEL

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of HEADSET
   if items_code=='1155':
      if money >= HEADSET:
         money=money-HEADSET

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")



         #Calculating and Returning the Correct Change Of PROTIENSHAKE
   if items_code=='1166':
      if money >= PROTIENSHAKE:
         money=money-PROTIENSHAKE

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")

         



         #Calculating and Returning the Correct Change Of STERIODS
   if items_code=='1177':
      if money >= STERIODS:
         money=money-STERIODS

         print("......................")
         print("Your change is",money)
         print("......................")
         print("Your order has been Dispensed")
         print("......................")
         print("Take your Receipt")
         print("......................")
         print("Have a Nice Day")
         print("......................")
         print("PLEASE VISIT AGAIN")
      else:
         print("Try Again.Insufficient balance.Money Refunded")
