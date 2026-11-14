const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const list = document.querySelector('#list_movies');
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      list.appendChild(listItem);
    });
  })
  .catch(error => console.error('Error:', error));
