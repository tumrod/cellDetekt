# cellDetekt | [How cellDetekt works?](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2818.2005.01450.x/full)

## Getting started

Download: [MacOSX](https://cdn.rawgit.com/tumrod/cellDetekt/master/dist_dmg.zip) |  [Windows](https://cdn.rawgit.com/tumrod/cellDetekt/master/dist_exe.zip)
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

### Download and Run!
<MacOSX example>
![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/celldetekt-dmg-demo.gif)

## Usage
* Medium-Strong Expression Detection
![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/strong-expression.png)

* Weak Expression Detection
![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/weak-expression.png)

* Background Detection
![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/bg.png)

* Cellular Scaling
![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/scaling.png)

* Running
![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/run.png)
