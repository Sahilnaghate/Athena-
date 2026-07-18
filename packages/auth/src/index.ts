export interface AuthenticatedPrincipal {
  id: string;
}
export function isAuthenticated(value: unknown): value is AuthenticatedPrincipal {
  return typeof value === 'object' && value !== null && 'id' in value;
}
