<div align="center">
    <img src="https://github.com/dawnl3ss/Theia/blob/main/images/ascii.png">
    <h3>🔎Get data from an ip-adress with Theia 🔍</h3>
    <img src="https://github.com/dawnl3ss/Theia/blob/main/images/shell.png">
</div>

## 📌 Installation :
```console
# Clone the repository
$ git clone https://github.com/dawnl3ss/Theia

# go to the Theia directory
$ cd Theia


# Start the script (lookup one's ip-adress)
$ python theia.py -a 45.45.45.45

# Start the script (lookup your own ip-address)
$ python theia.py -s True
```

## Alternative Installation : 
#### exposes the theia command to the whole  system
```shell
# Clone the repository
$ git clone https://github.com/dawnl3ss/Theia

# go to the Theia directory
$ cd Theia

# create a symlink bound to the theia.sh script
sudo ln -s $(realpath theia.sh) /usr/bin/theia
```

## 📌 Usage :
```console
$ python theia.py --help
[/] Starting Theia...

                ▄▄▄█████▓ ██░ ██ ▓█████  ██▓ ▄▄▄         
                ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▓██▒▒████▄       
                ▒ ▓██░ ▒░▒██▀▀██░▒███   ▒██▒▒██  ▀█▄     
                ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ░██░░██▄▄▄▄██    
                  ▒██▒ ░ ░▓█▒░██▓░▒████▒░██░ ▓█   ▓██▒   
                  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░▓   ▒▒   ▓▒█░   
                    ░     ▒ ░▒░ ░ ░ ░  ░ ▒ ░  ▒   ▒▒ ░   
                  ░       ░  ░░ ░   ░    ▒ ░  ░   ▒      
                          ░  ░  ░   ░  ░ ░        ░  ░ 
    
usage: theia.py [-h] [-a ADRESS] [-s SELF]

optional arguments:
  -h, --help            show this help message and exit
  -a ADRESS, --adress ADRESS
                        victim ip-adress
  -s SELF, --self SELF  you own ip-adress
```
