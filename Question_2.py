#!/usr/bin/python
#try running this with python 2.x
# Processing instance metadata and asking user to provide a key
# not sure if question is to get the data for boto3 client and get the ec2 instance data, if yes then we can get the instance details as below which comes in json format default.
#import boto3
#ec2 = boto3.client('ec2')
#response = ec2.describe_instance()
#print "", response
#we can use the filter to get specific details for an instance. 

import json
import urllib2
import sys
import optparse

def processMetaData(data_key):
	data = ""
	#Below url gives metadata for aws instance
	instance_metadata = urllib2.urlopen('http://169.254.169.254/latest/meta-data/').read()
	#Converting data to json
	metadata = json.dumps(instance_metadata)
	print "metadata", metadata
	if data_key:
		dataResponse = urllib2.urlopen('http://169.254.169.254/latest/meta-data/{0}'.format(data_key)).read()
		data = json.dumps(dataResponse)
		print "data", data
	return data

def main():
    try:
		parser = optparse.OptionParser()
		parser.add_option("-d", "--data_key", dest="dataKey", help="UserOption to choose build system")
		(options,args) = parser.parse_args()
		data_key = options.dataKey
		print "data_key", data_key
		if not data_key:
			print "INFO: You can also provide the specific data key details by providing --data_key option"
		response = processMetaData(data_key)
		return response
    except Exception, e:
        print "exception in processing data key", e
        sys.exit(1)


if __name__ == "__main__":
    main()



