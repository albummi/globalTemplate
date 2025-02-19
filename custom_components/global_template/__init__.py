import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Global Template integration."""
    _LOGGER.info("Global Template integration setup.")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up a specific entry for Global Template."""
    _LOGGER.info("Setting up Global Template entry: %s", entry.title)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a specific entry for Global Template."""
    _LOGGER.info("Unloading Global Template entry: %s", entry.title)
    return True
