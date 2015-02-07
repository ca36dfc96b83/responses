#!/usr/bin/env python

#  change_cname.py - update the cname of a record from X to X' 
#  Author: Brendan M. 2/2015

import urllib2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--domain', help='the domain name of the record you are updating', required=True)
parser.add_argument('--old_cname', help='the old cname you intend to replace', required=True)
parser.add_argument('--new_cname', help='the new cname you intent to insert', required=True)
args = parser.parse_args()

base_url = 'https://restapi.ultradns.com/'
auth_url = base_url + 'v1/authorization/token'

auth_params = urllib.urlencode({
              'username': username,
              'password': password
}]

data = urllib2.urlopen(auth_url, params).read()

get_url = base_url + 'v1/zones/' + args.domain + '/rrsets'

get_data = urllib2.urlopen(get_url, params).read()

get_data.replace(args.old_cname, args.new_cname)

put_url = base_url + 'v1/zones/' + args.domain + '/rrsets/ownername'

put_data = urllib2.urlopen(put_url, get_data) 

# This is a very rough sketch, but unfortunately due to current work constraints this is all i am able to put forth
