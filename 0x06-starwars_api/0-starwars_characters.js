#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = 'https://swapi-api.hbtn.io/api/films/';
const argslen = process.argv.length;
const filmId = process.argv[2];

if (argslen > 2) {
  request(url + filmId, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
    );

    Promise.all(charactersName)
      .then((names) => console.log(names.join('\n')))
      .catch((allErr) => console.log(allErr));
  });
}
