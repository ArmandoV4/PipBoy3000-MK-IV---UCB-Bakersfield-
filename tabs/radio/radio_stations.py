from resources.assets import Assets
from tabs.submenu import Submenu

class RadioStation(Submenu):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name: str = 'RADIO STATIONS'