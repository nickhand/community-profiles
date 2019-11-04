from .core import CensusDataset

__all__ = ["MedianHouseholdIncome"]


class MedianHouseholdIncome(CensusDataset):
    """
    Median household income in the past 12 months (in inflation-adjusted dollars).
    """

    UNIVERSE = "households"
    TABLE_NAME = "B19013"
    RAW_FIELDS = {"001": "median"}
