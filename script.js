
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".collapsible").forEach(button => {
        button.addEventListener("click", () => {
            button.classList.toggle("active");
            const content = button.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    });

    // Scroll fluide
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            target.scrollIntoView({ behavior: 'smooth' });
        });
    });
