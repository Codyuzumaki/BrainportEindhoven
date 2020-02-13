# BrainportEindhoven
This repo contains a solution to clasify some Philips products among 4 clases.

To run the algorythm, these files and folder should be downloaded and placed in the same folder:

**-DockerFile**

**-Philips_model_v.3.7.h5**

**-Philips_Product_Analyzer.py**

**-New_Images (folder)**

The images to be classified must be placed in the "New_Images" folder.

Docker must be installed in the local computer to run the algorythm.

Once Docker was installed, these commands should be executed in a command window in the path where the files are located (Notice the last dot in the first command) to build and run the solution:

**docker build -t PhilipsSolution .**

**docker run PhilipsSolution**

The command window will show the results of the analysis.
