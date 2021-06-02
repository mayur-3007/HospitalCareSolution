
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# creating a class Hospital with pass as syntactical statement so code would not throw error
class Hospital:
    pass

# creating class Equipments with only dictionary consiting of fixed key - values pairs
class Equipments:
    equip = {
        "flat beds":80,
        "recliner beds":100,
        "ventilator":16,
        "oxygen cylinder":110,
        "normal masks":200,
        "non rebreather masks":120
    }


# Inherting above two classes Hospital and Equipments in class Rooms
class Rooms(Hospital,Equipments):
    # Assigning fixed values to different types of rooms 
    NormalRooms = 50
    OxygenRooms = 50
    ICU = 20

    # initializing the attributes when object is called
    def __init__(self,room_name,equip = {}):
        self.equip = super().equip
        self.room_name = room_name

    # method used for user interaction
    def while_call(self):
        select = ["Normal Room","Oxygen Room","ICU Room","Exit"]
        while True:
            a = ""
            a = int(input("\nPlease Enter the type of room you want to reserve: \n1.Normal Room \n2.Oxygen Room \n3.ICU Room \n4.Exit \n\n"))
            if(select[a-1] == "Normal Room" or select[a-1] == "Oxygen Room" or select[a-1] == "ICU Room"):
                self.room_name = select[a-1]
                self.valuate(self.room_name)
                x = input("\n%sDo you wish to continue y or n: %s"%(bcolors.OKCYAN,bcolors.ENDC))
                if(x == "n" or x != "y"):
                    break
            elif(select[a-1] == "Exit"):
                print("\n%sThank you for using the service%s"%(bcolors.OKBLUE,bcolors.ENDC))
                break

    def remaining_available(self):
        print("""\n%sRemaining availability:\nNormal Rooms: %s\nOxygen Rooms: %s\nICU: %s %s""" %(bcolors.WARNING,self.NormalRooms,self.OxygenRooms,self.ICU,bcolors.ENDC))

    # evaluating the availablity of the room depending on the equipements required by each room
    def valuate(self,room_name):
        if(self.room_name == "Normal Room"):
            if(self.equip["flat beds"] >= 1 and self.equip["normal masks"] >= 2 and self.NormalRooms > 0):
                self.equip["flat beds"] -= 1
                self.equip["normal masks"] -= 2
                self.NormalRooms -= 1
                print("""%s01 %s(with 1 flat bed + 2 normal masks) reserved%s"""%(bcolors.OKGREEN,self.room_name,bcolors.ENDC))
                self.remaining_available()
            else:
                print("%s-- Sorry, no room could be reserved.%s"%(bcolors.HEADER,bcolors.ENDC))
                self.remaining_available()

        elif(self.room_name == "Oxygen Room"):
            if(self.equip["oxygen cylinder"] >= 2 and self.equip["recliner beds"] >= 1 and self.equip["non rebreather masks"] >= 2 and self.OxygenRooms > 0):
                self.equip["oxygen cylinder"] -= 2
                self.equip["recliner beds"] -= 1
                self.equip["non rebreather masks"] -= 2
                self.OxygenRooms -= 1
                print("""%s01 %s(2 oxygen cylinder + 1 recliner bed + 2 non rebreather masks) reserved.%s"""%(bcolors.OKGREEN,self.room_name,bcolors.ENDC))
                self.remaining_available()
            else:
                print("%s-- Sorry, no room could be reserved.%s"%(bcolors.HEADER,bcolors.ENDC))
                self.remaining_available()
        
        elif(self.room_name == "ICU Room"):
            if(self.equip["oxygen cylinder"] >= 1 and self.equip["ventilator"] >= 1 and self.equip["recliner beds"] >= 1 and self.ICU > 0):
                self.equip["oxygen cylinder"] -= 1
                self.equip["recliner beds"] -= 1
                self.equip["ventilator"] -= 1
                self.ICU -= 1
                print("""%s01 %s(with 1 ventilator + 1 oxygen cylinder + 1 recliner bed) reserved.%s"""%(bcolors.OKGREEN,self.room_name,bcolors.ENDC))
                self.remaining_available()
            else:
                print("%s-- Sorry, no room could be reserved.%s"%(bcolors.HEADER,bcolors.ENDC))
                self.remaining_available()
        else:
            print("%s-- Sorry, no room could be reserved.%s"%(bcolors.HEADER,bcolors.ENDC))
            self.remaining_available()


def main():
    x = Rooms("Normal Room")
    x.while_call()

# special variable which is defined when python file is executed
if __name__=="__main__":
    main()
