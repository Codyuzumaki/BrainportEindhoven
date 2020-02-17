# Brainport Eindhoven Tech Xperience 2020
This repo contains a solution to clasify some Philips products among 4 clases.

To run the algorythm, you must download and unzip the BrainportEindhovenPhilips.zip file:

Since the convolutional network weights file is too large to be stored at GitHub, you must download it from this Google Drive path and place it in the uncompressed:

https://drive.google.com/open?id=1xkmTosS4TGqpPnXnj_vj8hZMwYl-gtOd

The images to be classified must be placed in the "New_Images" folder. Note that there are already 4 images in the folder in case it is necessary to test the system without new images. You can remove them before starting a new test.

The images can be of any size, buy the algorithm was optimized to work with 4032x3024 images.

Docker must be installed in the local computer to run the algorythm.

Once Docker is installed and running, you should run the Run_Analyzer.bat file. A command window will appear and the configuration of the environment will start. Immediately after the configuration ends, the classificator will automatically start to analyze every image in the New_Images folder and will give a result for each one with a single execution.

As an alternative to this .bat file, you can run these below commands in a command window in the path where the files are located (Notice the last dot in the first command) to build and run the solution:


**docker build -t philipssolution .**

**docker run philipssolution**
 
 
For any doubt, you can contact me through my e-mail below.

-----------------------
 
*Víctor Ramos Vicedo*

victorramos7@gmail.com
