import logging
import yaml
import os
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant

DOMAIN = "global_template"  # Hier direkt definieren

_LOGGER = logging.getLogger(__name__)

@config_entries.HANDLERS.register(DOMAIN)
class GlobalTemplateConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Global Template."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step of the flow."""
        errors = {}

        if user_input is not None:
            try:
                templates_file = f"/config/custom_components/{DOMAIN}/templates.yaml"
                if os.path.exists(templates_file):
                    with open(templates_file, "r") as f:
                        templates = yaml.safe_load(f)

                    # Templates in Home Assistant speichern
                    self.hass.data[DOMAIN] = templates
                    _LOGGER.info("Templates erfolgreich geladen!")

                    return self.async_create_entry(title="Global Template", data=user_input)
                else:
                    _LOGGER.error("Die Datei templates.yaml wurde nicht gefunden.")
                    errors["base"] = "file_not_found"
            except Exception as e:
                _LOGGER.error("Fehler beim Laden der Templates: %s", e)
                errors["base"] = "loading_failed"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            errors=errors
        )
