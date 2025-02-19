"""Global Template integration for Home Assistant."""

import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import discovery

DOMAIN = "global_template"

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the global_template component."""
    _LOGGER.info("Setting up Global Template integration")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up global_template from a config entry."""
    _LOGGER.info("Setting up global_template from entry: %s", entry.entry_id)
    return True
