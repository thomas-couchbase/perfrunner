[clusters]
DGM-aws =
    172.23.122.98:8091
    172.23.122.99:8091
    172.23.122.100:8091
    172.23.122.101:8091

[clients]
hosts =
    172.23.122.97
credentials = root:couchbase  

[storage]
data = /data
index = /data

[credentials]
rest = Administrator:password
ssh = root:couchbase

[parameters]
Platform = VM        
OS = Centos 6.5
CPU = Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz
Memory = 15GB
Disk = SSD
