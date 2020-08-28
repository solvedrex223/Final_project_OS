'''
At the time this file only contains general use parsing functions


'''
import os
import sys

string = sys.path[0]
string = string.split("/")
while string[len(string) - 1] != "web_server":
    string.pop()
string.append("file_system")
string.append("FileSystem")
string.append("Packages")
for i in range(len(string)):
    string[i]+= "/"
string = "".join(string)
route = string+"hard_drive/"

def string_to_int(string):
    binary  = ""
    num = 0
    for char in string:
        binary += format(ord(char), '08b')
    for char in binary:
        binary = char + binary[:-1]
    for i in range(len(binary)):
        num += int(binary[i]) * 2 ** i
    return num

def int_to_string(num, bytes):
    string = "{0:b}".format(num)
    string =  "0" *  (8*bytes - (len(string))) + string
    newstring = ""
    for i in range(len(string)//8):
        number = 0
        for j in range(7,-1,-1):
            number += int(string[i*8+7-j])* (2 ** j)
        newstring += chr(number)
    return newstring

def write_str_bin(file, string):
    for char in string:
        file.write(bytes([ord(char)]))
    return

def bytes_to_string(byte_array):
    string= ""
    for char in byte_array:
        string += chr(char)
    return string