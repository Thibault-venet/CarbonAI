__all__ = ["PowerMeter"]


from PyPowerGadget.PowerGadget import *
from PyPowerGadget.settings import *

class PowerMeter():
    def __init__(self, power_log_path=""):
        self.platform = sys.platform
        if self.platform == MAC_PLATFORM:
            self.power_gadget = PowerGadgetMac(power_log_path=power_log_path)
        elif self.platform == WIN_PLATFORM:
            self.power_gadget = PowerGadgetWin(power_log_path=power_log_path)
        self.pue = 1.28  # pue for my laptop
        # self.pue = 1.58 # pue for a server


    def aggregate_power(self, recorded_power):
        print(recorded_power)
        used_energy = self.pue * (recorded_power[TOTAL_ENERGY_CPU] + recorded_power[TOTAL_ENERGY_MEMORY])

    def mesure_power(self, func, time_interval=1):

        def wrapper(*args, **kwargs):
            results = self.power_gadget.wrapper(func, *args, time_interval=time_interval, **kwargs)
            self.aggregate_power(self.power_gadget.recorded_power)
            return results

        return wrapper
