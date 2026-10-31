/**
 * Muscle Fitness Gym 2 — Interactive Controller
 * Dynamic Typewriter, Counter Animation, Mobile Drawer & Training Goal Estimator
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Drawer Navigation
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');

  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      drawer.classList.toggle('open');
    });

    document.addEventListener('click', (e) => {
      if (!drawer.contains(e.target) && !toggleBtn.contains(e.target)) {
        drawer.classList.remove('open');
      }
    });

    drawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        drawer.classList.remove('open');
      });
    });
  }

  // 2. Dynamic Typewriter Animation
  const typewriterEl = document.querySelector('.typewriter-text');
  if (typewriterEl) {
    const phrases = [
      "Elite Strength & Hypertrophy Training",
      "Powerlifting & Heavy Barbells in Tollygunge",
      "One-on-One Transformation Mentorship",
      "Science-Backed Conditioning in Mahabirtala"
    ];
    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let speed = 90;

    function typeLoop() {
      const currentPhrase = phrases[phraseIdx];

      if (isDeleting) {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx - 1);
        charIdx--;
        speed = 45;
      } else {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx + 1);
        charIdx++;
        speed = 90;
      }

      if (!isDeleting && charIdx === currentPhrase.length) {
        isDeleting = true;
        speed = 2200;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
        speed = 400;
      }

      setTimeout(typeLoop, speed);
    }

    typeLoop();
  }

  // 3. Counter Animation
  const counters = document.querySelectorAll('.telemetry-val');
  if (counters.length > 0) {
    let animated = false;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !animated) {
          animated = true;
          counters.forEach(counter => {
            const rawTarget = counter.getAttribute('data-target');
            if (!rawTarget) return;
            const target = parseFloat(rawTarget);
            const isDecimal = rawTarget.includes('.');
            let count = 0;
            const step = target / 40;

            const timer = setInterval(() => {
              count += step;
              if (count >= target) {
                counter.textContent = isDecimal ? target.toFixed(1) : Math.floor(target) + (rawTarget.includes('+') ? '+' : '');
                clearInterval(timer);
              } else {
                counter.textContent = isDecimal ? count.toFixed(1) : Math.floor(count);
              }
            }, 35);
          });
        }
      });
    }, { threshold: 0.3 });

    const heroTelemetry = document.querySelector('.hero-telemetry');
    if (heroTelemetry) observer.observe(heroTelemetry);
  }

  // 4. Interactive Goal & Training Intake Widget
  const goalSelect = document.getElementById('fitnessGoal');
  const trainingModeSelect = document.getElementById('trainingMode');
  const slotSelect = document.getElementById('workoutSlot');

  const estTitle = document.getElementById('estTitle');
  const estTimeline = document.getElementById('estTimeline');
  const estWaBtn = document.getElementById('estWaBtn');

  function updateEstimator() {
    if (!goalSelect || !trainingModeSelect || !estTitle || !estWaBtn) return;

    const goalVal = goalSelect.value;
    const modeVal = trainingModeSelect.value;
    const slotVal = slotSelect ? slotSelect.value : 'Flexible Daily Hours';

    estTitle.textContent = `${goalVal} — ${modeVal}`;
    estTimeline.textContent = `Includes: Full Gym Arena Access, Bio-mechanical Machine Circuit, Body Composition Analysis (${slotVal})`;

    const phone = '917003433661';
    const message = `Hello Muscle Fitness Gym 2! 🏋️‍♂️💪 I would like to consult on joining:\n- Fitness Goal: ${goalVal}\n- Training Mode: ${modeVal}\n- Preferred Slot: ${slotVal}\n\nPlease share details and trial workout availability at Mahabirtala studio!`;
    estWaBtn.href = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
  }

  if (goalSelect && trainingModeSelect) {
    goalSelect.addEventListener('change', updateEstimator);
    trainingModeSelect.addEventListener('change', updateEstimator);
    if (slotSelect) slotSelect.addEventListener('change', updateEstimator);
    updateEstimator();
  }
});
