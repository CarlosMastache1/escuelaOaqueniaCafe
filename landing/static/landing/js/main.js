/* Escuela Oaxaqueña del Café — Animaciones e Interactividad */

(function() {
  'use strict';

  /* ==================================================
     Preloader
  ================================================== */
  const preloader = document.getElementById('preloader');

  function hidePreloader() {
    if (!preloader) return;
    preloader.classList.add('fade-out');
    setTimeout(() => {
      preloader.style.display = 'none';
      document.body.style.overflow = 'auto';
    }, 800);
  }

  function initPreloader() {
    if (!preloader) return;
    document.body.style.overflow = 'hidden';
    window.addEventListener('load', () => {
      setTimeout(hidePreloader, 1200);
    });
  }

  /* ==================================================
     Animaciones de scroll (Intersection Observer)
  ================================================== */
  const animateOnScroll = (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const delay = parseFloat(el.dataset.delay) || 0;
        const direction = el.dataset.animate;

        setTimeout(() => {
          el.classList.add('animated');
          if (direction) {
            el.classList.add(direction);
          }
        }, delay * 600);

        observer.unobserve(el);
      }
    });
  };

  const scrollObserver = new IntersectionObserver(animateOnScroll, {
    threshold: 0.12,
    rootMargin: '0px 0px -50px 0px'
  });

  function initScrollAnimations() {
    document.querySelectorAll('[data-animate]').forEach(el => {
      scrollObserver.observe(el);
    });
  }

  /* ==================================================
     Parallax suave del hero
  ================================================== */
  function initParallax() {
    const heroBg = document.querySelector('.hero-bg');
    if (!heroBg) return;

    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      const rate = scrolled * 0.5;
      heroBg.style.transform = `translateY(${rate}px)`;
    });
  }

  /* ==================================================
     Header scroll estado
  ================================================== */
  function initHeaderScroll() {
    const header = document.getElementById('header');
    if (!header) return;
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
      const currentScroll = window.pageYOffset;

      if (currentScroll > 80) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }

      lastScroll = currentScroll;
    });
  }

  /* ==================================================
     Navegación móvil
  ================================================== */
  function initMobileNav() {
    const toggle = document.getElementById('navToggle');
    const nav = document.getElementById('mainNav');
    const body = document.body;

    if (!toggle || !nav) return;

    toggle.addEventListener('click', () => {
      const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', !isExpanded);
      body.classList.toggle('nav-open');
    });

    // Cerrar menú al hacer clic en un enlace
    nav.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ==================================================
     Testimonial slider
  ================================================== */
  function initTestimonialSlider() {
    const track = document.getElementById('testimonialTrack');
    const dots = document.querySelectorAll('.nav-dot');
    const slides = document.querySelectorAll('.testimonial-slide');

    if (!track || slides.length === 0) return;

    let currentSlide = 0;
    let autoplayInterval;

    function showSlide(index) {
      slides.forEach((slide, i) => {
        slide.classList.toggle('active', i === index);
      });
      dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
      });
      currentSlide = index;
    }

    function nextSlide() {
      currentSlide = (currentSlide + 1) % slides.length;
      showSlide(currentSlide);
    }

    function startAutoplay() {
      autoplayInterval = setInterval(nextSlide, 6000);
    }

    function stopAutoplay() {
      clearInterval(autoplayInterval);
    }

    // Dot navigation
    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const slideIndex = parseInt(dot.dataset.slide);
        showSlide(slideIndex);
        stopAutoplay();
        startAutoplay();
      });
    });

    // Touch swipe support
    let touchStartX = 0;
    let touchEndX = 0;

    track.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    track.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, { passive: true });

    function handleSwipe() {
      const diff = touchStartX - touchEndX;
      const threshold = 50;

      if (Math.abs(diff) > threshold) {
        if (diff > 0) {
          currentSlide = (currentSlide + 1) % slides.length;
        } else {
          currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        }
        showSlide(currentSlide);
        stopAutoplay();
        startAutoplay();
      }
    }

    startAutoplay();
  }

  /* ==================================================
     Formulario de contacto
  ================================================== */
  function initContactForm() {
    const form = document.getElementById('contactForm');
    if (!form) return;

    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const formData = new FormData(form);
      const name = formData.get('nombre');
      const email = formData.get('email');
      const subject = formData.get('asunto');
      const message = formData.get('mensaje');

      // Validación básica
      if (!name || !email || !subject || !message) {
        showFormError('Por favor, completa todos los campos.');
        return;
      }

      if (!isValidEmail(email)) {
        showFormError('Por favor, ingresa un email válido.');
        return;
      }

      // Simular envío
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;

      submitBtn.innerHTML = '<span>Enviando...</span>';
      submitBtn.disabled = true;

      setTimeout(() => {
        form.reset();
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
        showFormSuccess('¡Gracias! Tu mensaje ha sido enviado. Nos pondremos en contacto pronto.');
      }, 1200);
    });

    function isValidEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(String(email).toLowerCase());
    }

    function showFormError(message) {
      showFormMessage(message, 'error');
    }

    function showFormSuccess(message) {
      showFormMessage(message, 'success');
    }

    function showFormMessage(message, type) {
      // Remove existing message
      const existing = form.querySelector('.form-message');
      if (existing) existing.remove();

      const msgDiv = document.createElement('div');
      msgDiv.className = `form-message form-message--${type}`;
      msgDiv.textContent = message;
      form.appendChild(msgDiv);

      // Auto-remove after 5 seconds
      setTimeout(() => {
        msgDiv.style.opacity = '0';
        setTimeout(() => msgDiv.remove(), 400);
      }, 5000);
    }
  }

  /* ==================================================
     Navegación suave con resaltado de sección activa
  ================================================== */
  function initSmoothNav() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');

    if (sections.length === 0) return;

    const navIntersectionObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const id = entry.target.id;
        const navLink = document.querySelector(`.nav-link[href="#${id}"]`);

        if (entry.isIntersecting && navLink) {
          navLinks.forEach(link => link.classList.remove('active'));
          navLink.classList.add('active');
        }
      });
    }, { threshold: 0.4 });

    sections.forEach(section => navIntersectionObserver.observe(section));
  }

  /* ==================================================
     Animación de café flotante en fondos
  ================================================== */
  function initCoffeeParticles() {
    const particles = document.querySelectorAll('.particle');

    if (particles.length === 0) return;

    particles.forEach(particle => {
      let pos = {
        x: parseFloat(particle.style.left) || Math.random() * 100,
        y: parseFloat(particle.style.top) || Math.random() * 100
      };

      // Add subtle mouse-follow effect
      document.addEventListener('mousemove', (e) => {
        const rect = particle.parentElement.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        if (mouseX > 0 && mouseX < rect.width && mouseY > 0 && mouseY < rect.height) {
          const dx = (mouseX / rect.width - 0.5) * 10;
          const dy = (mouseY / rect.height - 0.5) * 10;
          particle.style.transform = `translate(${dx}px, ${dy}px)`;
        }
      });
    });
  }

  /* ==================================================
     Inicialización
  ================================================== */
  document.addEventListener('DOMContentLoaded', () => {
    initPreloader();
    initScrollAnimations();
    initParallax();
    initHeaderScroll();
    initMobileNav();
    initTestimonialSlider();
    initContactForm();
    initSmoothNav();
    initCoffeeParticles();
  });

  /* ==================================================
     Performance: Reducir motion para usuarios que prefieren
  ================================================== */
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const style = document.createElement('style');
    style.textContent = `
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
      [data-animate] {
        opacity: 1 !important;
        transform: none !important;
      }
    `;
    document.head.appendChild(style);
  }
})();
