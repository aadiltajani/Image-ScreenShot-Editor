import fnmatch
import os
import pytesseract
import zipfile
import platform 

z = zipfile.ZipFile("input.docx")

#print all files in zip archive
all_files = z.namelist()

#get all files in word/media/ directory


if platform.system() == 'Windows':

    images = filter(lambda x: x.startswith('word\\media\\'), all_files)

else:
    
    images = filter(lambda x: x.startswith('word/media/'), all_files)


for image in images :
    print(image)
    curr_image = z.open(image).read()
    f = open("image1.jpeg",'wb')
    f.write(curr_image)
    z.extract(image, r'Images')



listOfFiles = os.listdir(r'Images/word/media')
print(listOfFiles)
pattern_list = ["*.png", "*.jpg", "*.jpeg"]
with open('file_names.txt', 'w') as names:

    for entry in listOfFiles:

        for pattern in pattern_list:

            if fnmatch.fnmatch(entry, pattern):


                if platform.system() == 'Windows':

                    names.write("Images\\word\\media\\" + entry+"\n")

                else:

                    names.write("Images/word/media/" + entry+"\n")
               
                names.writelines("Images\\" + entry+"\n")

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
