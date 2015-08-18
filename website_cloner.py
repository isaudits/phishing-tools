#!/usr/bin/python

'''
@author: Matthew C. Jones, CPA, CISA, OSCP
IS Audits & Consulting, LLC
TJS Deemer Dana LLP

Downloads a website into a format suitable for use with phishing frenzy
'''

import sys
import argparse
import os
import shutil
from BeautifulSoup import BeautifulSoup, NavigableString
import urllib2
import ConfigParser

def main(argv):
    
    parser = argparse.ArgumentParser(description='Downloads a website into a format suitable for use with phishing frenzy')
    parser.add_argument("site_addr", action="store", help="Site address")
    
    args = parser.parse_args()
    site_addr = args.site_addr
    
    #########################################
    #Get stuff from config file
    #########################################
    config_file = "config/website_cloner.config"
    if os.path.exists(config_file):
        pass
    else:
        try:
            print "Specified config file not found. Copying example config file..."
            shutil.copyfile("config/website_cloner.default", config_file)
        except:
            print "Error copying default config file...quitting execution..."
            sys.exit()
    
    config = ConfigParser.SafeConfigParser()
    config.read(config_file)
    
    try:
        working_dir = config.get("general", "working_dir")
        header_text = config.get("html", "header_text")
        body_text = config.get("html", "body_text")
        
    except:
        print "Missing required config file sections. Check running config file against provided example\n"
        sys.exit()
    
    site_path = site_addr.replace("http://","")
    site_path = site_path.replace("https://","")
    working_dir = os.path.join(working_dir, site_path,'')
    if not os.path.exists(working_dir):
        os.makedirs(working_dir)
    
    os.chdir(os.path.dirname(working_dir))
    
    #########################################
    #Get the site we are cloning
    #########################################    
    
    if not site_addr[:4] == "http":
        site_addr = "http://"+site_addr
        
    try:
        site_text=urllib2.urlopen(site_addr).read()
    except:
        print "Could not open site...quitting..."
        sys.exit()
        
    #soup=BeautifulSoup(header_text+site_text)
    soup=BeautifulSoup(site_text)
    head=soup.find('head')
    head.insert(0,NavigableString(header_text))
    body=soup.find('body')
    body.insert(0,NavigableString(body_text))
    
    ###############################################
    #Detect hyperlinked images and download locally
    ###############################################
    imageList = []
    
    for tag in soup.findAll('img', src=True):
        imageList.append(tag['src'])

    if not imageList:
        pass
    else:
        for url in imageList:
            print "getting " + url + "..."
            filename = url.split('/')[-1].split('#')[0].split('?')[0]
            open(filename,"wb").write(urllib2.urlopen(url, timeout=5).read())
            soup = BeautifulSoup(str(soup).decode("UTF-8").replace(url,filename).encode("UTF-8"))

    cssList = []
    
    for tag in soup.findAll('link', {'rel':'stylesheet'}):
        cssList.append(tag['href'])

    if not cssList:
        pass
    else:
        for url in cssList:
            try:
                print "getting " + url + "..."
                filename = url.split('/')[-1].split('#')[0].split('?')[0]
                open(filename,"wb").write(urllib2.urlopen(url, timeout=5).read())
                soup = BeautifulSoup(str(soup).decode("UTF-8").replace(url,filename).encode("UTF-8"))
            except:
                pass

    scriptList = []
    
    for tag in soup.findAll('script', src=True):
        scriptList.append(tag['src'])

    if not scriptList:
        pass
    else:
        for url in scriptList:
            try:
                print "getting " + url + "..."
                filename = url.split('/')[-1].split('#')[0].split('?')[0]
                open(filename,"wb").write(urllib2.urlopen(url, timeout=5).read())
                soup = BeautifulSoup(str(soup).decode("UTF-8").replace(url,filename).encode("UTF-8"))
            except:
                pass

    ##########################################
    #Clean up html output and make it readable
    ##########################################                               
    mainpage = soup.prettify()
    mainpage = mainpage.replace('&lt;','<')
    mainpage = mainpage.replace('&gt;','>')
    
    open("index.php","wb").write(mainpage)
    
if __name__ == "__main__":
    main(sys.argv[1:])
