"""
Configure the setup.yaml file before executing this script
"""

import yaml

PARAM_FILE = "C:\\Users\\Somnath\\PycharmProjects\\TestDataGenerator\\setup.yml"

with open(PARAM_FILE, 'r') as f:
    doc = yaml.load(f, Loader=yaml.FullLoader) # also, yaml.SafeLoader
    STATE_CODE_FILE_TYPE = doc["state_code_file"]["file_type"]
    STATE_CODE_FILE_NAME = doc["state_code_file"]["file_name"]
    PARTY_FILE_TYPE = doc["party_data_file"]["file_type"]
    PARTY_FILE_NAME = doc["party_data_file"]["file_name"]

    TrizettoFile1 = doc["TrizettoORG"]
    TrizettoFile2 = doc["TrizettoProvider"]

    print("Seed Data File #######################################")
    print("Party File Name : " + PARTY_FILE_NAME)
    print(TrizettoFile1)
    print(TrizettoFile2)
    print("\n")
