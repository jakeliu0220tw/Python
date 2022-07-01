from redis import Redis

conn = Redis(host='10.140.0.3', port=6380)
ret = conn.ping()
print(f'ret = {ret}')

keys = conn.keys("*")
print(f'keys = {keys}')

# lpush
conn.lpush("dev-build-android","A")
conn.lpush("dev-build-android","B")
conn.lpush("dev-build-android","C")
count = conn.llen("dev-build-android")
print(f'count of dev-build-android = {count}')
keys = conn.keys("*")
print(f'keys = {keys}')

# rpop
value = conn.rpop("dev-build-android")
if value != None:
    print(f'value = {value}')
value = conn.rpop("dev-build-android")
if value != None:
    print(f'value = {value}')
value = conn.rpop("dev-build-android")
if value != None:
    print(f'value = {value}')
count = conn.llen("dev-build-android")
print(f'count of dev-build-android = {count}')

# pipeline
pipe = conn.pipeline()
pipe.lpush("dev-build-android", '1')
pipe.lpush("dev-build-android", '2')
pipe.lpush("dev-build-android", '3')
pipe.execute()
print(f'count of dev-build-android = {conn.llen("dev-build-android")}')

# lpos
pos = conn.lpos("dev-build-android", '1')
print(f'pos of 1 = {pos}')
conn.delete("dev-build-android")
pos = conn.lpos("dev-build-android", '1')
print(f'pos of 1 = {pos}')
if pos == None:
    print('not exist value 1')