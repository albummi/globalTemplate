# Global Template

## Overview
The "Global Template" integration allows you to define reusable templates for `custom:button-card` across multiple dashboards in Home Assistant.

## Installation
1. Install this integration via HACS.
2. Define your templates in `templates.yaml`.
3. Use the templates in your `custom:button-card` configuration.

## Example Usage

```yaml
type: custom:button-card
template: custom_button_template
entity: light.kitchen
