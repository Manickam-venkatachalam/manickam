import configparser
import colorama
from colorama import Fore


# print(Fore.PINK + 'This text is red in color')

# CREATE OBJECT
config_file = configparser.ConfigParser()
print("enter the profile name")
profile = input('press 1 to to edit name or press Enter to continue with default name: ')
if profile == '1':
    profile_name = input("enter the profile name: ")
else : 
    profile_name = 'default'
print ("your profile name is '{}'".format(profile_name))
access_key = input('AWS Access Key ID [****************MRPG] ')
secrets_key = input('AWS Secret Access Key [****************Z7+l] ')

region = input('press 1 to enter the region name or press 2 for list region press enter to leave default: ')
if region == '1':
    region = input("enter the region name: ")
elif region == '2':
    print("1: us-east-1 US East (N. Virginia)")
    print("2: us-east-2 US East (Ohio)")
    print("3: us-west-1 US West (N. California)")
    print("4: us-west-2 US West (Oregon)")
    print("5: af-south-1 africa(Cape Town)")
    print("6: ap-east-1 Asia Pacific (Hong Kong)")
    print("7: ap-southeast-3 Asia Pacific (Jakarta)")
    print("8: ap-south-1 Asia Pacific (Mumbai)")
    print("9: ap-northeast-3 Asia Pacific (Osaka)")
    print("10: ap-northeast-2 Asia Pacific (Seoul)")
    print("11: ap-northeast-1 Asia Pacific (Singapore)")
    print("12: ap-northeast-1 Asia Pacific (Tokyo)")
    print("13: ap-southeast-2 Asia Pacific (Sydney)")
    print("14: ap-northeast-1 Asia Pacific (Tokyo)")
    print("15: aa-central-1 canada(Central)")
    print("16: au-central-1 Europe (Frankfurt)")
    print("17: eu-west-1 Europe (Ireland)")
    print("18: eu-west-2 Europe (London)" )
    print("19: eu-south-1 Europe (Milan)")
    print("20: eu-west-3 Europe (Paris)")
    print("21: eu-north-1 Europe (Stockholm)")
    print("22: me-south-1 Middle East (Bahrain)")
    print("23: sa-east-1 South America (Sao Paulo)")
    input("enter the region name from the above list[us-east-1]: ")
else: 
    region = 'us-east-1'


# ADD SECTION
config_file.add_section("AWSSettings")
# ADD SETTINGS TO SECTION
config_file.set("AWSSettings", "access_key", access_key)
config_file.set("AWSSettings", "secrets_key",secrets_key)
config_file.set("AWSSettings", "profile_name", profile_name)
config_file.set("AWSSettings", "region", region)

# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("config were created successfully")

# PRINT FILE CONTENT
read_file = open("configurations.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()