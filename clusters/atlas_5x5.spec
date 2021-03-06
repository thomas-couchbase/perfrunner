[clusters]
atlas_c1 =
	172.23.96.100:8091
    172.23.96.101:8091
    172.23.96.102:8091
    172.23.96.103:8091
    172.23.96.104:8091
atlas_c2 =
    172.23.96.105:8091
    172.23.96.106:8091
    172.23.96.107:8091
    172.23.96.108:8091
    172.23.96.109:8091

[clients]
hosts =
    172.23.96.110
    172.23.96.111
credentials = root:couchbase

[storage]
data = /data
index = /data

[credentials]
rest = Administrator:password
ssh = root:couchbase

[parameters]
Platform = Physical
OS = CentOS 6.5
CPU = Intel Xeon E5-2680 v2 (40 vCPU)
Memory = 256 GB
Disk = RAID 10 SSD
