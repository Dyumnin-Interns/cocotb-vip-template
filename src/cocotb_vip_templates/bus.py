"""Bus."""
from cocotb_bus.bus import Bus as B
from .config import Config


class Bus:
    def __init__(
        dut,
        prefix: str = "",
        suffix: str = "",
        bus_seperator: str = "_",
        clk: str = "clk",
        reset: str = "rst_n",
        active_high_reset=True,
        uppercase: bool = False,
    ):
        """
        Args:
            dut (SimHandle): ...
            prefix (str):...
        """
        pass

    def get_bus(self):
        """creates and returns the bus object."""
        pass

    def get_somespecialfunction_bus(self, params):
        """
        This function handles a special signal naming convention seen in this protocol that is not covered by the default bus structure and creates and returns the bus.
        Args:
            params (sometype):...
        """
        pass
