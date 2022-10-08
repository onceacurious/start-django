// const targetSection = document.querySelector(".lhi_pabpnq");
const heroFeatureCon = document.getElementById("heroFeatureContainer");
const heroSection = document.getElementById("heroSection");
const nav = document.getElementById("navBar");
const prod = document.getElementById("productContainer");

const ulNavBar = document.getElementById("navCollBtn");

const heroOptions = {
  root: null,
  threshold: 0.75,
  rootMargin: "-20px",
};

const heroObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      heroFeatureCon.className = "container absolute";
      heroSection.className = "mqh_bsspwi hero-inner-shadow";
      nav.style.background = "transparent";
    } else {
      heroFeatureCon.className = "container relative";
      heroSection.className = "mqh_bsspwi hero-drop-shadow";
      nav.style.background = "#360c26";
    }
  });
}, heroOptions);

heroObserver.observe(heroSection);

function navToggle() {
  var classes = window.getComputedStyle(ulNavBar).backgroundColor;
  // console.log(classes);
  if (classes == "rgba(0, 0, 0, 0)") {
    ulNavBar.style.backgroundColor = "#360c26";
  } else {
    ulNavBar.style.backgroundColor = "transparent";
  }
}
