import yaml
import logging
import os
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import discovery

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the global template integration and load templates."""
    # Überprüfe, ob Templates bereits geladen wurden
    templates = hass.data.get("global_template", {})

    # Service für das Abrufen der Templates
    async def get_templates_service(call):
        """Gibt die geladenen Templates zurück."""
        return templates

    # Registriere den Service
    hass.services.async_register("global_template", "get_templates", get_templates_service)

    # Wenn Templates erfolgreich geladen wurden, loggen wir eine Nachricht
    if templates:
        _LOGGER.info("Global Templates erfolgreich geladen.")
    else:
        _LOGGER.error("Keine Templates gefunden oder geladen.")
    
    return True
