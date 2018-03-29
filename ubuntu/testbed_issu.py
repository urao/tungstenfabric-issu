from fabric.api import env                                                                    

#Management ip addresses of hosts in the cluster
host1 = 'root@192.168.122.10'                      
host2 = 'root@192.168.122.11'                          
host3 = 'root@192.168.122.13'

# v1_host(1,2,) old controller information
v1_host1 = 'root@192.168.122.14'                      
v1_host2 = 'root@192.168.122.15'                          
v1_host3 = 'root@192.168.122.16'

#External routers if any
#for eg.                
ext_routers = []                            

#Autonomous system number
router_asn = 64512       

#Host from which the fab commands are triggered to install and provision
host_build = 'root@192.168.122.10'                                             
v1_host_build = 'root@192.168.122.14'                                             

#Role definition of the hosts.
env.roledefs = {                                
    'all': [host1,host2, host3],                                   
    'cfgm': [host1,host2,host3],                                                   
    'control': [host1,host2,host3],                                                               
    'collector': [host1,host2,host3],                                                             
    'webui': [host1,host2,host3],                                                                 
    'database': [host1,host2,host3],                                                              
    'build': [host_build],                                                                        
    'compute': [],                                                                                
    'oldcfgm': [v1_host1, v1_host2, v1_host3],                                                             
    'oldcontrol':[v1_host1, v1_host2, v1_host3],                                                           
    'olddatabase':[v1_host1, v1_host2, v1_host3],                                                          
    'oldcollector':[v1_host1, v1_host2, v1_host3],                                                          
    'oldwebui':[v1_host1, v1_host2, v1_host3]                                                                        
}                                                                                                            

                                                                                                      
env.hostnames = {                                                                                          
    host1: 'host-1',                                                                                         
    host2: 'host-2',                                                                                           
    host3: 'host-3',                                                                                           
    v1_host1: 'host-4',                                                                                           
    v1_host2: 'host-5',                                                                                             
    v1_host3: 'host-6',                                                                                              
}                                            

# Passwords of each host
# for passwordless login's no need to set env.passwords,
# instead populate env.key_filename in testbed.py with public key.
env.passwords = {                                                 
    host1: 'contrail123',                                              
    host2: 'contrail123',                                              
    host3: 'contrail123',                                              
    v1_host1: 'contrail123',                                                                                         
    v1_host2: 'contrail123',                                                                                         
    v1_host3: 'contrail123',                                                                                         
                                                                                                              
    host_build: 'contrail123',  
    v1_host_build: 'contrail123',                                                                                                                      

}                                                                                                                                                   

# SSH Public key file path for passwordless logins
# if env.passwords is not specified.              
#env.key_filename = '/root/.ssh/id_rsa.pub'       

#For reimage purpose
env.ostypes = {     
    host1: 'ubuntu',
    host2: 'ubuntu',
    host3: 'ubuntu',
    v1_host1: 'ubuntu',
    v1_host2: 'ubuntu',
    v1_host3: 'ubuntu',
}                    

env.orchestrator = 'none' #other values are 'vcenter', 'none' default:openstack
                                                
analytics_flow_ttl = 4                                                           

#following parameter allows to specify minimum amount of disk space in the analytics
#database partition, if configured amount of space is not present, it will fail provisioning
minimum_diskGB = 26                                                                         
                                                                                                           
                                          
env.ha = {                                                                                                            
    'contrail_internal_vip'   : '141.102.0.200',       #Internal Virtual IP of the contrail HA Nodes.                                                                              
}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

#To enable multi-tenancy feature
multi_tenancy = False
           
# To configure the encapsulation priority. Default: MPLSoGRE
env.encap_priority =  "'MPLSoUDP','MPLSoGRE','VXLAN'"      
       
