from NOOBSHER import server as nb_server
server = nb_server(
    host="127.0.0.1", 
    port=8080, 
    directory="test/server",
    quiet=False)
server.init_dir()
nb_server_version = server.getInfo('version')
if not nb_server_version[0]:
    nb_server_version[1] = "[[unable to load]]"
print("\\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/")
print("NOOBesher_cli")
print("This was made as cli interface and demo for NOOBSHER ;))")
print(f"Server version {nb_server_version[1]}")
print("/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\\")

menu_manager = {
    "curent_menu": 0,
    "max_main_menu": 3
}

def getIntInput(text, min, max):
    res = input(text)
    try:
        val = int(str(res))
        if (min <= val <= max):
            return (True, val)
        return (False, None)
    except:
        return (False, None)

def mainMenu():
    print("//Main menu" \
    "\n-[1] Condfig" \
    "\n-[2] Info" \
    "\n-[3] Share manager" \
    "\n-[0] Close")
    is_int, input_int = getIntInput("Select input:", 0, 3)
    if (is_int):
        menu_manager["curent_menu"] = input_int
        if (input_int == 0):
            server.exit()
            menu_manager["curent_menu"] = -1
    else: print("provided action wasn't able to execute")
        
def configMenu():
    print("//Config menue" \
    "\nAtm nothing")
    input("return:")
    menu_manager["curent_menu"] = 0
    
def infoMenu():
    print("//Info menue" \
    "\nAtm nothing")
    input("return:")
    menu_manager["curent_menu"] = 0

def shareManager():
    print("//Share manager menu" \
    "\n-[1] Back to main menu" \
    "\n-[2] List shares" \
    "\n-[3] Create shares" \
    "\n-[4] Edit shares")
    is_int, input_int = getIntInput("Select input:", 1, 4)
    if (is_int):
        match input_int:
            case 1:
                menu_manager["curent_menu"] = 0
            case 2:
                pass
    else: print("provided action wasn't able to execute")

while True:
    match menu_manager["curent_menu"]:
        case -1:
            break
        case 0:
            mainMenu()
        case 1: 
            configMenu()
        case 2: 
            infoMenu()
        case _:
            mainMenu()

print("Program has been closed!")