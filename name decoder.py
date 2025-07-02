name = input("Tell me the name you want to decode: ")
if len(name)<=3:
    print("Your decoded name is: ",name[::-1])
elif len(name)>=4:
    
    hdecoded=name[3:-3]
    fdecoded=hdecoded[-1]+hdecoded[:-1]
    print("Your decoded name is: ",fdecoded)