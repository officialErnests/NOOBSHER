# NOOBSHER
It is a python tool that syncs files, more crude and dumber. Made for tailscale and local networks in mind ;PP

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

