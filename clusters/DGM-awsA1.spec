[clusters]
DGM-aws =
    10.0.0.69:8091

[clients]
hosts =
    ec2-52-20-31-56.compute-1.amazonaws.com
credentials = root:couchbase  

[storage]
data = /data
index = /data

[credentials]
rest = Administrator:password
ssh = root:couchbase

[parameters]
Platform = AWS       
OS = Centos 6.5
CPU = Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz
Memory = 15GB
Disk = vDisk
