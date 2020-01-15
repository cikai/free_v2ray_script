# -*- coding: UTF-8 -*-

##############################
# pip install beautifulsoup4 #
##############################

import urllib.request

from bs4 import BeautifulSoup

response = urllib.request.urlopen('https://view.freev2ray.org')
html = response.read()
soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
address = soup.find(id="ip").string.strip()
port = soup.find(id="port").string.strip()
uuid = soup.find(id="uuid").string.strip()
vmess = soup.find("button", {"class": "copybtn"})['data-clipboard-text'].strip()

print(address)
print(port)
print(uuid)
print(vmess)
