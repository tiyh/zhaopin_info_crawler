# zhaopin_info_crawler
crawl phone numbers and titles on www.zhaopin.com/ and www.51job.com/ for job fair sponsor

Scrapy + Selenium + PhantomJS + Redis 

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

4.  Redis
    pip install redis

    redis-cli -h localhost -p 6379 -a {password} --raw

#### Run:

    scrapy crawl {spider_name}

    or using release script :
    cd release/ && python release.py



#### Redis:
    redis-cli -h localhost -p 6379 {-a password} --raw

    redis rdb default path in Ubuntu：/var/lib/redis/dump.rdb

    echo "HGETALL qiancheng_zhengzhou" | redis-cli -h localhost -p 6379 {-a password} --raw >> qiancheng_zhengzhou_all.txt

