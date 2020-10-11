#!/usr/bin/env python3

import sys, os
import subprocess
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--full", dest="full", help="Run full version of app (with elasticsearch, texlive)", action="store_true")
parser.add_argument("--user", dest="git_user", help="Git user", default="zestedesavoir")
parser.add_argument("--branch", dest="git_branch", help="Git branch", default="dev")
parser.add_argument("--pr", dest="pr_id", help="Pull request Id")
args = parser.parse_args()


if args.pr_id:
    url = "https://api.github.com/repos/zestedesavoir/zds-site/pulls/{}".format(args.pr_id)
    r = requests.get(url)
    if r.status_code != 200:
        print("We can't find information of PR {}".format(args.pr_id))
        sys.exit(1)
    else:
        data = r.json()
        label = data.get("head", {}).get("label", None)
        if label is None:
            print("We can't find information about PR {}".format(args.pr_id))
            sys.exit(1)
        else:
            infos = label.split(':')
            git_user = infos[0]
            git_branch = infos[1]
else:
    if not args.git_user:
        print("Provide --user field")
        sys.exit(1)
    if not args.git_branch:
        print("Provide --branch field")
        sys.exit(1)

    git_branch = args.git_branch
    git_user = args.git_user


os.environ["GIT_BRANCH"] = git_branch
os.environ["GIT_USER"] = git_user

print("===================================================")
print("{}/{}".format(git_user, git_branch))
print("===================================================")

file = "docker-compose-lite.yml"
if args.full:
    print("DEPLOY FULL VERSION OF SITE")
    file = "docker-compose.yml"

build = subprocess.run(["docker-compose", "-f", file, "build", "--force-rm", "--no-cache"])

print("===================================================")
print("Start app")
print("===================================================")

if build.returncode == 0:
    subprocess.run(["docker-compose", "down", "-v"])
    subprocess.run(["docker-compose", "-f", file, "up"])
