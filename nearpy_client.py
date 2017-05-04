import numpy
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections
from redis import Redis
from nearpy.storage.storage_redis import RedisStorage
from pymongo import MongoClient
from nearpy.storage.storage_mongo import MongoStorage
from nearpy.utils.utils_storage import getsize


class GetStorageFactory(object):
    @classmethod
    def get_storage(cls, storage_name):
        if storage_name =='local':
            return None
        if storage_name == 'mongo':
            return cls.get_mongo()
        if storage_name == 'redis':
            return cls.get_redis()
        return None

    @classmethod
    def get_redis(cls):
        redis_object = Redis(host='localhost', port=6379, db=0)
        redis_storage = RedisStorage(redis_object)
        return redis_storage

    @classmethod
    def get_mongo(cls):
        mongo_uri = "<mongo_uri>"
        client = MongoClient(mongo_uri)
        mongo_object = client.rfk.vs_nearpy
        mongo_storage = MongoStorage(mongo_object)
        return mongo_storage


def measure_size(storage_name):
    # Dimension of our vector space
    dimension = 1024

    # Create a random binary hash with 10 bits
    rbp = RandomBinaryProjections('rbp_random', 10)

    # Create engine with pipeline configuration
    storage = GetStorageFactory.get_storage(storage_name)

    engine = Engine(dimension, lshashes=[rbp], storage=storage)

    # Index 1000000 random vectors (set their data to a unique string)

    for index in range(100000):
        v = numpy.random.randn(dimension)
        engine.store_vector(v, 'data_%d' % index)
        if index % 1000 == 0:
            print "iteration number: %s" % (index/1000)

    return getsize(engine)

if __name__ =='__main__':
    measure_size('redis')