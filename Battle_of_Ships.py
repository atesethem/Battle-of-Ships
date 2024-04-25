from doctest import OutputChecker
import sys
errors = []
inputs = ["Player1.txt", "Player2.txt", "Player1.in", "Player2.in"]
for file in sys.argv[1:5]:
  try:
   if file == sys.argv[1]:
     assignment4 = open(sys.argv[1], "r")
     continue
   if file==sys.argv[2]:
     assignment4_2 = open(sys.argv[2], "r")
     continue
   if file == sys.argv[3]:
     shotsfile = open(sys.argv[3], "r")
     continue
   if file == sys.argv[4]:
     shotsfile2 = open(sys.argv[4], "r")
     continue
  except IOError:
    errors.append(file)
  except Exception:
    print("KaBoom! Run for your life.")
OptionalPlayer1= open("OptionalPlayer1.txt", "r")  # i used optinoal files
OptionalPlayer2 = open("OptionalPlayer2.txt", "r")
output = open("battleship.out.txt", "w")
shots1=""
shots2=""
player1 = "Player1"
player2 = "Player2"
all_lines=[]
all_lines_2 = []
all_lines1 = []
all_lines2 = []
myboard=[["-"]*10 for x in range(10)]
finalboard1 = [["-"]*10 for x in range(10)]   #i created two boards first one is to show second one is the background board
finalboard2 = [["-"]*10 for x in range(10)]
showingboard=[["-"]*10 for x in range(10)]
myboard2=[["-"]*10 for x in range(10)]
showingboard2=[["-"]*10 for x in range(10)]
listship = ["Carrier -","Battleship - -", "Destroyer -", "Submarine -", "Patrol Boat - - - -"]
list1ship = ["Carrier -","Battleship - -", "Destroyer -", "Submarine -", "Patrol Boat - - - -"]
wordsandnumbers={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10} #providing to make easier to convert words to numbers
if not errors == []:
  print(str(errors) + " are not reachable.") #if some files are missing. It shows that which files are missing
  exit()
try:
 for i in shotsfile:
   shots1=i
except NameError:
  print("Player1's board are not reachable. Please check your inputs.")#controling boards
  exit()
try: 
 for i in shotsfile2:
   shots2=i
except NameError:
  print("Player2's moves are not reachable. Please check your inputs.")#controling player2s board
  exit()
shots1 = shots1.split(";")
shots2 = shots2.split(";")
try:
  for line in assignment4_2:
    b = line.split()
    all_lines_2.append(b)
except:
  print("Player2's board is not reachable. Please check your inputs.")
  exit()
try:
 for line in assignment4:
    b= line.split()
    all_lines.append(b)
except:
  print("Player1's board is not reachable. Please check your inputs.")
  exit()
for line in OptionalPlayer1:
    b= line.split()
    all_lines1.append(b)
for line in OptionalPlayer2:
    b= line.split()
    all_lines2.append(b)
def creatinglocations(player,boards,finalboards): #This part is just for the Carrier and the Destroyer beacuse there is only one of them. 
 justnumber = 0
 for line in player:
    count = 0
    for indexs in line[0]:
        if indexs == ";":
            count += 1
        elif indexs=="B" or indexs== "P":
              finalboards[justnumber][count] = indexs
        else:
            boards[justnumber][count] = indexs
    justnumber+=1
