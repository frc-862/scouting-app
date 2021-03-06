'''
Create to Database
'''

Red1 = "IRScout_Red1.csv"
Red2 = "IRScout_Red2.csv"
Red3 = "IRScout_Red3.csv"
Blue1 = "IRScout_Blue1.csv"
Blue2 = "IRScout_Blue2.csv"
Blue3 = "IRScout_Blue3.csv"


import json
import csv
import math

def TryFile(fileName, station):
    try:
        open(fileName, "r")
        return 1
    except IOError:
        print("[ERROR] " + station + "'s Specified File Doesn't Exist!")
        return 0

finaloutput = open("LightningDatabaseOutput.csv", "w")
dataout = "Team Number,Team Name,Match Number,Comp ID,Scout Name,Initiation Line,(A) Lower PC,(A) Outer PC,(A) Inner PC,(A) Missed PC,(A) Made/Shot PC,(A) Points,(T) Lower PC,(T) Outer PC,(T) Inner PC,(T) Missed PC,(T) Made:Shot PC,(T) Cycles,(T) Shot/Cycle PC,(T) Scored/Cycle,(T) Control Panel Rotation,(T) Control Panel Position,(T) Points,(E) Parked,(E) Attemped Climb,(E) Successful Climb,(E) Balanced Climb,(G) Robot Disabled,(E) Points, TOTAL SCORE\n"
numfilesaccessed = 0
if(TryFile(Red1, "Red1")!= 0):
    numfilesaccessed += 1
    with open(Red1) as thistoread:
        dataarray = []
        csv_reader = csv.reader(thistoread, delimiter=",")
        #READABLE FORMAT
        for csvconvert in csv_reader:
            dataarray.append(csvconvert)
        numberofmatches = 0
        for num in dataarray:
            numberofmatches += 1
        numberofmatches -= 1
        #ACCOUNTING FOR # OF MATCHES
        numberofmatches = math.floor(numberofmatches / 20)
        #DATASTRING OUTPUT
        for y in range(0,numberofmatches):
            #TEAM DATA
            print("[ENTRY] Team "+str(dataarray[2+(y*20)][1]))
            dataout = dataout + (dataarray[2+(y*20)][1]) + ","
            dataout = dataout + (dataarray[1+(y*20)][1]) + ","
            dataout = dataout + (dataarray[4+(y*20)][1]) + ","
            dataout = dataout + (dataarray[3+(y*20)][1]) + ","
            dataout = dataout + (dataarray[6+(y*20)][1]) + ","
            #AUTON DATA
            dataout = dataout + (dataarray[7+(y*20)][1]) + ","
            alower = int(dataarray[8+(y*20)][1])
            aouter = int(dataarray[9+(y*20)][1])
            ainner = int(dataarray[10+(y*20)][1])
            amissed = int(dataarray[11+(y*20)][1])
            dataout = dataout + str(alower) + "," + str(aouter) + "," + str(ainner) + "," + str(amissed) + ","
            dataout = dataout + str(((alower + aouter + ainner)/(alower+aouter+ainner+amissed if (alower+aouter+ainner+amissed) > 0 else 1))*100) + "%,"
            autonpoints = (alower*2)+(aouter*4)+(ainner*6)+(int(dataarray[7+(y*20)][1])*5)
            dataout = dataout + str(autonpoints) + ","
            #TELEOP DATA
            tlower = 0
            touter = 0
            tinner = 0
            tmissed = 0
            cycles = 0
            for tln in range(0,22):
                if(tln > 1):
                    tlower += int(dataarray[8+(y*20)][tln]) 
            for ton in range(0,22):
                if(ton > 1):
                    touter += int(dataarray[9+(y*20)][ton])
            for tin in range(0,22):
                if(tin > 1):
                    tinner += int(dataarray[10+(y*20)][tin])
            for tmn in range(0,22):
                if(tmn > 1):
                    tmissed += int(dataarray[11+(y*20)][tmn])
            for tcn in range(0,22):
                if(tcn > 1):
                    cycles += int(dataarray[12+(y*20)][tcn])
            dataout = dataout + str(tlower) + "," + str(touter) + "," + str(tinner) + "," + str(tmissed) + ","
            dataout = dataout + str(((tlower + touter + tinner)/(tlower+touter+tinner+tmissed if (tlower+touter+tinner+tmissed) > 0 else 1))*100) + "%,"
            dataout = dataout + str(cycles) + ","
            dataout = dataout + str(((tlower + touter + tinner + tmissed)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(((tlower + touter + tinner)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(dataarray[13+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[14+(y*20)][1]) + ","
            teleoppoints = (tlower)+(touter*2)+(tinner*3)+(int(dataarray[13+(y*20)][1])*10)+(int(dataarray[14+(y*20)][1])*20)
            dataout = dataout + str(teleoppoints) + ","
            #ENDGAME DATA
            dataout = dataout + str(dataarray[15+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[16+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[17+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[18+(y*20)][1]) + ","
            #ROBOT DISABLED
            dataout = dataout + str(dataarray[19+(y*20)][1]) + ","
            #BACK TO ENDGAME
            endgamepoints = (int(dataarray[15+(y*20)][1])*5)+(int(dataarray[17+(y*20)][1])*25)+(int(dataarray[18+(y*20)][1])*15)
            dataout = dataout + str(endgamepoints) + ","
            dataout = dataout + str(autonpoints + teleoppoints + endgamepoints) + "\n"
if(TryFile(Red2, "Red2")!= 0):
    numfilesaccessed += 1
    with open(Red2) as thistoread:
        dataarray = []
        csv_reader = csv.reader(thistoread, delimiter=",")
        #READABLE FORMAT
        for csvconvert in csv_reader:
            dataarray.append(csvconvert)
        numberofmatches = 0
        for num in dataarray:
            numberofmatches += 1
        numberofmatches -= 1
        #ACCOUNTING FOR # OF MATCHES
        numberofmatches = math.floor(numberofmatches / 20)
        #DATASTRING OUTPUT
        for y in range(0,numberofmatches):
            #TEAM DATA
            print("[ENTRY] Team "+str(dataarray[2+(y*20)][1]))
            dataout = dataout + (dataarray[2+(y*20)][1]) + ","
            dataout = dataout + (dataarray[1+(y*20)][1]) + ","
            dataout = dataout + (dataarray[4+(y*20)][1]) + ","
            dataout = dataout + (dataarray[3+(y*20)][1]) + ","
            dataout = dataout + (dataarray[6+(y*20)][1]) + ","
            #AUTON DATA
            dataout = dataout + (dataarray[7+(y*20)][1]) + ","
            alower = int(dataarray[8+(y*20)][1])
            aouter = int(dataarray[9+(y*20)][1])
            ainner = int(dataarray[10+(y*20)][1])
            amissed = int(dataarray[11+(y*20)][1])
            dataout = dataout + str(alower) + "," + str(aouter) + "," + str(ainner) + "," + str(amissed) + ","
            dataout = dataout + str(((alower + aouter + ainner)/(alower+aouter+ainner+amissed if (alower+aouter+ainner+amissed) > 0 else 1))*100) + "%,"
            autonpoints = (alower*2)+(aouter*4)+(ainner*6)+(int(dataarray[7+(y*20)][1])*5)
            dataout = dataout + str(autonpoints) + ","
            #TELEOP DATA
            tlower = 0
            touter = 0
            tinner = 0
            tmissed = 0
            cycles = 0
            for tln in range(0,22):
                if(tln > 1):
                    tlower += int(dataarray[8+(y*20)][tln]) 
            for ton in range(0,22):
                if(ton > 1):
                    touter += int(dataarray[9+(y*20)][ton])
            for tin in range(0,22):
                if(tin > 1):
                    tinner += int(dataarray[10+(y*20)][tin])
            for tmn in range(0,22):
                if(tmn > 1):
                    tmissed += int(dataarray[11+(y*20)][tmn])
            for tcn in range(0,22):
                if(tcn > 1):
                    cycles += int(dataarray[12+(y*20)][tcn])
            dataout = dataout + str(tlower) + "," + str(touter) + "," + str(tinner) + "," + str(tmissed) + ","
            dataout = dataout + str(((tlower + touter + tinner)/(tlower+touter+tinner+tmissed if (tlower+touter+tinner+tmissed) > 0 else 1))*100) + "%,"
            dataout = dataout + str(cycles) + ","
            dataout = dataout + str(((tlower + touter + tinner + tmissed)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(((tlower + touter + tinner)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(dataarray[13+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[14+(y*20)][1]) + ","
            teleoppoints = (tlower)+(touter*2)+(tinner*3)+(int(dataarray[13+(y*20)][1])*10)+(int(dataarray[14+(y*20)][1])*20)
            dataout = dataout + str(teleoppoints) + ","
            #ENDGAME DATA
            dataout = dataout + str(dataarray[15+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[16+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[17+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[18+(y*20)][1]) + ","
            #ROBOT DISABLED
            dataout = dataout + str(dataarray[19+(y*20)][1]) + ","
            #BACK TO ENDGAME
            endgamepoints = (int(dataarray[15+(y*20)][1])*5)+(int(dataarray[17+(y*20)][1])*25)+(int(dataarray[18+(y*20)][1])*15)
            dataout = dataout + str(endgamepoints) + ","
            dataout = dataout + str(autonpoints + teleoppoints + endgamepoints) + "\n"
if(TryFile(Red3, "Red3")!= 0):
    numfilesaccessed += 1
    with open(Red3) as thistoread:
        dataarray = []
        csv_reader = csv.reader(thistoread, delimiter=",")
        #READABLE FORMAT
        for csvconvert in csv_reader:
            dataarray.append(csvconvert)
        numberofmatches = 0
        for num in dataarray:
            numberofmatches += 1
        numberofmatches -= 1
        #ACCOUNTING FOR # OF MATCHES
        numberofmatches = math.floor(numberofmatches / 20)
        #DATASTRING OUTPUT
        for y in range(0,numberofmatches):
            #TEAM DATA
            print("[ENTRY] Team "+str(dataarray[2+(y*20)][1]))
            dataout = dataout + (dataarray[2+(y*20)][1]) + ","
            dataout = dataout + (dataarray[1+(y*20)][1]) + ","
            dataout = dataout + (dataarray[4+(y*20)][1]) + ","
            dataout = dataout + (dataarray[3+(y*20)][1]) + ","
            dataout = dataout + (dataarray[6+(y*20)][1]) + ","
            #AUTON DATA
            dataout = dataout + (dataarray[7+(y*20)][1]) + ","
            alower = int(dataarray[8+(y*20)][1])
            aouter = int(dataarray[9+(y*20)][1])
            ainner = int(dataarray[10+(y*20)][1])
            amissed = int(dataarray[11+(y*20)][1])
            dataout = dataout + str(alower) + "," + str(aouter) + "," + str(ainner) + "," + str(amissed) + ","
            dataout = dataout + str(((alower + aouter + ainner)/(alower+aouter+ainner+amissed if (alower+aouter+ainner+amissed) > 0 else 1))*100) + "%,"
            autonpoints = (alower*2)+(aouter*4)+(ainner*6)+(int(dataarray[7+(y*20)][1])*5)
            dataout = dataout + str(autonpoints) + ","
            #TELEOP DATA
            tlower = 0
            touter = 0
            tinner = 0
            tmissed = 0
            cycles = 0
            for tln in range(0,22):
                if(tln > 1):
                    tlower += int(dataarray[8+(y*20)][tln]) 
            for ton in range(0,22):
                if(ton > 1):
                    touter += int(dataarray[9+(y*20)][ton])
            for tin in range(0,22):
                if(tin > 1):
                    tinner += int(dataarray[10+(y*20)][tin])
            for tmn in range(0,22):
                if(tmn > 1):
                    tmissed += int(dataarray[11+(y*20)][tmn])
            for tcn in range(0,22):
                if(tcn > 1):
                    cycles += int(dataarray[12+(y*20)][tcn])
            dataout = dataout + str(tlower) + "," + str(touter) + "," + str(tinner) + "," + str(tmissed) + ","
            dataout = dataout + str(((tlower + touter + tinner)/(tlower+touter+tinner+tmissed if (tlower+touter+tinner+tmissed) > 0 else 1))*100) + "%,"
            dataout = dataout + str(cycles) + ","
            dataout = dataout + str(((tlower + touter + tinner + tmissed)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(((tlower + touter + tinner)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(dataarray[13+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[14+(y*20)][1]) + ","
            teleoppoints = (tlower)+(touter*2)+(tinner*3)+(int(dataarray[13+(y*20)][1])*10)+(int(dataarray[14+(y*20)][1])*20)
            dataout = dataout + str(teleoppoints) + ","
            #ENDGAME DATA
            dataout = dataout + str(dataarray[15+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[16+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[17+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[18+(y*20)][1]) + ","
            #ROBOT DISABLED
            dataout = dataout + str(dataarray[19+(y*20)][1]) + ","
            #BACK TO ENDGAME
            endgamepoints = (int(dataarray[15+(y*20)][1])*5)+(int(dataarray[17+(y*20)][1])*25)+(int(dataarray[18+(y*20)][1])*15)
            dataout = dataout + str(endgamepoints) + ","
            dataout = dataout + str(autonpoints + teleoppoints + endgamepoints) + "\n"
if(TryFile(Blue1, "Blue1")!= 0):
    numfilesaccessed += 1
    with open(Blue1) as thistoread:
        dataarray = []
        csv_reader = csv.reader(thistoread, delimiter=",")
        #READABLE FORMAT
        for csvconvert in csv_reader:
            dataarray.append(csvconvert)
        numberofmatches = 0
        for num in dataarray:
            numberofmatches += 1
        numberofmatches -= 1
        #ACCOUNTING FOR # OF MATCHES
        numberofmatches = math.floor(numberofmatches / 20)
        #DATASTRING OUTPUT
        for y in range(0,numberofmatches):
            #TEAM DATA
            print("[ENTRY] Team "+str(dataarray[2+(y*20)][1]))
            dataout = dataout + (dataarray[2+(y*20)][1]) + ","
            dataout = dataout + (dataarray[1+(y*20)][1]) + ","
            dataout = dataout + (dataarray[4+(y*20)][1]) + ","
            dataout = dataout + (dataarray[3+(y*20)][1]) + ","
            dataout = dataout + (dataarray[6+(y*20)][1]) + ","
            #AUTON DATA
            dataout = dataout + (dataarray[7+(y*20)][1]) + ","
            alower = int(dataarray[8+(y*20)][1])
            aouter = int(dataarray[9+(y*20)][1])
            ainner = int(dataarray[10+(y*20)][1])
            amissed = int(dataarray[11+(y*20)][1])
            dataout = dataout + str(alower) + "," + str(aouter) + "," + str(ainner) + "," + str(amissed) + ","
            dataout = dataout + str(((alower + aouter + ainner)/(alower+aouter+ainner+amissed if (alower+aouter+ainner+amissed) > 0 else 1))*100) + "%,"
            autonpoints = (alower*2)+(aouter*4)+(ainner*6)+(int(dataarray[7+(y*20)][1])*5)
            dataout = dataout + str(autonpoints) + ","
            #TELEOP DATA
            tlower = 0
            touter = 0
            tinner = 0
            tmissed = 0
            cycles = 0
            for tln in range(0,22):
                if(tln > 1):
                    tlower += int(dataarray[8+(y*20)][tln]) 
            for ton in range(0,22):
                if(ton > 1):
                    touter += int(dataarray[9+(y*20)][ton])
            for tin in range(0,22):
                if(tin > 1):
                    tinner += int(dataarray[10+(y*20)][tin])
            for tmn in range(0,22):
                if(tmn > 1):
                    tmissed += int(dataarray[11+(y*20)][tmn])
            for tcn in range(0,22):
                if(tcn > 1):
                    cycles += int(dataarray[12+(y*20)][tcn])
            dataout = dataout + str(tlower) + "," + str(touter) + "," + str(tinner) + "," + str(tmissed) + ","
            dataout = dataout + str(((tlower + touter + tinner)/(tlower+touter+tinner+tmissed if (tlower+touter+tinner+tmissed) > 0 else 1))*100) + "%,"
            dataout = dataout + str(cycles) + ","
            dataout = dataout + str(((tlower + touter + tinner + tmissed)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(((tlower + touter + tinner)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(dataarray[13+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[14+(y*20)][1]) + ","
            teleoppoints = (tlower)+(touter*2)+(tinner*3)+(int(dataarray[13+(y*20)][1])*10)+(int(dataarray[14+(y*20)][1])*20)
            dataout = dataout + str(teleoppoints) + ","
            #ENDGAME DATA
            dataout = dataout + str(dataarray[15+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[16+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[17+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[18+(y*20)][1]) + ","
            #ROBOT DISABLED
            dataout = dataout + str(dataarray[19+(y*20)][1]) + ","
            #BACK TO ENDGAME
            endgamepoints = (int(dataarray[15+(y*20)][1])*5)+(int(dataarray[17+(y*20)][1])*25)+(int(dataarray[18+(y*20)][1])*15)
            dataout = dataout + str(endgamepoints) + ","
            dataout = dataout + str(autonpoints + teleoppoints + endgamepoints) + "\n"
if(TryFile(Blue2, "Blue2")!= 0):
    numfilesaccessed += 1
    with open(Blue2) as thistoread:
        dataarray = []
        csv_reader = csv.reader(thistoread, delimiter=",")
        #READABLE FORMAT
        for csvconvert in csv_reader:
            dataarray.append(csvconvert)
        numberofmatches = 0
        for num in dataarray:
            numberofmatches += 1
        numberofmatches -= 1
        #ACCOUNTING FOR # OF MATCHES
        numberofmatches = math.floor(numberofmatches / 20)
        #DATASTRING OUTPUT
        for y in range(0,numberofmatches):
            #TEAM DATA
            print("[ENTRY] Team "+str(dataarray[2+(y*20)][1]))
            dataout = dataout + (dataarray[2+(y*20)][1]) + ","
            dataout = dataout + (dataarray[1+(y*20)][1]) + ","
            dataout = dataout + (dataarray[4+(y*20)][1]) + ","
            dataout = dataout + (dataarray[3+(y*20)][1]) + ","
            dataout = dataout + (dataarray[6+(y*20)][1]) + ","
            #AUTON DATA
            dataout = dataout + (dataarray[7+(y*20)][1]) + ","
            alower = int(dataarray[8+(y*20)][1])
            aouter = int(dataarray[9+(y*20)][1])
            ainner = int(dataarray[10+(y*20)][1])
            amissed = int(dataarray[11+(y*20)][1])
            dataout = dataout + str(alower) + "," + str(aouter) + "," + str(ainner) + "," + str(amissed) + ","
            dataout = dataout + str(((alower + aouter + ainner)/(alower+aouter+ainner+amissed if (alower+aouter+ainner+amissed) > 0 else 1))*100) + "%,"
            autonpoints = (alower*2)+(aouter*4)+(ainner*6)+(int(dataarray[7+(y*20)][1])*5)
            dataout = dataout + str(autonpoints) + ","
            #TELEOP DATA
            tlower = 0
            touter = 0
            tinner = 0
            tmissed = 0
            cycles = 0
            for tln in range(0,22):
                if(tln > 1):
                    tlower += int(dataarray[8+(y*20)][tln]) 
            for ton in range(0,22):
                if(ton > 1):
                    touter += int(dataarray[9+(y*20)][ton])
            for tin in range(0,22):
                if(tin > 1):
                    tinner += int(dataarray[10+(y*20)][tin])
            for tmn in range(0,22):
                if(tmn > 1):
                    tmissed += int(dataarray[11+(y*20)][tmn])
            for tcn in range(0,22):
                if(tcn > 1):
                    cycles += int(dataarray[12+(y*20)][tcn])
            dataout = dataout + str(tlower) + "," + str(touter) + "," + str(tinner) + "," + str(tmissed) + ","
            dataout = dataout + str(((tlower + touter + tinner)/(tlower+touter+tinner+tmissed if (tlower+touter+tinner+tmissed) > 0 else 1))*100) + "%,"
            dataout = dataout + str(cycles) + ","
            dataout = dataout + str(((tlower + touter + tinner + tmissed)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(((tlower + touter + tinner)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(dataarray[13+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[14+(y*20)][1]) + ","
            teleoppoints = (tlower)+(touter*2)+(tinner*3)+(int(dataarray[13+(y*20)][1])*10)+(int(dataarray[14+(y*20)][1])*20)
            dataout = dataout + str(teleoppoints) + ","
            #ENDGAME DATA
            dataout = dataout + str(dataarray[15+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[16+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[17+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[18+(y*20)][1]) + ","
            #ROBOT DISABLED
            dataout = dataout + str(dataarray[19+(y*20)][1]) + ","
            #BACK TO ENDGAME
            endgamepoints = (int(dataarray[15+(y*20)][1])*5)+(int(dataarray[17+(y*20)][1])*25)+(int(dataarray[18+(y*20)][1])*15)
            dataout = dataout + str(endgamepoints) + ","
            dataout = dataout + str(autonpoints + teleoppoints + endgamepoints) + "\n"
if(TryFile(Blue3, "Blue3")!= 0):
    numfilesaccessed += 1
    with open(Blue3) as thistoread:
        dataarray = []
        csv_reader = csv.reader(thistoread, delimiter=",")
        #READABLE FORMAT
        for csvconvert in csv_reader:
            dataarray.append(csvconvert)
        numberofmatches = 0
        for num in dataarray:
            numberofmatches += 1
        numberofmatches -= 1
        #ACCOUNTING FOR # OF MATCHES
        numberofmatches = math.floor(numberofmatches / 20)
        #DATASTRING OUTPUT
        for y in range(0,numberofmatches):
            #TEAM DATA
            print("[ENTRY] Team "+str(dataarray[2+(y*20)][1]))
            dataout = dataout + (dataarray[2+(y*20)][1]) + ","
            dataout = dataout + (dataarray[1+(y*20)][1]) + ","
            dataout = dataout + (dataarray[4+(y*20)][1]) + ","
            dataout = dataout + (dataarray[3+(y*20)][1]) + ","
            dataout = dataout + (dataarray[6+(y*20)][1]) + ","
            #AUTON DATA
            dataout = dataout + (dataarray[7+(y*20)][1]) + ","
            alower = int(dataarray[8+(y*20)][1])
            aouter = int(dataarray[9+(y*20)][1])
            ainner = int(dataarray[10+(y*20)][1])
            amissed = int(dataarray[11+(y*20)][1])
            dataout = dataout + str(alower) + "," + str(aouter) + "," + str(ainner) + "," + str(amissed) + ","
            dataout = dataout + str(((alower + aouter + ainner)/(alower+aouter+ainner+amissed if (alower+aouter+ainner+amissed) > 0 else 1))*100) + "%,"
            autonpoints = (alower*2)+(aouter*4)+(ainner*6)+(int(dataarray[7+(y*20)][1])*5)
            dataout = dataout + str(autonpoints) + ","
            #TELEOP DATA
            tlower = 0
            touter = 0
            tinner = 0
            tmissed = 0
            cycles = 0
            for tln in range(0,22):
                if(tln > 1):
                    tlower += int(dataarray[8+(y*20)][tln]) 
            for ton in range(0,22):
                if(ton > 1):
                    touter += int(dataarray[9+(y*20)][ton])
            for tin in range(0,22):
                if(tin > 1):
                    tinner += int(dataarray[10+(y*20)][tin])
            for tmn in range(0,22):
                if(tmn > 1):
                    tmissed += int(dataarray[11+(y*20)][tmn])
            for tcn in range(0,22):
                if(tcn > 1):
                    cycles += int(dataarray[12+(y*20)][tcn])
            dataout = dataout + str(tlower) + "," + str(touter) + "," + str(tinner) + "," + str(tmissed) + ","
            dataout = dataout + str(((tlower + touter + tinner)/(tlower+touter+tinner+tmissed if (tlower+touter+tinner+tmissed) > 0 else 1))*100) + "%,"
            dataout = dataout + str(cycles) + ","
            dataout = dataout + str(((tlower + touter + tinner + tmissed)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(((tlower + touter + tinner)/cycles if cycles > 0 else 1)) +","
            dataout = dataout + str(dataarray[13+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[14+(y*20)][1]) + ","
            teleoppoints = (tlower)+(touter*2)+(tinner*3)+(int(dataarray[13+(y*20)][1])*10)+(int(dataarray[14+(y*20)][1])*20)
            dataout = dataout + str(teleoppoints) + ","
            #ENDGAME DATA
            dataout = dataout + str(dataarray[15+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[16+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[17+(y*20)][1]) + ","
            dataout = dataout + str(dataarray[18+(y*20)][1]) + ","
            #ROBOT DISABLED
            dataout = dataout + str(dataarray[19+(y*20)][1]) + ","
            #BACK TO ENDGAME
            endgamepoints = (int(dataarray[15+(y*20)][1])*5)+(int(dataarray[17+(y*20)][1])*25)+(int(dataarray[18+(y*20)][1])*15)
            dataout = dataout + str(endgamepoints) + ","
            dataout = dataout + str(autonpoints + teleoppoints + endgamepoints) + "\n"
print("----------------\n[FINAL] " + str(numfilesaccessed) + " out of 6 files successfully accessed (" + str(math.ceil((numfilesaccessed/6)*100)) + "%)")
finaloutput.write(dataout)