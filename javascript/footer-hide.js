// Get the footer element
const footer = document.querySelector('footer');

// Hide the footer if it's under an element with a higher z-index
function hideFooter() {
  if (!footer) return;
  let footerTop = footer.getBoundingClientRect().top;
  let higherZIndexElements = document.querySelectorAll('*');
  higherZIndexElements = Array.prototype.filter.call(higherZIndexElements, function(element) {
    return window.getComputedStyle(element).getPropertyValue('z-index') > 0;
  });
  let shouldHideFooter = false;
  for (let i = 0; i < higherZIndexElements.length; i++) {
    let elementBottom = higherZIndexElements[i].getBoundingClientRect().bottom;
    if (elementBottom > footerTop) {
      shouldHideFooter = true;
      break;
    }
  }
  if (shouldHideFooter) {
    if (footer.style.display !== 'none') {
      footer.style.display = 'none';
    }
  } else {
    if (footer.style.display !== 'block') {
      footer.style.display = 'block';
    }
  }
}

// Call the hideFooter function whenever the window is resized or scrolled
window.addEventListener('resize', hideFooter);
window.addEventListener('scroll', hideFooter);