creatinglocations(all_lines,myboard,finalboard1)#they are created
creatinglocations(all_lines_2,myboard2,finalboard2)
def creatingbsandps(easyinputs,boards): #for battleships and patrol boats.. i put them into board as B1 B2 and P1 P2 P3 P4. This function is just for putting them into board and prevent some possible errors.
    for line in easyinputs:
      try:
        row = ""
        column = ""
        b = line[0].split(";")
        if not b[0][4]== "0":
         row = int(b[0][3])
         column = b[0][5]
        else:
         row = int(b[0][3:5])
         column = b[0][6]
        if b[0][0] == "B":
            if b[1] == "right":
                a = 0
                while a < 4:
                  if boards[row-1][wordsandnumbers[column]+a-1] == "-":
                    boards[row-1][wordsandnumbers[column]+a-1] = b[0][0:2]
                    a+=1 
                  else:
                    raise AssertionError
            else:
                a = 0
                while a < 4:  
                  if boards[row-1+a][wordsandnumbers[column]-1] == "-":   
                    boards[row-1+a][wordsandnumbers[column]-1] = b[0][0:2]
                    a+=1
                  else:
                    raise AssertionError
        else:
            if b[1] == "right":
                a = 0
                while a < 2:
                  if boards[row-1][wordsandnumbers[column]+a-1] == "-":
                    boards[row-1][wordsandnumbers[column]+a-1] = b[0][0:2]
                    a+=1
                  else:
                    raise AssertionError
            else:
                a = 0
                while a < 2:
                  if boards[row-1+a][wordsandnumbers[column]-1] == "-":
                    boards[row-1+a][wordsandnumbers[column]-1] = b[0][0:2]
                    a+=1
                  else:
                   raise AssertionError
      except AssertionError:
        print("AssertionError: Some ships have common coordinates.")
        output.write("AssertionError: Some ships have common coordinates.")         
creatingbsandps(all_lines1,myboard)
creatingbsandps(all_lines2,myboard2)
def shot(shots,rounds,boards,showingboards,finalboards):      #this function is analyzing the data from txts and changing "-" from the main board and the showing board and also it includes some error preventing.
  try:
   if len(shots[rounds])== 4:
    row = int(shots[rounds][0:2])-1
   elif len(shots[rounds])== 3:
    row = int(shots[rounds][0])-1
   else:
     raise IndexError
   if len(shots[rounds])== 4:
    column = int(wordsandnumbers[str(shots[rounds][3])])-1
   elif len(shots[rounds])== 3:
     column = int(wordsandnumbers[str(shots[rounds][2])])-1
   else:
    raise IndexError
   if boards[row][column] == "-":
    showingboards[row][column] = "O"
    finalboards[row][column] = "O"
   else:
    showingboards[row][column] = "X"
    boards[row][column] = "X"
    finalboards[row][column] = "X"
  except IndexError:
    output.write("IndexError: Some of your moves are not correctly formatted")
    print("IndexError: Some of your moves are not correctly formatted")
    shot(shots,rounds,boards+1,showingboards,finalboards)
  except ValueError:
    output.write("ValueError: There are some distortions in your moves")
    print("ValueError: There are some distortions in your moves")
  except:
    output.write(" kaBOOM: run for your life!”")
    print(" kaBOOM: run for your life!”")
def shipcounter(boards,lists): #number checking of classified ships
  c,d,s,ba,p=0,0,0,{"B1":0,"B2":0},{"P1":0,"P2":0,"P3":0,"P4":0}
  for i in boards:
    for j in i:
      if j == "C":
        c+=1
      if j == "D":
        d+=1
      if j == "S":
        s+=1
      if j == "B1":
          ba["B1"]+=1
      if j == "B2":
          ba["B2"]+=1
      if j == "P1":
          p["P1"]+=1
      if j == "P2":
          p["P2"]+=1
      if j == "P3":
          p["P3"]+=1
      if j == "P4":
          p["P4"]+=1
  wordsc = lists[0].split()
  wordsb = lists[1].split()
  wordsd = lists[2].split()
  wordss = lists[3].split()
  worldsp= lists[4].split()
  if c == 0:
    wordsc[1] = "X"
  if ba["B1"] == 0:
    wordsb[1] = "X"
  if ba["B2"] == 0:
    wordsb[2] = "X"
  if d == 0:
    wordsd[1] = "X"
  if s == 0:
    wordss[1] = "X"
  if p["P1"] == 0:
    worldsp[2] = "X"
  if p["P2"] == 0:
    worldsp[3] = "X"
  if p["P3"] == 0:
    worldsp[4] = "X"
  if p["P4"] == 0:
    worldsp[5] = "X"
  lists[0] = "  ".join(wordsc)
  lists[1] = "  ".join(wordsb)
  lists[2] = "  ".join(wordsd)
  lists[3] = "  ".join(wordss)
  lists[4] = "  ".join(worldsp)
