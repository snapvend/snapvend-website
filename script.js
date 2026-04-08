const defaultMarketingConfig = {
  googlePlayUrl: "https://play.google.com/store/apps/details?id=com.snapvend.gallery",
  appStoreUrl: "",
  monthlyPrice: "",
  yearlyPrice: "",
  demoVideoUrl: "",
  clarityProjectId: "",
  pricesByLocale: {},
};

const marketingConfig = {
  ...defaultMarketingConfig,
  ...(window.snapVendMarketingConfig || {}),
};

const hasValue = (value) => String(value || "").trim().length > 0;
const currentLocale = (document.documentElement.lang || "tr").toLowerCase();
const localePreferenceKey = "snapvendPreferredLocale";
const supportedLocalePaths = {
  tr: "./index.html",
  en: "./en/index.html",
  es: "./es/index.html",
  fr: "./fr/index.html",
  de: "./de/index.html",
  it: "./it/index.html",
  pt: "./pt/index.html",
  ru: "./ru/index.html",
  ar: "./ar/index.html",
  hi: "./hi/index.html",
  ja: "./ja/index.html",
  zh: "./zh/index.html",
};

const localeAliases = {
  tr: "tr",
  "tr-tr": "tr",
  en: "en",
  "en-us": "en",
  "en-gb": "en",
  "en-ca": "en",
  "en-au": "en",
  es: "es",
  "es-es": "es",
  "es-mx": "es",
  "es-ar": "es",
  "es-co": "es",
  fr: "fr",
  "fr-fr": "fr",
  "fr-ca": "fr",
  "fr-be": "fr",
  "fr-ch": "fr",
  de: "de",
  "de-de": "de",
  "de-at": "de",
  "de-ch": "de",
  it: "it",
  "it-it": "it",
  "it-ch": "it",
  "it-sm": "it",
  pt: "pt",
  "pt-br": "pt",
  "pt-pt": "pt",
  ru: "ru",
  "ru-ru": "ru",
  "ru-kz": "ru",
  ar: "ar",
  "ar-sa": "ar",
  "ar-ae": "ar",
  "ar-eg": "ar",
  hi: "hi",
  "hi-in": "hi",
  ja: "ja",
  "ja-jp": "ja",
  zh: "zh",
  "zh-cn": "zh",
  "zh-sg": "zh",
  "zh-hans": "zh",
};

const normalizeLocaleTag = (value) => String(value || "").trim().toLowerCase().replace(/_/g, "-");

const resolveSupportedLocale = (value) => {
  const normalized = normalizeLocaleTag(value);

  if (!hasValue(normalized)) {
    return "";
  }

  if (localeAliases[normalized]) {
    return localeAliases[normalized];
  }

  const baseLocale = normalized.split("-")[0];
  return supportedLocalePaths[baseLocale] ? baseLocale : "";
};

const isRootPage = () => {
  const path = window.location.pathname || "/";
  return path === "/" || path.endsWith("/index.html");
};

const setupLocalePreference = () => {
  document.querySelectorAll(".language-option[lang]").forEach((link) => {
    link.addEventListener("click", () => {
      const selectedLocale = resolveSupportedLocale(link.getAttribute("lang"));
      if (hasValue(selectedLocale)) {
        window.localStorage.setItem(localePreferenceKey, selectedLocale);
      }
    });
  });
};

const setupLocaleRedirect = () => {
  if (!isRootPage() || currentLocale !== "tr") {
    return;
  }

  const savedLocale = resolveSupportedLocale(window.localStorage.getItem(localePreferenceKey));
  const browserLocale = [navigator.language, ...(navigator.languages || [])]
    .map(resolveSupportedLocale)
    .find(Boolean);
  const preferredLocale = savedLocale || browserLocale;

  if (!hasValue(preferredLocale) || preferredLocale === "tr") {
    return;
  }

  const targetPath = supportedLocalePaths[preferredLocale];
  if (!hasValue(targetPath)) {
    return;
  }

  window.location.replace(targetPath);
};

const getConfiguredValue = (key) => {
  const localizedPrices = marketingConfig.pricesByLocale || {};
  const exactLocalePricing = localizedPrices[currentLocale] || {};
  const baseLocalePricing = localizedPrices[currentLocale.split("-")[0]] || {};
  const localizedValue = exactLocalePricing[key] || baseLocalePricing[key];

  if (hasValue(localizedValue)) {
    return localizedValue;
  }

  return marketingConfig[key];
};

const applyPricing = () => {
  document.querySelectorAll("[data-config-text]").forEach((node) => {
    const key = node.dataset.configText;
    const configuredValue = getConfiguredValue(key);
    if (hasValue(configuredValue)) {
      node.textContent = configuredValue;
    }
  });
};

const setupDemoMedia = () => {
  const demoVideoUrl = String(marketingConfig.demoVideoUrl || "").trim();

  document.querySelectorAll("[data-demo-video]").forEach((video) => {
    const fallback = video.parentElement?.querySelector("[data-demo-fallback]");

    if (!hasValue(demoVideoUrl)) {
      video.hidden = true;
      return;
    }

    video.src = demoVideoUrl;
    video.hidden = false;
    video.load();

    if (fallback) {
      fallback.hidden = true;
      video.poster = fallback.currentSrc || fallback.src || "";
    }
  });
};

