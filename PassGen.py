import random

length=int(input("Password Length:"))
symbols=['!','@','#','$','%','^','&','*','(',')','<','>','?']
numbers=['1','2','3','4','5','6','7','8','9','0']
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha_big=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
final_list=alpha+alpha_big+numbers+symbols
print( "Your Random Password:")
for i in range(length+1):

    password=random.choice(final_list)
    print( password, end=' ')

        
        
