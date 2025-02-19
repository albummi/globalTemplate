import logging
import os
import yaml
from homeassistant import config_entries
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)
DOMAIN = "global_template"

class GlobalTemplateConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Global Template."""
    
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            try:
                templates_file = f"/config/custom_components/{DOMAIN}/templates.yaml"
                if os.path.exists(templates_file):
                    with open(templates_file, "r") as f:
                        templates = yaml.safe_load(f)
                    self.hass.data[DOMAIN] = templates.get("button_card_templates", {})
                    _LOGGER.info("Templates loaded from config_flow.")
                else:
                    _LOGGER.error("templates.yaml not found in config_flow.")
                    return self.async_abort(reason="file_not_found")
                return self.async_create_entry(title="Global Template", data=user_input)
            except Exception as e:
                _LOGGER.error("Error loading templates in config_flow: %s", e)
                return self.async_abort(reason="loading_failed")
        return self.async_show_form(step_id="user", data_schema={})
