'use client';

import { useEffect, useState } from 'react';

interface Sector { name: string; rank: number; relative_strength: number; momentum: number; trend: string; }
interface Overview { market_health: number | null; market_regime: string | null; last_updated: string | null; sectors: Sector[]; }

export default function MarketDashboard() {
  const [overview, setOverview] = useState<Overview | null>(null);
  useEffect(() => { fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/market/overview`).then((response) => response.json()).then((payload) => setOverview(payload.data)); }, []);
  return <main className="mx-auto max-w-5xl px-8 py-16"><p className="text-sm font-semibold tracking-[0.3em] text-cyan-400">MARKET INTELLIGENCE</p><h1 className="mt-4 text-4xl font-bold">Market Dashboard</h1><section className="mt-10 grid gap-6 md:grid-cols-2"><article className="rounded-xl border border-zinc-800 p-6"><p className="text-zinc-400">Market Regime</p><p className="mt-2 text-3xl font-semibold">{overview?.market_regime ?? 'No data'}</p></article><article className="rounded-xl border border-zinc-800 p-6"><p className="text-zinc-400">Market Health Score</p><p className="mt-2 text-3xl font-semibold">{overview?.market_health ?? '—'}</p></article></section><p className="mt-8 text-sm text-zinc-400">Last updated: {overview?.last_updated ? new Date(overview.last_updated).toLocaleString() : 'No data available'}</p><section className="mt-6 overflow-hidden rounded-xl border border-zinc-800"><table className="w-full text-left"><thead className="bg-zinc-900 text-zinc-400"><tr><th className="p-4">Rank</th><th>Sector</th><th>Strength</th><th>Momentum</th><th>Trend</th></tr></thead><tbody>{overview?.sectors.map((sector) => <tr className="border-t border-zinc-800" key={sector.name}><td className="p-4">{sector.rank}</td><td>{sector.name}</td><td>{sector.relative_strength}</td><td>{sector.momentum}</td><td>{sector.trend}</td></tr>)}</tbody></table></section></main>;
}
