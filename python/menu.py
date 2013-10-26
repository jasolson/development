import sys
import aws_ec2_functions as ec2

def main():
	print "Welcome to AWS!"
	while(True):
		function = mainMenu()
		if(function == 'listec2'):
			ec2.listEC2Instances()	
		elif(function == 'listebs'):
			ec2.listEBSVolumes()	
		elif(function == 'listzones'):
			ec2.listEC2Zones()	
		elif(function == 'deleteebs'):
			deleteVol()
		elif(function == 'exit'):
			break
			



def mainMenu():
	while(True):
		print "Please select an option\n"
		print "1) List instances"
		print "2) List EBS instances"
		print "3) List EC2 Zones"
		print "4) Delete EBS instance by id"
		print "0) Exit"
		try:
			selection = input("Your selection:")
		except SyntaxError:
			continue
	#	print "You selected:{0}".format(selection)
		if(str(selection) == '1'):
			return 'listec2'
		elif(str(selection) == '2'):
			return 'listebs'
		elif(str(selection) == '3'):
			return 'listzones'
		elif(str(selection) == '4'):
			return 'deleteebs'
		elif(str(selection) == '0'):
			return 'exit'
		else:
			print "Select one of the options, i.e. \"1\""

def deleteVol():
	while(True):
		print "Select from this list of volumes..."
		vols = ec2.getEBSVolumes()
		count = 0
		for vol in vols:
			count = count +1
			print count,") Volume ID:",vol.id," Volume Size:",vol.size	
		print "0) Exit(Do nothing)"
		try:
			selection = raw_input("What would you like to select:")	
			if(str(selection) == '0'):
				return
			else:
				ec2.deleteEBSVolume(vols[int(selection)-1])	
				return
		except SyntaxError:
			continue
	
main()
		
