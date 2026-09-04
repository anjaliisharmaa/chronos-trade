from models import Stock


mock_stocks: list[Stock] = [
    Stock(
        symbol="NVDA",
        name="NVIDIA Corporation",
        current_price=134.25,
        change_percent=2.84,
        volume=248_600_000,
        sector="Technology",
    ),
    Stock(
        symbol="MSFT",
        name="Microsoft Corporation",
        current_price=418.92,
        change_percent=0.67,
        volume=18_400_000,
        sector="Technology",
    ),
    Stock(
        symbol="TSLA",
        name="Tesla, Inc.",
        current_price=248.98,
        change_percent=-1.42,
        volume=96_700_000,
        sector="Automotive",
    ),
    Stock(
        symbol="TM",
        name="Toyota Motor Corporation",
        current_price=184.36,
        change_percent=0.93,
        volume=7_900_000,
        sector="Automotive",
    ),
    Stock(
        symbol="ENPH",
        name="Enphase Energy, Inc.",
        current_price=71.48,
        change_percent=3.16,
        volume=12_300_000,
        sector="Green Energy",
    ),
    Stock(
        symbol="FSLR",
        name="First Solar, Inc.",
        current_price=214.67,
        change_percent=-0.58,
        volume=4_600_000,
        sector="Green Energy",
    ),
]


baseline_volumes: dict[str, int] = {
    "NVDA": 165_000_000,
    "MSFT": 16_000_000,
    "TSLA": 72_000_000,
    "TM": 7_000_000,
    "ENPH": 8_000_000,
    "FSLR": 4_000_000,
}
