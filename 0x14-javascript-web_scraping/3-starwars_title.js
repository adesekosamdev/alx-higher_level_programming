#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = 'http://swapi.co/api/films/' + episode;
request(url, function (error, response, body) {
	console.log(error || JSON.parse(body).title);
});
