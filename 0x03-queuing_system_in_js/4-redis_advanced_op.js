import {createClient} from 'redis';
import redis from 'redis';
const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));


const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
  client.HSET('HolbertonSchools', key, values[index], redis.print);
});

client.HGETALL('HolbertonSchools', (err, reply) => {
    if (err) {
        console.log(err);
    } else {
        console.log(reply)
    }
})