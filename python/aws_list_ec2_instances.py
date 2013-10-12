import boto.ec2
from tabulate import tabulate
conn = boto.ec2.connect_to_region("us-east-1")

reservations = conn.get_all_reservations()

headers = ['id','public dns name', 'instance type','state']
instance_rows =  [ headers ]
for r in reservations:
	for i in r.instances:
		instance_rows.append([i.id,i.public_dns_name,i.instance_type,i.state]) 	

print tabulate(instance_rows)
