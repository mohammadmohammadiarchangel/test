import psycopg2
conn = psycopg2.connect(database = "fastfood", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
def update() :
      i=1
      while i==1 :
            cur = conn.cursor()
            print("select table to update")
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
                  a=input("enter name of food")
                  a="\'"+a +"\'"
                  q=int( input("enter price of food"))
                  p=int( input("enter qty of food") )
                  query1="UPDATE foods set price = %d,qty = %d where name_food = %s" % (q,p,a)
                  cur.execute(query1)
                  conn.commit()
                  print("Records updated successfully")  
                  print("\n")
   
            elif (choose == "2"):
                  a=input("enter name of raw_food")
                  a="\'"+a +"\'"
                  p=int( input("enter price of food"))
                  q=int( input("enter amount of food") )
                  query1="UPDATE raw_food set price = %d,amount = %d where name_raw = %s" % (p,q,a)
                  cur.execute(query1)
                  conn.commit()
                  print("Records updated successfully") 
                  print("\n")
      
            elif (choose == "3"):
                  b=int( input("enter id_customer"))
                  a=input("enter name_customer")
                  a="\'"+a +"\'"
                  q=int( input("enter phone_customer"))
                  query1="UPDATE customer set name_customer = %s,phone = %d where id_customer = %d" % (a,q,b)
                  cur.execute(query1)
                  conn.commit()
                  print("Records updated successfully") 
                  print("\n")
      
            elif (choose == "4"):
                  a=int( input("enter id_order"))
                  b=int( input("enter id_customer"))
                  q=int( input("enter name_food"))
                  p=int( input("enter qty_order"))
                  query1="UPDATE order_list set id_customer = %d,name_food = %s,qty_order = %d where id_order = %d" % (b,q,p,a)
                  cur.execute(query1)
                  conn.commit()
                  print("Records updated successfully") 
                  print("\n")
           
            elif (choose == "5"):
                  a=int( input("enter id_customer"))
                  b=int( input("enter id_order"))
                  q=int( input("enter sum_price"))
                  p=int( input("enter id_factor") )
                  query1="UPDATE customer set sum_price = %s,id_factor = %d where id_customer=%d,id_order = %d" % (q,p,a,b)
                  cur.execute(query1)
                  conn.commit()
                  print("Records updated successfully") 
                  print("\n")
         
            elif (choose == "6"):
                  b=int( input("enter id_employe"))
                  a=input("enter name_employe")
                  a="\'"+a +"\'"
                  q=int( input("enter salary"))
                  e=input("enter job")
                  e="\'"+e +"\'"
                  query1="UPDATE employe set name_employe = %s,salary = %d,job = %d where id_employe = %d" % (a,q,e,b)
                  cur.execute(query1)
                  conn.commit()
                  print("Records updated successfully") 
                  print("\n")
        
            elif (choose == "0"):
                  i=0

