import { api } from './api';
import type { Message, VaultStats, BackendHealth, Chat } from '../types';
import { AxiosError } from 'axios';

/**
 * Shape returned by the POST /chat endpoint.
 */
interface ChatApiResponse {
  answer: string;
  sources: string[]; // e.g. ["ML - BASICS.md", "COSINE SIMILARITY.md"]
}

/**
 * Normalise a network / Axios error into a user-friendly message string.
 */
function friendlyError(err: unknown): string {
  if (err instanceof AxiosError) {
    if (err.code === 'ECONNABORTED') {
      return 'The request timed out. The backend may be overloaded — please try again.';
    }
    if (!err.response) {
      // Network error — backend is likely offline
      return 'Unable to reach the backend. Make sure the server is running at http://127.0.0.1:8000.';
    }
    const status = err.response.status;
    if (status >= 500) {
      return `Server error (${status}). Please try again later.`;
    }
    if (status === 422) {
      return 'The request was malformed. Please try rephrasing your question.';
    }
    return `Request failed with status ${status}.`;
  }
  return 'An unexpected error occurred. Please try again.';
}

export const chatService = {
  /**
   * Send a chat query to POST /chat and return a Message for the store.
   * On error, returns a Message with role "assistant" whose content is the
   * error description — this keeps the chat flow intact.
   */
  async sendMessage(query: string, _chatHistory: Message[] = []): Promise<Message> {
    try {
      const { data } = await api.post<ChatApiResponse>('/chat', { query });

      // Map the flat source-string array into Source objects
      const sources = (data.sources ?? []).map((title, idx) => ({
        id: `src-${Date.now()}-${idx}`,
        title,
      }));

      return {
        id: Date.now().toString(),
        role: 'assistant',
        content: data.answer,
        sources,
      };
    } catch (err) {
      return {
        id: Date.now().toString(),
        role: 'assistant',
        content: `⚠️ **Error**\n\n${friendlyError(err)}`,
        isError: true,
      };
    }
  },

  // ─── The endpoints below remain mocked until the backend exposes them ──

  async syncVault(): Promise<{ success: boolean; stats: VaultStats }> {
    // No backend endpoint yet — keep mock
    await new Promise((r) => setTimeout(r, 2000));
    return {
      success: true,
      stats: {
        documentCount: 1420,
        embeddingCount: 1420,
        lastSync: new Date().toISOString(),
      },
    };
  },

  async getHealth(): Promise<BackendHealth> {
    try {
      const start = performance.now();
      await api.get('/health');
      const latency = Math.round(performance.now() - start);
      return { status: 'online', latency };
    } catch {
      return { status: 'offline' };
    }
  },

  async getStats(): Promise<VaultStats> {
    // No backend endpoint yet — keep mock
    await new Promise((r) => setTimeout(r, 800));
    return {
      documentCount: 1245,
      embeddingCount: 1200,
      lastSync: new Date(Date.now() - 3600000).toISOString(),
    };
  },

  async getRecentChats(): Promise<Chat[]> {
    // No backend endpoint yet — keep mock
    await new Promise((r) => setTimeout(r, 500));
    return [
      { id: '1', title: 'Brainstorming startup ideas', updatedAt: new Date().toISOString() },
      { id: '2', title: 'Notes on Stoicism', updatedAt: new Date(Date.now() - 86400000).toISOString() },
    ];
  },
};
