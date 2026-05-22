function initNavbar() {
  const navbar = document.getElementById("navbar");
  if (!navbar) return;

  window.addEventListener("scroll", function () {
    if (window.scrollY > 20) {
      navbar.classList.add("solid");
    } else {
      navbar.classList.remove("solid");
    }
  });
}

function initMenu() {
  const btn = document.getElementById("menu-btn");
  const links = document.getElementById("nav-links");

  if (!btn || !links) return;

  btn.addEventListener("click", function () {
    links.classList.toggle("open");
  });
}

function initLangDropdown() {
  const btn = document.getElementById("langBtn");
  const menu = document.getElementById("langMenu");

  if (!btn || !menu) return;

  btn.addEventListener("click", function (e) {
    e.stopPropagation();
    menu.classList.toggle("open");
  });

  document.addEventListener("click", function () {
    menu.classList.remove("open");
  });

  menu.addEventListener("click", function (e) {
    e.stopPropagation();
  });
}

function initOldSvgMapTooltip() {
  const tooltip = document.getElementById("map-tooltip");
  if (!tooltip) return;

  document.querySelectorAll(".route-dot").forEach(function (dot) {
    dot.addEventListener("mousemove", function (e) {
      const lang = document.documentElement.lang;

      tooltip.style.display = "block";
      tooltip.style.left = e.offsetX + 20 + "px";
      tooltip.style.top = e.offsetY + 20 + "px";

      tooltip.textContent =
        lang === "hy"
          ? dot.dataset.nameHy
          : lang === "en"
          ? dot.dataset.nameEn
          : dot.dataset.name;
    });

    dot.addEventListener("mouseleave", function () {
      tooltip.style.display = "none";
    });

    dot.addEventListener("click", function () {
      dot.classList.add("active");
      setTimeout(function () {
        dot.classList.remove("active");
      }, 1500);
    });
  });
}

function initLeafletRouteMap() {
  const el = document.getElementById("leaflet-route-map");
  if (!el || typeof L === "undefined") return;

  const map = L.map(el, {
    scrollWheelZoom: false,
    attributionControl: false,
    zoomControl: true
  }).setView([40.1772, 44.5035], 4);

  L.tileLayer("https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png", {
    maxZoom: 19,
    attribution: ""
  }).addTo(map);

  const lang = document.documentElement.lang || "hy";

  const points = (window.routePoints || [])
    .filter(p => p.lat && p.lng)
    .map(p => ({
      name: lang === "hy" ? p.name_hy : lang === "ru" ? p.name_ru : p.name_en,
      lat: Number(p.lat),
      lng: Number(p.lng),
      name_en: p.name_en
    }));

  if (!points.length) return;

  const center = points.find(p => p.name_en === "Armenia") || points[0];

  function curve(from, to) {
    const arr = [];
    const offset = Math.min(Math.abs(to.lng - from.lng) * 0.16 + 3, 10);

    for (let i = 0; i <= 70; i++) {
      const t = i / 70;

      const lat =
        (1 - t) * (1 - t) * from.lat +
        2 * (1 - t) * t * ((from.lat + to.lat) / 2 + offset) +
        t * t * to.lat;

      const lng =
        (1 - t) * (1 - t) * from.lng +
        2 * (1 - t) * t * ((from.lng + to.lng) / 2) +
        t * t * to.lng;

      arr.push([lat, lng]);
    }

    return arr;
  }

  points.forEach(p => {
    if (p === center) return;

    L.polyline(curve(center, p), {
      color: "#f59e0b",
      weight: 3,
      opacity: 0.95,
      dashArray: "10 10",
      lineCap: "round",
      lineJoin: "round"
    }).addTo(map);
  });

  points.forEach(p => {
    const isCenter = p === center;

    const marker = L.circleMarker([p.lat, p.lng], {
      radius: isCenter ? 11 : 9,
      color: "#ffffff",
      weight: 3,
      fillColor: isCenter ? "#2563eb" : "#f59e0b",
      fillOpacity: 1
    }).addTo(map);

    marker.bindTooltip(p.name, {
      permanent: true,
      direction: isCenter ? "bottom" : "top",
      offset: isCenter ? [0, 16] : [0, -14],
      className: isCenter ? "route-label route-label-main" : "route-label"
    });
  });

  map.fitBounds(L.latLngBounds(points.map(p => [p.lat, p.lng])), {
    padding: [70, 70],
    maxZoom: 4
  });

  setTimeout(() => map.invalidateSize(), 300);
}

document.addEventListener("DOMContentLoaded", function () {
  initNavbar();
  initMenu();
  initLangDropdown();
  initOldSvgMapTooltip();
  initLeafletRouteMap();
});