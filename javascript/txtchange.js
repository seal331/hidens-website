const textSequence = ['WHAT H', 'Foo', 'Bar', 'h', 'H', 'Test-Text-For-A-Test-Thing', 'gentoo balls', 'Foobar', 'norton'];
let index = 0;

const sequenceElement = document.getElementById("sequence");
sequenceElement.textContent = textSequence[index];

setInterval(() => {
  index = (index + 1) % textSequence.length;
  sequenceElement.textContent = textSequence[index];
}, 500);
