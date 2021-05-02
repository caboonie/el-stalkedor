from flask import Flask, request, redirect, render_template, Response, send_file, url_for, flash
  
app = Flask(__name__)
  
@app.route('/', methods = ['GET'])  
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()


from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
import json


# app = Flask(__name__)
# app.config['SECRET_KEY'] = "a;lfkdsjaflksdj"

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')


# query = input("query image")# you can change the query for the image  here
def get_image(query):
    image_type="ActiOn"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
    print(url)
    #add the directory for your image here
    DIR="Pictures"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url,header)

    images = []
    i = 0
    for b in soup.find_all("img")[1:]:
        print(b)
        print(b["src"])
        images.append(b["src"])
        if (i == 2):
            break
        i+= 1
    return images


'''
@app.route('/<string:query>', methods = ['GET'])  
def home_search(query):
    print("searching for ", query)
    return json.dumps(get_image(query))

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
'''