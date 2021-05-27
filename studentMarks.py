
import json
import csv
import os

filename= "studentMarksList.txt"
resultFile = "./results.txt"

""" Method takes input as textfile and output as dict """


def textToDict(filename):

    with open(filename) as f:
        fileContent = f.read()

    skip= ["{","}","[","]",":","\n","\r","\t"," "]

    for skp in skip:
        fileContent = fileContent.strip(skp)

    findName = fileContent.find("name")
    fileContent = fileContent[findName+6:]

    for skp in skip:
        fileContent = fileContent.strip(skp)

    fileContent = fileContent.split("\n")

    studentDict = {}

    for i in fileContent:
        cont = i.strip("\n").strip("\r").strip("\t").strip(" ")
        idx = cont.find(":")
        nameList = cont[:idx]
        nameList = nameList.strip('"')
        marks = cont[idx+1:]
        marks = marks[:-1]

        studentDict[nameList] = marks
    return studentDict



# Calling textToDict Function

studentDict = textToDict(filename)

for student in studentDict:
    myList = studentDict[student]
    myList = myList[1:-1]

    marksList = list(myList.split(","))

    total = 0
    count = 0
    for mark in range(len(marksList)):
        marks = float(int(marksList[mark]))
        total = total + marks
        avg = total / len(marksList)

    try:
        with open("results.txt","a+") as resIn:
            res = " --> Name: "+student + " | Total: "+ str(total) +" | Average: "+ str(avg) +"\n"
            resIn.writelines(res)
            print(res)
    except Exception:
        print("File Error")