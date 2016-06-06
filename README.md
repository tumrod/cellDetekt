# cellDetekt | [Paper](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2818.2005.01450.x/full)

## Getting started

Download: [MacOSX](https://cdn.rawgit.com/tumrod/cellDetekt/master/celldetekt.dmg) |  [Windows](https://cdn.rawgit.com/tumrod/cellDetekt/master/dist_exe.zip)
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
![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/demo/celldetekt-dmg-demo.gif)

---

## Usage
#### Preview:
* **Selection:** Preview selected section
* **Image A:** Pixellated Detection
* **Paited:** Expression painted to original image

#### Colors:
* **Red:** Strong expression in the cell
* **Blue:** Medium expression in the cell
* **Yellow:** Weak expression in the cell
* **Gray:** Cellular (no expression)
* **Black:** Background/ no cell

#### Medium-Strong Expression Detection

![strong-expression](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/strong-expression.png)

**Threshold between 0-255**: Red/Blue color represented on the preview
* detect strong/medium expression
* for example, some image has a relatively light stained but there are some noticable strong expression, adjusting the scale to be on a lower threshold will detect the cellular expression at lower level.

**Channels**: Red, Green, Blue, Grey
* Depends on the staining colors, choosing the contrasting channel
* for example, purple stain (blue+red), the contrasting channel would be green

![strong-expression](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/strong-exp.png)

#### Weak Expression Detection

![weak-expression](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/weak-expression.png)

**Threshold between 0-255**: Yellow color represented on the preview
* detect weak expression

**Channels**: Red, Green, Blue, Grey
* Depends on the staining colors, choosing the contrasting channel
* for example, purple stain (blue+red), the contrasting channel would be green

![weak-expression-demo](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/weak-exp.png)

#### Background Detection

![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/bg.png)

**Threshold between 0-255**: Grey color represented on the preview
* detect cellular background

**Channels**: Red, Green, Blue, Grey
* default to grey, unless the background is colored

#### Cellular Scaling

![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/scaling.png)

* Scaling the cell size: smaller number = smaller cell size

![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/scaling-3.png)

#### Running

![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/run.png)

**Update Preview:** 
* update the image preview on the right panels
* anytime there is a change in parameter, the update preview button is needed to be clicked

**Run File:**
* Run the current parameters and create Image A and Painted image for the whole input file
* Output in the selected output directory

**Run Folder:**
* Run the current parameters and create Image A and Painted image for all the images in the selected input directory
* Output in the selected output directory
