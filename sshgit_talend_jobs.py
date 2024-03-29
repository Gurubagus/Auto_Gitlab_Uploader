# FUTURE REFERENCE: set remote url to https://username(w/o "@.com"):password@gitlab.beneservices.com/BI_Labs/<dir>.git

import paramiko	
import gitlab

ssh_client= None

def main():
	print('\n*************Talend Jobs backup: Starting*************\n')
	try:
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname='80.88.187.155',username='benemen',password='HamR32XwLNd3!')
		ssh_client.exec_command('export LD_LIBRARY_PATH=/lib64/:$LD_LIBRARY_PATH')
		stdin, stdout, stderr = ssh_client.exec_command('cd /etl/talend_jobs; export LD_LIBRARY_PATH=/lib64/:$LD_LIBRARY_PATH; git add -A ; git commit -m "auto-upload"; git push origin master')
		out = stdout.read()
		print(out)
	except Exception as e:
		print('The following error has occurred during the Talend Jobs backup process')
		print(e.message)
	finally:
		if ssh_client:
			ssh_client.close()
		print('\n*************Talend Jobs backup: Complete*************\n')

			
if __name__ == '__main__':
	main()