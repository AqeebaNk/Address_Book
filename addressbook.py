import json
import os
from os.path import *

class Address_class:
    def __init__(self,Address_var):
        self.Address_Var=Address_var
    def Main_address_book(self):
        n=int(input("enter the number of Enteries: "))
        for i in range(n):
            book_name=input("enter the book name: ")
        
            if self.Address_Var.get(book_name)is not None:
                print("User already Exist")
            else:    
                self.Address_Var[book_name]={}
                First_name=input("Enter the First name: ")
                self.Address_Var[book_name]['First Name']=First_name
                Second_name=input("Enter the Second name: ")
                self.Address_Var[book_name]['Second name: ']=Second_name
                Mobile_Number=int(input("Enter the Mobile Number: "))
                self.Address_Var[book_name]['Mobile Number']=Mobile_Number
                Email_address=input("Enter the Email address: ")
                self.Address_Var[book_name]['Email address']=Email_address
        print(self.Address_Var)
        

    def Editing_address_book(self):
        n=int(input("enter the number of Enteries: "))
        
        for i in range(n):
            book_name=input("Enter the book name: ")
            if self.Address_Var.get(book_name)is not None:
                print("1 to enter the First Name:\n2 to enter the second name:\n3 to enter the Mobile number:\n4 to enter the Email address")
                option1=int(input())
                if option1==1:
                    First_name=input("Enter the First name: ")
                    self.Address_Var[book_name]['First name']=First_name
                elif option1==2:
                    Second_name=input("Enter the Second name: ")    
                    self.Address_Var[book_name]['Second number']=Second_name
                elif option1==3:
                    Mobile_number=input("Enter the Mobile Number: ")    
                    self.Address_Var[book_name]['Mobile Number']=Mobile_number  
                elif option1==4:

                    Email_address=input("Enter the Email Address: ")    
                    self.Address_Var[book_name]['Email Address']=Email_address
                else:
                    print("Enter a valide book name")    
            print(self.Address_Var) 

    def Deleting_book_name(self):
        n=int(input("Enter the Number of Enteries to Delete: "))
        for i in range(n):
            book_name=input("Enter the name of the book: ")
            if self.Address_Var.get(book_name)is not None:
                del self.Address_Var[book_name]
            else:
                print("Enter a valide book name: ")    
        print(self.Address_Var)        

    def write_to_json(self):
        new1=input("Enter the file name: ")
        file = open(f"{new1}.json",'w')
        json_object = json.dumps(self.Address_Var)
        file.write(json_object) 
        file.close()
        # print(json_object)    


    def read_from_json(self):
        new1=input("Enter the existing json file: ")
        f = open(f"{new1}.json",'r')
        json_object2=json.load(f)
        print(json_object2)
        f.close()

    def Display(self):
        print(self.Address_Var)    

    def list_json_files(self):
        path = dirname(__file__)
        dir_list = os.listdir(path)
        for i in dir_list:
            if ".json" in i:
                print(i)







    



