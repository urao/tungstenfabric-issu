Tested ISSU upgrade from R3.0.3 to R3.2.8

Steps:

1) Bring up new contrail controllers with R3.2.8 
2) Make sure, the contrail services are all active
3) Modify existing testbed.py under /opt/contrail/utils/fabfile/testbeds/ which old controller information as given the sample [testbed.py](https://github.com/urao/tungstenfabric-issu/blob/master/ubuntu/testbed_issu.py) 
4) Run: cd /opt/contrail/utils && fab issu_contrail_generate_conf
5) Run: cd /opt/contrail/utils && fab issu_contrail_migrate_config
6) Verify that the database on old controllers is copied over to new controllers
7) Migrate computes
8) Run, cd /opt/contrail/utils && fab issu_contrail_migrate_compute_node:3.0.3,/root/contrail-install-packages-3.2.8.0-66_centos73mitaka.el7.centos.noarch.rpm,<DISCOVERY_IP/VIP>,root@191.168.100.10”
9) Verify “contrail-status” on compute node
10) Run, cd /opt/contrail/utils && fab issu_contrail_finalize:<OLD_DISCOVERY_IP>,<NEW_DISCOVERY_IP>

Refer Links:
1) [ISSU](http://www.opencontrail.org/opencontrail-in-service-software-upgrade/)
