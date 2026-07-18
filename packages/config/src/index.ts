export interface PlatformConfig {
  apiUrl: string;
}

export const platformConfig: PlatformConfig = {
  apiUrl: process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000',
};
