from mysql.connector import connect

hostname = "localhost"
user_name = "root"
pwd = "20010227"


def execute_and_commit(query):
    # step1: create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # step2: create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # step3: execute the statement
            mysql_cursor.execute(query)
            # step4: commit the changes
            mysql_connection_object.commit()
   
            
# INSERT QUERY
def add_customer(customer_id, phone_number, address, full_name, email):
    add_customer_query = f"""INSERT INTO hypersleds.customer (customer_id, phone_number, address, full_name, email) 
    value ("{customer_id}", "{phone_number}", "{address}", "{full_name}", "{email}")"""
    
    execute_and_commit(add_customer_query)
    
# test
# add_customer(4, 29388439, "St. John's", "MJQ", "jasd.com")

def add_order(order_id, order_date, order_status, address, customer_id, product_id):
    add_order_query = f"""INSERT INTO hypersleds.orders (order_id, order_date, order_status, address, customer_id, product_id)
    value ("{order_id}", "{order_date}", "{order_status}", "{address}", "{customer_id}", "{product_id}")"""
    
    execute_and_commit(add_order_query)
    
# test
# add_order(6, "2022-04-08", "undelivered", "23 Star Ave, St. John's, NL", 1, 1)

def add_product(product_id, product_quanity, product_description, product_price):
    add_product_query = f"""INSERT INTO hypersleds.product (product_id, product_quanity, product_description, product_price)
    value ("{product_id}", "{product_quanity}", "{product_description}", "{product_price}")"""
    # it should be product_quantity, but that's a typo last time which is quanity
    
    execute_and_commit(add_product_query)
    
# test
# add_product(13, 43, "test", 99.99)

def add_store(store_id, store_number, store_address, product_id):
    add_store_query = f"""INSERT INTO hypersleds.store (store_id, store_number, store_address, product_id)
    value ("{store_id}", "{store_number}", "{store_address}", "{product_id}")"""

    execute_and_commit(add_store_query)
    
#test
# add_store(3, 35068, "test", 4)

def add_vendor(vendor_id, vendor_name, vendor_address, product_id):
    add_vendor_query = f"""INSERT INTO hypersleds.vendor (vendor_id, vendor_name, vendor_address, product_id)
    value ("{vendor_id}", "{vendor_name}", "{vendor_address}", "{product_id}")"""

    execute_and_commit(add_vendor_query)
    
# test
# add_vendor(4, "test", "test", 1)

def add_invoice(invoice_id, order_id):
    add_invoice_query = f"""INSERT INTO hypersleds.invoice (invoice_id, order_id)
    value ("{invoice_id}", "{order_id}")"""
    
    execute_and_commit(add_invoice_query)
    
# test
# add_invoice(6, 6)


# REMOVE QUERY
def remove_customer(customer_id):
    delete_customer_from_customer = f"DELETE FROM hypersleds.customer WHERE customer_id = {customer_id};"
    delete_customer_from_orders = f"DELETE FROM hypersleds.orders WHERE customer_id = {customer_id};"
    
    execute_and_commit(delete_customer_from_customer)
    execute_and_commit(delete_customer_from_orders)
    
# test
# remove_customer(4)

def remove_order(order_id):
    delete_order_from_orders = f"DELETE FROM hypersleds.orders WHERE order_id = {order_id};"
    delete_order_from_invoice = f"DELETE FROM hypersleds.invoice WHERE order_id = {order_id};"
    
    execute_and_commit(delete_order_from_invoice)
    execute_and_commit(delete_order_from_orders)
    
#test
# remove_order(6)

def remove_product(product_id):
    delete_product_from_product = f"DELETE FROM hypersleds.product WHERE product_id = {product_id};"
    delete_product_from_store = f"DELETE FROM hypersleds.store WHERE product_id = {product_id};"
    
    execute_and_commit(delete_product_from_store)
    execute_and_commit(delete_product_from_product)
    
# test
# remove_product(13)

def remove_store(store_id):
    delete_store_from_store = f"DELETE FROM hypersleds.store WHERE store_id = {store_id};"
    
    execute_and_commit(delete_store_from_store)
    
# test
# remove_store(3)

def remove_vendor(vendor_id):
    delete_vendor_from_vendor = f"DELETE FROM hypersleds.vendor WHERE vendor_id = {vendor_id};"
    
    execute_and_commit(delete_vendor_from_vendor)
    
# test
# remove_vendor(4)

def remove_invoice(invoice_id):
    delete_invoice_from_invoice = f"DELETE FROM hypersleds.invoice WHERE invoice_id = {invoice_id};"
    
    execute_and_commit(delete_invoice_from_invoice)
    
# test
# remove_invoice(5)


# UPDATE FUNCTION

def update_info(table_name, info_need_to_change, new_info, id_name, id):
    update_info = f'UPDATE hypersleds.{table_name} SET {info_need_to_change} = "{new_info}" WHERE {id_name} = "{id}";'
    
    execute_and_commit(update_info)
    
    
# GENERATE INVOICE
def generate_invoice(order_id):
    # step1: create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # step2: create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            
            get_order_info = f"SELECT orders.order_date, orders.order_status, orders.address, customer.phone_number, customer.full_name, customer.email from hypersleds.orders inner join hypersleds.customer on orders.customer_id = customer.customer_id where order_id = {order_id};"
            
            mysql_cursor.execute(get_order_info)
             
            invoice = []
            print("HELLO, HERE IS YOUR INVOICE.")
            for invoice_info in mysql_cursor:
                invoice.append(invoice_info)
        print('\nOrder Date: ', invoice_info[0])
        print('Order Status: ', invoice_info[1])
        print('Address to deliver: ', invoice_info[2])
        print('Recipient: ', invoice_info[4])
        print('Customer Phone Number: ', invoice_info[3])
        print('Customer Email: ', invoice_info[5])
    return invoice

# test
# generate_invoice(1)