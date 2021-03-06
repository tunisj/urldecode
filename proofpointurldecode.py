#!/usr/bin/python
# Import our Modules
import urlparse
import re
url = raw_input("Enter Proofpoint Encoded URL:  ")
class ppdecode(object):
    def __init__(self, url):
        self.pplink = url
        self.arguments = urlparse.parse_qs(urlparse.urlparse(url).query)
        self.url = self._decodeurl()
        self._parse()

    def _decodeurl(self):
        tmp = self.arguments['u'][0].replace("_", "/")
        for x in list(set(re.findall('-[0-9A-F]{2,2}', tmp))):
            tmp = tmp.replace(x, chr(int(x[1:3], 16)))
        return tmp

    def _parse(self):
        if 'r' in self.arguments:
            self.recipient = self.arguments['r'][0]
        if 'c' in self.arguments:
            self.site = self.arguments['c'][0]

p = ppdecode(url)
print ''' '''
print '''You're decoded URL is:'''
print ''' '''
print p.url
