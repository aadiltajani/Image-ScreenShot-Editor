import fnmatch
import os
import pytesseract

listOfFiles = os.listdir(r'Images')
pattern_list = ["*.png", "*.jpg", "*.jpeg"]
with open('file_names.txt', 'w') as names:
    for entry in listOfFiles:
        for pattern in pattern_list:
            if fnmatch.fnmatch(entry, pattern):
                names.writelines("Images\\" + entry)

# SET PATH BELOW FOR WINDOWS ONLY
# pytesseract.pytesseract.tesseract_cmd = r'<path to Tesseract-OCR\tesseract.exe>'
text = pytesseract.image_to_string('file_names.txt')

while (True):
    test = input("Do you want to replace anything ? (Y/N)")
    if test != 'Y' and test != 'y':
        break
    old, new = input("Enter original string and new string for replacing: ").split(" ")
    old = old.rstrip()
    new = new.rstrip()
    text = text.replace(old, new)

with open('Changed_files.doc', 'w') as f:
    f.write(text)
print("File \"Changed_files.doc\" created !!!")