roundnumbers= int(len(shots1)-1)
def printingconstants(roundnumberr,playername):   #printing constants for each round.
  output.write(playername + "'s Move"+ "\n\n"+ "round : " + str(roundnumberr+1) + "	\t\t\t "+ "Grid Size:10x10" +  "\n\n"+ "Player1’s Hidden Board" + "\t"+ "Player2’s Hidden Board" + "\n"+ "  A B C D E F G H I J		  A B C D E F G H I J" + "\n")
  print(playername + "'s Move"+ "\n\n"+ "round : " + str(roundnumberr+1) + "\t "+ "Grid Size:10x10" +  "\n\n"+ "Player1’s Hidden Board" + "\t\t" "Player2’s Hidden Board" + "\n"+ "  A B C D E F G H I J		  A B C D E F G H I J" + "\n")
def printing(boards1,boards2,list1,list2): #while tour process this function provides to print some changes on the board.
  a = 0
  for i in range(10):
    if a<9:
      output.write(str(a+1) + " " + str(" ".join(boards1[a]))+ "\t\t"+ str(a+1) + " " + str(" ".join(boards2[a]))+ "\n")
      print(str(a+1) + " " + str(" ".join(boards1[a]))+ "\t\t"+ str(a+1) + " " + str(" ".join(boards2[a]))+ "\n")
    else:
      output.write(str(a+1) + str(" ".join(boards1[a])) + "\t\t"  + str(a+1) + str(" ".join(boards2[a]))+"\n")
      print((str(a+1) + str(" ".join(boards1[a])) + "\t\t"  + str(a+1) + str(" ".join(boards2[a]))+"\n"))
    a+=1
  for k in range(5):
    output.write("\n" + list1[k] + "\t\t\t" + list2[k])
    print("\n" + list1[k] + "\t\t\t" + list2[k])
def printingconstants1(roundnumber,shots):#second constants
  output.write("\n\n" + "Enter your move: " + str(shots[roundnumber]) + "\n\n")
  print("\n\n" + "Enter your move: " + str(shots[roundnumber]) + "\n\n")
output.write("Battle of Ships Game " + "\n\n")
print("Battle of ships Game " + "\n\n")
for w in range(roundnumbers):# tour process i combined every function i wrote
  printingconstants(w,player1)
  printing(showingboard,showingboard2,listship,list1ship)
  printingconstants1(w,shots1)
  shot(shots1,w,myboard2,showingboard2,finalboard2)
  shipcounter(myboard2,list1ship)
  printingconstants(w,player2)
  printing(showingboard,showingboard2,listship,list1ship)
  printingconstants1(w,shots2)
  shot(shots2,w,myboard,showingboard,finalboard1)
  shipcounter(myboard,listship)
t = 0
y = 0
for theline in listship:# for final case i created a new board if had not done this, final board include some numbers beacuse of what i did to create battleships and patrol boats
  u=theline.split()
  for k in u:
    if k == "-":
      t+=1
if t == 0:
  output.write("Player2 wins!"+ "\n\n" + "final information" +"\n\n" + "Player1's Hidden board" + "\t\t" + "Player2's Hidden board" + "\n"+ "  A B C D E F G H I J		  A B C D E F G H I J" + "\n")
  print("Player2 wins!"+ "\n\n" + "final information" +"\n\n" + "Player1's Hidden board" + "\t\t" + "Player2's Hidden board" + "\n"+ "  A B C D E F G H I J		  A B C D E F G H I J" + "\n")
  printing(finalboard1,finalboard2,listship,list1ship)
for theline1 in list1ship:
  u=theline1.split()
  for k in u:
    if k == "-":
      y+=1
if y == 0:
  output.write("Player1 wins!"+ "\n\n" + "final information" +"\n\n" + "Player1's Hidden board" + "\t\t" + "Player2's Hidden board"+ "\n" + "  A B C D E F G H I J		  A B C D E F G H I J" + "\n")
  print("Player1 wins!"+ "\n\n" + "final information" +"\n\n" + "Player1's Hidden board" + "\t\t" + "Player2's Hidden board" + "\n"+ "  A B C D E F G H I J		  A B C D E F G H I J" + "\n")
  printing(finalboard1,finalboard2,listship,list1ship)














      

      
      


    
          

