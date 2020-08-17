const nav = document.querySelector('nav');
const sectionOne = document.querySelector('.showcase');

const sectionOneOptions = {
    rootMargin: "-800px 0px 0px 0px"
  };
  
  const sectionOneObserver = new IntersectionObserver(function(
    entries,
    sectionOneObserver
  ) {
    entries.forEach(entry => {
      if (!entry.isIntersecting) {
        nav.classList.add("nav-scrolled");
      } else {
        nav.classList.remove("nav-scrolled");
      }
    });
  },
  sectionOneOptions);
  
  sectionOneObserver.observe(sectionOne);