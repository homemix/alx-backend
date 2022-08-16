import {createClient} from 'redis';

const {promisify} = require('util');

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
            if (err) {
                console.log(err);
            } else {
                console.log(reply)
            }
        }
    );
}

const redis_get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    const value = await redis_get(schoolName);
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');