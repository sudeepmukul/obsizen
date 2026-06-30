export type Role = 'user' | 'assistant';

export interface Source {
  id: string;
  title: string;
  path?: string;
}

export interface Message {
  id: string;
  role: Role;
  content: string;
  sources?: Source[];
}

export interface Chat {
  id: string;
  title: string;
  updatedAt: string;
}

export interface VaultStats {
  documentCount: number;
  embeddingCount: number;
  lastSync: string;
}

export interface BackendHealth {
  status: 'online' | 'offline' | 'checking';
  latency?: number;
}
