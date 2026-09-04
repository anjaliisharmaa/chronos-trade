from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from mock_data import baseline_volumes, mock_stocks
from models import DeltaReport, WatchlistEntry

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"status": "Chronos Trade API is running"}


@app.post("/api/watchlist/catch-up", response_model=list[DeltaReport])
def watchlist_catch_up(entries: list[WatchlistEntry]) -> list[DeltaReport]:
    stocks_by_symbol = {stock.symbol: stock for stock in mock_stocks}
    reports: list[DeltaReport] = []

    for entry in entries:
        stock = stocks_by_symbol.get(entry.symbol)
        if stock is None:
            raise HTTPException(
                status_code=404,
                detail=f"No mock stock data found for symbol {entry.symbol}",
            )

        price_delta_percent = (
            ((stock.current_price - entry.last_seen_price) / entry.last_seen_price) * 100
            if entry.last_seen_price
            else 0.0
        )
        volume_surge = stock.volume >= baseline_volumes[entry.symbol] * 1.5
        is_meaningful = abs(price_delta_percent) > 2.0 or volume_surge

        if price_delta_percent > 0:
            price_description = f"up {price_delta_percent:.2f}%"
        elif price_delta_percent < 0:
            price_description = f"down {abs(price_delta_percent):.2f}%"
        else:
            price_description = "unchanged"

        volume_description = " with a notable volume surge" if volume_surge else ""
        reports.append(
            DeltaReport(
                symbol=entry.symbol,
                price_delta_percent=round(price_delta_percent, 2),
                volume_surge=volume_surge,
                is_meaningful=is_meaningful,
                summary_headline=(
                    f"{stock.name} is {price_description}{volume_description}."
                ),
            )
        )

    return sorted(reports, key=lambda report: report.is_meaningful, reverse=True)