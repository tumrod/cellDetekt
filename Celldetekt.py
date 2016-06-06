# ---------------
# celldetekt.py
# James P. carson
# Tipparat Umrod
# ---------------

from Tkinter import *
from numpy import *
from tkFileDialog import askopenfilename, askdirectory
from PIL import Image, ImageTk, ImageChops, Image, ImageFilter, ImageStat, ImageEnhance, PngImagePlugin, TiffImagePlugin, BmpImagePlugin, JpegImagePlugin
import sys, os, glob

# ------------
# ImagePreview
# ------------
class ImagePreview:
    '''
    Class ImagePreview created the GUI for Celldetekt
    '''

    # ----
    # init
    # ----

    def __init__(self,root):
        '''
        initial setup with default input
        window frame: 900 x 850
        canv: middle column (whole image view)
        original: None <original image file>
        image10xeh: None <enhanced image file>
        new_img: None <new image preview (selection)>
        cropped: None <cropped selection>
        color_list: red, green, blue, grey

        '''
        root.geometry("900x850")
        self.canv = Canvas(root, width=300, height=300)
        self.original = None
        self.imag10xenh = None
        self.new_img = None
        self.cropped = None
        self.color_list = ["red", "green", "blue", "grey"]

        # create toolbars/ controller
        self.setup_controller()

        # create image preview frame (right column)
        self.fm2 = Frame(root, width=150, height=200)
        self.fm2.pack(side=RIGHT)

        # create image preview canvas (right column from top to bottom)
        self.canv2 = Canvas(self.fm2, width=150, height=150)        # cropped of image/ selection preview
        self.canv3 = Canvas(self.fm2, width=150, height=150)        # painted image
        self.canv4 = Canvas(self.fm2, width=150, height=150)        # image_a

        # label for each section
        self.canv3.pack(side=BOTTOM)
        Label(self.fm2, text="Painted", width=10).pack(side=BOTTOM)
        self.canv4.pack(side=BOTTOM)
        Label(self.fm2, text="Image A", width=10).pack(side=BOTTOM)
        self.canv.pack(side=LEFT)
        self.canv2.pack(side=BOTTOM)
        Label(self.fm2, text="Selection", width=10).pack(side=BOTTOM)

    # ----------------
    # setup_controller
    # ----------------
    def setup_controller(self):
        '''
        setup the controller bar (the left column)
        '''
        self.fm1 = Frame(root, width=900, height=450)
        self.fm1.pack(side=LEFT, expand=NO, fill=NONE)

        self.intro=Label(self.fm1, text="Welcome to Celldetekt version 2.7!")
        self.intro.pack(side=TOP)

        self.lblthrs1=Label(self.fm1, text="\nStrong expression detection threshold")
        self.lblthrs1.pack(side=TOP)
        self.thres_entry=Entry(self.fm1)
        self.thres_entry.pack(side=TOP)
        self.thres_entry.insert(END, str(100))
        self.thres= int(self.thres_entry.get())

        self.lblchn1=Label(self.fm1, text="\nStrong expression detection channel")
        self.lblchn1.pack(side=TOP)
        self.radioFm1 = Frame(self.fm1, width=900, height=450)
        self.chn1 = IntVar()
        self.chn1.set(1)
        Radiobutton(self.radioFm1, text="Red",padx = 2, variable= self.chn1, value=0).pack(side=LEFT)
        Radiobutton(self.radioFm1, text="Green",padx = 2, variable= self.chn1,value=1).pack(side=LEFT)
        Radiobutton(self.radioFm1, text="Blue",padx = 2, variable= self.chn1,value=2).pack(side=LEFT)
        Radiobutton(self.radioFm1, text="Grey",padx = 2, variable= self.chn1,value=3).pack(side=LEFT)
        self.radioFm1.pack(side=TOP)

        self.lblthrs2=Label(self.fm1, text="\nWeak expression detection threshold")
        self.lblthrs2.pack(side=TOP)
        self.thresw_entry=Entry(self.fm1)
        self.thresw_entry.pack(side=TOP)
        self.thresw_entry.insert(END, str(100))
        self.thresw= int(self.thresw_entry.get())

        self.lblchn2=Label(self.fm1, text="\nWeak expression detection channel")
        self.lblchn2.pack(side=TOP)
        self.radioFm2 = Frame(self.fm1, width=900, height=450)
        self.chn2 = IntVar()
        self.chn2.set(1)
        Radiobutton(self.radioFm2, text="Red",padx = 2, variable= self.chn2, value=0).pack(side=LEFT)
        Radiobutton(self.radioFm2, text="Green",padx = 2, variable= self.chn2,value=1).pack(side=LEFT)
        Radiobutton(self.radioFm2, text="Blue",padx = 2, variable= self.chn2,value=2).pack(side=LEFT)
        Radiobutton(self.radioFm2, text="Grey",padx = 2, variable= self.chn2,value=3).pack(side=LEFT)
        self.radioFm2.pack(side=TOP)

        self.lblthrs3=Label(self.fm1, text="\nCellular background detection threshold")
        self.lblthrs3.pack(side=TOP)
        self.thresn_entry=Entry(self.fm1)
        self.thresn_entry.pack(side=TOP)
        self.thresn_entry.insert(END, str(230))
        self.thresn= int(self.thresn_entry.get())

        self.lblchn3=Label(self.fm1, text="\nCellular background detection channel")
        self.lblchn3.pack(side=TOP)
        self.radioFm3 = Frame(self.fm1, width=900, height=450)
        self.chn3 = IntVar()
        self.chn3.set(3)
        Radiobutton(self.radioFm3, text="Red",padx = 2, variable= self.chn3, value=0).pack(side=LEFT)
        Radiobutton(self.radioFm3, text="Green",padx = 2, variable= self.chn3,value=1).pack(side=LEFT)
        Radiobutton(self.radioFm3, text="Blue",padx = 2, variable= self.chn3,value=2).pack(side=LEFT)
        Radiobutton(self.radioFm3, text="Grey",padx = 2, variable= self.chn3,value=3).pack(side=LEFT)
        self.radioFm3.pack(side=TOP)

        self.lblscale=Label(self.fm1, text="\nScaling")
        self.lblscale.pack(side=TOP)
        self.ima_scale=Entry(self.fm1)
        self.ima_scale.pack(side=TOP)
        self.ima_scale.insert(END, "2")

        self.lblfn=Label(self.fm1, text="\nImage name")
        self.lblfn.pack(side=TOP)
        self.fn = StringVar()
        self.outputDirBtn = Button(self.fm1, text='Choose File', command= lambda: self.select_file(self.fn)).pack(side=TOP)
        Label(self.fm1, textvariable=self.fn).pack(side=TOP)

        self.lbldir2=Label(self.fm1, text="\nOutput Folder")
        self.lbldir2.pack(side=TOP)
        self.dir2 = StringVar()
        self.outputDirBtn = Button(self.fm1, text='Choose Directory', command= lambda: self.select_folder(self.dir2)).pack(side=TOP)
        Label(self.fm1, textvariable=self.dir2).pack(side=TOP)

        self.fm5 =Frame(self.fm1, width=450, height=15)
        self.fm5.pack(side=BOTTOM)
        self.status = StatusBar(self.fm5)
        self.status.pack(side=BOTTOM)
        self.status.set("Ready to work")

        self.fm4 =Frame(self.fm1, width=450, height=15)
        self.fm4.pack(side=BOTTOM)
        self.run_preview = Button(self.fm4, text="Update Preview", command=self.run_preview)
        self.run_preview.pack(side=LEFT)
        self.run_runFile = Button(self.fm4, text="Run File", command=lambda: self.run_celldim(singleFile=True))
        self.run_runFile.pack(side=LEFT)
        self.run_runFolder = Button(self.fm4, text="Run Folder", command= lambda: self.run_celldim(singleFile=False))
        self.run_runFolder.pack(side=LEFT)

    # ----------
    # select_file
    # ----------
    def select_file(self, fn):
        '''
        select_file creates popup dialog for choosing file
        fn: function passing in <this case is StringVar()>
        '''
        fileName = askopenfilename()
        f = fileName.split("/")
        fileNameLen = len(f[len(f)-1])
        self.filedir = fileName[0:len(fileName)-fileNameLen]
        fn.set(f[len(f)-1])

    # -------------
    # select_folder
    # -------------
    def select_folder(self, dir):
        '''
        select_folder creates popup dialog for choosing folder
        dir: passing the directory
        '''
        folderName = askdirectory()
        dir.set(folderName + "/")

    # -----------
    # run_preview
    # -----------
    def run_preview(self):
        '''
        Run the preview of the cropped image
        '''
        try:
            self.process_original_img()

        except ValueError:
            status.set("Input error, please try again")

    # --------------------
    # process_original_img
    # --------------------
    def process_original_img(self):
        '''
        Process the original image
        '''
        self.thres= int(self.thres_entry.get())
        self.chan = self.color_list[self.chn1.get()]
        self.thresw= int(self.thresw_entry.get())
        self.chanw = "10x" + self.color_list[self.chn2.get()]
        self.thresn= int(self.thresn_entry.get())
        self.chann = self.color_list[self.chn3.get()]

        self.status.set("Process original image")

        ###################
        self.outdir = self.dir2.get()
        self.filename = self.fn.get()
        self.orig_img = Image.open(self.filedir+self.filename)

        # enhance the original image
        self.original = Image.open(self.filedir+self.filename)
        self.enhanceImg(self.outdir+ self.filename[:-4] + "_enhanced.png")

        self.img_file = self.imag10xenh

        # rescale the image to be shown as a full image on middle column
        x,y = self.img_file.size
        self.rescale(x, y)
        self.img_file = self.img_file.resize((int(x/self.scale), int(y/self.scale)), resample=Image.NEAREST)
        self.imgPreview = ImageTk.PhotoImage(self.img_file)
        self.img_x, self.img_y = 450/2,450/2

        if (self.cropped == None):
            self.cropped = self.imag10xenh.crop((int(self.img_x/2*self.scale)-60, int(self.img_y/2*self.scale)-60, int(self.img_x/2*self.scale)+60, int(self.img_y/2*self.scale)+60))
            self.cropped2 = self.cropped.resize((120, 120),Image.BILINEAR)

        # image selection (cropped) preview
        self.create_img_preview()
        self.new_img = ImageTk.PhotoImage(self.cropped2)
        self.canv2.update()
        self.canv2.after(0, self.create_canv2)
        self.preview_celldim()

        # image_painted preview
        self.canv3.update()
        self.canv3.after(0, self.create_img_painted)

        # image_a preview
        self.canv4.update()
        self.canv4.after(0, self.create_img_a)

    # -------
    # rescale
    # -------
    def rescale(self, x, y):
        '''
        Rescale the image to be within 450 x 450 pixel frame
        Parameter: x: width, y: height
        '''
        new_x = x
        new_y = y
        self.scale = 1
        if (x > 450):
            self.scale = x/450.0
            new_x = new_x/self.scale

        if (y > 450):
            new_y = new_y/self.scale

    # ------------
    # create_canv2
    # ------------
    def create_canv2(self):
        '''
        Create Canv2, the cropped preview/ selection preview
        '''
        # show cropped image, self.new_img
        self.show_img = self.canv2.create_image(18, 18, image=self.new_img, anchor=NW)
        self.canv2.tag_raise(self.show_img)

    # ------------------
    # create_img_painted
    # ------------------
    def create_img_painted(self):
        '''
        Create painted image after runing celldim
        When running celldim, self.imv is created along with self.imrgb
        create_img_painted() resize the resulting image (self.imv) and show in the preview
        '''

        self.imv = self.imv.resize((int(self.imv.size[0]*self.cell_scale),int(self.imv.size[1]*self.cell_scale)),Image.BILINEAR)
        self.imv = self.imv.resize((120, 120),Image.BILINEAR)
        self.imv = ImageTk.PhotoImage(self.imv)
        self.canv3.create_image(18, 18, image=self.imv, anchor=NW)

    # ------------
    # create_img_a
    # ------------
    def create_img_a(self):
        '''
        Create image a after runing celldim
        When running celldim, self.imv is created along with self.imrgb
        create_img_a() resize the resulting image (self.imrgb) and show in the preview
        '''
        self.imrgba = self.imrgba.resize((int(self.imrgba.size[0]*self.cell_scale*4),int(self.imrgba.size[1]*self.cell_scale*4)), Image.NEAREST)
        self.imrgba = self.imrgba.resize((120, 120),Image.BILINEAR)
        self.imrgba = ImageTk.PhotoImage(self.imrgba)
        self.canv4.create_image(18, 18, image=self.imrgba, anchor=NW)

    # ------------------
    # create_img_preview
    # ------------------
    def create_img_preview(self):
        '''
        Create the middle column (whole image preview)
        Bind with mouse roll over for crop selection
        '''
        # box for curser
        self.rect = self.canv.create_rectangle(0, 0, 0, 0)

        # mouse roll over
        self.canv.bind('<Motion>', self.roll_over)
        self.canv.config(width=self.imgPreview.width(), height=self.imgPreview.height())
        self.obj1 = self.canv.create_image(0, 0, image=self.imgPreview, anchor=NW)

        # create crop image: self.crop when selected
        self.canv.tag_bind(self.obj1, '<Button-1>', self.crop)
        self.canv.tag_raise(self.rect)

    # ----
    # crop
    # ----
    def crop(self, event):
        '''
        crop the selection by curser location (x, y) coordinate
        update the image preview according to the cropped image
        '''
        x, y = event.x, event.y
        self.img_x, self.img_y = event.x, event.y

        self.cropped = self.imag10xenh.crop((int(x*self.scale)-int(self.scale*10), int(y*self.scale)-int(self.scale*10), int(x*self.scale)+int(self.scale*10), int(y*self.scale)+int(self.scale*10)))

        self.cropped2 = self.cropped.resize((120, 120),Image.BILINEAR)
        self.new_img = ImageTk.PhotoImage(self.cropped2)

        # update all of the preview
        self.canv2.update()
        self.canv2.after(0, self.create_canv2)
        self.preview_celldim()

        self.canv3.update()
        self.canv3.after(0, self.create_img_painted)

        self.canv4.update()
        self.canv4.after(0, self.create_img_a)

    # ---------
    # roll_over
    # ---------
    def roll_over(self, event):
        x, y = event.x, event.y
        self.img_x, self.img_y = event.x, event.y
        position = str(self.img_x) + ", " + str(self.img_y)
        self.canv.coords(self.rect, x - 10, y - 10, x + 10, y + 10)

    # ----------
    # enhanceImg
    # ----------
    def enhanceImg(self, enh_file):
        if(os.path.exists(enh_file)):
            self.file_enh = enh_file
            self.imag10xenh = Image.open(self.file_enh)
        else:
            self.status.set("Enhance image")
            imag10xstats=ImageStat.Stat(self.original)
            imag10xmedian=imag10xstats.median
            print "Median pixel value detected to be: ",imag10xmedian
            del imag10xstats

            imag10xadj=self.original.point(lambda i: (i*255)/min(imag10xmedian))
            print "Image intensity levels adjusted to 0 - 1 - ",min(imag10xmedian)
            del self.original

            self.imag10xenh=ImageEnhance.Sharpness(imag10xadj).enhance(2).convert("RGB")
            print "Image sharpness enhanced"
            del imag10xadj

            self.imag10xenh.save(enh_file)
            print "Enhanced image saved as jpeg"
            self.file_enh = enh_file

    # ---------------
    # preview_celldim
    # ---------------
    def preview_celldim(self):
        self.status.set("Run on selected image")
        self.thres= int(self.thres_entry.get())
        self.chan = self.color_list[self.chn1.get()]
        self.thresw= int(self.thresw_entry.get())
        self.chanw = "10x" + self.color_list[self.chn2.get()]
        self.thresn= int(self.thresn_entry.get())
        self.chann = self.color_list[self.chn3.get()]

        self.outdir=self.dir2.get()
        self.filename=self.fn.get()

        if (self.chanw[0:3]=='10x'):
            self.imr, self.img, self.imb=self.cropped.split()
        if self.chanw=="10xred":
            self.ima=self.imr.point(lambda i: i-self.thresw, "1")
        elif self.chanw=="10xgreen":
            self.ima=self.img.point(lambda i: i-self.thresw, "1")
        elif self.chanw=="10xblue":
            self.ima=self.imb.point(lambda i: i-self.thresw, "1")
        else:
            self.ima=self.cropped.convert("L").point(lambda i: i-self.thresw, "1")
        del self.imr,self.img,self.imb

        self.cell_scale = float(self.ima_scale.get())
        self.ima5x=self.ima.convert("L").resize((int(self.ima.size[0]/self.cell_scale), int(self.ima.size[1]/self.cell_scale)),Image.BILINEAR)

        print "10x signal preserved"
        self.status.set("10x signal preserved")

        self.imag=self.cropped.resize((int(self.cropped.size[0]/self.cell_scale),int(self.cropped.size[1]/self.cell_scale)),Image.ANTIALIAS)
        
        print "Image resized to 5x"
        self.status.set("Image resized to 5x")

        self.status.set("Processing image takes awhile")
        self.imv,self.imrgba= celldim(self.imag,self.thres,self.chan,self.thresw,self.chanw,self.thresn,self.chann,self.ima5x)

        del self.imag,self.ima5x

        self.status.set("Result--->>")
        self.imrgba = rgba_to_rgb(self.imrgba)

    # -----------
    # run_celldim
    # -----------
    def run_celldim(self, singleFile):
        self.status.set("Processing----")
        self.thres= int(self.thres_entry.get())
        self.chan = self.color_list[self.chn1.get()]
        self.thresw= int(self.thresw_entry.get())
        self.chanw = "10x" + self.color_list[self.chn2.get()]
        self.thresn= int(self.thresn_entry.get())
        self.chann = self.color_list[self.chn3.get()]
        self.outdir=self.dir2.get()
        self.filename=self.fn.get()

        if (singleFile):
            fileList = [self.filedir+self.filename]
        else:
            fileList = glob.glob(self.filedir + "*")

        for f in fileList:
            parsefile=f.split(".")
            lpf=len(parsefile)
            f_ext=parsefile[lpf-1]
            filePath = f.split("/")
            filename = filePath[len(filePath)-1]
            if ((f_ext<>"jpg")&(f_ext<>"tif")&(f_ext<>"png")&(f_ext<>"gif")&(f_ext<>"bmp")&(f_ext<>"tiff")):
                print "Unrecognized image file type ",file
                print "Must be jpg, jpeg, tif, tiff, png, gif, or bmp"
                print "Skipping file: " + filename
                self.status.set("Skipping "+ filename)
            else:
                self.original = Image.open(f)
                self.enhanceImg(self.outdir+ filename[:-4] + "_enhanced.png")
                self.imag10xenh = Image.open(self.file_enh)
                if (self.chanw[0:3]=='10x'):
                    self.imr, self.img, self.imb= self.imag10xenh.split()
                if self.chanw=="10xred":
                    self.ima=self.imr.point(lambda i: i-self.thresw, "1")
                elif self.chanw=="10xgreen":
                    self.ima=self.img.point(lambda i: i-self.thresw, "1")
                elif self.chanw=="10xblue":
                    self.ima=self.imb.point(lambda i: i-self.thresw, "1")
                else:
                    self.ima=self.cropped.convert("L").point(lambda i: i-self.thresw, "1")
                del self.imr,self.img,self.imb

                self.cell_scale = float(self.ima_scale.get())
                self.ima5x=self.ima.convert("L").resize((int(self.ima.size[0]/self.cell_scale), int(self.ima.size[1]/self.cell_scale)),Image.BILINEAR)
                
                print "10x signal preserved"
                self.status.set("10x signal preserved")

                self.imag=self.imag10xenh.resize((int(self.imag10xenh.size[0]/self.cell_scale),int(self.imag10xenh.size[1]/self.cell_scale)),Image.ANTIALIAS)

                print "Image resized to 5x"
                self.status.set("Image resized to 5x")

                self.status.set("Detecting cells...")
                self.imv,self.imrgba= celldim(self.imag,self.thres,self.chan,self.thresw,self.chanw,self.thresn,self.chann,self.ima5x)

                self.imrgba = rgba_to_rgb(self.imrgba)
                print "saving images"
                self.status.set("Saving images...")

                self.imv.save(self.outdir+ filename[0:len(filename)-4] + "_painted.png")
                self.imrgba.save(self.outdir+ filename[0:len(filename)-4] + "_a.png")
                self.status.set("Saving" + filename)
                self.status.set("Done.")
                #self.imag10xenh = None

