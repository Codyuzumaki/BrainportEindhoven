# BrainportEindhoven
This repo contains a solution to clasify some Philips products among 4 clases.

To run the algorythm, these files and folder should be downloaded and placed in the same folder:

**-DockerFile**

**-Philips_Product_Analyzer.py**

**-New_Images (folder)**

**-Philips_model_v.3.7.h5**

This last file is too large to be stored at GitHub, so you must download it from this Google Drive path:

https://drive.google.com/open?id=1xkmTosS4TGqpPnXnj_vj8hZMwYl-gtOd

The images to be classified must be placed in the "New_Images" folder.

Docker must be installed in the local computer to run the algorythm.

Once Docker was installed, these commands should be executed in a command window in the path where the files are located (Notice the last dot in the first command) to build and run the solution:

**docker build -t philipssolution .**

**docker run philipssolution**

The command window will show the results of the analysis.
 
-----------------------
 
*Víctor Ramos Vicedo*

victorramos7@gmail.com
