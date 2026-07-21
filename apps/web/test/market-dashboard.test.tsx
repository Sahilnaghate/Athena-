import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import type { ReactNode } from 'react';

import MarketDashboard from '../app/market/page';

const initialState = {
  snapshot: { market_health_score: 78, snapshot_time: '2026-07-21T09:15:00Z' },
  regime: { value: 'BULL', confidence: 82, reason: 'Positive breadth.' },
  sectors: [{ rank: 1, name: 'IT', strength: 89, momentum: 4.2 }],
};

function response(data: unknown, ok = true) {
  return { ok, json: async () => ({ data }) } as Response;
}

function renderDashboard(children: ReactNode = <MarketDashboard />) {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return render(<QueryClientProvider client={client}>{children}</QueryClientProvider>);
}

describe('MarketDashboard', () => {
  afterEach(() => vi.unstubAllGlobals());

  it('renders a loading state before the latest response resolves', () => {
    vi.stubGlobal('fetch', vi.fn(() => new Promise(() => undefined)));
    renderDashboard();

    expect(screen.getByText('Loading Market data…')).toBeInTheDocument();
  });

  it('renders current Market API data and sector rankings', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(response(initialState)));
    renderDashboard();

    expect(await screen.findByText('Market Dashboard')).toBeInTheDocument();
    expect(screen.getByText('BULL')).toBeInTheDocument();
    expect(screen.getByText('IT')).toBeInTheDocument();
  });

  it('renders an API failure', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(response({}, false)));
    renderDashboard();

    expect(await screen.findByText('Unable to load Market data.')).toBeInTheDocument();
  });

  it('renders the empty sector response', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(response({ ...initialState, sectors: [] })));
    renderDashboard();

    expect(await screen.findByText('No sector strength data available.')).toBeInTheDocument();
  });

  it('refreshes and invalidates the latest Market query', async () => {
    const refreshedState = { ...initialState, snapshot: { ...initialState.snapshot, market_health_score: 81 } };
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce(response(initialState))
      .mockResolvedValueOnce(response(initialState))
      .mockResolvedValueOnce(response(refreshedState));
    vi.stubGlobal('fetch', fetchMock);
    renderDashboard();

    await screen.findByText('78');
    fireEvent.click(screen.getByRole('button', { name: 'Refresh market' }));

    await waitFor(() => expect(screen.getByText('81')).toBeInTheDocument());
    expect(fetchMock).toHaveBeenCalledTimes(3);
    expect(fetchMock.mock.calls[1][0]).toContain('/api/v1/market/refresh');
    expect(fetchMock.mock.calls[1][1]).toMatchObject({ method: 'POST' });
  });
});
