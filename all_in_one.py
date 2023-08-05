# for cnd
# import easyocr
from pdf2image import convert_from_path
from PIL import Image

# for ocalc (table)
import pandas as pd
import numpy as np
import tabula
import pandas as pd
import pdfminer
import re
from pdfminer.high_level import extract_text

# both
import time

start_time = time.process_time()



def extract_numbers(string):
    numbers = re.findall(r"\d+", string)
    return numbers


# pole_length_values = ["30", "35", "40", "45", "50", "55"]
# pole_class_values = ["1", "2", "3", "4", "5", "h1"]
# setting_depth_values = ["6", "6.5", "7", "7.5", "8", "8.5", "9"]

# pole_length_class_pattern = r"\d+'?(?:-\d+|\s\d+)"

# OneDrive_1_7-22-2023/Con6-complex.pdf
# for cnd
pdf_path = 'uploads/first.pdf'

images = convert_from_path(pdf_path, poppler_path='poppler-23.05.0/Library/bin')

reader = easyocr.Reader(['en'], gpu=False)

cnd_results = []

image_path = "uploads/first.jpg"
images[0].save(image_path)
# 35' /40'-5

# Open the PNG image
image = Image.open("uploads/first.jpg")

# Rotate the image by 90 degrees counter-clockwise
rotated_image = image.rotate(-90, expand=True)

# Save the rotated image as a new PNG file
rotated_image.save("uploads/rotated_first.jpg")


image_results = reader.readtext("uploads/first.jpg")
rotated_image_results = reader.readtext("uploads/rotated_first.jpg")

cnd_results.extend(image_results)
cnd_results.extend(rotated_image_results)

cnd_text = ""
for result in cnd_results:
    # print(result[1])
    cnd_text += result[1]+" "


# print(cnd_text)

# for cnd

# for ocalc (table)

pdf_path = 'uploads/second.pdf'

images = convert_from_path(pdf_path, poppler_path='poppler-23.05.0/Library/bin')

reader = easyocr.Reader(['en'], gpu=False)

ocl_results = []

i = 0

for image in images:
    image_path = f"uploads/{i}.jpg"
    image.save(image_path)
    i += 1
# 35' /40'-5


for j in range(1):  # for j in range(i-1):

    # Open the PNG image
    # image = Image.open(f"uploads/{j}.jpg")
    image = Image.open(f"uploads/0.jpg")

    image_results = reader.readtext(f"uploads/{j}.jpg")

    ocl_results.extend(image_results)

ocl_text = ""
for result in ocl_results:
    # print(result[1])
    ocl_text += result[1]+" "

# print(ocl_text)
# both


