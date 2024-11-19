"""The garo_schedueler component."""
import logging

_LOGGER = logging.getLogger("custom_components.garo_schedueler.init")

DOMAIN = "garo_schedueler"


async def async_setup(hass, config):
  _LOGGER.info("Setting up garo_schedueler component")
  hass.states.async_set("hello_state.world", "Paulus")

  # Return boolean to indicate that initialization was successful.
  return True