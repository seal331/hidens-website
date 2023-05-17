const footer = document.querySelector('footer');

function isFooterBelowHigherZIndexElements() {
  if (!footer) return false;
  let footerTop = footer.getBoundingClientRect().top;
  let higherZIndexElements = document.querySelectorAll('*');
  higherZIndexElements = Array.prototype.filter.call(higherZIndexElements, function(element) {
    return window.getComputedStyle(element).getPropertyValue('z-index') > 0;
  });
  for (let i = 0; i < higherZIndexElements.length; i++) {
    let elementBottom = higherZIndexElements[i].getBoundingClientRect().bottom;
    if (elementBottom > footerTop) {
      return true;
    }
  }
  return false;
}

function stickFooterToBottom() {
  if (!footer) return;
  if (isFooterBelowHigherZIndexElements()) {
    footer.style.bottom = '100%'
    footer.style.position = 'relative';
    footer.style.marginLeft = '0%'
    footer.style.width = '92.5%'
  } else {
    footer.style.position = 'fixed';
  }
}

window.addEventListener('scroll', stickFooterToBottom);
