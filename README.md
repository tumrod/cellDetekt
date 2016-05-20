# cellDetekt

## Getting started
### Running from command line/terminal

#### Requirements:
- Python 2.7
- virtualenv 
- pip

###### Using easy_install or pip to install
```
$ easy_install virtualenv
$ easy_install pip
```
(Note - for installations, you may need to use sudo. New versions of python may have pip already installed.)


#### Step 1: Clone this repository
```
$ git clone https://github.com/tumrod/cellDetekt.git
```

#### Step 2: Create a virtualenv  
you may need to specify the python path with: -p < python path >

```
$ virtualenv -p /usr/bin/python2.7 cdenv
$ virtualenv cdenv
$ source cdenv/bin/activate 
```

#### Step 3: Install required packages
```
(cdenv) $ pip install -r requirements.txt
```

#### Step 4: Run the script file
```
(cdenv) $ python celldetekt.py
```

#### Tips: 
- You may need to use sudo at start of other commands if there are permission issues.
- You can deactivate the virtualenv by 
```
(cdenv) $ deactivate 
```

[![ScreenShot](https://raw.github.com/GabLeRoux/WebMole/master/ressources/WebMole_Youtube_Video.png)](https://github.com/tumrod/cellDetekt/blob/master/celldetekt-dmg-demo.mov)

### dmg for Mac
[Download](https://cdn.rawgit.com/tumrod/cellDetekt/master/dist_dmg.zip)

### exe for Windows
[Download](https://cdn.rawgit.com/tumrod/cellDetekt/master/dist_exe.zip)
