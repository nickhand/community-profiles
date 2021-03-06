import esri2gpd
from . import EPSG
from .core import *
from .regions import *

__all__ = ["RebuildSites"]


class RebuildSites(Dataset):
    """
    Philadephia's selected or eligible Rebuild sites.
    The Rebuild program was implemented to improve community facilities. 
    
    Source
    ------
    https://phl.maps.arcgis.com/home/item.html?id=2cee6cd0c0864258b326108707b8942b
    """

    @classmethod
    def download(cls, **kwargs):

        fields = [
            "ASSET_NAME",
            "ASSET_ADDR",
            "SITE_NAME",
            "Copy_of_Master_Site_List_9_24_2",
            "Copy_of_Master_Site_List_9_24_5",
            "Copy_of_Master_Site_List_9_24_7",
            "Copy_of_Master_Site_List_9_24_8",
            "Copy_of_Master_Site_List_9_24_9",
            "Copy_of_Master_Site_List_9_2_10",
            "Copy_of_Master_Site_List_9_2_11",
            "Copy_of_Master_Site_List_9_2_13",
        ]

        url = "https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services/Rebuild_Sites/FeatureServer/0"

        return (
            esri2gpd.get(url, fields=fields)
            .to_crs(epsg=EPSG)
            .rename(
                columns={
                    "Copy_of_Master_Site_List_9_24_2": "SITE_TYPE",
                    "Copy_of_Master_Site_List_9_24_5": "PRELIMINARY_SITE_NEEDS",
                    "Copy_of_Master_Site_List_9_24_7": "ROUGH_EST_COST",
                    "Copy_of_Master_Site_List_9_24_8": "PROJECT_STATUS",
                    "Copy_of_Master_Site_List_9_24_9": "PROJECT_TYPE",
                    "Copy_of_Master_Site_List_9_2_10": "COUNCIL_PRIORITY",
                    "Copy_of_Master_Site_List_9_2_11": "PPR_PRIORITY",
                    "Copy_of_Master_Site_List_9_2_13": "HIGH_NEED",
                }
            )
            .pipe(geocode, ZIPCodes.get())
            .pipe(geocode, Neighborhoods.get())
            .pipe(geocode, PUMAs.get())
        )
