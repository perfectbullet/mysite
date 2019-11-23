import redis


if __name__ == '__main__':
    # rds = redis.Redis(host='127.0.0.1', port=6379, db=0, charset='utf8')
    rds = redis.Redis()
    re = rds.set('bing', 'baz')
    print(rds.get('mobile'))
