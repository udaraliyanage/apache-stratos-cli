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
# ----------------------------------------------------------------------------

import urllib2
import base64
import json
from tabulate import tabulate

url = 'https://localhost:9443/stratos/admin/policy/deployment'
request = urllib2.Request(url)

base64string = base64.encodestring('%s:%s' % ('admin', 'admin')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)

response = urllib2.urlopen(request).read()
dep_policies = json.loads(response)

table = []
for p in dep_policies['deploymentPolicy']:
    id = p['id']
    row = [id]
    table.append(row)

headers = ["Id"]
print tabulate(table, headers)
