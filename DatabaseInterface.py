import pymongo

"""
Program Description: CLI Application to read/write/query data from MongoDB database.
Version: 0.0.1
Last Modified: 3/29/2024
"""

def display_choices():
    print("*** Mongo Database Interface ***")
    print("0) Quit")
    print("1) New Entry")
    print("2) Edit Existing Entry")
    print(">>> ",end="")

def main():        
    choice = -1
    DB_USER = ""
    DB_PASS = ""
    DB_HOST = ""
    DB_NAME = ""
    
    myclient = ""
    mydb = ""


    with open ("config.txt", 'r') as file:
        delim = "="
        def getValue(s):
            value = s[s.index(delim)+1:]
            value = value.strip()
            return value
        for line in file:
            if line.startswith("DB_USER"):
                DB_USER = getValue(line)
            elif line.startswith("DB_PASS"):
                DB_PASS = getValue(line)
            elif line.startswith("DB_HOST"):
                DB_HOST = getValue(line)
            elif line.startswith("DB_NAME"):
                DB_NAME = getValue(line)
    
    print("Attempting connection to Mongo database `@%s`..." % (DB_HOST))
    
    while (True):
        print("*** Authentication (Defaults stored in config.txt)***")
        print("Username: ", end="")
        DB_USER = input() or DB_USER
        print("Password: ", end="")
        DB_PASS = input() or DB_PASS
        
        try:
            myclient = pymongo.MongoClient("mongodb://%s:%s@%s/" % (DB_USER, DB_PASS, DB_HOST))

            myclient.list_database_names() # Will error if not authenticated.
            print("Successfully connected to `mongodb://%s:%s@%s/`.\n" % (DB_USER, DB_PASS, DB_HOST))
            
            print(myclient.list_database_names())
            
            print("Select a database: ", end="")
            DB_NAME = input() or DB_NAME
            
            mydb = myclient[DB_NAME]
            
            print("Successfully connected to `mongodb://%s:%s@%s/%s`.\n" % (DB_USER, DB_PASS, DB_HOST, DB_NAME))
            break
        except:
            print("Failed to authenticate `mongodb://%s:%s@%s/`." % (DB_USER, DB_PASS, DB_HOST) + " Please try again.\n")


    while (choice != '0' or choice != 'q'):
        display_choices()
        try:
            choice = input().lower()

            if (choice == '0' or choice == 'q'):
                break

            elif (choice == '1'):
                print("Chose 1 (TEMP)")
                
            elif (choice == '2'):
                print("Chose 2 (TEMP)")

            else:
                print("Unknown command. Please try again.\n")
                continue
  
        except:
            print("Invalid command. Please try again.\n")
            continue

if __name__ == "__main__":
    main()
