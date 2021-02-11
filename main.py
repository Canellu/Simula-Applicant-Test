#Simula: Project - Stem Cell database

import yaml
import requests

#Exercise 1
#Returns the URL found in yaml-file.
def read_yaml_url():
    with open("D:\Documents\Python\Simula - Stem Cell\input.yaml") as file: #Manages the file
        return yaml.full_load(file)["url"] #Returns value from field "url"


#Exercise 2
#Returns a list containing dictionaries as data from the URL
def get_url_data():
    response = requests.get(read_yaml_url())

    #Checking if data is succesfully collected.
    if response:
        print("Data acquired!")
        return response.json()
    else:
        print("Couldn't retrieve data.")
        return None


#Exercise 3
#Prints total number of elements for each distinct userId.
def print_userId(list): #parameter is a list with data from url in yaml-file

    new_list = [dict["userId"] for dict in list] #new list containing all the userIds (including duplicates) from our data.

    new_dict = {userId: new_list.count(userId) for userId in new_list} #A dictionary containing unique userIds as keys and the amount of each as value.

    #printing formatted key and value pairs from new_dict.
    print("Total num: " + str(len(new_list)) + "\n{:>6}{:>6}".format("userId", "Num"))
    for key, value in new_dict.items():
        print("{:>6}{:>6}".format(key, value))
    print()


#Exercise 4
#Create a new list consisting only of elements with 'completed == True'
def only_completed_true(list): #parameter is list with data from url in yaml-file

    new_list = [element for element in list if element["completed"] == True] #Creates new list with elements fullfilling condition: "completed == True"

    #for Exercise 6
    return new_list


#Exercise 5
#Print total number of elements for each distinct userId from list with elements "completed == True"
def print_userId_completed(list): #parameter is list with data from url in yaml-file

    print("Users with complete status 'true':")
    print_userId(only_completed_true(list))


#Exercise 6
#Saving list from Exercise 4 to file "output.yaml"
def output_yaml(list):
    with open("D:\Documents\Python\Simula - Stem Cell\output.yaml", 'w') as file: #Manages the file
        stream = yaml.dump(list, sort_keys=False)
        file.write(stream.replace('\n- ', '\n\n- '))#writes stream to file with formatting some formatting
        print("Output.yaml created!")



#Lines to run our program---
data = get_url_data() #Our data in form of list containing dicts to be passed as argument to functions.

print_userId(data)
print_userId_completed(data)
#output_yaml(only_completed_true(data)) #uncomment to create output.yaml to specified path.
