fetch('https://fakestoreapi.com/products/1')
  .then(response => response.json())
  .then(product => {
    console.log('One Product:', product);
  });


fetch('https://fakestoreapi.com/products')
  .then(response => response.json())
  .then(products => {
    console.log('all products:', products);
  });