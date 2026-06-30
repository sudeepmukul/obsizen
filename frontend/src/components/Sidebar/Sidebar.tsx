import { useEffect } from 'react';
import { motion } from 'framer-motion';
import { Plus, Search, RefreshCw, Network, FileText, Terminal, Settings } from 'lucide-react';
import { AnimatedLogo } from '../UI/AnimatedLogo';
import { HealthIndicator } from '../UI/HealthIndicator';
import { useStore } from '../../store/useStore';
import { chatService } from '../../services/chat';

export const Sidebar = () => {
  const { 
    recentChats, 
    vaultStats, 
    backendStatus, 
    setRecentChats, 
    setVaultStats, 
    setBackendStatus,
    isSidebarOpen 
  } = useStore();

  useEffect(() => {
    // Load initial data
    chatService.getRecentChats().then(setRecentChats);
    chatService.getStats().then(setVaultStats);
    chatService.getHealth().then(setBackendStatus);
  }, []);

  const handleSync = async () => {
    const res = await chatService.syncVault();
    if (res.success) {
      setVaultStats(res.stats);
    }
  };

  if (!isSidebarOpen) return null;

  return (
    <motion.aside 
      initial={{ x: -280 }}
      animate={{ x: 0 }}
      className="w-[280px] h-screen glass border-r border-border flex flex-col flex-shrink-0"
    >
      {/* Brand */}
      <div className="p-4 border-b border-border/50">
        <AnimatedLogo />
      </div>

      {/* Actions */}
      <div className="p-3 space-y-1">
        <button className="w-full flex items-center gap-2 px-3 py-2.5 rounded-lg bg-surface hover:bg-surface/80 border border-border/50 transition-colors text-text-primary text-sm font-medium">
          <Plus size={16} />
          <span>New Chat</span>
        </button>
        <button className="w-full flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-surface/50 transition-colors text-text-secondary hover:text-text-primary text-sm">
          <Search size={16} />
          <span>Search Vault</span>
        </button>
        <button onClick={handleSync} className="w-full flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-surface/50 transition-colors text-text-secondary hover:text-text-primary text-sm">
          <RefreshCw size={16} />
          <span>Sync Vault</span>
        </button>
      </div>

      {/* Navigation Links */}
      <div className="px-3 py-2 space-y-1 border-b border-border/50">
        <button className="w-full flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-surface/50 transition-colors text-text-secondary hover:text-text-primary text-sm">
          <Network size={16} />
          <span>Knowledge Graph</span>
        </button>
        <button className="w-full flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-surface/50 transition-colors text-text-secondary hover:text-text-primary text-sm">
          <FileText size={16} />
          <span>Documents</span>
        </button>
        <button className="w-full flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-surface/50 transition-colors text-text-secondary hover:text-text-primary text-sm">
          <Terminal size={16} />
          <span>Prompts</span>
        </button>
      </div>

      {/* RAG Index Section */}
      <div className="p-4 border-b border-border/50">
        <h3 className="text-xs font-semibold text-text-secondary uppercase tracking-wider mb-3">Index Status</h3>
        {vaultStats ? (
          <div className="space-y-2 text-xs text-text-secondary">
            <div className="flex justify-between">
              <span>Documents</span>
              <span className="text-text-primary">{vaultStats.documentCount}</span>
            </div>
            <div className="flex justify-between">
              <span>Embeddings</span>
              <span className="text-text-primary">{vaultStats.embeddingCount}</span>
            </div>
            <div className="text-[10px] opacity-70 pt-1">
              Last sync: {new Date(vaultStats.lastSync).toLocaleTimeString()}
            </div>
          </div>
        ) : (
          <div className="animate-pulse flex space-x-4">
            <div className="flex-1 space-y-3 py-1">
              <div className="h-2 bg-border rounded"></div>
              <div className="h-2 bg-border rounded w-5/6"></div>
            </div>
          </div>
        )}
      </div>

      {/* Recent Chats */}
      <div className="flex-1 overflow-y-auto p-3">
        <h3 className="text-xs font-semibold text-text-secondary uppercase tracking-wider mb-2 px-1">Recent</h3>
        <div className="space-y-1">
          {recentChats.map((chat) => (
            <button key={chat.id} className="w-full text-left truncate px-3 py-2 rounded-lg hover:bg-surface/50 transition-colors text-text-secondary hover:text-text-primary text-sm">
              {chat.title}
            </button>
          ))}
        </div>
      </div>

      {/* Bottom User Section */}
      <div className="p-4 border-t border-border/50 bg-surface/30">
        <div className="flex items-center justify-between">
          <button className="flex items-center gap-2 text-text-secondary hover:text-text-primary transition-colors">
            <Settings size={18} />
            <span className="text-sm">Settings</span>
          </button>
          <HealthIndicator health={backendStatus} />
        </div>
      </div>
    </motion.aside>
  );
};
