from datetime import datetime

from pydantic import BaseModel


class Stock(BaseModel):
    symbol: str
    name: str
    current_price: float
    change_percent: float
    volume: int
    sector: str


class WatchlistEntry(BaseModel):
    symbol: str
    added_at: datetime
    last_seen_price: float
    last_seen_timestamp: datetime


class DeltaReport(BaseModel):
    symbol: str
    price_delta_percent: float
    volume_surge: bool
    is_meaningful: bool
    summary_headline: str
