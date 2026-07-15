import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { Message, Chat, VaultStats, BackendHealth } from '../types';

interface StoreState {
  // Chat state
  messages: Message[];
  currentChatId: string | null;
  recentChats: Chat[];
  isLoading: boolean;
  isSidebarOpen: boolean;
  
  // Backend & Vault state
  backendStatus: BackendHealth;
  vaultStats: VaultStats | null;

  // Actions
  setMessages: (messages: Message[] | ((prev: Message[]) => Message[])) => void;
  addMessage: (message: Message) => void;
  setCurrentChatId: (id: string | null) => void;
  setRecentChats: (chats: Chat[]) => void;
  setIsLoading: (loading: boolean) => void;
  toggleSidebar: () => void;
  setBackendStatus: (status: BackendHealth) => void;
  setVaultStats: (stats: VaultStats) => void;
}

export const useStore = create<StoreState>()(
  persist(
    (set) => ({
      messages: [],
      currentChatId: null,
      recentChats: [],
      isLoading: false,
      isSidebarOpen: true,
      
      backendStatus: { status: 'checking' },
      vaultStats: null,

      setMessages: (messages) => set((state) => ({ 
        messages: typeof messages === 'function' ? messages(state.messages) : messages 
      })),
      addMessage: (message) => set((state) => ({ 
        messages: [...state.messages, message] 
      })),
      setCurrentChatId: (id) => set({ currentChatId: id }),
      setRecentChats: (chats) => set({ recentChats: chats }),
      setIsLoading: (loading) => set({ isLoading: loading }),
      toggleSidebar: () => set((state) => ({ isSidebarOpen: !state.isSidebarOpen })),
      setBackendStatus: (status) => set({ backendStatus: status }),
      setVaultStats: (stats) => set({ vaultStats: stats }),
    }),
    {
      name: 'obsizen-storage',
      partialize: (state) => ({ recentChats: state.recentChats }), // Only persist recentChats
    }
  )
);
