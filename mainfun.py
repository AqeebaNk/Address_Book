from addressbook import Address_class

if __name__ == "__main__":
    address_book={}
    obj=Address_class(address_book)
    
    while True:
        print("select any option\n1: To enter the address book\n2: To edit the address book\n3: To delete a book\n4: write to json\n5: read from json\n6:Display\n7:To list directory")
        option2=int(input())
        if option2==1:
            obj.Main_address_book()
        elif option2==2:
            obj.Editing_address_book()
        elif option2==3:
            obj.Deleting_book_name()   
        elif option2==4:
            obj.write_to_json()  
        elif option2==5:
            obj.read_from_json()    
        elif option2==6:
            obj.Display()
        elif option2==7:
            obj.list_json_files()    
        else:
            print("invalide option")   
