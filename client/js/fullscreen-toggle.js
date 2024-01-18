function toggleFullScreen() {
  // Prüfen, ob der Vollbildmodus bereits aktiv ist
  if (!document.fullscreenElement) {
    // Wählen Sie das Element aus, das in den Vollbildmodus versetzt werden soll
    const elementToFullScreen = document.documentElement; // für gesamte Seite

    // Versuchen Sie, den Vollbildmodus anzufragen
    if (elementToFullScreen.mozRequestFullScreen) { // Firefox
      elementToFullScreen.mozRequestFullScreen();
    } else if (elementToFullScreen.webkitRequestFullscreen) { // Chrome, Safari und Opera
      elementToFullScreen.webkitRequestFullscreen();
    } else if (elementToFullScreen.msRequestFullscreen) { // Internet Explorer und Edge
      elementToFullScreen.msRequestFullscreen();
    }
  } else {
    // Verlassen des Vollbildmodus
    if (document.mozCancelFullScreen) { // Firefox
      document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) { // Chrome, Safari und Opera
      document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { // Internet Explorer und Edge
      document.msExitFullscreen();
    }
  }
};

// Fügen Sie den Event Listener zum Schalter hinzu
document.getElementById('fullscreen-toggle').addEventListener('change', function() {
  toggleFullScreen();
});

document.addEventListener('fullscreenchange', function() {
  // Prüfen, ob der Vollbildmodus aktiv ist
  if (document.fullscreenElement) {
    // Setzen Sie die Checkbox auf checked
    document.getElementById('fullscreen-toggle').checked = true;
  } else {
    // Setzen Sie die Checkbox auf unchecked
    document.getElementById('fullscreen-toggle').checked = false;
  }
});
