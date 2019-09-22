# Apache IP Filter 0.1 by Xiao_Jin
# GitHub: https://github.com/jinzhijie
import os

print('\n\t\t<<  Apache IP Filter 0.1 by Xiao_Jin  >>')
os.system('title Apache IP Filter by Xiao_Jin')
# Settings
LogFilePath = r"log.txt"  # Log File
WhiteListPath = r"white-list.txt"
AttackIPsFile = r"attack-ips.txt"

# Program
# LogFile = open(LogFilePath, "a")
# LogFile.write("\n")
LogFile = open(LogFilePath, "r+")
Log_with_useless_parts_lists = LogFile.readlines()
if os.path.isfile(WhiteListPath):
    WhiteList = open(WhiteListPath, "r+")
    White_ips_list = WhiteList.readlines()
else:
    White_ips_list = []
attack_ips_txt = open(AttackIPsFile, "w+")
attack_ips_txt.write("")

ip_lists_ori = []
new_ip_lists = []

for i in Log_with_useless_parts_lists:
    useless_start = i.find("-")
    useless_end = i.find('\n')
    log_useless_part = i[useless_start - 1:useless_end + 1]
    log_with_ip = i.replace(log_useless_part, "")
    ip_lists_ori.append(log_with_ip)

for i in ip_lists_ori:
    if i not in new_ip_lists and i not in White_ips_list:
        new_ip_lists.append(i)

print('\t\t\tAttack count: \t' + str(len(ip_lists_ori)))
print('\t\t\tProxy ips: \t' + str(len(new_ip_lists)))
attack_ips_txt = open(AttackIPsFile, 'a')
for i in new_ip_lists:
    attack_ips_txt.write(i + "\n")

print("\n[OK] " + str(len(new_ip_lists)) + r' IPs has been saved in "' + AttackIPsFile + '" successfully!')
