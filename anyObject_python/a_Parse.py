# coding: utf-8
import sys, os
sys.path.append(os.pardir)
from xml.etree.ElementTree import parse

def function():
    print("xml parse")
    return

tree = parse("../servicegroup/licenseCheck/config/servicegroup.xml")
root = tree.getroot()


root = tree.getroot()
for element in root.findall("song"):
    print(element.findtext("title"))
    print(element.findtext("length"))

#print(root.findall("service-group"))
#print(root.get("service-group"))


#for element in root.findall("ns11:service-group"):
#    print(type(element))

#print(note.keys())
#print(note.items())
##print(note.get("ns11:name"))
#print(note.findall("ns11"))