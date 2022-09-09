from pprint import pprint
import os

file_1 = open("1.txt", encoding="utf-8")
name_1 = os.path.basename(r'\1.txt')
file_2 = open("2.txt", encoding="utf-8")
name_2 = os.path.basename(r'\2.txt')
file_3 = open("3.txt", encoding="utf-8")
name_3 = os.path.basename(r'\3.txt')

content_1 = file_1.readlines()
content_2 = file_2.readlines()
content_3 = file_3.readlines()

all_files_len = [len(content_1), len(content_2), len(content_3)]
all_files = [content_1, content_2, content_3]
all_names = [name_1, name_2, name_3]

dict = {}

dict[all_files_len[0]] = all_names[0]
dict[all_files_len[1]] = all_names[1]
dict[all_files_len[2]] = all_names[2]

with open("4.txt", "w+", encoding="utf-8") as file_4:
    for item in sorted(dict):
        for i in all_files:
            if len(i) == item:
                file_4.write("\n")
                file_4.write(dict[item])                
                file_4.write("\n")
                file_4.write(str((len(i))) + "\n")
                for item in i:
                    file_4.write(item)
