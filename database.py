import pyodbc
import os
import datetime

#The block of code from lines 6-12 is what's needed to get the python program connected to the access database. 
dbpath = rf"{os.getcwd()}\LogDatabase.accdb"
cnn_string = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf'DBQ={dbpath};'
)
cnn = pyodbc.connect(cnn_string)
cursor = cnn.cursor()


#currentShift checks the current time and returns which shift it is to multiple pieces of the program. 
def currentShift(): 
    now = datetime.datetime.now()
    if ((now.hour >= 7) and (now.hour < 15)):
        return "1"
    elif ((now.hour >= 15) and (now.hour < 23)):
        return "2"
    else:
        return "3"


#Explaining dbLogic - This function checks the current shift from currentShift, first and second shift are fine and won't be affected.
#However 3rd shift passes into the next day so you can't simply tell the SQL statement to only grab the current day or 3rd shift will
#lose all of it's entries up until that point an hour into the shift. 
def dbLogic(): 
    if (currentShift() == '1') or (currentShift() == '2'):
        return f'''SELECT * FROM SHIFT{currentShift()} where backendDate = date() ORDER by backendDate DESC, Loggedtime DESC'''
    elif currentShift() == '3':
        currentHour = datetime.datetime.now().hour
        if (currentHour >=23):
            return f'''SELECT * FROM SHIFT{currentShift()} where backendDate = date() ORDER by backendDate DESC, LoggedTime DESC'''
        else: #This should only fire on third shift after 12AM.
            return f'''SELECT * FROM SHIFT{currentShift()} WHERE backendDate >= date()-1 ORDER by backendDate DESC, Loggedtime DESC'''
    else: #This else shouldn't fire unless something is really wrong. 
        print('Something is really broken.')


#Needed a snidbit of code to just give the current time and date for the data entry.
def currentTime(arg): # 1 for time, 2 for date.
    now = datetime.datetime.now()
    if arg == 1:
        return now.strftime('%H:%M:%S')
    elif arg == 2:
        return now.strftime('%m/%d/%Y')
    else:
        print('Incorrect Arg, pass date or time.')
