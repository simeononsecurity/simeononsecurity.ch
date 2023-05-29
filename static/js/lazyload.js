document.addEventListener('DOMContentLoaded', function () {
    // Get all the images within the page
    var images = document.querySelectorAll('img');

    // Check if there is only one image on the page
    if (images.length === 1) {
        // Check if the image doesn't already have the 'loading' attribute set to 'lazy'
        if (!images[0].hasAttribute('loading')) {
            // Add the 'loading' attribute with the value 'lazy'
            images[0].setAttribute('loading', 'lazy');
        }
    } else {
        // Loop through the images starting from the second one
        for (var i = 1; i < images.length; i++) {
            // Check if the image doesn't already have the 'loading' attribute set to 'lazy'
            if (!images[i].hasAttribute('loading')) {
                // Add the 'loading' attribute with the value 'lazy'
                images[i].setAttribute('loading', 'lazy');
            }
        }
    }
});