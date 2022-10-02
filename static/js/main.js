// const targetSection = document.querySelector(".lhi_pabpnq");
const heroFeatureCon = document.getElementById("heroFeatureContainer");
const heroSection = document.getElementById("heroSection");
const nav = document.getElementById("navBar");
const prod = document.getElementById("productContainer");

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
      nav.className = "container fle_cajrzm";
    } else {
      heroFeatureCon.className = "container relative";
      heroSection.className = "mqh_bsspwi hero-drop-shadow";
      nav.className = "container fle_cajrzm nav-background";
    }
  });
}, heroOptions);

heroObserver.observe(heroSection);

const heroSubOptions = {
  root: null,
  threshold: 0,
  rootMargin: "-20px",
};

const subHeroObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      prod.className = "sup_kzezbz";
    } else {
      prod.className = "sup_kzezbz margin-top";
    }
  });
});

subHeroObserver.observe(heroFeatureCon);
