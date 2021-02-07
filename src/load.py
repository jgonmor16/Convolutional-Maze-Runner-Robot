####################################################################
# Load Data Function
####################################################################

def load(loc):
    file = open("/var/www/html/config/proj/" + loc)
    cont = file.read()
    file.close()

    return cont

def write(loc,cont):
    file = open("/var/www/html/config/proj/" + loc, 'w')
    file.write(str(cont))
    file.close()

def imp(cont, on):
    if (cont == "f"):
        print("Moving Forward")
    elif (cont == "s"):
        print("Stopping")
    elif (cont == "l"):
        print("Turning Left")
    elif (cont == "r"):
        print("Turning Right")
    elif (cont == "b"):
        print("Moving Backwards")
    elif (cont == "0"):
        print ("MANUAL Mode selected")
    elif (cont == "1"):
        print("AUTO Mode selected")
    elif (on == "0"):
        print("Current status: OFF")
    elif (on == "1"):
        print("Current status: ON")

def decorate(cont):
    print("==================================================================")
    print("= " + cont)
    print("==================================================================")

def superdecorate(cont):
    print("##################################################################")
    print("#                                                                #")
    print("#                " + cont + "                 #")
    print("#                                                                #")
    print("##################################################################")
    
