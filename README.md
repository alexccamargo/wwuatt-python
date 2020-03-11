# wwuatt-python

# install python3.7
1. Check if it installed: 
    ```
    brew info python 
    ```
2. If installed any version 3 lower than 3.7, run 
    ```
    brew update && brew upgrade python
    ```
3. If not installed use 
    ```
    brew install python3
    echo "alias python=/usr/local/bin/python3" >> ~/.zshrc
    ```
Source used: https://opensource.com/article/19/5/python-3-default-mac

# install dependencies
```
pip3 install flask
pip3 install sqlalchemy
pip3 install cryptography
```