def extract_parameters_from_con(text):
    # Regular expressions for different formats
    # Order them by priority, as you mentioned    40'/45'-1   45 1
    pole_length_class_regexes = [
        re.compile(
            r"[345][05]\s*'\s*\/\s*[345][05]\s*'\s*-\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/\s*[345][05]\s*'?\s*-\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'\s*\/\s*[345][05]\s*'\s*_\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/\s*[345][05]\s*'?\s*_\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'\s*\/\s*[345][05]\s*'\s*[\-_*]\s*CL?\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/\s*[345][05]\s*'?\s*[\-_*]\s*CL?\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'\s*\/\s*[345][05]\s*'\s*[\*]?-\s*CL?\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/?\s*[345][05]\s*'?\s*[\-_*]?\s*CL?\s*[12345h]"),
        re.compile(
            r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'\s*[\-_*]\s*CL?\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/\s*[345][05]\s*'?\s*-?\s*[12345h]"),
        re.compile(
            r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'\s*[\-_*]?CL\s*[12345h]"),
        re.compile(
            r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'?\s*[\-_*]?CL?\s*[12345h]"),
        re.compile(
            r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'?\s*[\-_*]\s*CL?\s*[12345h]"),
        # re.compile(
        #     r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'?\s*[\-_*]?\s*CL?\s*[12345h]"),
        re.compile(r"[345][05]\s*'\s*[\-_*]\s*[12345h]?"),
        re.compile(r"[345][05]\s*'?\s*[\-_*]\s*[12345h]?")
    ]

    setting_depth_regexes = [re.compile(r"SET\s*[6-9][,.]?[05]?\s*'\s*DEEP"),
                             re.compile(r"SET\s*[6-9][,.]?[05]?\s*'?\s*DEEP"),
                             re.compile(r"SET?\s*[6-9][,.]?[05]?\s*'?\s*DEEP"),
                             re.compile(r"SET\s*[6-9][,.]?[05]?\s*'?\s*DEEP?"),
                             re.compile(r"SET?\s*[6-9][,.]?[05]?\s*'\s*DEEP?")]

    pole_length_matches = pole_length_class_regexes[0].findall(text)
    for reg in pole_length_class_regexes:
        if (len(pole_length_matches) == 0 or pole_length_matches[0] == ''):
            pole_length_matches = reg.findall(text)

    setting_depth_matches = setting_depth_regexes[0].findall(text)
    for reg in setting_depth_regexes:
        if (len(setting_depth_matches) == 0 or setting_depth_matches[0] == ''):
            setting_depth_matches = reg.findall(text)

    # Extracting values
    if pole_length_matches:
        pole_length = pole_length_matches
        pole_class = pole_length_matches
    else:
        print("length is none")
        pole_length = None
        pole_class = None

    setting_depth = setting_depth_matches if setting_depth_matches else None

    # Return a dictionary with the extracted values
    return {
        "pole_length": pole_length,
        "pole_class": pole_class,
        "setting_depth": setting_depth
    }


def extract_parameters_from_ocl(text):
    # Regular expressions for different formats
    # Order them by priority, as you mentioned    40'/45'-1   45 1
    pole_length_class_regexes = [
        re.compile(
            r"Pole\s*Length\s*Class:\s*[345][05]\s*'?\s*\/\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/\s*[345][05]\s*'?\s*-\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'\s*\/\s*[345][05]\s*'\s*_\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/\s*[345][05]\s*'?\s*_\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'\s*\/\s*[345][05]\s*'\s*[\-_*]\s*CL?\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/\s*[345][05]\s*'?\s*[\-_*]\s*CL?\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'\s*\/\s*[345][05]\s*'\s*[\*]?-\s*CL?\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/?\s*[345][05]\s*'?\s*[\-_*]?\s*CL?\s*[12345h]"),
        re.compile(
            r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'\s*[\-_*]\s*CL?\s*[12345h]"),
        re.compile(
            r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'\s*[\-_*]?CL\s*[12345h]"),
        re.compile(
            r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'?\s*[\-_*]?CL?\s*[12345h]"),
        re.compile(
            r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'?\s*[\-_*]\s*CL?\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/\s*[345][05]\s*'?\s*-?\s*[12345h]"),
        # re.compile(
        #     r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'?\s*[\-_*]?\s*CL?\s*[12345h]"),
        re.compile(r"[345][05]\s*'\s*[\-_*]\s*[12345h]?"),
        re.compile(r"[345][05]\s*'?\s*[\-_*]\s*[12345h]?")
    ]

    setting_depth_regexes = [re.compile(r"Setting\s*Depth\s*\(ft\)\s*:\s*[6-9][,.]?[05]?\s*'?"),
                             re.compile(
                                 r"Setting?\s*Depth\s*\(ft\)\s*:\s*[6-9][,.]?[05]?\s*'?"),
                             re.compile(
                                 r"Setting?\s*Depth\s*(\(ft\))?\s*:\s*[6-9][,.]?[05]?\s*'?"),
                             re.compile(
                                 r"setting?\s*Depth\s*(\(ft\))?\s*:\s*[6-9][,.]?[05]?\s*'?"),
                             re.compile(
                                 r"Setting?\s*depth\s*(\(ft\))?\s*:\s*[6-9][,.]?[05]?\s*'?"),
                             re.compile(
                                 r"setting?\s*depth\s*(\(ft\))?\s*:\s*[6-9][,.]?[05]?\s*'?"),
                             re.compile(
                                 r"setting?\s*depth\s*(\(ft\))?\s*:?\s*[6-9][,.]?[05]?\s*'?")
                             ]

    at_replace_regexes = [re.compile(r"At Replace \(Existing\)"),
                          re.compile(
        r"At Replace \(\s*Existing\s*\)"),
        re.compile(
        r"At Replace (\(\s*Existing\s*\))?")
    ]
    at_replace_matches = at_replace_regexes[0].findall(text)
    for reg in at_replace_regexes:
        if (len(at_replace_matches) == 0 or at_replace_matches[0] == ''):
            at_replace_matches = reg.findall(text)

    if (at_replace_matches):
        bool_at_replace = True
    else:
        bool_at_replace = False
    pole_length_matches = pole_length_class_regexes[0].findall(text)
    for reg in pole_length_class_regexes:
        if (len(pole_length_matches) == 0 or pole_length_matches[0] == ''):
            pole_length_matches = reg.findall(text)

    setting_depth_matches = setting_depth_regexes[0].findall(text)
    for reg in setting_depth_regexes:
        if (len(setting_depth_matches) == 0 or setting_depth_matches[0] == ''):
            setting_depth_matches = reg.findall(text)

    # Extracting values
    if pole_length_matches:
        pole_length = pole_length_matches
        pole_class = pole_length_matches
    else:
        pole_length = None
        pole_class = None

    setting_depth = setting_depth_matches if setting_depth_matches else None

    # Return a dictionary with the extracted values
    return {
        "pole_length": pole_length,
        "pole_class": pole_class,
        "setting_depth": setting_depth,
        "at_replace": bool_at_replace
    }


# Example usage
parameters = extract_parameters_from_con(cnd_text)
# print("Con")
# print(parameters)

# Example usage
parameters2 = extract_parameters_from_ocl(ocl_text)
# print("Ocl")
# print(parameters2)

# print(re.compile(r"[345][05]").findall(parameters))
# print(re.compile(r"[345][05]").findall(parameters))
# print(re.compile(r"[12345h]").findall(parameters))
# print(re.compile(r"[345][05]").findall(parameters2))
# print(re.compile(r"[12345h]").findall(parameters2))

lenoutputs = re.compile(
    r"[345][05]").findall(parameters['pole_length'][0])

if (len(lenoutputs)  >= 1):
    con_pole_length1 = float(lenoutputs[0])
# print(parameters['pole_length'])
if (len(lenoutputs) > 1):
    # print("len is > 1")
    con_pole_length2 = float(lenoutputs[1])
else:
    # print("len is <= 1")
    con_pole_length2 = float(con_pole_length1)

con_pole_class = float(re.compile(
    r"[12345h]").findall(parameters['pole_class'][0])[-1])
if (parameters['setting_depth']):
    con_pole_depth = float(re.compile(
        r"[6-9][,.]?[05]?").findall(parameters['setting_depth'][0])[0])
ocl_pole_length = float(re.compile(
    r"[345][05]").findall(parameters2['pole_length'][0])[0])
ocl_pole_class = float(re.compile(
    r"[12345]").findall(parameters2['pole_class'][0])[-1])
ocl_pole_depth = float(re.compile(
    r"[6-9][,.]?[05]?").findall(parameters2['setting_depth'][0])[0])

at_replace = parameters2['at_replace']


bool_for_class = False
bool_for_depth = False
bool_for_length = False
if (not parameters['setting_depth']):
    # if (con_pole_depth == None):
    if (at_replace):
        bool_for_depth = True
    else:
        bool_for_depth = False
else:
    if (abs(con_pole_depth - ocl_pole_depth)/ocl_pole_depth <= 0.05):
        bool_for_depth = True


# print(f"con depth: {con_pole_depth}")
# print(ocl_pole_depth)
# print(bool_for_depth)
# print((con_pole_length1 - ocl_pole_length)/ocl_pole_length)
# print(con_pole_length1)
# print(con_pole_length2)
# print(f"class: {con_pole_class}")
# print(ocl_pole_class)
# print(ocl_pole_length)


if (abs(con_pole_length1 - ocl_pole_length)/ocl_pole_length <= 0.05):
    bool_for_length = True


# print((con_pole_length2 - ocl_pole_length)/ocl_pole_length)
# print(ocl_pole_length)
# print(con_pole_length2)

if (abs(con_pole_length2 - ocl_pole_length)/ocl_pole_length <= 0.05):
    bool_for_length = True

if (ocl_pole_class == con_pole_class):
    bool_for_class = True
print(f"pole length: {bool_for_length}, ")
print(f"pole class: {bool_for_class}, ")
print(f"setting depth: {bool_for_depth}, ")

if (bool_for_class & bool_for_length & bool_for_depth):
    print("PASSED")
else:
    print("FAILED")

end_time = time.process_time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")