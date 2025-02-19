import logging
import os
import yaml
from homeassistant import config_entries
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

class GlobalTemplateConfigFlow(config_entries.ConfigFlow, domain="global_template"):
    """Handle a config flow for Global Template."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step of the flow."""
        if user_input is not None:
            # Wenn Benutzer auf "OK" klickt, laden wir die Templates aus der YAML-Datei
            try:
                templates_file = "/config/custom_components/global_template/templates.yaml"
                if os.path.exists(templates_file):
                    with open(templates_file, "r") as f:
                        templates = yaml.safe_load(f)

                    # Hier speichern wir die Templates in Home Assistant
                    self.hass.data["global_template"] = templates
                    _LOGGER.info("Templates erfolgreich geladen!")
                else:
                    _LOGGER.error("Die Datei templates.yaml wurde nicht gefunden.")
                    return self.async_abort(reason="file_not_found")

                # Rückgabe der Konfiguration
                return self.async_create_entry(
                    title="Global Template Integration", data=user_input
                )
            except Exception as e:
                _LOGGER.error("Fehler beim Laden der Templates: %s", e)
                return self.async_abort(reason="loading_failed")

        return self.async_show_form(
            step_id="user", data_schema=None, description_placeholders={}
        )
