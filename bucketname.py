import re
  

# from s3files import *
  
# bucketname=manickam()
# print(bucketname)

# from mysql_connect import *
# objectname, object_url, file_size, FILE_NAME = 'mysql_conncetcheck1', 'https://manickam1.me', '123456', 'success'

# manickam(objectname, object_url, file_size, FILE_NAME)
# print('function ivoked sucessfully the file inserted in mysql') 

# myTuple = input("enter the file name: ")

# x = "_".join(myTuple)

# print(x)

# def remove(string):
#     return string.replace(" ", "")

# sample= remove("this is a sample string")
# print(sample)

# def remove(string):
#     pattern = re.compile(r'\s+')
#     return re.sub(pattern, '', string)
      
# # Driver Program
# string = ' muthukarthi resume.pdf '
# print(remove(string))

# import re

# def camelCase(tag_str):
#     words = re.findall(r'\w+', tag_str)
#     nwords = len(words)
#     if nwords == 1:
#         return words[0] # leave unchanged
#     elif nwords > 1: # make it camelCaseTag
#         return words[0].lower() + ''.join(map(str.title, words[1:]))
#     return '' # no word characters

# sample= camelCase('muthukarthi.png')
# print(sample)

# a_string = "manickam resume.pdf"

# new_string = a_string.replace(" ", "_")

# print(new_string)

# import configparser
# from turtle import screensize

# # CREATE OBJECT
# config_file = configparser.ConfigParser()

# access_key = 'AKIAJ7Z5ZQZ5Z5Z5Z5Z5'
# secrets_key = 'asdaddfsfwefwedfcsasadasadad'
# profile_name = 'default'

# # ADD SECTION
# config_file.add_section("AWSSettings")
# # ADD SETTINGS TO SECTION
# config_file.set("AWSSettings", "access_key", access_key)
# config_file.set("AWSSettings", "secrets_key",secrets_key)
# config_file.set("AWSSettings", "profile_name", profile_name)

# # SAVE CONFIG FILE
# with open(r"configurations.ini", 'w') as configfileObj:
#     config_file.write(configfileObj)
#     configfileObj.flush()
#     configfileObj.close()

# print("Config file 'configurations.ini' created")

# # PRINT FILE CONTENT
# read_file = open("configurations.ini", "r")
# content = read_file.read()
# print("Content of the config file are:\n")
# print(content)
# read_file.flush()
# read_file.close()

print("working")