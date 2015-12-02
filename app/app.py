#!/usr/bin/env python
# coding=utf-8

from urllib2 import urlopen
from bs4 import BeautifulSoup as bs

def getdata():
    exception = [u'Nama Perjalanan Dinas', u'Tempat Tujuan', u'Tanggal Berangkat', u'Tanggal Kembali']
    soup = bs(urlopen("http://diskominfo.riau.go.id/semua-dinasluar.html"))
    raw = [d.text.encode('ascii') for d in soup.findAll("td") if d.text not in exception]
    return raw

if __name__ == "__main__":
    print getdata()





