#!/usr/bin/env python3

import argparse
import os
import toml
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument('dir', help='the directory of gravity/nodes')
gravity_dir = parser.parse_args().dir

if not os.path.isdir(gravity_dir):
    print("ERROR: ", gravity_dir, "is not a directory")
    exit(1)

conf = [f for f in os.listdir(gravity_dir) if os.path.isfile(os.path.join(gravity_dir,f)) and '.conf' in f]

prefix2name = {}

for f in conf:
    with open(os.path.join(gravity_dir, f), mode='r') as fp:
        s = fp.read()
        c = toml.loads(s)
        h =  hashlib.shake_256()
        h.update( bytes(c['PublicKey'],'ascii') )
        prefix2name[h.hexdigest(2)] = f.replace('.conf','')

for k in prefix2name:
    print(prefix2name[k],',,,2a0c:b641:69c:',k,'::/64', sep='')
