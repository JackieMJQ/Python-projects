from hypersleds import *

# ADD QUERY
def input_customer():
    customer_id = int(input('Customer ID: '))
    phone_number = int(input('Phone Number: '))
    address = input('Address: ')
    full_name = input('Name: ')
    email = input('Email: ')
    add_customer(customer_id, phone_number, address, full_name, email)
    print(f'Customer {full_name} have added successfully!')
        
        
def input_order():
    order_id = int(input('Order ID: '))
    order_date = input('Order Date: ')
    order_status = input('Order Status(delivered / undelivered / delivering): ')
    address = input('Address: ')
    customer_id = int(input('Customer ID: '))
    product_id = int(input('Product ID: '))
    add_order(order_id, order_date, order_status, address, customer_id, product_id)
    print(f'Order {order_id} have added successfully!')
    
def input_product():
    product_id = int(input('Product ID: '))
    product_quanity = int(input('Product Quantity: '))
    product_description = input('Product Description: ')
    product_price = float(input('Product Price: '))
    add_product(product_id, product_quanity, product_description, product_price)
    print(f'Product {product_id} have added successfully!')
    
def input_store():
    store_id = int(input('Store ID: '))
    store_number = int(input('Store Number: '))
    store_address = input('Store Address: ')
    product_id = int(input('Product ID: '))
    add_store(store_id, store_number, store_address, product_id)
    print(f'Store {store_id} have added successfully!')
    
def input_vendor():
    vendor_id = int(input('Vendor ID: '))
    vendor_name = input('Vendor Name: ')
    vendor_address = input('Vendor Address: ')
    product_id = int(input('Product ID: '))
    add_vendor(vendor_id, vendor_name, vendor_address, product_id)
    print(f'Vendor {vendor_id} have added successfully!')
    
def input_invoice():
    invoice_id = int(input('Invoice ID: '))
    order_id = int(input('Order ID: '))
    add_invoice(invoice_id, order_id)
    print(f'Invoice {invoice_id} have added successfully!')
    

# REMOVE QUERY
def remove_customer_input():
    customer_id = int(input('Customer ID(DELETE): '))
    remove_customer(customer_id)
    print(f'Customer {customer_id} have removed successfully!')
    
def remove_order_input():
    order_id = int(input('Order ID(DELETE): '))
    remove_order(order_id)
    print(f'Order {order_id} have removed successfully!')
    
def remove_product_input():
    product_id = int(input('Product ID(DELETE): '))
    remove_product(product_id)
    print(f'Product {product_id} have removed successfully!')
    
def remove_store_input():
    store_id = int(input('Store ID(DELETE): '))
    remove_store(store_id)
    print(f'Store {store_id} have removed successfully!')
    
def remove_vendor_input():
    vendor_id = int(input('Vendor ID(DELETE): '))
    remove_vendor(vendor_id)
    print(f'Vendor {vendor_id} have removed successfully!')
    
def remove_invoice_input():
    invoice_id = int(input('Invoice ID(DELETE): '))
    remove_invoice(invoice_id)
    print(f'Invoice {invoice_id} have removed successfully!')
 
 
# UPADTE QUERY
def update_input():
    table_name = input('Choose table name you want to update: ')
    id = input('Type the ID of the info you want to change: ')
    id_name = input('Type that ID name: ')
    info_need_to_change = input('Choose what infomation you want to change: ')
    new_info = input('New infomation: ')
    update_info(table_name, info_need_to_change, new_info, id_name, id)
    print('Update successfully!')
    
# PRINT ORDER
def print_order():
    order_print = int(input('Type Order ID to generate invoice: '))
    generate_invoice(order_print)
    
    
# MENU
def display_menu():
    print('\nMENU:')
    print('1.   ADD')
    print('2.   DELETE')
    print('3.   UPDATE')
    print('4.   PRINT INVOICE')
    print('5.   QUIT')
    

def main():
    quit = True
    while quit == True:
        display_menu()
        choice = input('\nEnter your choice(1 / 2 / 3 / 4 / 5): ')
        
        if choice == '1':
            print('\nChoose which table you want to add data in?')
            print('1.   Customer')
            print('2.   Order')
            print('3.   Product')
            print('4.   Store')
            print('5.   Vendor')
            print('6.   Invoice')
            choice_1 = input('\nEnter your choice(1 / 2 / 3 / 4 / 5 / 6): ')
            if choice_1 == '1':
                input_customer()
            if choice_1 == '2':
                input_order()
            if choice_1 == '3':
                input_product()
            if choice_1 == '4':
                input_store()
            if choice_1 == '5':
                input_vendor()
            if choice_1 == '6':
                input_invoice()
        
        elif choice == '2':
            print('\nChoose which table you want to delete data in?')
            print('1.   Customer')
            print('2.   Order')
            print('3.   Product')
            print('4.   Store')
            print('5.   Vendor')
            print('6.   Invoice')
            choice_2 = input('\nEnter your choice(1 / 2 / 3 / 4 / 5 / 6): ')
            if choice_2 == '1':
                remove_customer_input()
            if choice_2 == '2':
                remove_order_input()
            if choice_2 == '3':
                remove_product_input()
            if choice_2 == '4':
                remove_store_input()
            if choice_2 == '5':
                remove_vendor_input()
            if choice_2 == '6':
                remove_invoice_input()
                
        elif choice == '3':
            update_input()
        
        elif choice == '4':
            print_order()
        
        elif choice == '5':
            quit = False
            print('Bye!')
            
        else:
            print('\nInvalid Choice.  Try Again.')
            
if __name__ == '__main__':
    main()