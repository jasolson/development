#!/usr/bin/python
import boto.ec2
import time
from tabulate import tabulate


def listEC2Instances():
	conn = getEC2Connection()

	reservations = conn.get_all_reservations()

	headers = ['id','public dns name', 'instance type','state','region']
	instance_rows =  [ headers ]
	for r in reservations:
		for i in r.instances:
			instance_rows.append([i.id,i.public_dns_name,i.instance_type,i.state,i.region.name]) 	
	
	print tabulate(instance_rows)
def listEC2Zones():
	for r in boto.ec2.regions():
		print r.name

def listEBSVolumes():
	vols = 	getEBSVolumes()
	for volume in vols:
		print "Volume Name:",volume.id," Volume Size:",volume.size," Zone:",volume.zone

def getEC2Connection():
	return boto.connect_ec2()


def deleteEBSVolume(vol):
	vol.delete()
	vol.update()

def getEBSVolumes():
	conn = getEC2Connection()
	vols = conn.get_all_volumes()	
	return vols
