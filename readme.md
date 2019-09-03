# Virtual env configuration
`virtualenv env`
`source env/bin/activate`

### install dependencies
`pip install -r requirements.txt`

# Install cassandra
`cd /Tools/cassandra`
`mkdir node1 node2`

### up first node
`docker run --name cassandra1 -p 9042:9042 -v /Tools/cassandra/node1:/var/lib/cassandra/data -e CASSANDRA_CLUSTER_NAME=MyCluster -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra`

### check status
`docker exec -it cassandra1  nodetool status`

### up second node 
`docker run --name cassandra2 -v /Tools/cassandra/node2:/var/lib/cassandra/data -e CASSANDRA_SEEDS="$(docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra1)" -e CASSANDRA_CLUSTER_NAME=MyCluster -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra:latest`

### check status
`docker exec -it cassandra1  nodetool status`

# Configuration

`docker exec -it cassandra2  cqlsh`

### create keyspace
`create keyspace CityInfo with replication = {'class' : 'SimpleStrategy', 'replication_factor':2}`

### use keyspace
`use cityinfo ;`

### create tables
`CREATE TABLE cities (`
`id int,`
`name text,`
`country text,`
`PRIMARY KEY(id)`
`);`

`CREATE TABLE users (`
`username text,`
`name text,`
`age int,`
`PRIMARY KEY(username)`
`);`

### insert test data
`INSERT INTO cities(id,name,country) VALUES (3,'Dubai','UAE');`
`INSERT INTO cities(id,name,country) VALUES (4,'Berlin','Germany');`
`INSERT INTO users(username,name,age) VALUES ('jack01','Jack David',23);`
`INSERT INTO users(username,name,age) VALUES ('ninopk','Nina Rehman',34);`

# Testing cassandra-connect
`python cassandra-connect.py`
