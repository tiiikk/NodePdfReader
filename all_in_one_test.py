# for cnd
import easyocr
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


def extract_numbers(string):
    numbers = re.findall(r"\d+", string)
    return numbers


cnd_text = "CONSTRUCTION NOTE PRIVATE 1 TRUCK  ACCESSIBLE PROPERTY L1149 30E 45' 40' 62'4 SAPH101258094 12W 59' 40' /45' 4 SET 7.5' DEEP HARD  SET   SOUTH REUSE EXISTING ANCHOR A 20M EXP _ 24'/255' 4 REM:   RUSTED ANCHOR B 20M EXP 16'/13 8 3 REM: 2-5/16 PRI DG INST:   20M PISA 13'/13 83 INST: 4-3/8 PRI DG 8 8 VICINITY SKETCH 2 1 g CURRUSIUN AREA: NUN LINSULAIIUN VISI: D LaiI Veiuig Yuu Viy_II ISSULS IPWEIE NUIIF: 125824640 LAIE: 0//0b/*2U25 EXEMPTEQUIP INST : N/A FIRE  AREA: SRA-TIER 3 GAS CONFUCT: NO NEAR LOC: N/A PM: 35416495 SHEET: OF 1 REV: 0 5 0 12K 3-2AR 3-2AR 4 0 1 6 Shey Way Pondero8s ] ] 1 8 328228882 8 1 2 08 3 #8e7e8- 1 0 3 g ~ 28 p 8 7 43 2 2 31 8 3 3 1 8 0J 3 3 > U 761 2 8 af 1 I 3 1 8 Acl ! 8 8 8 8 5 8 SSD RECLOSER   13438 31 25 MILES 3 1 0 0 J 0 8 I 3 2 VSOUJONOd Sih7 S771H 8-7 05 3-2AR 12W 262' 1 "
# both
ocl_text = "0-Calc@ ProAnalysis GO 95 Thursday, March 23,2023 12.25 PM SAP Equip ID: TBA Pole Length Class: 45 /4 Code: GO 95 Structure Type: Angle PM Order Number 35416495 Species: DOUGLAS FIR GO 95 Rule: At Installation (New) Pole Strength Factor: 0.33 Estimator LAN ID JE3X   Setting Depth (ft): 7.5 Construction Grade: B Transverse Wind LF: 1.00 Sketch Location GIL Circumference (in): 34.46   Loading District: Heavy Wire Tension LF: 1.00 Joint Pole Number NIA GIL Fiber Stress (psi): 7,600 Ice Thickness (in): 0.50 Vertical LF: 1.00 Notification 123824640 Allowable Stress (psi): 2,408 Wind Speed (mph): 48.41 Pole Factor of Safety: 4.91 Aux Data 6 Unset Fiber Stress Ht. Reduc: No Wind Pressure (psf): 6.00 Vertical Factor of Safety: 5.60 Latitude: 38.47714 Longitude: -120.627109 Elevation: 2909.61' Bending Factor of Safety: 6.12 Pole Capacity Utilization (%) Height Wind Angle Crossarm allowance 300 Ibs (ft) (deg) Maximum 61.0 0.0 144.1 Groundline 61.0 0.0 143.4 Vertical 53.6 34.3 134.0 Pole Moments (ft-Ib) Load Angle Wind Angle Crossarm allowance 300 Ibs (deg) (deg) Max Util 12,758 143.4 144.1 Groundline 12,758 143.4 143.4 GL Allowable 26,007 Overturn 67,000 3/23/23 User:je3x PGE OCP:6.02 Includes Load Factor(s) Page 1 of 4 2 Worst Wind Per Wire Wind At 144.1 LOC_1 Cap Guy Pole ID: 7701103793 0-Calc@ Pro Analysis GO 95 Thursday, March 23,2023 12.25 PM System Component Summary Load From Worst Wind Individual Maximum Load Angle on Pole With Overload Applied Description Lead Length Lead Angle Height Nominal Wind Angle Max* Load Wind Angle (ft) (deg) (ft) Capacity (%) (deg) Capacity (%) (deg) Anchor 2OM 13.0 13.0 66.6 144.1 66.6 140.6 EHS 3/8 (Down) 36.5 84.9 144.1 84.9 138.4 EHS 3/8 (Down) 34.5 88.2 144.1 88.2 142.7 Anchor 20M 24.0 255.0 40.9 144.1 41.7 105.0 EHS 3/8 (Down) 36.3 50.8 144.1 51.7 110.0 EHS 3/8 (Down) 31.5 55.3 144.1 56.6 100.0 System Capacity Summary: Adequate Adequate Groundline Load Summary Reporting Angle Mode: Load Reporting Angle: 143.49 Shear Applied Bending Applied Pole Bending Vertical Vertical Total Pole Load* Load Moment Moment Capacity Stress Load Stress Stress Capacity (Ibs) (%) (ft-Ib) (%) %) (+I- psi) (Ibs) (psi) (psi) '%) Powers 5,347 572.7 79,876 626.1 307.1 17,216 -46 17,215 714.8 GuyBraces -4,603 -493.0 -68,806 5539.3 264.6 -14,830 19,327 205 -14,625 -607.3 Pole 166 17.7 1,337 10.5 5.1 288 975 10 299 12.4 Crossarms 15 1.6 213 1.7 0.8 46 126 47 2.0 Insulators 9 1.0 139 1.1 0.5 30 66 31 1.3 Pole Load 934 100.0 12,758 100.0 49.1 2,750 20,448 216 2,966 123.2 Pole Reserve Capacity 13,249 50.9 341 5558 23.2 Load Summary by Owner Reporting Angle Mode: Load Reporting Angle: 143.49 Shear Applied Bending Applied Pole Bending Vertical Vertical Total Pole Load* Load Moment Moment Capacity Stress Load Stress Stress Capacity (Ibs) (%) (ft-Ib) (%) (%) (+I- psi) (Ibs) (psi) (psi) (%) PG&E 934 100.0 12,758 100.0 49.1 2,750 20,448 216 2,966 123.2 Totals: 934 100.0 12,758 100.0 49.1 2,750 20,448 216 2,966 123.2 Detailed Load Components: Power Owner Height Horiz_ Cable Sag at Cable LeadiSpan Span Wire Tension Tension Offset Wind Moment (ft) Offset Diameter Max Weight Length Angle Length (Ibs) Moment* Moment* Moment* at (in) (in) Temp (Ibslft) (ft) (deg) (ft) (ft-Ib) (ft-Ib) (ft-Ib) (ft-Ib) (ft) Primary 2 (7/1) ACSR PG&E 36.75 11.39 0.3250 0.95 0.107 261.1 192.9 261.1 1,690 40,225 29 1,822 42,077 (SPARATE) HVY Includes Load Factor(s) Page 2 of 4 2 Worst Wind Per Guy Wire Wind At 144.1 Guy GL Pole ID: 7701103793 0-Calc@ Pro Analysis GO 95 Thursday, March 23,2023 12.25 PM Primary 2 (7M1_ ACSR PG&E 36.42 11.40 0.3250 0.06 0.107 58.3 75.1 58.3 1,690 22,701 -19 610 23,293 (SPARATE) HVY Primary 2 (7/1) ACSR PG&E 34.92 48.03 0.3250 0.96 0.107 262.0 193.3 262.0 1,690 37,919 34 1,759 39,712 (SPARATE) HVY Primary 2 (7/1) ACSR PG&E 34.92 48.07 0.3250 0.96 0.107 261,44 193.2 261.4 1,690 38,038 32 1,747 39,753 (SPARATE) HVY Primary 2 (7/1) ACSR PG&E 31.92 47.76 0.3250 0.06 0.107 59.1 77.4 59.1 1,690 21,778 55 524 22,357 (SPARATE) HVY Primary 2 (7/1) ACSR PG&E 31.92 47.77 0.3250 0.06 0.107 58.7 73.3 58.7 1,690 18,222 557 551 18,715 (SPARATE) HVY Totals: 178,883 7,013 185,908 Crossarm Owner Height Horiz: Offset Rotate Unit Unit Unit Depth Unit Offset Wind Moment at (ft) Offset Angle Angle Weight Height (in) Length Moment* Moment* GL* (in) (deg) (deg) (Ibs) (in) (in) (ft-Ib) (ft-Ib) (ft-Ib Normal 9L Composite Dead-End PG&E 34.92 5.80 13.2 13.2 63.00 3.63 4.63 108.00 -20 407 388 Arm Normal 9L Composite Dead-End PG&E 31.92 55.97 72.5 72.5 63.00 3.63 4.63 108.00 10 118 108 Arm Totals: 30 526 496 Insulator Owner Height Horiz_ Offset Rotate Unit Unit Unit Offset Wind Moment at (ft) Offset Angle Angle Weight Diameter Length Moment* Moment* GL* (in) (deg) (deg) (Ibs (in) (in) (ft-Ib; (ft-Ib) (ft-Ib Deadend Insulator PG&E 36.75 0.00 193.0 193.0 8.99 3.00 8.00 37 37 Deadend Insulator PG&E 36.42 0.00 90.0 90.0 8.99 3.00 8.00 36 36 Pin Pin-Poly Light 7.5 PG&E 35.07 550.00 289.8 0.0 6.00 5.50 7.50 61 61 Deadend Insulator PG&E 34.92 48.00 96.3 180.1 8.99 3.00 8.00 35 35 Deadend Insulator PG&E 34.92 -48.00 290.1 180.1 8.99 3.00 8.00 35 35 Pin Insulator PG&E 32.07 50.00 169.3 0.0 6.00 5.50 7.50 55 55 Deadend Insulator PG&E 31.92 -48.00 335.4 2.0 8.99 3.00 8.00 32 32 Deadend Insulator PG&E 31.92 48.00 169.6 2.0 8.99 3.00 8.00 32 32 Totals: 323 323 Wire and Brace Owner Attach End Height Lead/Span Wire Percent Lead Angle Incline Wire Weight Rest Length Stretch Height (ft) Length Diameter Solid (deg) Angle (Ibslft) (ft) Length (ft) (ft) (in) (%) (deg) (in) EHS 3/8 Down PG&E 36.50 0.00 13.00 0.375 75.00 13.0 70.2 0.273 43.30 1.78 EHS 3/8 PG&E 34.50 0.00 13.00 0.375 75.00 13.0 69.1 0.273 41,.38 1,.77 EHS 3/8 PG&E 36.25 0.00 24.00 0.375 75.00 255.0 56.3 0.273 47.26 1.17 EHS 3/8 Down PG&E 31.50 0.00 24.00 0.375 75.00 255.0 52.5 0.273 43.13 1.16 Includes Load Factor(s) Page 3 of 4 2 Worst Wind Per Wire 3 Wind At 144.1 Guy Down Down Guy"


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
            r"[345]?[05]?\s*'?\s*\/?\s*[345][05]\s*'\s*[\-_*]?CL\s*[12345h]"),
        re.compile(
            r"[345][05]\s*'?\s*\/\s*[345][05]\s*'?\s*-?\s*[12345h]"),
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
            r"[345][05]\s*'?\s*\/\s*?[345][05]\s*'?\s*[12345h]"),
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
        "setting_depth": setting_depth
    }


