import re
def func11(cc):
    if cc == "REG":
        def funcq():
            email = input("enter email address you want to sigin with:")
            if re.search("[A-Z]", email):
                print("enter a valid email it should not have upper case")
                funcq()
            elif re.match(r'\d{1}', email):
                print("enter a valid email first word should be apphabet")
                funcq()
            elif re.search("[@][.]", email):
                print("enter a valid emailshould not have {.} dot before @ " )
                funcq()
            elif not re.search("@.", email):
                print("enter a valid email")
                funcq()
            else:
                C=1
                with open("assig.txt") as q:
                    for i in q:
                        x, b = i.split(",")
                        b = b.strip()
                        if x == email:
                            print("Email alread exist try again")
                            funcq()
                            C=0
                            break
                    if C==1:
                        with open("assig.txt", "a") as f:
                                f.write("\n"+email+",")
        funcq()
        def pass1():
            password = input("create your password:")
            if len(password) < 5 or 16 < len(password):
                print('your password len should be between 5 to 16')
                pass1()
            elif not re.search('[a-z]', password):
                print("enter a valid password, it should have atleast one lower case")
                pass1()
            elif not re.search('[A-Z]', password):
                print("enter a valid password, it should have atleast one lower case")
                pass1()
            elif not re.search('[0-9]', password):
                print("enter a valid password,should have one upper case ")
                pass1()
            else:
                d = input("R-Enter Password:")
                if d != password:
                    print("Password did not match Re-enter password")
                    pass1()
                else:
                    with open("assig.txt", "a") as f:
                        f.write(password)
                        print("Regestration Successful!!")
        pass1()
def begin():
    c = input("enter REG for Regestration, or LOG to login:")
    return c
def login(ss):
    if ss == "LOG":
        qmail = input("enter email you want to login with:")
        a = input("enter pass:")
        o=1
        oc=1
        o=1
        with open("assig.txt") as s:
            for j in s:
                x, b = j.split(",")
                b = b.strip()
                if x == qmail and b == a:
                    print("Login successful")
                    oc=0
                    break
                elif x==qmail and b!=a:
                    oc+=1
            if oc == 1:
                print("Sorry email does not exist kindly register:")
                func11("REG")
            elif oc==2:
                with open("assig.txt") as s:
                    for j in s:
                        x, b = j.split(",")
                        b = b.strip()
                        if x == qmail and b != a:
                            print("SORRY !! your password do not match")
                            aa = input("if you want to login again type (TRY), else for forget password (FOR), to change password(CHNG)")
                            if aa == "TRY":
                                login("LOG")
                            elif aa == "FOR":
                                print("your password is :", b)
                                break
                            else:
                                def pass1():
                                    password = input("create your password")
                                    if len(password) < 5 or 16 < len(password):
                                        print('your password len should be between 5 to 16')
                                        pass1()
                                    elif not re.search('[a-z]', password):
                                        print("enter a valid password")
                                        pass1()
                                    elif not re.search('[A-Z]', password):
                                        print("enter a valid password")
                                        pass1()
                                    elif not re.search('[0-9]', password):
                                        print("enter a valid password")
                                        pass1()
                                    else:
                                        d = input("R-Enter Password")
                                        if d != password:
                                            print("Password did not match Re-enter password")
                                            pass1()
                                        else:
                                                ff=open("assig.txt","r")
                                                tt=ff.read()
                                                tt=tt.replace(b,password)
                                                ff.close()
                                                ff=open("assig.txt","w")
                                                ff.write(tt)
                                                ff.close()
                                                print("Your password has been Successful changed!!")
                                pass1()


ss = begin()
func11(ss)
login(ss)




