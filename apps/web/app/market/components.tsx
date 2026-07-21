export type State = {
  snapshot: { market_health_score: number; snapshot_time: string };
  regime: { value: string; confidence: number | null; reason: string | null };
  sectors: { rank: number; name: string; strength: number; momentum: number }[];
};
export function MarketHealthCard({ snapshot }: Pick<State, 'snapshot'>) {
  return (
    <article className="rounded-xl border border-zinc-800 p-6">
      <p className="text-zinc-400">Market Health</p>
      <p className="mt-2 text-4xl font-semibold text-emerald-400">{snapshot.market_health_score}</p>
      <p className="mt-3 text-sm text-zinc-500">
        {new Date(snapshot.snapshot_time).toLocaleString()}
      </p>
    </article>
  );
}
export function MarketRegimeCard({ regime }: Pick<State, 'regime'>) {
  return (
    <article className="rounded-xl border border-zinc-800 p-6">
      <p className="text-zinc-400">Market Regime</p>
      <p className="mt-2 text-3xl font-semibold">{regime.value}</p>
      <p className="mt-3 text-sm">Confidence: {regime.confidence ?? '—'}</p>
      <p className="mt-1 text-sm text-zinc-500">{regime.reason ?? 'Not available'}</p>
    </article>
  );
}
export function SectorStrengthTable({ sectors }: Pick<State, 'sectors'>) {
  return (
    <table className="mt-4 w-full overflow-hidden rounded-xl border border-zinc-800 text-left">
      <thead className="bg-zinc-900 text-zinc-400">
        <tr>
          <th className="p-4">Rank</th>
          <th>Sector</th>
          <th>Strength</th>
          <th>Momentum</th>
        </tr>
      </thead>
      <tbody>
        {sectors.length === 0 ? (
          <tr>
            <td className="p-4 text-zinc-500" colSpan={4}>
              No sector strength data available.
            </td>
          </tr>
        ) : sectors.map((sector) => (
          <tr className="border-t border-zinc-800" key={sector.rank}>
            <td className="p-4">{sector.rank}</td>
            <td>{sector.name}</td>
            <td>{sector.strength}</td>
            <td>{sector.momentum}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
export function LastRefreshCard({ timestamp }: { timestamp: string }) {
  return (
    <p className="mt-3 text-sm text-zinc-500">
      Last updated: {new Date(timestamp).toLocaleString()}
    </p>
  );
}
export function RefreshButton({ pending, onRefresh }: { pending: boolean; onRefresh: () => void }) {
  return (
    <button
      className="rounded-lg bg-cyan-400 px-4 py-2 font-semibold text-zinc-950 disabled:opacity-50"
      disabled={pending}
      onClick={onRefresh}
    >
      {pending ? 'Refreshing…' : 'Refresh market'}
    </button>
  );
}
