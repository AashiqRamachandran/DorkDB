from urllib.parse import urlparse
from googlesearch import search
from bs4 import BeautifulSoup
import argparse
import json
import time
import os
import csv
import whois
import requests
import threading

def find_base_url(link):
    parsed_uri = urlparse(link)
    base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return base_url

def build_reply(link):
    base_url = find_base_url(link)
    reply = "Hi owner/ representative of "+str(base_url)+",\nMy name is Wednesday and I just wanted to quickly bring to your attention about a possible security vulnerability I have discovered on your website. \nThere is critical information disclosure on "+str(link)+" \nIf this is a false positive please ignore! \nNOTE: I am an automated bot created to ensure the safety and security of corporations on the internet and hold no liability to any conditions and have not tried to exploit any service in any way. \nAmen"
    return reply

def get_email_and_build_reply():
    with open("email_link_pair.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow(["url","email_id","subject", "reply"])
        temp = open("results/all_dorks.txt","r")
        for link in temp:
            base_url = find_base_url(link)
            results = whois.whois(base_url)
            reply = build_reply(link)
            writer.writerow([link, results.emails, "Responsible Disclosure of Possible Vulnerability", reply])
            print(str(link)+" record has been written: ")

def sleep():
    time.sleep(2)

def main():
    print("[+] Wednesday invoked. Beginning collection")
    get_email_and_build_reply()
