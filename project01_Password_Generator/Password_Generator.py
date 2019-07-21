import random                                           #importing random and string modules 
import string 

pass_len = input("enter the lenght of the password=",)  #getting the password len from the user & make it as int 
pass_len = int(pass_len)


count = 0
passw1 = []

while True : 
    count = count +1                                    #increse the count value by 2
    if count > pass_len :                               #if the count value is greater than $pass_len , break the while 
        break
    small_alfa = random.choice(string.ascii_lowercase)  #generates random lowercase letter 
    caps_alfa = random.choice(string.ascii_uppercase)   #generates random uppercase letter
    numeric = random.choice(string.digits)              #generates numeric 
    spl_char = random.choice(string.punctuation)        #generates spl_character
    #print("infinte")
    var = (small_alfa,caps_alfa,numeric,spl_char)       #generating radom charcter from the $small_alfa ,$caps_alfa, $numeric, $spl_char
    var01 =  random.choice(var)
    
    passw1.append(var01)                                #appending them in the list which declared before $passw1
psswd = ''.join(passw1)                                    
print(psswd)
