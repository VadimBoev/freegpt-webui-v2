let shiftAmount = 70;
let mainContainer = document.querySelector('.main-container'); 

function shiftContentUp() {
   mainContainer.style.marginTop = "-" + shiftAmount + "%";
}

function resetContent() {
  mainContainer.style.marginTop = "0";
}

function toggleFullScreen() {
  if (!document.fullscreenElement) {
    const elementToFullScreen = document.documentElement;
        if (elementToFullScreen.mozRequestFullScreen) { // Firefox
      elementToFullScreen.mozRequestFullScreen();
    } else if (elementToFullScreen.webkitRequestFullscreen) { // Chrome, Safari und Opera
      elementToFullScreen.webkitRequestFullscreen();
    } else if (elementToFullScreen.msRequestFullscreen) { // Internet Explorer und Edge
      elementToFullScreen.msRequestFullscreen();
    }
  } else {
    if (document.mozCancelFullScreen) { // Firefox
      document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) { // Chrome, Safari und Opera
      document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { // Internet Explorer und Edge
      document.msExitFullscreen();
    }
  }
};

document.getElementById('message-input').addEventListener('focus', function() {
  if (document.fullscreenElement) {
    shiftContentUp();
  }
});

document.getElementById('message-input').addEventListener('blur', function() {
  if (document.fullscreenElement) {
    resetContent();
  }
});

document.addEventListener('fullscreenchange', function() {
  if (document.fullscreenElement) {
    document.getElementById('fullscreen-toggle').checked = true;
  } else {
    document.getElementById('fullscreen-toggle').checked = false;
  }
});

document.getElementById('fullscreen-toggle').addEventListener('change', function() {
  toggleFullScreen(this.checked);
});

