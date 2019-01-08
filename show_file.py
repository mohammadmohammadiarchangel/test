import psycopg2
conn = psycopg2.connect(database = "fastfood", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
def show() :
    

    i=1
    while i==1 :
        print("enter name of table to show")
        print("1. foods")
        print("2. raw_food")
        print("3. customer")
        print("4. order_list")
        print("5. sell")
        print("6. employe")
        print("0. back to menu")
        print("\n")

        choose = input("Choose an option:")
        if (choose == "1"):
                cur.execute( " SELECT * From foods")
                rows = cur.fetchall()
                print("name_food ,price ,qty")
                for row in rows:
                        
                        print(row[0],"\t")
                        print(row [1],"\t")
                        print(row[2],"\t") 
                        print("\n")

        elif (choose == "2"):
                cur.execute( " SELECT * From raw_food")
                rows = cur.fetchall()
                print("raw_food ,price ,amount")
                for row in rows:
                        
                        print(row[0],"\t")
                        print(row [1],"\t")
                        print(row[2],"\t") 
                        print("\n")

        elif (choose == "3"):
                cur.execute( " SELECT * From customer")
                rows = cur.fetchall()
                print("id_customer ,name_customer ,phone")
                for row in rows:
                        print(row[0],"\t")
                        print(row [1],"\t")
                        print(row[2],"\t") 
                        print("\n")
        elif (choose == "4"):
                cur.execute( " SELECT * From order_list")
                rows = cur.fetchall()
                print("id_order,id_customer,food_name,qty_order")
                for row in rows:
                        print(row[0],"\t")
                        print(row [1],"\t")
                        print(row[2],"\t")
                        print(row[3],"\t") 
                        print("\n")
        elif (choose == "5"):
                cur.execute( " SELECT * From sell")
                rows = cur.fetchall()
                print("id_customer,id_order,sum_price ,id_factor")
                for row in rows:
                        print(row[0],"\t")
                        print(row [1],"\t")
                        print(row[2],"\t") 
                        print(row[3],"\t") 
                        print("\n")
        elif (choose == "6"):
                cur.execute( " SELECT * From employe")
                rows = cur.fetchall()
                print("id_employe,name_employe,salary,job")
                for row in rows:
                        print(row[0],"\t")
                        print(row [1],"\t")
                        print(row[2],"\t") 
                        print(row[3],"\t")
                        print("\n")
        elif(choose == "0"):
                i=0
        print( "show done successfully")
        print("\n")