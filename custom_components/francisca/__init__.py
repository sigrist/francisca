from homeassistant.helpers.typing import HomeAssistantType
import logging

DOMAIN = "francisca"


async def setup(hass: HomeAssistantType, config: dict):
    hass.states.async_set(f"{DOMAIN}.state", "on")
    entity = config["entity"]

    logging.info(f"Entity: {entity}")

    # Return boolean to indicate that initialization was successful.
    return True
