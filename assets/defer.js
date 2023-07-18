// Start Custom Scroll Up Button

  // Get the button:
  let mybutton = document.getElementById("myBtn");

  // When the user scrolls down 20px from the top of the document, show the button
  window.onscroll = function() {scrollFunction()};

  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }

  // When the user clicks on the button, scroll to the top of the document
  function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  } 

// End Custom Scroll Up Button

// Start Google Adsense iFrame Fixes

window.addEventListener("DOMContentLoaded", function() {
    try {
      var iframes = document.querySelectorAll(
        'iframe[src*="https://googleads.g.doubleclick.net"], iframe[data-google-container-id]'
      );

      iframes.forEach(function(iframe) {
        iframe.setAttribute("title", "google ads");
        iframe.setAttribute("role", "banner");

        if (
          iframe.hasAttribute("data-google-container-id") &&
          iframe.complete
        ) {
          setAttributes(iframe);
        } else {
          iframe.addEventListener("load", function() {
            setAttributes(iframe);
          });
        }
      });

      function setAttributes(iframe) {
        var containerId = iframe.getAttribute("data-google-container-id");
        iframe.setAttribute("title", "google ads");
        iframe.setAttribute("role", "banner");
      }
    } catch (error) {
      // Handle any errors that occur during the execution of the code
      console.error("An error occurred:", error);
    }
  });

// END Google Adsense iFrame Fixes