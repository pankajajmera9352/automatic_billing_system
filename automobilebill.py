


print('''****AUTOMOBILES BILLING SOFTWARE SYSTEM MADE BY PANKAJ AJMERA*****
      
       --- ANIT AUTO SERVICE CENTER---
        MR: KULDEEP AJMREA
        MOBILE NO: 9928842159,9024451240
        ''')
from datetime import datetime
current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d")
print("Current Date:", formatted_date)

import random
random_number = random.randint(1, 100)
print('bill no: =',random_number)

a=(input("ENTER CUSTOMER NAME: =  "))
b=(input("ENTER VEHICLE NAME: =  "))
def sum_of_n_numbers():
    n = int(input("insert the ITEMS : =  "))
    total = 0
    for i in range(n):
        a= (input(f"ITEM  NAME {i+1}: =  "))
        
        num = float(input(f"ITEM VALUE {i+1}: "))
        total += num
    print(f"TOTAL  OF THE  {n} ITEMS is: = {total}")

sum_of_n_numbers()
