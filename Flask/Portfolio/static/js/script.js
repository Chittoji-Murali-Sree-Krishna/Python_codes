const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelectorAll(".nav__links");

navToggle.addEventListener("click", () => {
  document.body.classList.toggle("nav-open");
});

navLinks.forEach((links) => {
  links.addEventListener("click", () => {
    document.body.classList.remove("nav-open");
  });
});
