#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:31:42 2022

@author: Naoya Kadota

A python software to download data from NASA AppEARS repository using the download links list text file
-This is a initial version -- will be concatenated to the ges_disc_downloader in the future
"""

import os
import sys
import time
import argparse
import requests
import urllib.request as rq
import base64
from http.cookiejar import CookieJar

def file_title(url): #parse filename from target url
    if url.endswith('.pdf') == True: #if the file is pdf
        #print('The file is pdf')
        file_name = url[(url.rfind('/')+1):]
        return file_name
    else:
        pass
    #Filename is the string between 'LABEL=' and '&'
    splitter = 'LABEL='
    str_idx = url.find(splitter)
    file_name = url[str_idx+len(splitter):]
    str_idx2 = file_name.find('&')
    file_name = file_name[:str_idx2]
    return file_name

def filepath_check(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print('new folder generated')
def downloader(target_url,user,passwd):
    try:
        url = target_url
        response = requests.get(url)
        folder_name = 'Downloaded_files'
        filepath_check(folder_name)
        def file_title_for_AppEARS(url): #parse filename from target url
            file_name = url[(url.rfind('/')+1):]
            return file_name

        filename = file_title_for_AppEARS(url)
        open((folder_name +'/'+ filename), 'wb').write(response.content)
        response.close()
        print(filename, 'has successfully been downloaded')
        return
    except Exception as e:
        print('An error occured. Unable to download', target_url)
        print(e)
        sys.exit()

def get_args():
    parser = argparse.ArgumentParser(description='input text file name, account user and account password. -h for help')
    parser.add_argument('file',type=str, help='file name') 
    parser.add_argument('-u','--user',type=str, help='Your User name here', required = False)
    parser.add_argument('-p','--password',type=str, help='Your password here', required = False)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    if hasattr(args, 'file'):
        pass
    print('File download starting...')
    with open(args.file, 'r') as f:
        file_data = f.readlines()
        for line in file_data:
            downloader(line.rstrip(),'random','strings')
            time.sleep(2)
    print('All file downloaded')
if __name__ == "__main__":
    main()