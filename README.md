# Usage: 

``` bash

  createCmakeProject projectName [OPTION (--force)]

```

* The above will create a ${projectName} folder
* If --force (or -f) is giver as argument, it will rm -rf folder and rebuilt



# Todo:
  * Create install script which will does:
    * -- Check if ~/bin exists
    * -- If not, create
    * -- add main createCmakeProject script to ~/bin
    * -- Check if ~/bin is in ${PATH} (Yes, this is linux only, don't care about windows)
    * -- If not, include ~/bin in ${PATH} (By appending to ~/.bashrc ?)