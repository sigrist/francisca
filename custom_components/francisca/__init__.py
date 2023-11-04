from homeassistant.helpers.typing import HomeAssistantType

DOMAIN = "francisca"


async def setup(hass: HomeAssistantType, config: dict):
    hass.states.async_set(f"{DOMAIN}.state", "on")

    # Return boolean to indicate that initialization was successful.
    return True
