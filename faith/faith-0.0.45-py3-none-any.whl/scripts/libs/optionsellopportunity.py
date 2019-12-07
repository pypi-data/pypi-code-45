class OptionSellOpportunity(object):

    def __init__(
        self,
        symbol: str,
        last_price: float,
        pct_chg_so_far: float,
        sd_this_week: float,
        mean_this_week: float,
        sd_next_week: float,
        mean_next_week: float,
    ) -> None:
        self._symbol = symbol
        self._last_price = last_price
        self._pct_chg_so_far = pct_chg_so_far
        self._sd_this_week = sd_this_week
        self._mean_this_week = mean_this_week
        self._sd_next_week = sd_next_week
        self._mean_next_week = mean_next_week

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def last_price(self) -> float:
        return self._last_price

    @property
    def pct_chg_so_far(self) -> float:
        return self._pct_chg_so_far

    @property
    def sd_this_week(self) -> float:
        return self._sd_this_week

    @property
    def mean_this_week(self) -> float:
        return self._mean_this_week

    @property
    def sd_next_week(self) -> float:
        return self._sd_next_week

    @property
    def mean_next_week(self) -> float:
        return self._mean_next_week

    @property
    def z_score_this_week(self) -> float:
        return abs(self.pct_chg_so_far - self.mean_this_week) / self.sd_this_week

    @property
    def z_score_next_week(self) -> float:
        if self.sd_next_week is None:
            return 0.0
        else:
            return abs(self.pct_chg_so_far - self.mean_next_week) / self.sd_next_week
