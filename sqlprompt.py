import sqlite3

conn = sqlite3.connect("newnum.db")

cursor = conn.cursor()

prompt = """
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""


while True:
  x = raw_input(prompt)

  if x in set(["1","2","3","4"]):
    operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(x)]
    cursor.execute("SELECT {}(num) from numbers".format(operation))
    get = cursor.fetchone()

    print operation + ": %f"%get[0]

  elif x == "5":
    print "Exit"
    break
