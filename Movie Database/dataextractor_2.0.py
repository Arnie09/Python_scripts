import requests
import os
import omdb
import json

a=0
list=[]
with open(os.path.join(os.getcwd(),'data.json'),'r+') as cp:
    if(os.stat(os.path.join(os.getcwd(),'data.json')).st_size is not 0):
        data=json.load(cp)
    else:
        data={}
top=os.getcwd()
for dirName, subdirList, fileList in os.walk(os.getcwd()):
    for filename in fileList:
        os.chdir(dirName)
        if ((filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(".avi") or filename.endswith(".m4v") or filename.endswith(".flv")) and os.stat(os.path.join(os.getcwd(),filename)).st_size > 100000000):
            if(filename not in data):
                list.insert(a,filename)
                a+=1
                os.chdir(top)

os.chdir("I:\Films")

dict = {}
for i in range(len(list)):
    print("FIlename : ",list[i])
    movie=list[i]
    api_url1='http://www.omdbapi.com/?t='
    api_url2='&apikey=9fad058c'
    print("\nThe filename is : ",movie)
    search_name=input("Enter the name you wanna search for : ")
    search_name.replace(' ','%20')
    final_url=api_url1+search_name+api_url2
    a=requests.get(final_url)
    if(a.json()=={"Response": "False", "Error": "Movie not found!"}):
        print("\nNo info found for that one!")
        continue
    dict[list[i]] = a.json()
    z={**data,**dict}
    with open(os.path.join(os.getcwd(),'data.json'), 'w') as fp:
        print(os.getcwd())
        json.dump(z, fp)
