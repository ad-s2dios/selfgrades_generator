#######################################################
#                                                     #
#           Created by Adriel Tan ad-s2dios           #
#                                                     #
#  https://github.com/ad-s2dios/selfgrades_generator  #
#                                                     #
#######################################################

#########################
#                       #
#  User Customizations  #
#                       #
#########################
enable_help_text = True
name = ""
email = ""
sid = ""



# Static variable and helper function setup
alphs = "abcdefghijklmnopqrstuvwxyz"

def printline():
    print("-" * 30)

def finish(f=None):
    if f != None:
        f.close()
    exit()



# Welcome Header
printline()
print("\nSELF GRADE GENERATOR\n")
printline()



# Question information entry
qns = input("Total no of qns: ")

try:
    qns = int(qns)
except:
    print("Please enter an integer")
    finish()

parts = [input("Largest part in qn " + str(i + 1) + ": ") for i in range(qns)]

try:
    for i in range(qns):
        parts[i] = parts[i].lower()
        if parts[i] not in alphs:
            raise Exception
except:
    print("Please enter an alphabet a-z")
    finish()



# Help text
if enable_help_text:
    printline()
    print("HELP")
    printline()
    print("If you got a 10, just hit enter")
    print("Else enter 0, 2, 5, or 8, space, and a text reason (optional)")
    print("For example")
    print("1a: 0 dog ate my homework")
    print("1b: ")
    print("1c: 2")
    input("Hit enter to continue...")



# Open file and write to it
f = open("self_grades.json", "w")
f.write("{")

qn_ids = ""
printline()

for i in range(qns):
    for p in range(alphs.index(parts[i]) + 1):
        qn_id = str(i + 1) + alphs[p]
        qn_ids += '"' + qn_id + '",'
        data = input(qn_id + ": ")
        f.write('"' + qn_id + '":"')
        if len(data) == 0:
            f.write('10","' + qn_id + '_text":"",')
        else:
            try:
                int(data[0])
                f.write(data[0] + '","' + qn_id + '_text":"' + data[2:] + '",')
            except:
                printline()
                print("Please follow the prescribed format")
                finish(f)

printline()
printline_after = False

f.write('"name":"')
if len(name) == 0:
    f.write(input("Name: "))
    printline_after = True
else:
    f.write(name)

f.write('","email":"')
if len(email) == 0:
    f.write(input("Email: "))
    printline_after = True
else:
    f.write(email)

f.write('","sid":"')
if len(sid) == 0:
    f.write(input("SID: "))
    printline_after = True
else:
    f.write(sid)

f.write('","question_ids":[' + qn_ids[:-1] + ']}')
f.close()



# Done!
if printline_after:
    printline()
print("self_grades.json successfully written!")
print("created by ad-s2dios\n")