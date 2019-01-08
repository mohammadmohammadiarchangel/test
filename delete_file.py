import psycopg2
conn = psycopg2.connect(database = "fastfood", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
def delete() :
      i=1
      while i==1 :
            print("select table to delete")
            print("1 foods table")
            print("2. raw_food table")
            print("3. customer table")
            print("4. order_list table")
            print("5. sell table")
            print("6. employe table")
            print("0. back to menu")
            print("\n")
            cur = conn.cursor()
            choose = input("Choose an option:")
            if (choose == "1"):
                  a=input("enter name of food")
                  a="\'"+a +"\'"
                  
                  query2="select name_food from foods where name_food=%s " %a
                  print("\n")
                  cur.execute(query2)
                  v=cur.fetchall()
                  if(v) :
                        query1="DELETE from foods where name_food= %s" % (a )
                        cur.execute(query1)
                        conn.commit()
                        print("Records deleted successfully")
                        print("\n")
                  else :
                        print("data is not found")
                        print("\n")

         
            elif (choose == "2"):
                  a=input("enter name of raw_food")
                  a="\'"+a +"\'"

                  query2="select name_raw from raw_food where name_raw=%s " %a
                  cur.execute(query2)
                  v=cur.fetchall()
                  print("\n")
                  if(v) :
                        query1="DELETE from raw_food  where name_raw= %s )" % (a )
                        cur.execute(query1)
                        conn.commit()
                  else :
                        print("data is not found")
                        print("\n")
            elif (choose == "3"):
                  b=int( input("enter id_customer"))
                  query2="select id_customer from customer where id_customer=%d " %b
                  cur.execute(query2)
                  v=cur.fetchall()
                  print("\n")
                  if(v) :
                        query1="DELETE from customer where id_customer= %d )" % (b )
                        cur.execute(query1)
                        conn.commit()
                  else :
                        print("data is not found")
                        print("\n")
            elif (choose == "4"):
                  a=int( input("enter id_order"))
                  query2="select id_order from order_list where id_order=%d " %a
                  cur.execute(query2)
                  v=cur.fetchall()
                  print("\n")
                  if(v) :
                        query1="DELETE from order_list where id_order= %d" % (a)
                        cur.execute(query1)
                        conn.commit()
                  else :
                        print("data is not found")
                        print("\n")
            elif (choose == "5"):
                  b=int( input("enter id_customer"))
                  a=int( input("enter id_order"))
                  query1="DELETE from sell where id_customer= %d ,id_order=%d )" % (b,a )
                  cur.execute(query1)
                  conn.commit()
       
            elif (choose == "6"):
                  b=int( input("enter id_employe"))
                  query2="select id_employe from employe where id_employe=%d " %b
                  cur.execute(query2)
                  v=cur.fetchall()
                  print("\n")
                  if(v) :
                        query1="DELETE from customer where id_employe= %d )" % (b )
                        cur.execute(query1)
                        conn.commit()
                  else :
                        print("data is not found")
                        print("\n")
           
            elif (choose == "0"):
                  i=0

