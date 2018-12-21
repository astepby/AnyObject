# coding: utf-8
import sys, os
sys.path.append(os.pardir)
from xml.etree.ElementTree import parse
from namespaces import servicegroup as ns_sg
from namespaces import dto as ns_dto

#servicegroupxml = parse("./../../servicegroup/licenseCheck/config/servicegroup.xml")
#tree = parse("/home/yunjy/development/anyObject/jenkins/workspace/Po7_Sys/TestSG/meta/com/tmax/DemoEMPDTO.dto")
#path_dto        = parse("/home/IMS/workspace/ims_sg/meta/com/tmax/ims/SampleDo.dto")
path_xmlHome="/home/IMS/workspace/ims_sg/download/config/"
path_dtoHome="/home/IMS/workspace/ims_sg/meta/"

def function():
    print("anyObject: xml parse")
    return

def getSO():
    path_servicegroupxml = parse(path_xmlHome + "servicegroup.xml")
    root = path_servicegroupxml.getroot()

    List_SO = []
    List_all = []

    for group_name in root.findall("ns14:group-name", ns_sg):
        print("group-name: \t", end="")
        print(group_name.text)

    for service_object in root.findall("ns14:service-object", ns_sg):
        print("service_object: \t", end="")
        print(service_object.text)

        List_one = {}
        for name in service_object.findall("ns14:name", ns_sg):
            print("name: \t", end="")
            print(name.text)
            List_SO.append(name.text)
            List_one["name"] = name.text

        for class_name in service_object.findall("ns14:class-name", ns_sg):
            print("class-name: \t", end="")
            print(class_name.text)
            List_one["class-name"]=class_name.text

        for logical_name in service_object.findall("ns14:logical-name", ns_sg):
            print("logical-name: \t", end="")
            print(logical_name.text)
            List_one["logical-name"]=logical_name.text

        for input_dto in service_object.findall("ns14:input-dto", ns_sg):
            print("input-dto: \t", end="")
            print(input_dto.text)
            List_one["input-dto"]=input_dto.text

        for output_dto in service_object.findall("ns14:output-dto", ns_sg):
            print("output-dto: \t", end="")
            print(output_dto.text)
            List_one["output-dto"]=output_dto.text
        List_all.append(List_one)


    return List_all

def getDTO(path_dto, DTO_type, SO_class_name):

    path_dtoEach = parse(path_dto)
    root = path_dtoEach.getroot()

    List_all = []
    List_logicalName = []
    for dtoField in root.findall("ns9:dtoField", ns_dto):
        #print("dtoField: \t", end="")
        #print(dtoField.attrib["logicalName"])
        #List_logicalName.append(dtoField.attrib["logicalName"])
        dtoField=dtoField.attrib.items()
        dtoField = list(dtoField)
        print(dtoField)
        dtoField_SO={}
        dtoField_DTO = [("DTO-type", DTO_type)]
        dtoField_SO=[("SO_class-name", SO_class_name)]+[("SO", SO_class_name.split(".")[-1])]
        print(dtoField_SO)
        print(type(dtoField))
        print(type(dtoField_SO))
        print("asdf")
        print(dtoField+dtoField_DTO+dtoField_SO)
        List_all.append(dtoField+dtoField_DTO+dtoField_SO)

    #return List_logicalName
    return List_all

SOs=getSO()
print("")
print("")
print("")
for SO in SOs:
    print(path_dtoHome+SO['input-dto'].replace(".","/")+".dto")
    path_dto=path_dtoHome + SO['input-dto'].replace(".", "/") + ".dto"
    inputDTOs=getDTO(path_dto,'input-dto',SO['class-name'])

    print(path_dtoHome + SO['output-dto'].replace(".", "/") + ".dto")
    path_dto = path_dtoHome + SO['output-dto'].replace(".", "/") + ".dto"
    outputDTOs =getDTO(path_dto,'output-dto',SO['class-name'])

print("")
print("")
print("")
print(SOs)
print(inputDTOs)
print(outputDTOs)
DTOs=[inputDTOs,outputDTOs]

print(DTOs)
print(len(DTOs))



def findDTO(logicalName,DTOs):
    List_DTOs=[]
    for DTO in DTOs:
        for attrbs in DTO:
            attrbs=dict((attrbs))
            #print(dict((attrbs)))

            if (logicalName==attrbs["logicalName"]):
                print(attrbs["logicalName"], attrbs["DTO-type"], attrbs["SO_class-name"])
                item=[attrbs["logicalName"], attrbs["DTO-type"], attrbs["SO_class-name"]]
                List_DTOs.append(item)
    print(List_DTOs)
    return(List_DTOs)




print("Fields by DTOs")
fieldsByDTOs=findDTO("EMPNO",DTOs)

print("Fields by DTOs")
for fieldByDTos in fieldsByDTOs:
    print(fieldByDTos)





