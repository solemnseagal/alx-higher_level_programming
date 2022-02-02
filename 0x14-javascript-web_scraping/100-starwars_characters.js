#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];

if (process.argv.length > 2) {
request(url, function (error, response, body) {
if (error) {
console.log(error)
} 
const characters = JSON.parse(body).characters;
characters.forEach((character) => {
request(character, function (error, response, body) {
if (error) {
console.log(error)
}
console.log(JSON.parse(body).name);
});
});
});
}
