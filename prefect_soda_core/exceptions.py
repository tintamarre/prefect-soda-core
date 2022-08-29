"""
Exceptions to raise in case of issues while configuring or running Soda.
"""


class SodaConfigurationException(Exception):
    """
    Exception to raise in case of issues with Soda configuration.
    """

    pass


class SodaScanRunException(Exception):
    """
    Exception to raise in case of issues during Soda scan runs
    """

    pass
