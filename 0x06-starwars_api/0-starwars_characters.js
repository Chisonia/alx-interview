#!/usr/bin/node

const request = require('request'); // Ensure the request module is installed
const movieId = process.argv[2]; // Get the movie ID from the command-line arguments

if (!movieId) {
  console.error('Please provide a Movie ID as a positional argument.');
  process.exit(1);
}

// API URL for the specified movie
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Fetch and print each character name
    characterUrls.forEach((url) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(`Error fetching character data: ${charError}`);
          return;
        }

        if (charResponse.statusCode === 200) {
          try {
            const character = JSON.parse(charBody);
            console.log(character.name);
          } catch (parseError) {
            console.error(`Error parsing character data: ${parseError}`);
          }
        } else {
          console.error(`Failed to fetch character. Status code: ${charResponse.statusCode}`);
        }
      });
    });
  } catch (parseError) {
    console.error(`Error parsing movie data: ${parseError}`);
  }
});
