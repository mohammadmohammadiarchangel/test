import psycopg2
conn = psycopg2.connect(database = "fastfood", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
def insert() :
      i=1
      while i==1 :
            cur = conn.cursor()
            print("select table to insert")
            print("1 foods table")
            print("2. raw_food table")
            print("3. customer table")
            print("4. order_list table")
            print("5. sell table")
            print("6. employe table")
            print("0. back to menu")
            print("\n")
            choose = input("Choose an option:")
            if (choose == "1"):
                  w=input("enter name of food")
                  a="\'"+w +"\'"
                  q=int( input("enter price of food"))
                  p=int( input("enter qty of food") )
                  query2="select name_food from foods where name_food=%s " %a
                  print("\n")
                  cur.execute(query2)
                  v=cur.fetchall()
                  if(v) :
                        print("data is duplicate")
                        print("\n")
                  else :
                        query1="INSERT INTO foods (name_food,qty,price) VALUES (%s,%d, %d )" % (a,q,p)
                        cur.execute(query1)
                        conn.commit()
                        print("Records created successfully") 
                        print("\n")

            elif (choose == "2"):
                  a=input("enter name of raw_food")
                  a="\'"+a +"\'"
                  p=int( input("enter price of food"))
                  q=int( input("enter amount of food") )
                  query2="select name_raw from raw_food where name_raw=%s " %a
                  cur.execute(query2)
                  v=cur.fetchall()
                  print("\n")
                  if(v) :
                        print("data is duplicate")
                        print("\n")

                  else :
                        query1="INSERT INTO raw_food (name_raw,price,amount) VALUES (%s,%d, %d )" % (a,p,q)
                        cur.execute(query1)
                        conn.commit()
                  
                        print("Records created successfully") 
                        print("\n")
                        
            elif (choose == "3"):
                  b=int( input("enter id_customer"))
                  a=input("enter name_customer")
                  a="\'"+a +"\'"
                  q=int( input("enter phone_customer"))
                  query2="select id_customer from customer where id_customer=%d " %b
                  cur.execute(query2)
                  v=cur.fetchall()
                  print("\n")
                  if(v) :
                        print("data is duplicate")
                        print("\n")
                  else :
                        query1="INSERT INTO customer (id_customer,name_customer,phone) VALUES (%d,%s, %d )" % (b,a,q)
                        cur.execute(query1)
                        conn.commit()
                        print("Records created successfully") 
                        print("\n")
          
     
            elif (choose == "4"):
                  a=int( input("enter id_order"))
                  b=int( input("enter id_customer"))
                  q=int( input("enter name_food"))
                  p=int( input("enter qty_order"))
                  query2="select id_order from order_list where id_order=%d " %a
                  cur.execute(query2)
                  v=cur.fetchall()
                  print("\n")
                  if(v) :
                        print("data is duplicate")
                        print("\n")

                  else :
                        query1="INSERT INTO order_list (id_order,id_customer,name_food,qty_order) VALUES (%d,%d, %d,%d )" % (a,b,q,p)
                        cur.execute(query1)
                        conn.commit()
                        print("Records created successfully") 
                        print("\n")
               
            elif (choose == "5"):
                  a=int( input("enter id_order"))
                  b=int( input("enter id_customer"))
                  q=int( input("enter sum_price"))
                  p=int( input("enter id_factor") )
                  query1="INSERT INTO sell (id_order,id_customer,sum-price,id_factor) VALUES (%d,%d, %d,%d )" % (a,b,q,p)
                  cur.execute(query1)
                  conn.commit()
                  print("Records created successfully") 
                  print("\n")
           
            elif (choose == "6"):
                  b=int( input("enter id_employe"))
                  a=input("enter name_employe")
                  a="\'"+a +"\'"
                  q=int( input("enter salary"))
                  e=input("enter job")
                  e="\'"+e +"\'"
                  query2="select id_employe from employe where id_employe=%d " %b
                  cur.execute(query2)
                  v=cur.fetchall()
                  print("\n")
                  if(v) :
                        print("data is duplicate")
                        print("\n")
                  else :
                        query1="INSERT INTO employe (id_customer,name_customer,phone) VALUES (%d,%s, %d,%s )" % (b,a,q,e)
                        cur.execute(query1)
                        conn.commit()
                        print("Records created successfully") 
                        print("\n")
            
 
            elif (choose == "0"):
                  i=0



