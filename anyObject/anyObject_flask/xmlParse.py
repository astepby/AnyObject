# coding: utf-8
import sys, os
sys.path.append(os.pardir)
from xml.etree.ElementTree import parse
from namespaces import servicegroup as sg

#servicegroupxml = parse("./../../servicegroup/licenseCheck/config/servicegroup.xml")
#tree = parse("/home/yunjy/development/anyObject/jenkins/workspace/Po7_Sys/TestSG/meta/com/tmax/DemoEMPDTO.dto")
dto             = parse("/home/IMS/workspace/ims_sg/meta/com/tmax/ims/SampleDo.dto")
servicegroupxml = parse("/home/IMS/workspace/ims_sg/download/config/servicegroup.xml")
root = servicegroupxml.getroot()

def function():
    print("anyObject: xml parse")
    return

def getSO():
    List_SO = []
    #a={"SO":{"class-name":"c", "logical-name":"l", "input-dto":"asdf", "output-dto":"out"}}

    for group_name in root.findall("ns14:group-name", sg):
        print("group-name: \t", end="")
        print(group_name.text)

    for service_object in root.findall("ns14:service-object", sg):
        print("service_object: \t", end="")
        print(service_object.text)

        for name in service_object.findall("ns14:name", sg):
            print("name: \t", end="")
            print(name.text)
            List_SO.append(name.text)

        for class_name in service_object.findall("ns14:class-name", sg):
            print("class-name: \t", end="")
            print(class_name.text)
        for logical_name in service_object.findall("ns14:logical-name", sg):
            print("logical-name: \t", end="")
            print(logical_name.text)

        for input_dto in service_object.findall("ns14:input-dto", sg):
            print("input-dto: \t", end="")
            print(input_dto.text)

        for output_dto in service_object.findall("ns14:output-dto", sg):
            print("output-dto: \t", end="")
            print(output_dto.text)

    return List_SO

SOs=getSO()
print(SOs)