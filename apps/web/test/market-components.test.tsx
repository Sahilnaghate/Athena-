import { fireEvent, render, screen } from '@testing-library/react';

import {
  LastRefreshCard,
  MarketHealthCard,
  MarketRegimeCard,
  RefreshButton,
  SectorStrengthTable,
} from '../app/market/components';

const timestamp = '2026-07-21T09:15:00Z';

describe('Market dashboard components', () => {
  it('renders the Market Health card', () => {
    render(<MarketHealthCard snapshot={{ market_health_score: 78, snapshot_time: timestamp }} />);

    expect(screen.getByText('Market Health')).toBeInTheDocument();
    expect(screen.getByText('78')).toBeInTheDocument();
  });

  it('renders regime fallbacks when optional values are absent', () => {
    render(<MarketRegimeCard regime={{ value: 'SIDEWAYS', confidence: null, reason: null }} />);

    expect(screen.getByText('SIDEWAYS')).toBeInTheDocument();
    expect(screen.getByText('Confidence: —')).toBeInTheDocument();
    expect(screen.getByText('Not available')).toBeInTheDocument();
  });

  it('renders ranked sectors and an explicit empty state', () => {
    const { rerender } = render(
      <SectorStrengthTable sectors={[{ rank: 1, name: 'IT', strength: 89, momentum: 4.2 }]} />,
    );
    expect(screen.getByText('IT')).toBeInTheDocument();
    expect(screen.getByText('4.2')).toBeInTheDocument();

    rerender(<SectorStrengthTable sectors={[]} />);
    expect(screen.getByText('No sector strength data available.')).toBeInTheDocument();
  });

  it('renders the last refresh timestamp', () => {
    render(<LastRefreshCard timestamp={timestamp} />);

    expect(screen.getByText(/Last updated:/)).toBeInTheDocument();
  });

  it('supports refresh interaction and loading state', () => {
    const onRefresh = vi.fn();
    const { rerender } = render(<RefreshButton pending={false} onRefresh={onRefresh} />);

    fireEvent.click(screen.getByRole('button', { name: 'Refresh market' }));
    expect(onRefresh).toHaveBeenCalledOnce();

    rerender(<RefreshButton pending onRefresh={onRefresh} />);
    expect(screen.getByRole('button', { name: 'Refreshing…' })).toBeDisabled();
  });
});
