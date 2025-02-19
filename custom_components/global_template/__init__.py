import logging
import os
import yaml
from homeassistant.core import HomeAssistant
from homeassistant.components.http import HomeAssistantView

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

class GlobalTemplateView(HomeAssistantView):
    """HTTP view to return global templates."""
    url = "/api/global_template"
    name = "api:global_template"
    requires_auth = True

    async def get(self, request):
        hass = request.app["hass"]
        templates = hass.data.get(DOMAIN, DEFAULT_TEMPLATES["button_card_templates"])
        return self.json(templates)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Global Template integration."""
    templates_file = hass.config.path("custom_components", DOMAIN, "templates.yaml")
    
    if os.path.exists(templates_file):
        try:
            with open(templates_file, "r") as f:
                templates = yaml.safe_load(f)
            if not templates or "button_card_templates" not in templates:
                _LOGGER.warning("templates.yaml is empty or missing 'button_card_templates'. Using default templates.")
                templates = DEFAULT_TEMPLATES
        except Exception as e:
            _LOGGER.error("Error loading templates.yaml: %s. Using default templates.", e)
            templates = DEFAULT_TEMPLATES
    else:
        _LOGGER.error("templates.yaml not found. Using default templates.")
        templates = DEFAULT_TEMPLATES

    hass.data[DOMAIN] = templates["button_card_templates"]
    _LOGGER.info("Global Template Integration: Templates registered: %s", hass.data[DOMAIN])
    
    # Registriere den HTTP-Endpoint, damit das Frontend die Templates abrufen kann.
    hass.http.register_view(GlobalTemplateView)
    
    return True
