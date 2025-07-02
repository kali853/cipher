def coder(name):
    import random
    import string
    if len(name)<=3:
        print("Your coded name is: ",name[::-1])
    elif len(name)>=4:
        rand_st=''.join(random.choices(string.ascii_letters,k=3))
        rand_end=''.join(random.choices(string.ascii_letters,k=3))
        coded=name[1:]+name[0]
        rand=rand_st+coded+rand_end
        print("Your coded name is: ",rand)
    else:
        print("Please enter a valid name.")

name=input("Tell me the name you want to code: ")
coder(name)