# ---------
# StatusBar
# ---------
class StatusBar(Frame):
    '''
    Class StatusBar created text status while running Celldetekt
    '''
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)
    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()
    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


#------------------------------------------------------------------------------
#------------------------------ Celldetekt 2.6 --------------------------------
#------------------------------------------------------------------------------

def celldim(im,thres,chan,thresw,chanw,thresn,chann,ima5x):
    # adjust raw image size to be multiple of four
    imc=im.crop([0,0,4*(im.size[0]/4),4*(im.size[1]/4)])
    ima5xc=ima5x.crop([0,0,4*(ima5x.size[0]/4),4*(ima5x.size[1]/4)])
    imr,img,imb=imc.split()

    # create thresholded image for strong expression detection
    if (chan[0:3]=='10x'):
        ima=ima5xc.point(lambda i: i-thres,"1")
    else:
        if chan=="red":
            ima=imr.point(lambda i: i-thres, "1")
        elif chan=="green":
            ima=img.point(lambda i: i-thres, "1")
        elif chan=="blue":
            ima=imb.point(lambda i: i-thres, "1")
        else:
            ima=imc.convert("L").point(lambda i: i-thres, "1")

    # create thresholded image for weak expression detection
    if (chanw[0:3]=='10x'):
        imaw=ima5xc.point(lambda i: i-240,"1")
    else:
        if chanw=="red":
            imaw=imr.point(lambda i: i-thresw, "1")
        elif chanw=="green":
            imaw=img.point(lambda i: i-thresw, "1")
        elif chanw=="blue":
            imaw=imb.point(lambda i: i-thresw, "1")
        else:
            imaw=imc.convert("L").point(lambda i: i-thresw, "1")

    # create thresholded image for non-expression detection
    if chann=="red":
        iman=imr.point(lambda i: i-thresn, "1")
    elif chann=="green":
        iman=img.point(lambda i: i-thresn, "1")
    elif chann=="blue":
        iman=imb.point(lambda i: i-thresn, "1")
    else:
        iman=imc.convert("L").point(lambda i: i-thresn, "1")

    del ima5xc

    #########################################################

    # create masking array
    ggmask=ones((ima.size[1],ima.size[0]))

    # create mask image
    imamask=Image.new("1",ima.size,1)

    # prepare RGBA at 25% scale for geneatlas.org
    imcsmallr,imcsmallg,imcsmallb=imc.resize((imc.size[0]/4,imc.size[1]/4),Image.ANTIALIAS).split()
    imcsmalla=Image.new("L",imcsmallr.size,255)

    # create A-channel array for small rgba
    ggsmalla=ones((imcsmalla.size[1],imcsmalla.size[0]))+254

    # create red,blue,green channels for big visual image
    ggbigr=zeros((im.size[1],im.size[0]))
    ggbigb=zeros((im.size[1],im.size[0]))
    ggbigg=zeros((im.size[1],im.size[0]))

    ########################################################

    # set up array for dust detection
    #g=imaw.getdata()
    #gg=resize(g,(ima.size[1],ima.size[0]))

    #print "Step 0, Removing embedded dust particles"
    #dustg=img.getdata()
    #dustgg=resize(dustg,(img.size[1],img.size[0]))
    #dustb=imb.getdata()
    #dustbb=resize(dustb,(imb.size[1],imb.size[0]))

    #for x in range(3,ima.size[1]-3):
    #   for y in range(3,ima.size[0]-3):
    #       if (gg[x][y]==0):
    #           if dustbb[x][y]<(dustgg[x][y]+9):
    #               ggmask=maskspot(ggmask,x,y)

    #del dustg,dustgg,dustb,dustbb
    del imr,img,imb


    ######################################################

    # mask out image and get new array
    #imamask.putdata(resize(ggmask,(1,ima.size[0]*ima.size[1]))[0])
    #ima=ImageChops.lighter(ima,ImageChops.invert(imamask).point(lambda i: i-254))
    g=ima.getdata()
    gg=resize(g,(ima.size[1],ima.size[0]))

    print "Step 1, Detecting Cells filled with Gene Expression"
    for x in range(3,ima.size[1]-3):
        for y in range(3,ima.size[0]-3):
            if (gg[x][y]==0):
                if (gg[x+1][y]==0):
                    if (gg[x-1][y]==0):
                        if (gg[x][y+1]==0):
                            if (gg[x+1][y+1]==0):
                                if (gg[x-1][y+1]==0):
                                    if (gg[x][y-1]==0)&(gg[x+1][y-1]==0)&(gg[x-1][y-1]==0):
                                        ggmask=maskspot(ggmask,x,y)
                                        ggsmalla[(x+2)/4][(y+2)/4]=253
                                        ggbigr=markspot(ggbigr,x,y)

    #######################################################

    # mask out image and get new array
    imamask.putdata(resize(ggmask,(1,ima.size[0]*ima.size[1]))[0])
    ima=ImageChops.lighter(ima,ImageChops.invert(imamask).point(lambda i: i-254))
    g=ima.getdata()
    gg=resize(g,(ima.size[1],ima.size[0]))


    print "Step 2, Detecting Cells partially filled with Gene Expression"
    for x in range(3,ima.size[1]-3):
        for y in range(3,ima.size[0]-3):
            if (gg[x][y]==0):
                if (gg[x+1][y]==0):
                    if (gg[x][y+1]==0):
                        if (gg[x+1][y+1]==0):
                            ggmask=maskspot(ggmask,x,y)
                            if ggsmalla[(x+2)/4][(y+2)/4]==255:
                                ggsmalla[(x+2)/4][(y+2)/4]=252
                            ggbigb=markspot(ggbigb,x,y)

    ########################################################

    # mask out image and get new array
    imamask.putdata(resize(ggmask,(1,ima.size[0]*ima.size[1]))[0])
    imaw=ImageChops.lighter(imaw,ImageChops.invert(imamask).point(lambda i: i-254))
    g=imaw.getdata()
    gg=resize(g,(ima.size[1],ima.size[0]))

    print "Step 3, Detecting Cells with scattered Gene Expression"
    for x in range(3,ima.size[1]-4):
        for y in range(3,ima.size[0]-4):
            if (gg[x][y]==0):
                if (gg[x+2][y+2]==0):
                    ggmask=maskspot(ggmask,x+1,y+1)
                    if ggsmalla[(x+2+1)/4][(y+2+1)/4]==255:
                        ggsmalla[(x+2+1)/4][(y+2+1)/4]=251
                    ggbigg=markspot(ggbigg,x+1,y+1)
                    gg=maskspot2(gg,x+1,y+1)
                elif (gg[x+2][y]==0)|(gg[x+2][y+1]==0):
                    ggmask=maskspot(ggmask,x+1,y)
                    if ggsmalla[(x+2+1)/4][(y+2)/4]==255:
                        ggsmalla[(x+2+1)/4][(y+2)/4]=251
                    ggbigg=markspot(ggbigg,x+1,y)
                    gg=maskspot2(gg,x+1,y)
                elif (gg[x][y+2]==0)|(gg[x+1][y+2]==0):
                    ggmask=maskspot(ggmask,x,y+1)
                    if ggsmalla[(x+2)/4][(y+2+1)/4]==255:
                        ggsmalla[(x+2)/4][(y+2+1)/4]=251
                    ggbigg=markspot(ggbigg,x,y+1)
                    gg=maskspot2(gg,x,y+1)
                else:
                    ggmask=maskspot(ggmask,x,y)
                    if ggsmalla[(x+2)/4][(y+2)/4]==255:
                        ggsmalla[(x+2)/4][(y+2)/4]=251
                    ggbigg=markspot(ggbigg,x,y)
                    gg=maskspot2(gg,x,y)


    ########################################################

    # compute display picture
    imr,img,imb=im.split()
    imr.putdata(resize(ggbigr,(1,im.size[0]*im.size[1]))[0])
    img.putdata(resize(ggbigg,(1,im.size[0]*im.size[1]))[0])
    imb.putdata(resize(ggbigb,(1,im.size[0]*im.size[1]))[0])

    del ggbigr,ggbigg,ggbigb

    immask=ImageChops.invert(ImageChops.lighter(imb,ImageChops.lighter(imr,img)))
    im2=ImageChops.darker(im,Image.merge("RGB",(immask,immask,immask)))

    imbnew=ImageChops.subtract(imb,imr)
    imgnew=ImageChops.subtract(ImageChops.subtract(img,imr),imbnew)
    imrnew=ImageChops.add(imgnew,imr)

    imview=ImageChops.lighter(im2,Image.merge("RGB",(imrnew,imgnew,imbnew)))

    del imrnew,imgnew,imbnew,im2,immask, imr, img, imb

    ########################################################

    imamask.putdata(resize(ggmask,(1,ima.size[0]*ima.size[1]))[0])
    iman=ImageChops.lighter(iman,ImageChops.invert(imamask).point(lambda i: i-254))
    g=iman.getdata()
    gg=resize(g,(ima.size[1],ima.size[0]))

    print "Step 4, Detecting Cells without Gene Expression"
    for x in range(3,ima.size[1]-4):
        for y in range(3,ima.size[0]-4):
            if (gg[x][y]==0):
                if (gg[x+2][y+2]==0):
                    ggmask=maskspot(ggmask,x+1,y+1)
                    if ggsmalla[(x+2+1)/4][(y+2+1)/4]==255:
                        ggsmalla[(x+2+1)/4][(y+2+1)/4]=250
                    gg=maskspot2(gg,x+1,y+1)
                elif (gg[x+2][y]==0)|(gg[x+2][y+1]==0):
                    ggmask=maskspot(ggmask,x+1,y)
                    if ggsmalla[(x+2+1)/4][(y+2)/4]==255:
                        ggsmalla[(x+2+1)/4][(y+2)/4]=250
                    gg=maskspot2(gg,x+1,y)
                elif (gg[x][y+2]==0)|(gg[x+1][y+2]==0):
                    ggmask=maskspot(ggmask,x,y+1)
                    if ggsmalla[(x+2)/4][(y+2+1)/4]==255:
                        ggsmalla[(x+2)/4][(y+2+1)/4]=250
                    gg=maskspot2(gg,x,y+1)
                else:
                    ggmask=maskspot(ggmask,x,y)
                    if ggsmalla[(x+2)/4][(y+2)/4]==255:
                        ggsmalla[(x+2)/4][(y+2)/4]=250
                    gg=maskspot2(gg,x,y)


    ########################################################

    # assemble RGBA
    imcsmalla.putdata(resize(ggsmalla,(1,imcsmalla.size[0]*imcsmalla.size[1]))[0])
    imcrgba=Image.merge("RGBA",(imcsmallr,imcsmallg,imcsmallb,imcsmalla))

    # insert header
    imcrgba.putpixel((0,0),(0,0,0,1))

    return imview,imcrgba

