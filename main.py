import sqlite3
from os import system

cnt = sqlite3.connect("backup.dp")  
cursor  =  cnt.cursor ()

#cursor.execute('''CREATE TABLE agenti ( id INTEGER(5) PRIMARY KEY NOT NULL , vardschar TEXT(15)  NOT NULL, uzvardschar TEXT(15)  NOT NULL,pilseta char(35),Valst char DEFAULT[LV], gada_apgrozijums char INTEGER(7,2), comission decimal(7,2));''')
def add_agent():
  s_id = input('Rakstit agenta Id:')
  s_name = input('Uzraksti vardu:')
  s_uzvard = input('Uzraksti uzvards:')
  s_city = input('Uzrakstiet pilsetu:')
  s_gada_apgrozijums = input("Uzrakstie gada_apgrozijums: ")
  s_comission = input("Uzrakstie kada comission: ")
  s_valst = input("Uzrakstie kada valst( LV , EST or LT) : ")
  cursor.execute("""
INSERT INTO agenti(id, vardschar ,uzvardschar , pilseta,gada_apgrozijums,comission, Valst)
VALUES (?,?,?,?,?,?,?)
""", (s_id, s_name, s_uzvard, s_city, s_gada_apgrozijums, s_comission,s_valst))
  cnt.commit ()
  print ( 'Data entered successfully.' )
def all_agents():
  print("ID " ,  "Vards ",   "Uzvards ",  "pilseta ",  "valst " ,  "gadapgroz " ,"comission" )
  query = cursor.execute("SELECT * FROM agenti")
  data = cursor.fetchall()
  for d in data:
    print(d)

#--------------------------------------------------------------------------------------  
#Palielini komisiju visiem aģentiem "LV"
cursor.execute('''UPDATE agenti SET comission=comission+20 WHERE Valst = "LV" ;''')
#--------------------------------------------------------------------------------------
#Noapaļo gada ienākumus līdz veselam skaitlim
cursor.execute("SELECT ROUND(gada_apgrozijums,-1) FROM agenti")
#--------------------------------------------------------------------------------------
def gada_apgrozijum_summu_tikai_LV():
  print("gada apgrozijumu summu LV")
  print("Vards ", "g_jums ", "Valst")
  cursor.execute('''SELECT vardschar , gada_apgrozijums, Valst FROM agenti WHERE Valst= "LV";''')
  data = cursor.fetchall()
  for q in data:
    print(q)
    
  cursor.execute(''';''')
  lv_year = cursor.fetchall()
  print("LV gada apgrozijums ir: ",lv_year)
  #--------------------------------------------------------------------------------------
  
def gada_apgrozijum_summu_tikai_EST():
  print("gada apgrozijumu summu EST")
  print("Vards ","g_jums ", "Valst")
  cursor.execute('''SELECT vardschar ,gada_apgrozijums, Valst FROM agenti WHERE Valst= "EST";''')
  data = cursor.fetchall()
  for w in data:
    print(w)
#--------------------------------------------------------------------------------------
def gada_apgrozijum_summu_tikai_LT():
  print("gada apgrozijumu summu LT")
  print("Vards ","g_jums ", "Valst")
  cursor.execute('''SELECT vardschar , gada_apgrozijums, Valst FROM agenti WHERE Valst= "LT";''')
  data = cursor.fetchall()
  for e in data:
    print(e)
    
def visaugstākais_komisijas_procents():
  print("visaugstākais komisijas procents")
  cursor.execute('''SELECT id, vardschar , comission FROM agenti ORDER BY comission DESC;''')
  print("id  ", "vards  ", "comission" )
  data = cursor.fetchall()
  for r in data:
    print(r)



def tikai_lv_agenti():
#--------------------------------------------------------------------------------
  print("ID     " ,  "Vards     ",    "Uzvards      ",  "pilseta    ",  "valst    " ,  "gadapgroz   " ,"comission" )
  query = cursor.execute('''SELECT * FROM agenti WHERE Valst= "LV";''')
  data = cursor.fetchall()
  for d in data:
    print(d)
def tikai_EST_agenti():
#--------------------------------------------------------------------------------
  print("ID     " ,  "Vards     ",    "Uzvards      ",  "pilseta    ",  "valst    " ,  "gadapgroz   " ,"comission" )
  query = cursor.execute('''SELECT * FROM agenti WHERE Valst= "EST";''')
  data = cursor.fetchall()
  for h in data:
    print(h)
def tikai_LT_agenti():
#--------------------------------------------------------------------------------
  print("ID     " ,  "Vards     ",    "Uzvards      ",  "pilseta    ",  "valst    " ,  "gadapgroz   " ,"comission" )
  query = cursor.execute('''SELECT * FROM agenti WHERE Valst= "LT";''')
  data = cursor.fetchall()
  for j in data:
    print(j)
#--------------------------------------------------------------------------------
def main():
    print(" 1-Add agent","\n", "2-gada apgrozijum summu tikai LV","\n", "3- gada apgrozijum summu tikai EST","\n" , "4- gada apgrozijum summu tikai LT","\n", "5-paskatit visas agent","\n","6- tikai LV agenti","\n", "7- tikai EST agenti","\n", "8 - tikai LT agenti")
    choice = input("Please make your choice: ").strip()
    if choice == "1":
        add_agent()
    elif choice == "2":
        gada_apgrozijum_summu_tikai_LV()
    elif choice == "3":
        gada_apgrozijum_summu_tikai_EST()
    elif choice == "4":
        gada_apgrozijum_summu_tikai_LT()
    elif choice == "5":
        all_agents()
    elif choice == "6":
        tikai_lv_agenti()
    elif choice == "7":
        tikai_EST_agenti()
    elif choice == "8":
        tikai_LT_agenti()
    else:
        print("Invalid input. Please try again.")

while True:
    system('clear')
    main()
    input("Press enter to continue: ")
