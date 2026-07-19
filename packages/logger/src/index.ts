import pino, { type Logger } from 'pino';

export interface LoggerContext {
  requestId?: string;
  correlationId?: string;
  [key: string]: unknown;
}

export function createLogger(service: string): Logger {
  return pino({
    base: { service },
    formatters: {
      level: (label) => ({ level: label }),
    },
    timestamp: () => `,"timestamp":"${new Date().toISOString()}"`,
  });
}

export const logger = createLogger('platform');
