# rugovinstagrams
Russian government and politics instagram data and code after march 2022 archival campaign.

# Requirements

Please install Python "typer' lib "pip install typer.

Please install "instaloader" - https://instaloader.github.io

Please install 7zip to archive data as packages - https://7-zip.org or rewrite this code to another archiver

# Usage

Run "python collect.py collect" to collect data from list of Instagram accounts in 'instagram.csv' file. Data saved to "data" dir with directory for each account.

Run "python collect.py collectshort" to collect data from list of instagram accounts in "shortlist.txt" with list of only accounts

Run "python collect.py package" to create archive of each account in "export" directory. One zip file per account


# Data

All collected data available at https://cdn1.ruarxive.org/public/webcollect2022/govinst2022/_govinstagrams_20220325.zip

# Authors

Ivan Begtin (ivan@begtin.tech)


# Regards

Russian national digital archive - http://ruarxive.org