# Example usag
parameters = extract_parameters_from_con(cnd_text)
print(parameters)

# Example usag
parameters2 = extract_parameters_from_ocl(ocl_text)
print(parameters2)


# print(re.compile(r"[345][05]").findall(parameters))
# print(re.compile(r"[345][05]").findall(parameters))
# print(re.compile(r"[12345h]").findall(parameters))
# print(re.compile(r"[345][05]").findall(parameters2))
# print(re.compile(r"[12345h]").findall(parameters2))

con_pole_length1 = float(re.compile(
    r"[345][05]").findall(parameters['pole_length'][0])[0])
print(parameters['pole_length'])
if (len(parameters['pole_length'][0]) > 1):
    print("len is > 1")
    con_pole_length2 = float(re.compile(
        r"[345][05]").findall(parameters['pole_length'][0])[1])
else:
    print("len is <= 1")
    con_pole_length2 = con_pole_length1

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
print(ocl_pole_depth)
print(bool_for_depth)
print((con_pole_length1 - ocl_pole_length)/ocl_pole_length)
print(con_pole_length1)
print(con_pole_length2)
print(f"class: {con_pole_class}")
print(ocl_pole_class)
print(ocl_pole_length)


if (abs(con_pole_length1 - ocl_pole_length)/ocl_pole_length <= 0.05):
    bool_for_length = True


print((con_pole_length2 - ocl_pole_length)/ocl_pole_length)
if (abs(con_pole_length2 - ocl_pole_length)/ocl_pole_length <= 0.05):
    bool_for_length = True

if (ocl_pole_class == con_pole_class):
    bool_for_class = True
print(bool_for_length)
print(bool_for_class)
print(bool_for_depth)

if (bool_for_class & bool_for_length & bool_for_depth):
    print("passed")
else:
    print("failed")
