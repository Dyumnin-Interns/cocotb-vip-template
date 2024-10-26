"""Driver when VIP is slave"""
import cocotb


class PrintCallback:
    """Only prints the parameters received."""

    def read(self, address: int, length: int = 4) -> int:
        cocotb.log.info(f"Dummy read callback got {address} returning 4 bytes of 0")
        return int.to_bytes(0, 4, "little")

    def write(self, address: int, data: bytes) -> None:
        cocotb.log.info(f"Dummy write callback got {address} {data} doing nothing.")

    def anyotherVIPCmd(self):
        """Any other command that is mentioned in VIP document."""
        pass


class SlaveDriver:
    def __init__(self, *, callback=PrintCallback()):
        pass
