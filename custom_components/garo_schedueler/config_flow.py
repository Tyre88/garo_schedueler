from homeassistant import config_entries
from .const import SENSOR

class GaroScheduelerFlowHandler(config_entries.ConfigFlow, domain=SENSOR):
    async def async_step_user(self, user_input=None):
        VERSION = 0
        MINOR_VERSION = 1
        if user_input is not None:
            return self.async_create_entry(title="Garo Schedueler", data={})
        return self.async_show_form(step_id="user")