create table  foods(
  name_food varchar(20),
  price float,
  qty integer,
  primary key(name_food)
)




create table raw_food(
 price float,
  name_raw varchar(20),
amount integer,
  primary key(name_raw)
	
)


create table customer(
	id_customer INTEGER,
	name_customer varchar(20),
	phone integer,
	primary key(id_customer)
)


create table order_list(
		id_customer integer,
		name_food varchar(20),
	qty_order integer,
	id_order INTEGER,
	primary key(id_order),
	 foreign key(name_food) references foods ,
foreign key(id_customer) references customer
	
)
     



create table sell(
  id_customer integer,
	id_order INTEGER,
	sum_price float,
	id_factor integer,
	primary key(id_customer,id_order),
	foreign key(id_customer) references customer,
	foreign key(id_order) references order_list
)





create table employe(
	name_employe VARCHAR(20),
	id_employe INTEGER,
	salary INTEGER,
	job VARCHAR(20),
	primary key (id_employe)
)
