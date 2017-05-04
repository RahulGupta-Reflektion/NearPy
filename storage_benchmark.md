# Benchmarking (redis_storage/mongo_storage/local_storage )

## Setup
* 100,000 vectors with 1024 dimensions 
* No data store 

## Test and Results
### local Memory 
* Size ~ 800 MB 

### Flat File 
* Size 2 GB

### Redis Memory
* Size ~ 800 MB 

### Mongo Memory 
* Size > 1 GB 

## Conclusions 
* Redis storage is very fast in storing data comapred to mongo. Surprisingly, mongo take 
more memory compared to redis and is slower.
* Objective of the test was to reduce memory footprint. So, it would be beneficial to avoid storing 
vectors, if we are not using them actively
* Since redis takes about 800 MB for 100,000 vectors, It's not a pressing issue to devote significant 
efforts on optimizing storage.