# function that creates rgb image from a channel of rgba
def rgba_to_rgb(imag_rgba):

    (w,h)=imag_rgba.size
    im3=Image.new('RGB',(w,h),(0,0,0))

    for x in range (w):
        for y in range (h):
            (r,g,b,a)=imag_rgba.getpixel((x,y))
            if a==255:
                r,g,b=0,0,0
            elif a==251:
                r,g,b=255,255,128
            elif a==252:
                r,g,b=0,0,255
            elif a==253:
                r,g,b=255,0,0
            elif a==250:
                r,g,b=128,128,128
            else:
                r,g,b=0,0,0
            im3.putpixel((x,y),(r,g,b))
    return im3

# function that masks out a region populated by a cell
def maskspot(arra,x,y):
    for j in range(-3,4):
        for k in range(-2,3):
            arra[x+j][y+k]=0
    for k in (-3,3):
        for j in range(-2,3):
            arra[x+j][y+k]=0
    return arra

# function that masks out a region populated by a cell
# used to prevent overcounting during weak detection
def maskspot2(arra,x,y):
    for j in range(-1,2):
        for k in range(-1,2):
            arra[x+j][y+k]=1
    return arra

# function that marks a spot for visually pleasing view
def markspot(arra,x,y):
    for j in range(-2,3):
        for k in range(-1,2):
            arra[x+j][y+k]=255
    for k in (-2,2):
        for j in range(-1,2):
            arra[x+j][y+k]=255
    return arra

if __name__ == '__main__':
    root = Tk()
    root.title("Celldetekt")
    App = ImagePreview(root)
    root.mainloop()
