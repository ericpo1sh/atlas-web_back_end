const listProducts = [
  {
    Id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    Id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    Id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    Id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
]
function getItemById(id) {
  let target_id;
  listProducts.forEach((product) => {
    if (product.Id === id) {
      target_id = product
    }
  })
  return target_id;
}

const express = require('express');
const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.send(JSON.stringify(listProducts));
});

app.get('/list_products/itemId(\\d+)', (req, res) => {
  const stockId = req.params.itemId
  res.send(JSON.stringify(stockId))
})

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

import redis from 'redis';
const { promisify } = require('util');

const client = redis.createClient();
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ' + err);
});

function reserveStockById(itemId, stock) {
  client.set(`item:${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item:${itemId}`);
  return parseInt(reservedStock) || 0;
}
