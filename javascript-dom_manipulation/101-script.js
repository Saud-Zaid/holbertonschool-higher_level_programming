document.addEventListener('DOMContentLoaded', function () {
  const btnTranslate = document.querySelector('#btn_translate');

  btnTranslate.addEventListener('click', function () {
    const languageCode = document.querySelector('#language_code').value;
    if (!languageCode) {
      return;
    }

    const url = `https://hellosalut.stefanbohacek.com/?lang=${languageCode}`;

    fetch(url)
      .then(response => response.json())
      .then(data => {
        document.querySelector('#hello').textContent = data.hello;
      })
      .catch(error => console.error('Error:', error));
  });
});
