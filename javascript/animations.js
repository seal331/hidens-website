window.addEventListener('DOMContentLoaded', function() {
  // Sidebar animation
  var sidebar = document.querySelector('.sidebar');
  animate(sidebar, 'left', '0', '-200px');

  // Footer animation
  var footer = document.querySelector('footer');
  animate(footer, 'bottom', '0', '-200px');

  // Icon hover effect
  var icons = document.querySelectorAll('.icon, .smallicon, .yticon, .discicon, .vpcicon');
  icons.forEach(function(icon) {
    icon.addEventListener('mouseenter', function() {
      this.classList.add('hover');
      this.style.transform = 'scale(1.2)';
    });

    icon.addEventListener('mouseleave', function() {
      this.classList.remove('hover');
      this.style.transform = 'scale(1)';
    });
  });
});

function animate(element, property, targetValue, initialValue) {
  var current = parseInt(initialValue);
  var target = parseInt(targetValue);
  var duration = 500; // Animation duration in milliseconds
  var start = null;

  function step(timestamp) {
    if (!start) start = timestamp;
    var progress = timestamp - start;
    if (progress < duration) {
      var value = easeInOutQuad(progress, current, target - current, duration);
      element.style[property] = value + 'px';
      requestAnimationFrame(step);
    } else {
      element.style[property] = targetValue;
    }
  }

  requestAnimationFrame(step);
}

function easeInOutQuad(t, b, c, d) {
  t /= d / 2;
  if (t < 1) return c / 2 * t * t + b;
  t--;
  return -c / 2 * (t * (t - 2) - 1) + b;
}
