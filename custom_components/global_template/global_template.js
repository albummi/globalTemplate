// global_template.js
(async () => {
  // Warte, bis Home Assistant (window.hass) verfügbar ist.
  while (!window.hass) {
    await new Promise(resolve => setTimeout(resolve, 500));
  }
  
  try {
    // Abruf der globalen Templates über den HTTP-Endpunkt
    const response = await fetch('/api/global_template', { credentials: 'same-origin' });
    const templates = await response.json();
    window.buttonCardTemplates = templates;
    console.info("Global templates loaded:", templates);
  } catch (err) {
    console.error("Error loading global templates:", err);
  }
})();
