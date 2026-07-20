from app.market.provider import MarketData

MAX_HEALTH_SCORE = 100.0
MIN_HEALTH_SCORE = 0.0


class MarketHealthCalculator:
    def calculate(self, data: MarketData) -> float:
        """Calculate a transparent placeholder score from breadth and volatility."""
        breadth_component = min(data.advance_decline_ratio / 2, 1) * 60
        volatility_component = max(0, min((25 - data.india_vix) / 15, 1)) * 40
        return round(max(MIN_HEALTH_SCORE, min(MAX_HEALTH_SCORE, breadth_component + volatility_component)), 2)


class MarketRegimeDetector:
    def detect(self, data: MarketData, health_score: float) -> str:
        """Classify the current environment; replace thresholds with validated research later."""
        # TODO: replace fixed thresholds with validated historical regime analysis.
        if health_score >= 65 and data.advance_decline_ratio >= 1:
            return "BULL"
        if health_score <= 40 or data.advance_decline_ratio < 0.8:
            return "BEAR"
        return "SIDEWAYS"
