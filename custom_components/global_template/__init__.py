import logging
import yaml
import os

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "global_template"

def load_templates(hass: HomeAssistant, config: ConfigType):
    """Lade Templates aus der YAML-Datei."""
    templates_file = hass.config.path(config[DOMAIN].get("templates_file", "templates.yaml"))

    if os.path.exists(templates_file):
        try:
            with open(templates_file, "r") as f:
                templates = yaml.safe_load(f)
            hass.data[DOMAIN] = templates
            _LOGGER.info("Templates erfolgreich geladen: %s", templates)
        except Exception as e:
            _LOGGER.error("Fehler beim Laden der Templates: %s", e)
    else:
        _LOGGER.error("Die Datei %s wurde nicht gefunden.", templates_file)

async def async_setup(hass: HomeAssistant, config: ConfigType):
    """Setup der Integration über configuration.yaml"""
    load_templates(hass, config)
    return True
