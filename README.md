# zhaopin_info_crawler
crawl phone numbers and titles on www.zhaopin.com/ and www.51job.com/ for Jinan job fair sponsor

Scrapy + Selenium + PhantomJS

#### Setup environment
1. scrapy : 

    download scrapy

    virtualenv ~/scrapy

    source ~/scrapy/bin/activate

2. PhantomJS :

    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2

    cp phantomjs to system path

3.  openpyxl (save data to Excel) :
  
    sudo pip  install openpyxl

#### Run:

    scrapy crawl zhaopin
    scrapy crawl qiancheng
