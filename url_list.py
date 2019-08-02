url_list = [
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/getallproductinfo','type':'get','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/associate2020toes','type':'post','param':{"U2020": {"productname": "U2020", "vomsuip": "10.10.2.130", "masterip": "10.10.2.131","masterpwdentry": ""},"ES": {"esvosmuip": "10.10.2.130", "esip": "172.28.130.139", "espwdentry": ""}}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/:setui/emergencymgr/updateAssociateInfo','type':'post','param': {"productname": "u2020", "syncswitch": "aaa", "backuptime": []}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/disableconnecthandler','type':'post','param':{"productName": "u2020", "operation": "aaa", "target": ""}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/ossservicehandler','type':'post','param':{"productName": "u2020", "operation": "aaa", "target": ""}},\
#            {'module':'ESMgrService','url':"/rest/plat/omp/v1/emergency/ui/emergencymgr/unassociate?productName=U2020",'type':'post','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/deleteremoteassociation?esIP=aaaa','type':'post','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/mergeassociation?filePath=sfafa','type':'post','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/queryassociationbyesip?esIP=10.10.2.139','type':'get','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/getassociateinfo?productName=U2020','type':'get','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/insatllremoteapp','type':'post','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencymgr/importdynamicdata?esIP=10.10.2.130','type':'post','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/emergencytask/manualsync?productName=U2020','type':'post','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/switchtask/takeover?productName=ES','type':'post','param':{}},\
#            {'module':'ESMgrService','url':'/rest/plat/omp/v1/emergency/ui/switchtask/stoptakeover?productName=ES','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/capability/ui/mgmtcapability/collectmanagementcapability','type':'post','param':{'productId': '8d2f9bf8-3ba1-47ff-a6e4-e76c1ca363b2', 'productName': 'U2020', 'productAlias': 'U2020','ipAddress': '172.28.131.222','nodeId': '','nodeName': 'u2020m','nodeType': 'APP,DB,master,u2020-cluster,master','productAlias': 'U2020','productId': '8d2f9bf8-3ba1-47ff-a6e4-e76c1ca363b2','productName': 'U2020','productOwn': '','productPath': '/opt/cloud','productType': 'U2020','productVersion': 'V300R019'}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/capability/ui/mgmtcapability','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/capability/ui/mgmtcapability/delete','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/capability/ui/mgmtcapability/querycapability','type':'post','param':{}},\
#            #{'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthchecktask/callback','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/devicearchives/ui/devicearchivesmgmt/archives','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/devicearchives/ui/devicearchivesmgmt/delarchives','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/devicearchives/ui/devicearchivesmgmt/createcollecttask','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/devicearchives/ui/devicearchivesmgmt/getproductinfo','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/devicearchives/ui/devicearchivesmgmt/querycfgIp','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/esn/ui/esnservice/queryESN','type':'post','param':{"productName":"U2020"}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/createCheckTaskForProjectInfo','type':'post','param':{"dateValue":"3","data":{"hardwareInfo":{"diskArrayLst":[],"boardLst":[]},"ilayerInfo":{"fsBaseInfoLst":[],"fsHostInfoLst":[]},"softwareInfo":{"osLst":[{"ip":"172.28.130.131","isSelectInDiag":"1"},{"ip":"172.28.130.132","isSelectInDiag":"1"},{"ip":"172.28.130.133","isSelectInDiag":"1"},{"ip":"172.28.130.134","isSelectInDiag":"1"},{"ip":"172.28.130.135","isSelectInDiag":"1"},{"ip":"172.28.130.139","isSelectInDiag":"1"},{"ip":"172.28.130.140","isSelectInDiag":"1"},{"ip":"172.28.130.141","isSelectInDiag":"1"},{"ip":"172.28.130.142","isSelectInDiag":"1"},{"ip":"172.28.130.143","isSelectInDiag":"1"},{"ip":"172.28.130.130","isSelectInDiag":"1"}],"dbLst":[{"ip":"172.28.130.133","isSelectInDiag":"1"},{"ip":"172.28.130.134","isSelectInDiag":"1"},{"ip":"172.28.130.143","isSelectInDiag":"1"}]}}}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/queryataecollectinfo','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/createchecktask','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/checkataecollectpassword','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/createataelocationtask','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/softwarepackage','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/getproductnodes','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/getproducts','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/getProjectInfo','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/querychecktaskprogess','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/updaterulepackage','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/healthcheckmgmt/delete','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/healthcheck/ui/collectmgmt/createCollectTask','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':"/rest/plat/omp/v1/healthcheck/ui/collectmgmt/queryTaskProgress?taskID='taskId'",'type':'post','param':{}},\
#            {'module':'HealthCheckService','url':"/rest/plat/omp/v1/healthcheck/ui/collectmgmt/getResultPackagePath?taskID='taskId'",'type':'post','param':{}},\
#            #{'module':'HealthCheckService','url':'/rest/plat/omp/v1/timer/ui/timerservice/modification','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/timer/ui/timerservice/timerinfo','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/querypreintegrated','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/queryilayerversion','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/getproductinfo','type':'get','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/getproductnodeinfo','type':'post','param':{'productName':'U2020','productType':'es'}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/queryproductversion','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/querynodeversion','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/queryVersionInfoFile','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/exportVersionInfo','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/queryTaskListRecord','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/exportTaskManageInfoList','type':'post','param':{}},\
#            {'module':'HealthCheckService','url':'/rest/plat/omp/v1/verinfo/ui/versionservice/queryexportprocess','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/queryRack','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/queryHardwareInfo','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/getHardwareInfo','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/querySubrack','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/queryBlade','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/queryDiskArray','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/queryBladeStatus?bladeList=abc','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/exportHardwareInfo','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/restartMCERService','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/queryversionatnode','type':'post','param':{'request': [{'versiontype': "subrack", 'producttype': "", 'instance': "", 'nodeips': ["172.28.164.17"]}]}},\
##            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/getswitchboard','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/getSwitch','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/updatesubracks','type':'post','param':{"subracks":[{"label":"17-7r-MPS-01-01","ip":"172.28.164.17"}],"subpad":"1234"}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/updatediskarray','type':'post','param':{"diskarrays":[{"label":"17-7r-BSS-01-10","ip1":"172.28.164.24","ip2":"172.28.164.25"}],"dispad":"1234"}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/querySubRackRegStatus','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/queryDiskArrayRegStatus','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/querySwitchBoardRegStatus','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/querySwitchRegStatus','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/queryswitchboard','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/updateswitchboardinfo','type':'post','param':{"switchboards":[{"ip":"172.28.164.21","id":1}],"password":"1234"}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/updateswitchmachineInfo','type':'post','param':{"swimachines":[{"label":"7r-CCLSW-01-11","ip":"172.28.164.30"},{"label":"7r-CCLSW-01-12","ip":"172.28.164.30"}],"swipad":"1234"}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwaremgmt/queryswitchmatchineInfo','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/alarm/queryswialarmparam','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/alarm/queryswiboardalarmparam','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/alarm/updateoraddswialarmparam','type':'post','param':{"alarmParameters":[{"nodeIp":"172.28.164.30","nodeType":"CE6851","userName":"fmroot","snmpPrivPwd":"Huawei_123","snmpAuthPwd":"Huwai_123","id":2}]}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/alarm/updateoraddswiboardalarmparam','type':'post','param':{"alarmParameters":[{"nodeIp":"172.28.164.20","nodeType":"CX320","userName":"fmroot","snmpPrivPwd":"Huawei_123","snmpAuthPwd":"Huawei_123","id":3}]}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/alarm/delete','type':'post','param':{"id":1,"nodeIp":"172.28.164.31"}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/alarm/setswitchbodirdnotify','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/alarm/setswitchnotify','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/alarm/validatealarmparam','type':'post','param':{"nodeIp":"172.28.164.30","userName":"fmroot","nodeType":"CE6851","snmpAuthPwd":"******","snmpPrivPwd":"******","extField":"old"}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/importHardwareInfo?jsonFileName=abc&import=123','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/queryBoard','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/queryFrame','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/queryRack','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/querySlot','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/querye9000snmpconfig','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/querydiskarraysnmpconfig','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/queryswitchboardpad?ip=192.168.1.1','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/queryswitchmachinepad?ip=192.168.1.1','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/querySubrack','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/queryDiskArray','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/querySubrackWithPwd','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/queryhardwareinfos','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/queryhardwareandilayerinfo','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/sete9000notify','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/setdiskarraynotify','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/hardware/ui/hardwareinnerservice/confighardwareerforupgrade','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/queryfusionsphereinfos','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/queryFSLinkedStatus','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/queryFMLinkedStatus','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/queryfusionmanagerinfos','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/updatefusionmanagerinfos','type':'post','param':{"fusionmanagers":[{"external_om_proxy_ip":"172.28.96.210","port":"643","user":"cloud_admin","password":"Huawei_123"}]}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/updatefusionsphereinfos','type':'post','param':{"fusionspheres":[{"url":"https://identity.az1.dc1.huawei.com/identity","domain":"OSSVDC","username":"hwvpc","userpad":"Huawei_123","k1-fsp":"Huawei_123","k1-root":"Huawei_123","manageip":"172.28.96.201"}]}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/register','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/queryVMwareLinkedStatus','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/query','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/delete','type':'post','param':{'id':'1'}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/queryCSMInfoNew','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/addVnfmUserpadInfo?csmInfoList=abc','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/queryopenstackinfos','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/updateopenstackinfos','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/queryOSRegStatus','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/deleteCSMInfoNew?deletecsmlist=abc','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/queryCSMStatus','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoservice/isLCMByVnfDn','type':'get','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/saveCSMInfonew?saveCSMInfoNew=abc','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/saveCSMInfonew?vnfFileName=abc','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/updateilayerinfo?hardwareJSONStr=abc','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/getvmstatusinfo','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/queryCSMInfoInn','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/getVNFInfo','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/queryfusionsphereinfos','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/queryfusionmanagerinfos','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/queryvmwareinfos','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/queryexternalip','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/querycsmver','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/configilayerforupgrade','type':'post','param':{}},\
#            {'module':'IAASEngGroup','url':'/rest/plat/omp/v1/iaas/ui/ilayerinfoinnerservice/updatevnfproductname','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/common/get_svrtime','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/common/get_language','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/common/get_platform_type','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/common/query_instances','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/common/get_ip_info_param','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/common/list_tasks','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/oss/get_diag_fault?instanceIp=172.28.130.131','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/oss/get_collect_fault?instanceIp=172.28.130.131&instanceName=U2020','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/system/create_sys_diag_task?instanceIp=172.28.130.131&instanceName=U2020','type':'post','param':{}},\
            {'module':'EMSFMAService','url':'/rest/emsfma/v1/system/query_sys_diag_process?instanceIp=172.28.130.131&instanceName=U2020','type':'post','param':{}}]
