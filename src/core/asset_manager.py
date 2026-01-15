import os

class AssetManager:
    # Base data folder relative to this script
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")

    @classmethod
    def get_path(cls, filename: str, subfolder: str | None = None) -> str:
        """
        Get the relative path to an asset.

        :param filename: Name of the file, e.g., 'player.png'
        :param subfolder: Optional subfolder under data, e.g., 'images'
        :return: Relative path to the asset
        """
        if subfolder:
            path = os.path.join(cls.DATA_DIR, subfolder, filename)
        else:
            path = os.path.join(cls.DATA_DIR, filename)
        return path