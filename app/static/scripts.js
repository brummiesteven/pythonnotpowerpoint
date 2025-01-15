document.addEventListener('DOMContentLoaded', function() {
    let currentSlide = 0;
    const slides = [
        'slide1.html',
        'slide2.html',
        'slide3.html'
    ];

    document.getElementById('next-slide').addEventListener('click', function() {
        currentSlide++;
        if (currentSlide < slides.length) {
            document.querySelector('.slide').src = slides[currentSlide];
        } else {
            alert('No more slides');
        }
    });
});
