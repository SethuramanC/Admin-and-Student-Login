from pymysql import*
from math import*

def add():
    try:
        num1=float(input("Enter the number"))
        num2=float(input("Enter the number"))
        output=num1+num2
        if(output.is_integer()):
            output=int(output)
            con=connect(host="localhost",user="root",database="calaculator",password="sethuraman16")
            q='insert into Addition_table values({0},{1},{2})'.format(num1,num2,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
        else:
            con=connect(host="localhost",user="root",database="calaculator",password='sethuraman16')
            q="insert into Addition_table values({0},{1},{2})".format(num1,num2,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
    except Exception as e:
        print(e)
     
def sub():
    try:
        num1=float(input("Enter the number"))
        num2=float(input("Enter the number"))
        output=num1-num2
        if(output.is_integer()):
            output=int(output)
            con=connect(host="localhost",user="root",database="calaculator",password="sethuraman16")
            q='insert into Subraction_table values({0},{1},{2})'.format(num1,num2,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
        else:
            con=connect(host="localhost",user="root",database="calaculator",password='sethuraman16')
            q="insert into Subraction_table values({0},{1},{2})".format(num1,num2,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
    except Exception as e:
        print(e)
  
def mul():
    try:
        num1=float(input("Enter the number"))
        num2=float(input("Enter the number"))
        output=num1*num2
        if(output.is_integer()):
            output=int(output)
            con=connect(host="localhost",user="root",database="calaculator",password="sethuraman16")
            q='insert into Multiplication_table values({0},{1},{2})'.format(num1,num2,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
        else:
            con=connect(host="localhost",user="root",database="calaculator",password='sethuraman16')
            q="insert into Multiplication_table values({0},{1},{2})".format(num1,num2,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
    except Exception as e:
        print(e)

def div():
    try:
        num1=float(input("Enter the number"))
        num2=float(input("Enter the number"))
        if(num2 == 0):
            raise ValueError("Division by zero is not allowed!")
        output=num1/num2
        if(output.is_integer()):
            output=int(output)
            con=connect(host="localhost",user="root",database="calaculator",password="sethuraman16")
            q='insert into Division_table values({0},{1},{2})'.format(num1,num2,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
        else:
            con=connect(host="localhost",user="root",database="calaculator",password="sethuraman16")
            q='insert into Division_table values({0},{1},{2})'.format(num1,num2,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
    except Exception as e:
        print(e)
 
def sq_root():
    try:
        num=float(input("Enter the number"))
        if num<0:
            raise ValueError("Square root of negative number is not possible")
        output=sqrt(num)
        if(output.is_integer()):
            output=int(output)
            con=connect(host="localhost",user="root",database="calaculator",password="sethuraman16")
            q="insert into Squareroot_table values({0},{1})".format(num,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
        else:
            con=connect(host="localhost",user="root",database="calaculator",password="sethuraman16")
            q="insert into Squareroot_table values({0},{1})".format(num,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
    except Exception as e:
        print(e)
        
def square():
    try:
        num=float(input("Enter the number"))
        output=num**2
        if(output.is_integer()):
            output=int(output)
            con=connect(host="localhost",user="root",database="calaculator",password="sethuraman16")
            q="insert into Square_table values({0},{1})".format(num,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
        else:
            con=connect(host="localhost",user="root",database="calaculator",password="sethuraman16")
            q="insert into Square_table values({0},{1})".format(num,output)
            cur=con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            print(output)
    except Exception as e:
        print(e)
        
def percentage():
    try:
        num1=float(input("Enter the number"))
        num2=int(input("Enter the Total"))
        if(num2<=0):
            raise ValueError("The Value cannot be in negative as well it can't be 0")
        output=round(num1/num2*100,1)
        print(output)
        con=connect(host="localhost",user="root",database="calaculator",password='sethuraman16')
        q="insert into Percentage_table values({0},{1},{2})".format(num1,num2,output)
        cur=con.cursor()
        cur.execute(q)
        con.commit()
        con.close()
    except Exception as e:
        print(e)
    
              
while(True):
    print("\n Calculator Menu")
    ch=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square Root\n6.Square\n7.Percentage\n8.Exit \nselect any 1:"))
    if(ch==1):
        add()
    elif(ch==2):
        sub()
    elif(ch==3):
        mul()
    elif(ch==4):
        div()
    elif(ch==5):
        sq_root()
    elif(ch==6):
        square()
    elif(ch==7):
        percentage()
    elif(ch==8):
        print("Thank You")
        break
    else:
        print("Invalid Choice, Please try again")
            
            
        
    