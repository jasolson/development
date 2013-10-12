#!/usr/bin/python

import boto
import boto.ec2
from tabulate import tabulate
import logging
import argparse

def setup_ec2_connection():
	conn = boto.ec2.connect_to_region("us-east-1")
	return conn


def get_all_instances(conn):
	all_instances = []
	reservations = conn.get_all_reservations()
	for r in reservations:
		for i in r.instances:
			all_instances.append(i)

	return all_instances
	
def main(loglevel):
	#numeric_level = getattr(logging, loglevel.upper(), 0)
	#print getattr(logging, loglevel.upper(), 0)
	#print numeric_level
	#print isinstance(numeric_level, int)
	#if not isinstance(numeric_level, int):
	#	raise ValueError('Invalid log level: %s' % loglevel.upper())
	logging.basicConfig(level=logging.INFO)	
	logging.info("Connecting to ec2")
	conn = setup_ec2_connection()
	instances = get_all_instances(conn)

	headers = ['id','public dns name', 'instance type','state']
	instance_rows =  [ headers ]

	for i in instances:
		instance_rows.append([i.id,i.public_dns_name,i.instance_type,i.state])

	print tabulate(instance_rows)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--log", help="Set debug level")
	args = parser.parse_args()
	logging= args.log
    	main(logging)

