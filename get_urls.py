from googlesearch import search

dork_dir = input ("Enter the full path to dorks directory: ")

advisories_and_vulns_object=open(dork_dir+"/advisories_and_vulnerabilities.dorks", "r")
advisories_and_vulns_list=advisories_and_vulns_object.readlines()

error_messages_object=open(dork_dir+"/error_messages.dorks","r")
error_messages_list=error_messages_object.readlines()

files_containing_juicy_info_object=open(dork_dir+"/files_containing_juicy_info.dorks","r")
files_containing_juicy_info_list=files_containing_juicy_info_object.readlines()

files_containing_passwords_object=open(dork_dir+"/files_containing_passwords.dorks","r")
files_containing_passwords_list=files_containing_passwords_object.readlines()

files_containing_usernames_object=open(dork_dir+"/files_containing_usernames.dorks","r")
files_containing_usernames_list=files_containing_usernames_object.readlines()

footholds_object=open(dork_dir+"/footholds.dorks","r")
footholds_list=footholds_object.readlines()

network_vulnerability_data_object=open(dork_dir+"/network_or_vulnerability_data.dorks","r")
network_vulnerability_data_list=network_vulnerability_data_object.readlines()

pages_containing_login_portals_object=open(dork_dir+"/pages_containing_login_portals.dorks","r")
pages_containing_login_portals_list=pages_containing_login_portals_object.readlines()

sensitive_directories_object=open(dork_dir+"/sensitive_directories.dorks","r")
sensitive_directories_list=sensitive_directories_object.readlines()

sensitive_online_shopping_object=open(dork_dir+"/sensitive_online_shopping_info.dorks","r")
sensitive_online_shopping_list=sensitive_online_shopping_object.readlines()

various_online_devices_object=open(dork_dir+"/various_online_devices.dorks","r")
various_online_devices_list=various_online_devices_object.readlines()

vulnerable_files_object=open(dork_dir+"/vulnerable_files.dorks","r")
vulnerable_files_list=vulnerable_files_object.readlines()

vulnerable_servers_object=open(dork_dir+"/vulnerable_servers.dorks","r")
vulnerable_servers_list=vulnerable_servers_object.readlines()

web_server_detection_object=open(dork_dir+"/web_server_detection.dorks","r")
web_server_detection_list=web_server_detection_object.readlines()

for dork in error_messages_list:
	query=dork
	for link in search(query, pause=2):
		print(link)
		
for dork in files_containing_juicy_info_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in files_containing_passwords_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in files_containing_usernames_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in footholds_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in network_vulnerability_data_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in pages_containing_login_portals_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in sensitive_directories_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in sensitive_online_shopping_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in various_online_devices_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in vulnerable_files_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in vulnerable_servers_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in web_server_detection_list:
	query=dork
	for link in search(query, pause=2):
		print(link)

for dork in advisories_and_vulns_list:
	query=dork
	for link in search(query, pause=2):
		print(link)
