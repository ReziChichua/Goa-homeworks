 const form = document.getElementById('search-form');
    const input = document.getElementById('search-input');
    const results = document.getElementById('results');

    form.addEventListener('submit', function(e) {
      e.preventDefault(); 
      const searchTerm = input.value.trim();
      if (!searchTerm) return;

    
      fetch(`https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => {
          results.innerHTML = ''; 

          if (!data.items) {
            results.innerHTML = '<p>Cant find.</p>';
            return;
          }

          data.items.forEach(book => {
            const info = book.volumeInfo;
            const title = info.title || 'unknown title';
            const year = info.publishedDate ? info.publishedDate.split('-')[0] : 'unknown year';
            const description = info.description || 'cant access';
            const pageCount = info.pageCount || 'unknownn pages';
            const thumbnail = info.imageLinks?.thumbnail || '';

            const bookDiv = document.createElement('div');
            bookDiv.className = 'book';
            bookDiv.innerHTML = `
              <img src="${thumbnail}" alt="${title}">
              <div>
                <h2>${title}</h2>
                <p><strong>Publish year:</strong> ${year}</p>
                <p><strong>Pages Count:</strong> ${pageCount}</p>
                <p>${description}</p>
              </div>
            `;
            results.appendChild(bookDiv);
          });
        })
    });