#Gera forrit sem prentar næsta tölu í sequence
#Algorithm virkar þannig að forritið á að leggja saman síðustu þrjár tölur til að fá næstu
#Keyri í n for loopu og legg saman 



n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = -1
num2 = 0
num3 = 1
seq = 1

for i in range(0, n+1):
    seq = num1 + num2 + num3
    if seq != 0:
        print(seq, end = " ")
    num1 = num2
    num2 = num3
    num3 = seq
