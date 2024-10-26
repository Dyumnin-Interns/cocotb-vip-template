"""Driver when VIP is bus master"""
import cocotb


class MasterDriver:
    def __init__(self):
        pass

    def read(self, address: int, length: int = 4) -> int:
        cocotb.log.info(f"Dummy read got {address} returning 4 bytes of 0")
        return int.to_bytes(0, 4, "little")

    def write(self, address: int, data: bytes) -> None:
        cocotb.log.info(f"Dummy write  got {address} {data} doing nothing.")

    def anyotherVIPCmd(self):
        """Any other command that is mentioned in VIP document."""
        pass
