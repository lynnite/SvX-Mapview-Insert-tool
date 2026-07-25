# SvX-Mapview-Insert-tool
Aids in creating new insert files for SVX-Map-viewer.

Usage:

converttool.py is specifically used for SVX-Map-Viewer to format RMC-14's insert marker YML files for the js to read. Reduces manual labor by alot while adding new inserts.

buildimages.py is used to build multiple insert map YML files into webp images without needing to do it manually 1 by 1 through the terminal. It builds every map yml file in the directory specified and outputs into your local RMC14/SVX14 repo's MapImages folder. Also reduces manual labor while adding new inserts but can be used for any task that requires building a mass of files.

How to use:
converttool.py

input_filename = "" Path of the file you want to format here 

output_filename = "" Path of the file that it will create here

Run converttool.py with python

How to use: buildimages.py

TARGET_DIR = "" Path of the directory it will build map images from

PROJECT_PATH = "" Path of your Content.Maprenderer

Run buildimages.py with python

All code licensed under MIT
