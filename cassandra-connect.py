from cassandra.cluster import Cluster
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == "__main__":
    cluster = Cluster([config['cassandra']['host']],port=int(config['cassandra']['port']))
    session = cluster.connect(config['cassandra']['keyspace'],wait_for_all_pools=True)

    rows = session.execute(config['cassandra']['query'])
    for row in rows:
        print(row.age,row.name,row.username)