const setupClarity = () => {
  const projectId = String(marketingConfig.clarityProjectId || "").trim();

  if (!hasValue(projectId) || document.querySelector("script[data-clarity-tag]")) {
    return;
  }

  window.clarity =
    window.clarity ||
    function (...args) {
      (window.clarity.q = window.clarity.q || []).push(args);
    };

  const script = document.createElement("script");
  script.async = true;
  script.src = `https://www.clarity.ms/tag/${encodeURIComponent(projectId)}`;
  script.dataset.clarityTag = "true";
  document.head.appendChild(script);
};

const setupStoreLinks = () => {
  document.querySelectorAll("[data-store-link]").forEach((link) => {
    const kind = link.dataset.storeLink;

    if (kind === "googlePlay") {
      link.href = marketingConfig.googlePlayUrl;
      link.target = "_blank";
      link.rel = "noreferrer";
      return;
    }

    if (kind === "appStore") {
      const fallbackSearch = link.dataset.appStoreSearch || "#";
      link.href = hasValue(marketingConfig.appStoreUrl)
        ? marketingConfig.appStoreUrl
        : fallbackSearch;
      link.target = "_blank";
      link.rel = "noreferrer";
      if (!hasValue(marketingConfig.appStoreUrl)) {
        link.classList.add("is-search-fallback");
      }
    }
  });
};

const toggleSetupNotes = () => {
  const missingPricing =
    !hasValue(getConfiguredValue("monthlyPrice")) ||
    !hasValue(getConfiguredValue("yearlyPrice"));

  document.querySelectorAll("[data-setup-note]").forEach((node) => {
    node.hidden = true;
  });

  document.querySelectorAll("[data-config-warning]").forEach((node) => {
    node.hidden = !missingPricing;
  });
};

const setupContactForms = () => {
  document.querySelectorAll("[data-contact-form]").forEach((form) => {
    const emailAddress = String(form.dataset.contactEmail || "").trim();
    if (!hasValue(emailAddress)) {
      return;
    }

    const directLink = form.querySelector(".contact-direct-link");
    if (directLink) {
      directLink.href = `mailto:${emailAddress}`;
    }

    form.addEventListener("submit", (event) => {
      event.preventDefault();

      const data = new FormData(form);
      const topic = String(data.get("topic") || "").trim();
      const fullName = String(data.get("fullName") || "").trim();
      const company = String(data.get("company") || "").trim();
      const email = String(data.get("email") || "").trim();
      const message = String(data.get("message") || "").trim();
      const subjectPrefix = String(form.dataset.contactSubjectPrefix || "SnapVend").trim();

      const labels = {
        topic: String(form.dataset.contactLabelType || "Topic").trim(),
        fullName: String(form.dataset.contactLabelName || "Name").trim(),
        company: String(form.dataset.contactLabelCompany || "Company").trim(),
        email: String(form.dataset.contactLabelEmail || "Email").trim(),
        message: String(form.dataset.contactLabelMessage || "Message").trim(),
      };

      const body = [
        `${labels.topic}: ${topic}`,
        `${labels.fullName}: ${fullName}`,
        `${labels.company}: ${hasValue(company) ? company : "-"}`,
        `${labels.email}: ${email}`,
        "",
        `${labels.message}:`,
        message,
      ].join("\n");

      const subject = hasValue(topic) ? `${subjectPrefix}: ${topic}` : subjectPrefix;
      const mailtoUrl = `mailto:${emailAddress}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      window.location.href = mailtoUrl;
    });
  });
};

const setupMobileMenu = () => {
  const menuToggles = document.querySelectorAll("[data-menu-toggle]");

  const closeMenu = (container, toggle) => {
    container.classList.remove("is-menu-open");
    toggle.setAttribute("aria-expanded", "false");
  };

  const openMenu = (container, toggle) => {
    container.classList.add("is-menu-open");
    toggle.setAttribute("aria-expanded", "true");
  };

  menuToggles.forEach((toggle) => {
    const container = toggle.closest(".topbar-inner");
    const panel = container?.querySelector("[data-menu-panel]");

    if (!container || !panel) {
      return;
    }

    toggle.addEventListener("click", () => {
      const isOpen = container.classList.contains("is-menu-open");
      if (isOpen) {
        closeMenu(container, toggle);
      } else {
        openMenu(container, toggle);
      }
    });

    panel.querySelectorAll("a[href^='#']").forEach((link) => {
      link.addEventListener("click", () => {
        if (window.innerWidth <= 820) {
          closeMenu(container, toggle);
        }
      });
    });

    document.addEventListener("click", (event) => {
      if (window.innerWidth > 820) {
        return;
      }

      if (!container.contains(event.target)) {
        closeMenu(container, toggle);
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeMenu(container, toggle);
      }
    });
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 820) {
      menuToggles.forEach((toggle) => {
        const container = toggle.closest(".topbar-inner");
        if (!container) return;
        container.classList.remove("is-menu-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    }
  });
};

const revealOnScroll = () => {
  const items = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    items.forEach((item) => item.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    {
      threshold: 0.16,
      rootMargin: "0px 0px -50px 0px",
    },
  );

  items.forEach((item) => observer.observe(item));
};

applyPricing();
setupLocalePreference();
setupLocaleRedirect();
setupDemoMedia();
setupStoreLinks();
toggleSetupNotes();
setupContactForms();
setupMobileMenu();
setupClarity();
revealOnScroll();
