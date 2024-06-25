import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ' + err);
});


client.HSET('HolbertonSchools', 'Portland', 50, redis.print);
client.HSET('HolbertonSchools', 'Seattle', 80, redis.print);
client.HSET('HolbertonSchools', 'New York', 20, redis.print);
client.HSET('HolbertonSchools', 'Bogota', 20, redis.print);
client.HSET('HolbertonSchools', 'Cali', 40, redis.print);
client.HSET('HolbertonSchools', 'Paris', 2, redis.print);

client.HGETALL('HolbertonSchools', (err, reply) => {
  if (err) {
    console.log('Error receiving hash: ' + err.message)
  } else {
    console.log(reply)
  }
});
