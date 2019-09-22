# Apache IP Filter 0.1 by Xiao_Jin
# GitHub: https://github.com/jinzhijie/Apache-IP-Filter
import os
import platform

print('\n\t\t<<  Apache IP Filter 0.1 by Xiao_Jin  >>')
if platform.uname()[0] == "Windows":
    os.system('title Apache IP Filter by Xiao_Jin')

# Settings
LogFilePath = r"log.txt"  # Log File
WhiteListPath = r"white-list.txt"
AttackIPsFile = r"attack-ips.txt"

# Program
LogFile = open(LogFilePath, "r+")
Log_with_useless_parts_lists = LogFile.readlines()
New_White_ips_list = []

if os.path.isfile(WhiteListPath):
    WhiteList = open(WhiteListPath, "r+")
    White_ips_list = WhiteList.readlines()
    for i in White_ips_list:
        New_White_ips_list.append(i.replace("\n", ""))
else:
    New_White_ips_list = []
attack_ips_txt = open(AttackIPsFile, "w+")
attack_ips_txt.write("")

ip_lists_ori = []
new_ip_lists = []

for i in Log_with_useless_parts_lists:
    useless_start = i.find("-")
    log_useless_part = i[useless_start - 1:-1]
    log_with_ip = i.replace(log_useless_part, "").replace("\n", "")
    ip_lists_ori.append(log_with_ip)

for i in ip_lists_ori:
    if i not in new_ip_lists and i not in New_White_ips_list:
        new_ip_lists.append(i)

print('\t\t\tAttack count: \t' + str(len(ip_lists_ori)))
print('\t\t\tProxy ips: \t' + str(len(new_ip_lists)))
attack_ips_txt = open(AttackIPsFile, 'a')

ips = ""
for i in sorted(new_ip_lists, key=lambda x: len(x), reverse=False):
    ips = ips + i + "\n"
attack_ips_txt.write(ips)

print("\n[OK] " + str(len(new_ip_lists)) + r' ips has been saved in "' + AttackIPsFile + '" successfully!')
