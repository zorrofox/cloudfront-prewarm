#! /bin/python

import dns.resolver as resolver
import requests

with open("edge.cfg", "r") as f:
    edges = f.read().split('\n')
if not edges[-1]:
    edges.remove(edges[-1])
with open("url.cfg", "r") as f:
    urls = f.read().split('\n')
if not urls[-1]:
    urls.remove(urls[-1])
with open("domain.cfg", "r") as f:
    domain = f.read().split('\n')[0]


cname = str(resolver.query(domain, 'CNAME')[0]).split('.')[0]

print('CloudFront CNAME Domain ID: {}'.format(cname))

headers = {'host': domain}

print('Begin Prewarm the Egde...')
print('#########################')
for edge in edges:
    for u in urls:
        url = 'http://{}.{}.cloudfront.cn{}'.format(cname, edge, u)
        r = requests.get(url, headers = headers)
        print('Get URL: {}'.format(url))
        print('Response status: {}'.format(r.status_code))
        print('Response CF Pop: {}'.format(r.headers['X-Amz-Cf-Pop']))
        print('Response Cache Status: {}'.format(r.headers['X-Cache']))
        print('------------------------')
print('#########################')
print('End Prewarm')
