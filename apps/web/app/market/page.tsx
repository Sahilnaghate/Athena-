'use client';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import {
  LastRefreshCard,
  MarketHealthCard,
  MarketRegimeCard,
  RefreshButton,
  SectorStrengthTable,
  type State,
} from './components';

const api = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';
async function request(path: string, init?: RequestInit) {
  const response = await fetch(`${api}${path}`, init);
  if (!response.ok) throw new Error('Market API request failed');
  return response.json() as Promise<{ data: State }>;
}
export default function MarketDashboard() {
  const client = useQueryClient();
  const latest = useQuery({
    queryKey: ['market'],
    queryFn: () => request('/api/v1/market/latest'),
  });
  const refresh = useMutation({
    mutationFn: () => request('/api/v1/market/refresh', { method: 'POST' }),
    onSuccess: () => client.invalidateQueries({ queryKey: ['market'] }),
  });
  if (latest.isLoading) return <main className="p-8 text-zinc-400">Loading Market data…</main>;
  if (latest.isError || !latest.data)
    return <main className="p-8 text-red-400">Unable to load Market data.</main>;
  const data = latest.data.data;
  return (
    <main className="mx-auto max-w-6xl px-6 py-12">
      <div className="flex items-center justify-between">
        <h1 className="text-4xl font-bold">Market Dashboard</h1>
        <RefreshButton pending={refresh.isPending} onRefresh={() => refresh.mutate()} />
      </div>
      {refresh.isError && <p className="mt-4 text-red-400">Refresh failed.</p>}
      <section className="mt-8 grid gap-6 md:grid-cols-2">
        <MarketHealthCard snapshot={data.snapshot} />
        <MarketRegimeCard regime={data.regime} />
      </section>
      <LastRefreshCard timestamp={data.snapshot.snapshot_time} />
      <h2 className="mt-10 text-xl font-semibold">Sector Strength</h2>
      <SectorStrengthTable sectors={data.sectors} />
    </main>
  );
}
