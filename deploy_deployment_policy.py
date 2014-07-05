#!/bin/bash
# ----------------------------------------------------------------------------
# Copyright 2005-2013 WSO2, Inc. http://www.wso2.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -----------------------------

import json
import urllib2
import logging
import base64

logging.basicConfig(filename='logs/stratos-cli.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

policy_file=open("/home/udara/projects/stratos-cli/testdep.json","r")
data=policy_file.read()
print data
url = 'https://localhost:9443/stratos/admin/policy/deployment'

request = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % ('admin', 'admin')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)
request.add_header('Content-Type', 'application/json')
response=""

try:
    resp = urllib2.urlopen(request, data)
    contents = resp.read()
    response = json.loads(contents)
    print response['stratosAdminResponse']['message']
except urllib2.HTTPError, error:
    contents = error.read()
    response = json.loads(contents)
    print "Error code: ", response['Error']['errorCode']
    print "Error message: ", response['Error']['errorMessage']

