import boto
ec2 = boto.connect_ec2()
key_pair = ec2.create_key_pair('python-script-key')  # only needs to be done once
key_pair.save('/home/jason/.ssh')
