function toggleMenu() {
  document.getElementById('navLinks').classList.toggle('open');
}

document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    document.getElementById('navLinks').classList.remove('open');
  });
});

const canvas  = document.getElementById('sparkCanvas');
const ctx     = canvas.getContext('2d');
let sparks    = [];
let animating = false;

function resizeCanvas() {
  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const COLORS = ['#D81B6A', '#F9E5EE', '#FFFFFF', '#A0174F', '#F2C8DC', '#FFD6E8'];

class Spark {
  constructor(x, y) {
    this.x    = x + (Math.random()-0.5) *200;
    this.y    = y + (Math.random()-0.5) *200;
    this.vx   = (Math.random()-0.5) *3;
    this.vy   = (Math.random()-0.5) *3 -1.5;
    this.size = Math.random()*6+3;
    this.life = 1;
    this.decay= Math.random()*0.018+0.012;
    this.color= COLORS[Math.floor(Math.random() * COLORS.length)];
    this.rot  = Math.random()*Math.PI*2;
    this.rotV = (Math.random()-0.5)*0.15;
    this.type = Math.random()>0.4 ? 'star' : 'circle';
  }

  update() {
    this.x    += this.vx;
    this.y    += this.vy;
    this.vy   += 0.04; 
    this.life -= this.decay;
    this.rot  += this.rotV;
  }

  draw() {
    ctx.save();
    ctx.globalAlpha = Math.max(this.life, 0);
    ctx.translate(this.x, this.y);
    ctx.rotate(this.rot);
    ctx.fillStyle = this.color;

    if (this.type === 'star') {
      drawStar(ctx, 0, 0, 4, this.size, this.size * 0.4);
    } else {
      ctx.beginPath();
      ctx.arc(0, 0, this.size * 0.55, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  }
}

function drawStar(ctx, cx, cy, spikes, outerR, innerR) {
  let rot = (Math.PI / spikes) * 0 - Math.PI / 2;
  ctx.beginPath();
  for (let i = 0; i < spikes * 2; i++) {
    const r   = i % 2 === 0 ? outerR : innerR;
    const ang = rot + (Math.PI / spikes) * i;
    i === 0
      ? ctx.moveTo(cx + r * Math.cos(ang), cy + r * Math.sin(ang))
      : ctx.lineTo(cx + r * Math.cos(ang), cy + r * Math.sin(ang));
  }
  ctx.closePath();
  ctx.fill();
}

function burstSparks(x, y, count = 40) {
  for (let i = 0; i < count; i++) sparks.push(new Spark(x, y));
  if (!animating) animateLoop();
}

function animateLoop() {
  animating = true;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  sparks = sparks.filter(s => s.life > 0);
  sparks.forEach(s => { s.update(); s.draw(); });
  if (sparks.length > 0) requestAnimationFrame(animateLoop);
  else animating = false;
}
const downloadBtn = document.getElementById('downloadBtn');
if (downloadBtn) {
  downloadBtn.addEventListener('click', e => {
    const r = downloadBtn.getBoundingClientRect();
    burstSparks(r.left + r.width / 2, r.top + r.height / 2, 55);
  });
  downloadBtn.addEventListener('mouseenter', e => {
    const r = downloadBtn.getBoundingClientRect();
    burstSparks(r.left + r.width / 2, r.top + r.height / 2, 20);
  });
}
const sparkBtn = document.getElementById('sparkBtn');
if (sparkBtn) {
  sparkBtn.addEventListener('click', e => {
    const r = sparkBtn.getBoundingClientRect();
    burstSparks(r.left + r.width / 2, r.top + r.height / 2, 40);
  });
}
window.addEventListener('load', () => {
  setTimeout(() => burstSparks(window.innerWidth / 2, window.innerHeight / 2, 60), 600);
});
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  navbar.style.boxShadow = window.scrollY > 20
    ? '0 4px 24px rgba(139,0,64,0.15)'
    : '0 2px 16px rgba(139,0,64,0.07)';
});

const observerOpts = { threshold: 0.15 };
const fadeEls = document.querySelectorAll(
  '.feature-card, .flip-card, .partner-card, .ods-badge, .video-wrapper'
);

fadeEls.forEach(el => {
  el.style.opacity    = '0';
  el.style.transform  = 'translateY(28px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
});

const observer = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.style.opacity   = '1';
        entry.target.style.transform = 'translateY(0)';
      }, i * 80);
      observer.unobserve(entry.target);
    }
  });
}, observerOpts);
let currentSlideIndex = 0;
const track = document.getElementById('carouselTrack');
const slides = document.querySelectorAll('.carousel-slide');
const indicators = document.querySelectorAll('.indicator');
const totalSlides = slides.length;

function updateCarousel() {
  if (!track) return;
  track.style.transform = `translateX(-${currentSlideIndex * 100}%)`;
  
  indicators.forEach((ind, i) => {
    ind.classList.toggle('active', i === currentSlideIndex);
  });
}

function moveSlide(direction) {
  currentSlideIndex = (currentSlideIndex + direction + totalSlides) % totalSlides;
  updateCarousel();
}

function goToSlide(index) {
  currentSlideIndex = index;
  updateCarousel();
}

const container = document.getElementById('carouselContainer');
let startX = 0;
let endX = 0;

if (container) {
  container.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
  }, { passive: true });

  container.addEventListener('touchend', (e) => {
    endX = e.changedTouches[0].clientX;
    handleSwipe();
  }, { passive: true });

  container.addEventListener('mousedown', (e) => {
    startX = e.clientX;
  });

  container.addEventListener('mouseup', (e) => {
    endX = e.clientX;
    handleSwipe();
  });
}

function handleSwipe() {
  const threshold = 50; 
  if (startX - endX > threshold) {
    moveSlide(1);
  } else if (endX - startX > threshold) {
    moveSlide(-1); 
  }
}
fadeEls.forEach(el => observer.observe(el));