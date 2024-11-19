"""The garo_schedueler component."""
import logging

_LOGGER = logging.getLogger("custom_components.garo_schedueler.init")

DOMAIN = "garo_schedueler"


def setup(hass, config):
    hass.states.set("garo_schedueler.world", "Paulus")

    # Return boolean to indicate that initialization was successful.
    return True