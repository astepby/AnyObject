# coding: utf-8
import sys, os
sys.path.append(os.pardir)
from xml.etree.ElementTree import parse


def function():
    print("xml parse")
    return

def getSO():
    tree = parse("../servicegroup/licenseCheck/config/servicegroup.xml")
    root = tree.getroot()
    namespaces = {'ns11': 'http://www.tmax.co.kr/proobject/servicegroup',
                  'ns21': 'http://www.tmax.co.kr/proobject/contents'}

    root = tree.getroot()
    print(root.findall("ns11:group-name"), namespaces)

    names = []
    for group_name in root.findall("ns11:group-name", namespaces):
        print("group-name: ", end="")
        print(group_name.text)

    for service_object in root.findall("ns11:service-object", namespaces):
        print("service_object: ", end="")
        print(service_object.text)

        for name in service_object.findall("ns11:name", namespaces):
            print("name: ", end="")
            print(name.text)
            names.append(name.text)

        for class_name in service_object.findall("ns11:class-name", namespaces):
            print("class-name: ", end="")
            print(class_name.text)

        for input_dto in service_object.findall("ns11:input-dto", namespaces):
            print("input-dto: ", end="")
            print(input_dto.text)

        for output_dto in service_object.findall("ns11:output-dto", namespaces):
            print("output-dto: ", end="")
            print(output_dto.text)

    list_SO=names
    print(list_SO)

    return list_SO


tree = parse("../servicegroup/licenseCheck/config/servicegroup.xml")
root = tree.getroot()
namespaces = {'ns11': 'http://www.tmax.co.kr/proobject/servicegroup',
              'ns21': 'http://www.tmax.co.kr/proobject/contents'}

root2 = tree.getroot()
print(root.findall("ns11:group-name"),namespaces)

names = []
for group_name in root2.findall("ns11:group-name", namespaces):
    print("group-name: ", end="")
    print(group_name.text)

for service_object in root.findall("ns11:service-object", namespaces):
    print("service_object: ", end="")
    print(service_object.text)

    for name in service_object.findall("ns11:name",namespaces):
        print("name: ", end="")
        print(name.text)
        names.append(name.text)

    for class_name in service_object.findall("ns11:class-name",namespaces):
        print("class-name: ", end="")
        print(class_name.text)

    for input_dto in service_object.findall("ns11:input-dto",namespaces):
        print("input-dto: ", end="")
        print(input_dto.text)

    for output_dto in service_object.findall("ns11:output-dto",namespaces):
        print("output-dto: ", end="")
        print(output_dto.text)


print(names)

