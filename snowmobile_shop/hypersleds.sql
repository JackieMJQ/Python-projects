#create databse
create database hypersleds;

#create table and insert data
CREATE TABLE customer (
  customer_id int NOT NULL AUTO_INCREMENT,
  phone_number int NOT NULL,
  address varchar(255) NOT NULL,
  full_name varchar(255) NOT NULL,
  email varchar(255) DEFAULT NULL,
  PRIMARY KEY (customer_id));

INSERT INTO customer 
VALUES (1,7094564,'57 Blvd','Mike Piercey','mikepiercey@cna.ca'),(2,7095425,'58 Blvd','Dino Way','dinoway@cna.ca'),(3,7096544,'59 BLVD','Jiaqi Mu','jiaqimu@cna.ca');
  
CREATE TABLE product (
  product_id int NOT NULL AUTO_INCREMENT,
  product_quanity int NOT NULL,
  product_description varchar(255) NOT NULL,
  product_price decimal(10,2) NOT NULL,
  PRIMARY KEY (product_id));

INSERT INTO product 
VALUES (1,10,'CKX Helment',3899.99),(2,30,'Dupont slides',49.99),(3,12,'Jethwear Helment',1649.99),(4,5,'Artic Cat Clutch',1427.99),(5,23,'BRP Gas Shock Kimpex',1191.99),(6,4,'Artic Cat Gas Shock Kimpex',1170.99),(7,7,'Polaris Gas Shock Kimpex',1156.99),(8,15,'Polaris Clutch',2429.99),(9,5,'Yamaha Clutch',2339.99),(10,7,'BRP Metal Ski Kimpex',1206.99),(11,9,'Artic Cat Metal Ski Kimpex',1152.99),(12,7,'Polaris Metal Ski Kimpex',1158.99);  

create table orders (
	order_id int NOT NULL auto_increment,
    order_date date DEFAULT NULL,
    order_status varchar(255) NOT NULL,
    address varchar(255) NOT NULL,
    customer_id int NOT NULL,
    product_id int NOT NULL,
    primary key(order_id),
    FOREIGN KEY(customer_id) references customer (customer_id),
    foreign key(product_id) references product (product_id));

insert into orders
values (1, '2021-05-18', 'delivered', '1456 Fournier/ Mirabel/ QC', 1, 2), (2, '2021-06-18', 'delivered', '4034 St George Street/Vancouver/BC', 2, 5), (3, '2021-10-08', 'delivered', '641 Ross Street/Perth/ON', 3, 4),(4, '2022-03-12', 'delivering', '1274 Main St/Halifax/NS', 3, 7),(5, '2022-03-18','delivering', '232 Cashin Ave/St.John/NB', 1, 1);

create table store (
	store_id int NOT NULL auto_increment,
    store_number int NOT NULL,
    store_address varchar(255) NOT NULL,
    product_id int NOT NULL,
    primary key(store_id),
    foreign key(product_id) references product (product_id));
    
INSERT INTO store 
VALUES (1,35066,'Corner Brook NL',5),(2,35067,'Gander NL',2);

CREATE TABLE vendor (
  vendor_id int NOT NULL AUTO_INCREMENT,
  vendor_name varchar(255) NOT NULL,
  vendor_address varchar(255) NOT NULL,
  product_id int NOT NULL,
  PRIMARY KEY (vendor_id),
  foreign key(product_id) references product (product_id));
  
INSERT INTO vendor 
VALUES (1,'Kimpex','Toronto ON',3),(2,'MFG Supply','Montreal QC',2),(3,'Great Snowmobile Parts','St. John NB',6);

CREATE TABLE invoice (
  invoice_id int NOT NULL AUTO_INCREMENT,
  order_id int NOT NULL,
  PRIMARY KEY (invoice_id),
  foreign key (order_id) references orders(order_id));
  
insert into invoice
values (1,1),(2,2),(3,3),(4,4),(5,5);

