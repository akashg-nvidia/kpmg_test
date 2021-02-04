#!/usr/bin/python
# Function To process the given object and fetch the value for given key 

import json
import urllib2
import sys
import optparse

def processObjectData(objct,key):   
	print "process key Object", objct
	objct_dump = json.dumps(objct)
	objct_dumpl = json.loads(objct_dump)
	print "objct_json_dump", objct_dump
	print "manual_json_dump_load", objct_dumpl
	key_wrap = key.split("/")
	for each_key in key_wrap:
		objct_dumpl = objct_dumpl[each_key]
		print "result:", objct_dumpl
	return objct_dumpl

def main():
    try:
		# Calling function
		# passing object and key
		data_object = {"a": {"b":{"c":"d"}}}
		data_key = "a/b/c"
		response = processObjectData(data_object,data_key)

    except Exception, e:
        print "exception in processing json object", e
        sys.exit(1)


if __name__ == "__main__":
    main()
