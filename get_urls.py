from urllib.parse import urlparse
from googlesearch import search
from bs4 import BeautifulSoup
import argparse
import time
import requests


def get_advisories_and_vulns():
    adv_url_file = open("results/advisories_and_vulns.txt", "w")
    advisories_and_vulns_object = open("dorks/advisories_and_vulnerabilities.dorks", "r")
    advisories_and_vulns_list = advisories_and_vulns_object.readlines()
    for dork in advisories_and_vulns_list:
        query = dork
        for link in search(query, pause=60):
            adv_url_file.write(link)
            adv_url_file.write("\n")


def get_error_messages():
    error_message_file = open("results/error_message_file.txt", "w")
    error_messages_object = open("dorks/error_messages.dorks", "r")
    error_messages_list = error_messages_object.readlines()
    for dork in error_messages_list:
        query = dork
        for link in search(query, pause=60):
            error_message_file.write(link)
            error_message_file.write("\n")


def get_files_containing_juciy_info():
    files_containing_juicy_info_file = open("results/files_containing_juicy_info.txt", "w")
    files_containing_juicy_info_object = open("dorks/files_containing_juicy_info.dorks", "r")
    files_containing_juicy_info_list = files_containing_juicy_info_object.readlines()
    for dork in files_containing_juicy_info_list:
        query = dork
        for link in search(query, pause=60):
            files_containing_juicy_info_file.write(link)
            files_containing_juicy_info_file.write("\n")


def get_file_containing_passwords():
    files_containing_passwords_file = open("results/files_containing_passwords.txt", "w")
    files_containing_passwords_object = open("dorks/files_containing_passwords.dorks", "r")
    files_containing_passwords_list = files_containing_passwords_object.readlines()
    for dork in files_containing_passwords_list:
        query = dork
        for link in search(query, pause=60):
            files_containing_passwords_file.write(link)
            files_containing_passwords_file.write("\n")


def get_files_containing_usernames():
    files_containing_usernames_file = open("results/files_containing_usernames.txt", "w")
    files_containing_usernames_object = open("dorks/files_containing_usernames.dorks", "r")
    files_containing_usernames_list = files_containing_usernames_object.readlines()
    for dork in files_containing_usernames_list:
        query = dork
        for link in search(query, pause=60):
            files_containing_usernames_file.write(link)
            files_containing_usernames_file.write("\n")


def get_footholds():
    footholds_file = open("results/fotholds.txt", "w")
    footholds_object = open("dorks/footholds.dorks", "r")
    footholds_list = footholds_object.readlines()
    for dork in footholds_list:
        query = dork
        for link in search(query, pause=60):
            footholds_file.write(link)
            footholds_file.write("\n")


def get_network_vulnerability_data():
    network_vulnerability_data_file = open("results/network_vulnerability_data.txt", "w")
    network_vulnerability_data_object = open("dorks/network_or_vulnerability_data.dorks", "r")
    network_vulnerability_data_list = network_vulnerability_data_object.readlines()
    for dork in network_vulnerability_data_list:
        query = dork
        for link in search(query, pause=60):
            network_vulnerability_data_file.write(link)
            network_vulnerability_data_file.write("\n")


def get_sensitive_directories():
    sensitive_directories_file = open("results/sensitive_directories.txt", "w")
    sensitive_directories_object = open("dorks/sensitive_directories.dorks", "r")
    sensitive_directories_list = sensitive_directories_object.readlines()
    for dork in sensitive_directories_list:
        query = dork
        for link in search(query, pause=60):
            sensitive_directories_file.write(link)
            sensitive_directories_file.write("\n")


def get_sensitive_online_shopping():
    sensitive_online_shopping_file = open("results/sensitive_online_shopping.txt", "w")
    sensitive_online_shopping_object = open("dorks/sensitive_online_shopping_info.dorks", "r")
    sensitive_online_shopping_list = sensitive_online_shopping_object.readlines()
    for dork in sensitive_online_shopping_list:
        query = dork
        for link in search(query, pause=6):
            sensitive_online_shopping_file.write(link)
            sensitive_online_shopping_file.write("\n")
            print("Written " + str(link))


def get_various_online_devices():
    various_online_devices_file = open("results/various_online_devices.txt", "w")
    various_online_devices_object = open("dorks/various_online_devices.dorks", "r")
    various_online_devices_list = various_online_devices_object.readlines()
    for dork in various_online_devices_list:
        query = dork
        for link in search(query, pause=60):
            various_online_devices_file.write(link)
            various_online_devices_file.write("\n")


def get_vulnerable_files():
    vulnerable_files_file = open("results/vulnerable_files.txt", "w")
    vulnerable_files_object = open("dorks/vulnerable_files.dorks", "r")
    vulnerable_files_list = vulnerable_files_object.readlines()
    for dork in vulnerable_files_list:
        query = dork
        for link in search(query, pause=60):
            vulnerable_files_file.write(link)
            vulnerable_files_file.write("\n")


def get_vulnerable_servers():
    vulnerable_servers_file = open("results/vulnerable_servers.txt", "w")
    vulnerable_servers_list = open("dorks/vulnerable_servers.dorks", "r")
    for dork in vulnerable_servers_list:
        query = dork
        for link in search(query, pause=60):
            vulnerable_servers_file.write(link)
            vulnerable_servers_file.write("\n")


def one_for_all():
    all_dorks_file = open("results/all_dorks.txt", "w")
    all_dorks_list = open("dorks/all_google_dorks.txt", 'r')
    for dork in all_dorks_list:
        query = link
        for link in search(query, pause=60):
            all_dorks_file.write(link)
            all_dorks_file.write("\n")


def main():
    choice = str(input("Which type of results would you like to query\n1. advisories and vulnerabilities\n2. error "
                       "messages\n3. files containing juicy info\n4. files containing passwords\n5. files containing "
                       "usernames\n6. files containing footholds\n7. files containing network vulnerability "
                       "data\n8. sensitive directories\n9. online devices\n10. vulnerable files\n11. vulnerable "
                       "servers\n[go crazy!]**Hail "
                       "Mary**\n-->  "))
    if choice == "advisories and vulnerabilities":
        get_advisories_and_vulns()
    elif choice == "error messages":
        get_error_messages()
    elif choice == "files containing juicy info":
        get_files_containing_juciy_info()
    elif choice == "files containing passwords":
        get_file_containing_passwords()
    elif choice == "files containing usernames":
        get_files_containing_usernames()
    elif choice == "files containing footholds":
        get_footholds()
    elif choice == "files containing network vulnerability data":
        get_network_vulnerability_data()
    elif choice == "sensitive directories":
        get_sensitive_directories()
    elif choice == "online devices":
        get_various_online_devices()
    elif choice == "vulnerable files":
        get_vulnerable_files()
    elif choice == "vulnerable servers":
        get_vulnerable_servers()
    elif choice == "Hail Mary":
        one_for_all()
    else:
        print("Enter valid option")


main()
