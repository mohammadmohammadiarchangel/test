
#1
select name_food
from foods
where price >20

#2
select qty
from foods
where name_food= "fish"

#3
selcet *
from foods
where name_food like "% rice %"

#4
select name_food
from foods
where qty=0

#5
select phone
from customer

#6
select name_customer
from customer
where id_customer =10

#7
select name_employe
from employe
order by name_employe asc

#8
select job
from employe
where id_employe =10

#9
select salary ,name_employe
from employe
where job =chef


#10
select name_customer
from customer ,order_list
where  customer.id_customer=order_list.id_customer
AND name_food= "meat" 
  
#11
select phone
from customer ,order_list
where  customer.id_customer=order_list.id_customer
AND qty_order >100


#12
select id_factor
from customer, sell
where  customer.id_customer=sell.id_customer
and name_customer= "mohammad"

#13
select id_factor
from sell
where sum_price >200


#14
select sum_price
from sell
where  id_customer= 20

#15
select sum_price
from sell
where  id_order= 20

#16
select name_raw
from raw_food
where amount <10

#17
select name_food
from order_list
where id_order =10


#18
select name_customer
from customer ,order_list
where customer.id_customer =order_list.id_customer
and name_food= "pizaa"
and qty_order >10


#19
Select name_food
from order_list
where id_customer=10

#20
select id_factor
from sell ,order_list
where sell.id_order=order_list.id_order
and name_food= "pizaa"
