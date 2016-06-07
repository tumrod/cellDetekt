# Celldetekt 2.7 

Celldetekt uses a sliding-window approach to quantify cellular gene expression within *in situ* hybridized tissue sections.  The algorithm is described in  [J Microscopy 217:3, 275-281 (2005)](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2818.2005.01450.x/full); when using Celldetekt, please cite this manuscript.  Restrictions on use are described in the [LICENSE.txt](LICENSE.txt) file.

## Updates to version 2.7 include:
- New graphical user interface (GUI)
- Scaling parameter introduced to allow adjustment for different image magnifications 
- Interactive preview of results to quickly optimize parameters

Version 2.7 updates were introduced by Tipparat Umrod while working at the Texas Advanced Computing Center at the University of Texas at Austin.

## Getting started

The easiest way to use Celldetekt is to download the executable for MacOSX or Windows using the following links:

[MacOSX](https://cdn.rawgit.com/tumrod/cellDetekt/master/celldetekt.dmg)

[Windows](https://cdn.rawgit.com/tumrod/cellDetekt/master/dist_exe.zip)

Then just double click the file to open up Celldetekt.  If you do this, skip ahead to "Download and Run".


Another option available is to run Celldetekt from the command line.

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

Celldetekt can be applied to a single image or a folder of images from the same ISH experiment.  The basic process is to:

1. Select a representative input image.
2. Select an output folder.
3. Click "Update preview".
4. Click a location on the image to set a preview region and see Celldetekt results  for that region.
5. Change parameters and then go to step 3 or 4.
6. Once happy with parameters, click "Run File" to apply to entire image or "Run Folder" to apply to all images in the same folder as the input image.

Here is an animation demonstrating the use of Celldetekt with MacOSX.

<MacOSX example>
![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/demo/celldetekt-dmg-demo.gif)

---

## GUI Map

#### Preview:
* **Selection:** Preview selected section
* **Image A:** "A" channel encoded into RGBA output image.  With proper scaling, 1 pixel roughly represents 1 cell
* **Painted:** Expression painted onto to resized original image

#### Color code for Image A:
* **Red:** Strong expression in the cel
* **Blue:** Medium expression in the cell
* **Yellow:** Weak expression in the cell
* **Gray:** Cell without expression
* **Black:** Background/ no cell

#### Strong Expression Detection

![strong-expression](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/strong-expression.png)

**Threshold between 0-255**: Red/Blue color represented on the preview
* Detect cells strongly or moderately expressing probed target
* Adjusting the scale to be on a lower threshold will detect the cellular expression at lower level.

**Channels**: Red, Green, Blue, Grey
* Depends on the color stain, choosing the contrasting channel
* For example, purple stain (blue+red), the contrasting channel would be green

![strong-expression](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/strong-exp.png)

#### Weak Expression Detection

![weak-expression](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/weak-expression.png)

**Threshold between 0-255**: Yellow color represented on the preview
* Detect cells weakly expressing probed target

**Channels**: Red, Green, Blue, Grey
* Depends on the staining colors, choosing the contrasting channel
* For example, purple stain (blue+red), the contrasting channel would be green

![weak-expression-demo](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/weak-exp.png)

#### Background Detection

![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/bg.png)

**Threshold between 0-255**: Grey color represented on the preview
* Detect cells not expressing probed target

**Channels**: Red, Green, Blue, Grey
* Default to grey, unless the tissue has background staining

#### Scaling

![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/scaling.png)

* Scaling the cell size: smaller number = smaller cell size

![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/scaling-3.png)

#### Running

![alt text](https://cdn.rawgit.com/tumrod/cellDetekt/master/asset/run.png)

**Update Preview:** 
* Update the image preview on the right panels with currently selected parameters
* 
**Run File:**
* Run the current parameters on current image to create Image A and Painted image for the entire image
* Outputs in the selected output directory

**Run Folder:**
* Run the current parameters on all the images in the selected input directory
* Outputs in the selected output directory
