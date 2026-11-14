document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;
    })
    .catch(error => console.error('Error:', error));
});
