import type { Message, VaultStats, BackendHealth, Chat } from '../types';

// Mock sleep utility to simulate network latency
const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

export const chatService = {
  async sendMessage(query: string, _chatHistory: Message[] = []): Promise<Message> {
    await sleep(1500); // simulate delay

    // Return a mock assistant response
    return {
      id: Date.now().toString(),
      role: 'assistant',
      content: `This is a simulated response to: **"${query}"**.\n\nHere's some markdown code:\n\`\`\`javascript\nconsole.log('Hello from ObsiZen!');\n\`\`\`\n\nI found this information in your vault.`,
      sources: [
        { id: '1', title: 'Stoicism.md' },
        { id: '2', title: 'YC IDEAS.md' },
      ],
    };
  },

  async syncVault(): Promise<{ success: boolean; stats: VaultStats }> {
    await sleep(2000);
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
    await sleep(500);
    return {
      status: 'online',
      latency: 42,
    };
  },

  async getStats(): Promise<VaultStats> {
    await sleep(800);
    return {
      documentCount: 1245,
      embeddingCount: 1200,
      lastSync: new Date(Date.now() - 3600000).toISOString(),
    };
  },
  
  async getRecentChats(): Promise<Chat[]> {
    await sleep(500);
    return [
      { id: '1', title: 'Brainstorming startup ideas', updatedAt: new Date().toISOString() },
      { id: '2', title: 'Notes on Stoicism', updatedAt: new Date(Date.now() - 86400000).toISOString() },
    ];
  }
};
