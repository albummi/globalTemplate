import logging
import os
import yaml
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)
DOMAIN = "global_template"

DEFAULT_TEMPLATES = {
    "button_card_templates": {
        "custom_button_template": {
            "name": "My Custom Button",
            "icon": "mdi:lightbulb",
            "show_state": True,
            "show_name": True,
            "size": 30,
            "tap_action": {"action": "toggle"},
            "hold_action": {"action": "more-info"},
            "styles": {
                "card": [
                    "height: 100px",
                    "width: 100px",
                    "font-size: 20px"
                ]
            }
        }
    }
}

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Global Template integration."""
    templates_file = hass.config.path("custom_components", DOMAIN, "templates.yaml")
    
    if os.path.exists(templates_file):
        try:
            with open(templates_file, "r") as f:
                templates = yaml.safe_load(f)
            if not templates or "button_card_templates" not in templates:
                _LOGGER.warning("templates.yaml ist leer oder enthält keine 'button_card_templates'. Standardvorlage wird verwendet.")
                templates = DEFAULT_TEMPLATES
        except Exception as e:
            _LOGGER.error("Fehler beim Laden von templates.yaml: %s. Standardvorlage wird verwendet.", e)
            templates = DEFAULT_TEMPLATES
    else:
        _LOGGER.error("Die Datei %s wurde nicht gefunden. Standardvorlage wird verwendet.", templates_file)
        templates = DEFAULT_TEMPLATES

    hass.data[DOMAIN] = templates["button_card_templates"]
    _LOGGER.info("Global Template Integration: Templates registriert: %s", hass.data[DOMAIN])
    return True
