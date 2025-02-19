// global_template.js
(async () => {
  // Warte, bis der Home Assistant-Objekt verfügbar ist.
  while (!window.hass) {
    await new Promise(resolve => setTimeout(resolve, 500));
  }
  try {
    // Rufe den Service auf, der (wenn implementiert) die Templates lädt.
    // Falls du den Service nicht implementierst, kannst du direkt auf die in hass.data gespeicherten Daten zugreifen.
    // Wir nehmen hier an, dass die Integration die Templates in window.hass.data["global_template"] speichert.
    if (window.hass.data && window.hass.data.global_template) {
      window.buttonCardTemplates = window.hass.data.global_template;
      console.info("Global Template loaded:", window.buttonCardTemplates);
    } else {
      console.error("Global Template data not found in hass.data");
    }
  } catch (e) {
    console.error("Error loading global templates", e);
  }
})();
