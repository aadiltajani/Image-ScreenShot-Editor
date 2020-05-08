import fnmatch
import os
import pytesseract
import zipfile
import platform

input_type = input("What is the source ?(doc/image): ")


if platform.system() == 'Windows':
    sep = '\\'
else:
    sep = '/'


if input_type == 'doc':
    z = zipfile.ZipFile("input.docx")
    all_files = z.namelist()

    # get all files in word/media/ directory
    images = filter(lambda x: x.startswith('word/media/'), all_files)

    # print all files in zip archive
    for image in images:
        print(image)
        curr_image = z.open(image).read()
        f = open("image1.jpeg", 'wb')
        f.write(curr_image)
        z.extract(image, 'Images')
    listOfFiles = os.listdir('Images{0}word{0}media'.format(sep))

else:
    listOfFiles = os.listdir('Images')


pattern_list = ["*.png", "*.jpg", "*.jpeg"]
with open('file_names.txt', 'w') as names:

    for entry in listOfFiles:

        for pattern in pattern_list:

            if fnmatch.fnmatch(entry, pattern):

                if input_type == 'doc':

                    names.write("Images{0}word{0}media{0}".format(sep) + entry + "\n")

                else:
                    names.write("Images{0}".format(sep) + entry + "\n")



######### SET PATH BELOW FOR WINDOWS ONLY

# pytesseract.pytesseract.tesseract_cmd = r'<PATH to \Tesseract-OCR\tesseract.exe   generally in C:\\ProgramFiles(
# x86) or where you install binary file>' 


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
