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
  const missingAppStoreUrl = !hasValue(marketingConfig.appStoreUrl);
  const missingPricing =
    !hasValue(getConfiguredValue("monthlyPrice")) ||
    !hasValue(getConfiguredValue("yearlyPrice"));

  document.querySelectorAll("[data-setup-note]").forEach((node) => {
    node.hidden = !(missingAppStoreUrl || missingPricing);
  });

  document.querySelectorAll("[data-config-warning]").forEach((node) => {
    node.hidden = !missingPricing;
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
setupDemoMedia();
setupStoreLinks();
toggleSetupNotes();
setupClarity();
revealOnScroll();
