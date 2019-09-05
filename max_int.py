#Write an algorithm
#Notandi slær inn tölu
#Forritið keyrir þangað til slegin er negative tala
#Nota max til að finna hæstu integer töluna
#Þegar neikvæð tala er slegin inn prenta max_int




# Fill in the missing code
max_int = 0
while True:   
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int
    if num_int < 0:
        break
        
print("The maximum is", max_int)    # Do not change this line

