import json,os

"""
    The question is: Can you extract the data from a file and split it into two different files? 
    To split the data, the following condition applies: Within the data, 
    instances of "completed": false and "completed": true should be identified. 
    Subsequently, place the entries with "completed": false in one file, 
    and the ones with "completed": true in another file. If there are any instances with data mismatches, 
    they should be placed in a separate file.
"""

def find_folder():
    return os.path.dirname(os.path.abspath(__file__))

def loadData_file():
    file = os.path.join(find_folder(),"data.json")
    return open(file,"r")

def convert_jsonTodict():
    file = loadDato_file()
    dict = json.loads(file)
    return dict


def extract_data():
    converted_data = convert_jsonTodict() 
    for i in converted_data:
        print(i)
        

extract_data()


