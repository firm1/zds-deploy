#!/usr/bin/env python3

import sys, os
import subprocess

args = sys.argv
if len(args) == 1:
    print("Error : The script require one args <git_user>:<git_branch>")
    sys.exit(1)
elif len(args) == 2:
    args = [args[0]] + args[1].split(":")
    if len(args) != 3:
        print("Error : The script require one args <git_user>:<git_branch>")
        sys.exit(1)

git_branch = args[2]
git_user = args[1]


os.environ["GIT_BRANCH"] = git_branch
os.environ["GIT_USER"] = git_user

print("===================================================")
print("{}/{}".format(git_user, git_branch))
print("===================================================")

build = subprocess.run(["docker-compose", "build", "--force-rm", "--no-cache"])

print("===================================================")
print("Start app")
print("===================================================")

if build.returncode == 0:
    subprocess.run(["docker-compose", "down", "-v"])
    subprocess.run(["docker-compose", "up"])