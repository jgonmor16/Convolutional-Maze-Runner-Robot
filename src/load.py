####################################################################
# Load Data Function
####################################################################

def load(loc):
    file = open("/var/www/html/config/proj/" + loc)

    return file.read()
