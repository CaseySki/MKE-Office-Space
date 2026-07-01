document.addEventListener('DOMContentLoaded', () => {

  // Footer year
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Mobile nav toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const mainNav = document.querySelector('.main-nav');
  if (menuToggle && mainNav) {
    menuToggle.addEventListener('click', () => {
      const open = mainNav.classList.toggle('is-open');
      menuToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mainNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mainNav.classList.remove('is-open');
        menuToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // "Click to hear the inscription" — reads the 1974 landmark marker text aloud
  const listenBtn = document.getElementById('listenBtn');
  const listenLabel = document.getElementById('listenBtnLabel');
  if (listenBtn && 'speechSynthesis' in window) {
    const inscription = "Designed by G. B. Ferry and A. C. Clas, erected in 1893 and later for the wholesale and retail grocery firm founded by William Steinmeyer, and designated as a Milwaukee Landmark in 1974 in recognition of its historical and architectural significance to the community.";

    listenBtn.addEventListener('click', () => {
      if (window.speechSynthesis.speaking) {
        window.speechSynthesis.cancel();
        listenBtn.setAttribute('aria-pressed', 'false');
        listenLabel.textContent = 'Click to hear the inscription';
        return;
      }
      const utterance = new SpeechSynthesisUtterance(inscription);
      utterance.rate = 0.95;
      utterance.onend = () => {
        listenBtn.setAttribute('aria-pressed', 'false');
        listenLabel.textContent = 'Click to hear the inscription';
      };
      window.speechSynthesis.speak(utterance);
      listenBtn.setAttribute('aria-pressed', 'true');
      listenLabel.textContent = 'Stop reading';
    });
  } else if (listenBtn) {
    listenBtn.hidden = true;
  }

  // District map — Steinmeyer Building location (43°2.651'N, 87°54.859'W)
  const mapEl = document.getElementById('districtMap');
  if (mapEl && window.L) {
    const lat = 43 + 2.651 / 60;
    const lng = -(87 + 54.859 / 60);
    const map = L.map(mapEl, { scrollWheelZoom: false }).setView([lat, lng], 16);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
      maxZoom: 19
    }).addTo(map);
    L.marker([lat, lng]).addTo(map)
      .bindPopup('<strong>The Steinmeyer Building</strong><br>205 W. Highland Ave, Milwaukee');
  }

  // Inquiry form — static demo submit (no backend wired up yet)
  const form = document.getElementById('inquiryForm');
  const formNote = document.getElementById('formNote');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      formNote.hidden = false;
      formNote.textContent = "Thanks — this demo form isn't wired to send email yet. Contact Luke or Richard directly for now.";
    });
  }

});
