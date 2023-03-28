#!/bin/python3

import os
import sys
import requests

basepath='wordlists-nginx'

file_names = []

with os.scandir(basepath) as entries:

    for entry in entries:
        if entry.is_file():
            file_names.append(entry.name)



host=sys.argv[1]

for filename in file_names:
    with open('wordlists-nginx/'+filename, 'r') as file:
        word_list = file.readlines()
        for word in word_list:
            if word[0] != '/': word = '/' + word
            full_host = 'http://'+host+word
            res = requests.get(full_host)
            if res.status_code == 200:
                print(full_host)
                print(res.text)
