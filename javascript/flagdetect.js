// Get the footer element
const footer = document.querySelector('footer');

// Function to check the visibility of the footer
function checkFooterVisibility() {
  // Get all the elements on the page
  const elements = document.getElementsByTagName('*');
  
  // Loop through all the elements and find the highest z-index
  let highestZIndex = -1;
  for (let i = 0; i < elements.length; i++) {
    const zIndex = parseInt(window.getComputedStyle(elements[i]).zIndex);
    if (zIndex > highestZIndex && !isNaN(zIndex)) {
      highestZIndex = zIndex;
    }
  }
  
  // If the highest z-index is greater than or equal to the footer's z-index, hide the footer
  if (highestZIndex >= parseInt(window.getComputedStyle(footer).zIndex)) {
    footer.style.display = 'none';
  } else {
    // Otherwise, show the footer
    footer.style.display = 'block';
  }
}

// Call the function when the page loads and whenever it resizes or scrolls
window.addEventListener('load', checkFooterVisibility);
window.addEventListener('resize', checkFooterVisibility);
window.addEventListener('scroll', checkFooterVisibility);
