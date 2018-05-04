#Python 3
#Clone assignment repositories

import os, subprocess, shutil, mosspy

print("Enter classroom organization:")
classroom = input()

print("Enter assignment:")
assignment = input()

print("Enter roster filepath:")
rosterFile = input()

print("Enter moss id:")
mossid = input()

with open(rosterFile) as i:
    users = i.read().splitlines()

os.mkdir("moss")
mossDir = os.path.join(os.getcwd(), "moss")

for u in users:
    os.system("git clone http://github.com/{}/{}-{}".format(classroom, assignment, u))
    os.mkdir(os.path.join("moss", u))

for root, dir, files in os.walk(os.getcwd()):
    for file in files:
        if ".java" in file:
            if "Test" not in file:
                for u in users:
                    if u in root:
                        shutil.copy(os.path.join(root, file), os.path.join(mossDir, u))

mVar = mosspy.Moss(mossid, "python")
mVar.addFilesByWildcard("moss/*/*[!Test].java")
url = mVar.send()

print ("Report Url: " + url)
mVar.saveWebPage(url, "moss/report.html")
mosspy.download_report(url,"moss/report/", connections=8)