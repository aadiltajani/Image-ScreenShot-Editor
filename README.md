# Image-ScreenShot-Editor
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/aadiltajani.svg?style=social&label=Follow%20%40tajani_aadil)](https://twitter.com/tajani_aadil)

A script which lets you edit image contents

Remember- It uses OCR so it might give unexpected symbols when it doesn't recognises the text

# How To Run:
  - `pip install -r requirements.txt`
  - After dealing with the dependencies, put the document into the root directory as `input.docx` if you want to edit images  from doc file or else put your image file in Images folder if you want to edit them directly.
  - `python EditorProgram.py`
  - This will ask you the source of image (doc/image).
  - This will ask you if you want to make edits.
  - Finally, the edited content will be available in the fle `Changed_files.doc`.
  - Change the formatting as you like :)


# Dependencies:
# pip install pytesseract

- Linux:

  sudo apt install tesseract-ocr

  sudo apt install libtesseract-dev

  Note for Ubuntu users: In case apt is unable to find the package try adding universe entry to the sources.list file as shown below.




- macOS:

  MacPorts
  To install Tesseract run this command:
  sudo port install tesserac

  Homebrew
  To install Tesseract run this command:
  brew install tesseract




- Windows:
  Install the tesseract binary file from https://github.com/UB-Mannheim/tesseract/wiki.
  
  To access tesseract-OCR from any location you may have to add the directory where the tesseract-OCR binaries are located to the Path variables, probably C:\Program Files\Tesseract-OCR.
  
  After installing, set path in the python file: pytesseract.pytesseract.tesseract_cmd = r'<PATH to Tesseract-OCR\tesseract.exe>"
