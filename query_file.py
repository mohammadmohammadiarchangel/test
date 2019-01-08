import psycopg2
conn = psycopg2.connect(database = "fastfood", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
def query() :
      query1 = input("ENTER YOUR QUERY :")
      cur.execute( query1 )
      conn.commit()
      print("query is successfull") 
