const child = document.getElementById('child');
let x = 0;
let y = 0;
const step = 5;


function moveChild(event) {
  switch (event.key) {
    case 'ArrowUp':
      y -= step;
      break;
    case 'ArrowDown':
      y += step;
      break;
    case 'ArrowLeft':
      x -= step;
      break;
    case 'ArrowRight':
      x += step;
      break;
  }
  child.style.transform = `translate(${x}px, ${y}px)`;
}


window.addEventListener('keydown', moveChild);