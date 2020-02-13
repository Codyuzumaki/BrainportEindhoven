# BrainportEindhoven
This repo contains a solution to clasify some Philips products among 4 clases.

To run the algorythm, these files and folder should be downloaded and placed in the same folder:

**-DockerFile**

**-Philips_Product_Analyzer.py**

**-New_Images (folder)**

**-Philips_model_v.3.7.h5**

Since this last file is too large to be stored at GitHub, you must download it from this Google Drive path:

https://drive.google.com/open?id=1xkmTosS4TGqpPnXnj_vj8hZMwYl-gtOd

The images to be classified must be placed in the "New_Images" folder. Note that there are already 4 images in the folder in case it is necessary to test the system without new images. You can remove them before starting a new test

Docker must be installed in the local computer to run the algorythm.

Once Docker is installed, these commands should be executed in a command window in the path where the files are located (Notice the last dot in the first command) to build and run the solution:

**docker build -t philipssolution .**

**docker run philipssolution**

The algorythm will analyze every image in the New_Images folder and will give a result for each one with a single execution
 
For any doubt, you can contact me through my e-mail below.
-----------------------
 
*Víctor Ramos Vicedo*

victorramos7@gmail.com
