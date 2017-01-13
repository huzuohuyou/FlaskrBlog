__author__ = 'jishu12'
import  pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'http://localhost:5000/myname/')
c.perform()

c = pycurl.Curl()
c.setopt(c.URL, 'http://localhost:5000/user/wuhailong')
c.perform()

c = pycurl.Curl()
c.setopt(c.URL, 'http://localhost:5000/post/998')
c.perform()