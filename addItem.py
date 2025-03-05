def create_print_list():
    
    try:
        num_items = int(input("enter no. of item you want:"))
        
        if num_items < 0:
            print("Items cannot be negative")
        
        item_list = []
        for i in range(num_items):
            item = input(f"enter an item {i + 1}:")
            item_list.append(item)
            
        print("List is", item_list)
        
    except ValueError:
        print("Invalid Input")
        

create_print_list()