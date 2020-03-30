import re
from pprint import pprint

# directory = "/home/user/dev/raw"

with open('./raw/rx1912010001.BBO', 'r') as file:

    order = file.read()
    # print(order)


# './raw/rx1911180001.ILO'
# './raw/rx1912010001.BBO'
# './raw/rx1912010001.MGO'

ORD_ANA = re.findall(r"STX=ANA[A]?[:]?[:1]?[\+]?(5\d{12})", order)
# May be useful as 'if-not-match-switch' for reroutes n ting
ORD_OAK = re.findall(r"\+(5\d{11}2)", order)
ORD_DATE = re.findall(r"\+(\d{6}):", order)
ORD_TYPE = re.findall(r"TYP=[:]?(\d{4})", order)
ORD_NUMS = re.findall(r"ORD=[:]?(.*)[:][::]", order)
ORD_DIN = re.findall(r"DIN=[:]?(\d{6})[\+\+]?[\+]?", order)
ORD_SUPL = re.findall(r"SDT=[:]?(\d+)[:]?[\+]?[\+]?(.*)'", order)
ORD_RTAL = re.findall(r"CDT=[:]?(\d+)[:]?[\+]?[.+]?[\+]?(.+)[\+]?'", order)
ORD_DEPO = re.findall(r"CLO=[:]?(\d+)[:]?(.{2,3})[\+\+]?[\+]?(.*)'", order)


# Ewwww
ORD_LINE = re.findall(
    r"OLD=[:]?[\d{1}][\+](.{13}?)?[:|\+|\+\+:]?(.+?)?[\+]?[\+\+:]?[:]?[\+\+:]?(\d+?)?[\+\+]?[+](\d+)?[+](\d+)\+\+\+\+?(.+?)?'", order)

pprint(ORD_NUMS)
