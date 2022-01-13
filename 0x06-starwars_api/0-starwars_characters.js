#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

url = 'https://swapi-api.hbtn.io/api/films/' + argv[2]

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  }
  else {
    for (const value of JSON.parse(body).characters) {
      request(value, (err, response, body) => {
        if (err) {
          console.log(err);
        }
        else {
          console.log(JSON.parse(body).name);
        }
      });
  }}
})
