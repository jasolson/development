import boto.ec2
conn = boto.ec2.connect_to_region("us-east-1",
	aws_access_key_id='AKIAIH3FJFBPT4OCMW3Q',
	aws_secret_access_key='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')

#reservation = conn.run_instances(image_id='ami-d5e2b5bc',
#	key_name='python-script-key',
#	instance_type='t1.micro'
#	)


# Wait a minute or two while it boots
for r in conn.get_all_instances():
    print r.instances[0].public_dns_name
#    if r.id == reservation.id:
#        break

#print r.instances[0].public_dns_name


