#!/usr/bin/env python
import csv
import sys
import os
import typer
FILEPATH = 'instagram.csv'
DIRPATH = 'data'

app = typer.Typer()

USERNAME = 'YOUR_INSTAGRAM_USERNAME'
PASSWORD = 'YOUR_INSTAGRAM_PASSWORD'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.42"


@app.command()
def collect():
    reader = csv.reader(open(FILEPATH, 'r', encoding='utf8'))
    n = 0
    for row in reader:
        n += 1
        if n == 1: continue
        if len(row) == 0: continue
        filename = row[2] + '.jsonl'
        fullpath = os.path.join(DIRPATH, filename)
        cwd = os.getcwd()
        os.chdir(DIRPATH)
        if not os.path.exists(row[2]):
            os.system('instaloader -V --no-pictures --login %ы -p %ы --user-agent "%s" %s' % (USERNAME, PASSWORD, USER_AGENT, row[2]))
        os.chdir(cwd)

@app.command()
def collectshort():
    reader = open('shortlist.txt', 'r', encoding='utf8')
    n = 0
    for row in reader:
        n += 1
        if n == 1: continue
        if len(row) == 0: continue
        filename = row + '.jsonl'
        fullpath = os.path.join(DIRPATH, filename)
        cwd = os.getcwd()
        os.chdir(DIRPATH)
        if not os.path.exists(row):
            os.system('instaloader -V --no-pictures --login %ы -p %ы --user-agent "%s" %s' % (USERNAME, PASSWORD, USER_AGENT, row))
        os.chdir(cwd)


@app.command()
def package():
    dirs = os.listdir(DIRPATH)
    cwd = os.getcwd()
    os.chdir(DIRPATH)
    for d in dirs:
        if os.path.exists('../export/%s_texts.zip' % (d)): continue
#        print('7z a -tzip %s ../export/%s.zip' % (d, d))
        os.system('7z a -tzip "../export/%s_texts.zip" %s' % (d, d))
    os.chdir(cwd)

if __name__ == "__main__":
    app()