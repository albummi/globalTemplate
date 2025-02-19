import logging
import yaml
import os
from homeassistant.core import HomeAssistant
from homeassistant.components.button_card import ButtonCard

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the global template integration."""
    
    templates_file = "/config/custom_components/global_template/templates.yaml"
    
    if os.path.exists(templates_file):
        try:
            with open(templates_file, "r") as f:
                templates = yaml.safe_load(f)
            
            # Prüfe, ob "button_card_templates" vorhanden sind
            if "button_card_templates" in templates:
                _LOGGER.info("Templates erfolgreich geladen und registriert.")
                hass.data["global_template"] = templates["button_card_templates"]
                
                # Registriere die Templates
                # Hier verwenden wir die `hass.data`-Daten, die die Templates global verfügbar machen
                ButtonCard.register_templates(hass, templates["button_card_templates"])
            else:
                _LOGGER.error("Keine Button Card Templates gefunden!")
        except Exception as e:
            _LOGGER.error("Fehler beim Laden der Templates: %s", e)
    else:
        _LOGGER.error("Die Datei templates.yaml wurde nicht gefunden.")
