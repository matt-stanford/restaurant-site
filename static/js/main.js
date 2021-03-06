const nav = document.querySelector('.navbar');

window.onscroll = function() {
  var top = window.scrollY;
  if (top >= 100) {
    nav.classList.add("nav-scrolled");
    } else {
      nav.classList.remove("nav-scrolled");
    }
}

// smooth scroll
$('#contact-link').on('click', function(e) {
  e.preventDefault();

  const hash = this.hash;

  $('html, body').animate({
    scrollTop: $(hash).offset().top
  }, 800);
});

// calendar

const date = new Date();

const renderCalendar = () => {
  const monthDays = document.querySelector('.days');

  const firstDay = new Date(date.getFullYear(), date.getMonth(), 1).getDate();
  const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();

  const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();

  const firstDayIndex = new Date(date.getFullYear(), date.getMonth(), 1).getDay()
  const lastDayIndex = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay();

  const nextDays = 7 - lastDayIndex - 1

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ]

  document.querySelector('.date h4').innerHTML = months[date.getMonth()];
  document.querySelector('.date p').innerHTML = new Date().toDateString();

  const prevArrow = document.querySelector('.prev');

  if (date.getMonth() === new Date().getMonth()) {
    prevArrow.style.visibility = 'hidden';
  } else {
    prevArrow.style.visibility = 'visible';
  }

  let days = ""

  for(let x = firstDayIndex; x > 0; x--) {
    days += `<div class="prev-date">${prevLastDay - x + 1}</div>`
  }

  for(let i = 1; i <= lastDay; i++) {
    if (i < new Date().getDate() && date.getMonth() === new Date().getMonth()) {
      days += `<div class="prev-date">${i}</div>`
    } else if (i === new Date().getDate() && date.getMonth() === new Date().getMonth()) {
      days += `<div class="select-date today">${i}</div>`;
    } else {
      days += `<div class="select-date">${i}</div>`;
    }
  }

  for(let j = 1; j <= nextDays; j++) {
    days += `<div class="select-date next-date">${j}</div>`;
    monthDays.innerHTML = days;
  }

  const bookingModalOpen = document.querySelector('.booking-modal-open');
  const bookingModal = document.querySelector('.booking-modal');

  bookingModalOpen.addEventListener('click', () => {
    bookingModal.style.display = 'block';
  });
  
  const daysOfMonth = Array.from(document.querySelectorAll('.select-date'));
  console.log(daysOfMonth)
  
  daysOfMonth.forEach(day => {
    day.addEventListener('click', () => {
      daysOfMonth.forEach(d => {
        d.classList.remove('selected-date')
      });
      day.classList.add('selected-date');
      bookingModal.style.display = 'none';
      const bookingDate = `${date.getFullYear()}-${("0" + (date.getMonth()+1)).slice(-2)}-${("0" + day.textContent).slice(-2)}`;
      bookingModalOpen.value = bookingDate;
    });
  });

}

document.querySelector('.prev').addEventListener('click', () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});

document.querySelector('.next').addEventListener('click', () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

renderCalendar()
