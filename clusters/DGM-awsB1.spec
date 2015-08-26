[clusters]
DGM-aws =
    10.0.0.177:8091

[clients]
hosts =
    ec2-54-6-32-220.compute-1.amazonaws.com
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
