"""
Script for auto updating gitlab.beneservices.com's repository for:

- BAP@80.88.187.129 /projects/BAP -> BAP.git
- Talend Server@80.88.187.155: /etl/talend_jobs -> talend_jobs.git
- Talend Server@80.88.187.155: /etl/development/BENEETL -> etl_development_BENEETL.git
- gpadmin@80.88.187.33: /etl/pg_dump/BeneDW.dmp -> benedw_schemas.git
- BENEG1\\Qlik_Admin@80.88.187.152: \inetpub\wwwroot\BeneReports -> benereports.git
- ESB@80.88.187.171 D:/TalendOS_ESB/Studio/workspace/BENE_ESB -> BENE_ESB.git
"""

import os
import paramiko
import git_BAP
import sshgit_talend_jobs
import sshgit_etl_development
import sshgit_etl_BeneDW
import sshgit_QlikSense_BeneReports
import sshgit_esb_beneesb


def main():
	
	git_BAP.main()
	sshgit_talend_jobs.main()
	sshgit_etl_development.main()
	sshgit_etl_BeneDW.main()
	sshgit_QlikSense_BeneReports.main()
	sshgit_esb_beneesb.main()
		
if __name__ == '__main__':
	main()