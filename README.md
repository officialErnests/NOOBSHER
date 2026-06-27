# NOOBSHER
It is a python tool that syncs files, more crude and dumber. Made for tailscale and local networks in mind ;PP
# Version
x.y.z <br>
x - big releses, think of beta / relse / whole rewrite <br>
y - new feature, expanded feature list <br>
z - patches / hotfixes <br>
# Install
In order to use this, get zip of /NOOBSHER folder <br>
For demu install all and run /demo.py

# Todo
## main:
- [ ] Create file system
- - [x] Inits folder structure
- - [ ] Inits all files
- - [ ] Create run log with exit codes
- [ ] Establish connection
- [ ] Sync file sytem
- [ ] Loaders
- [ ] Backups
- [ ] GUI
## optional:
- [ ] expand try except messages 

# Dev notes
## File variables
save.files [
    "main"
    |-"meta"
    |   |-"logs"
    |   |   |-> All  the loged files
    |   |-> config.txt
    |-"server"
    |-"backups"
    |-"sessions"
]

# Log list
Remade the main NOOBSHER file, and how server/client works