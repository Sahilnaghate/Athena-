export interface PlatformEvent<T = unknown> {
  name: string;
  payload: T;
  occurredAt: string;
}
