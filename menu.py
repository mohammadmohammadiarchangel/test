import show_file
import psycopg2
import insert_file
import update_file
import delete_file
import query_file


print("Welcome")
print("------------------------------------------------------------------------------------")
i=1
while i==1 :
      print("1. show all")
      print("2. insert")
      print("3. delete")
      print("4. update")
      print("5. query")
      print("0. finish")
      print("\n")

      choose = input("Choose an option:")
      if (choose == "1"):
            show_file.show()
      elif (choose == "2"):
            insert_file.insert()
      elif (choose == "3"):
            delete_file.delete()
      elif (choose == "4"):
            update_file.update()
      elif (choose == "5"):
            query_file.query()
      elif (choose == "0"):
            i=2
      else :
            print("choose wrong")
            print("\n")
