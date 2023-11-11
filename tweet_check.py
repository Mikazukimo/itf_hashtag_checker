import os
import glob
import csv

now = __file__
path = now.strip("tweet_check.py")
path = path.strip("c:")

folder = path + "CSV\*"
folder = folder.replace('\\', '/')

files = glob.glob(folder)
file_list = []
for file in files:
    file = file.replace('\\', '/')
    file_list.append(file)
for data in file_list:
    student_name = data
    main = ""
    time = ""
    tweetlist = []
    timelist = []
    with open(data, "r" ,encoding="utf-8_sig") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
           main = row[2]
           tweetlist.append(main)

    count = 0
    for i in range(len(tweetlist)):
            if "#コンテンツ入門2023" in tweetlist[i]:
                 count += 1

    print(f'『{student_name[-13:]}』は『{count}』件　ツイートしました')