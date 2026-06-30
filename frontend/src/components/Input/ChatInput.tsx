import React, { useState, useRef, useEffect } from 'react';
import { ArrowUp, Square } from 'lucide-react';
import { useStore } from '../../store/useStore';
import { chatService } from '../../services/chat';
import { cn } from '../../utils/cn';

export const ChatInput = () => {
  const [input, setInput] = useState('');
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const { isLoading, setIsLoading, addMessage, messages } = useStore();

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 200)}px`;
    }
  }, [input]);

  const handleSubmit = async (e?: React.FormEvent) => {
    e?.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage = {
      id: Date.now().toString(),
      role: 'user' as const,
      content: input.trim(),
    };

    addMessage(userMessage);
    setInput('');
    setIsLoading(true);

    try {
      const response = await chatService.sendMessage(userMessage.content, messages);
      addMessage(response);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="w-full max-w-3xl mx-auto p-4 relative">
      <div className={cn(
        "relative flex flex-col rounded-2xl bg-surface border transition-all duration-300",
        isLoading ? "border-brand-2 shadow-[0_0_15px_rgba(168,85,247,0.2)]" : "border-border/50 focus-within:border-border"
      )}>
        {/* Animated border for loading state */}
        {isLoading && (
          <div className="absolute inset-0 -z-10 rounded-2xl animate-gradient-bg opacity-30 blur-sm" />
        )}
        
        <textarea
          ref={textareaRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask your Vault..."
          className="w-full max-h-[200px] bg-transparent text-text-primary px-4 py-4 resize-none focus:outline-none placeholder:text-text-secondary/50"
          rows={1}
        />
        
        <div className="flex items-center justify-between px-3 pb-3">
          <div className="flex items-center gap-2">
            <div className="relative group">
              <select className="bg-surface border border-border/50 text-text-secondary text-xs rounded-lg pl-3 pr-8 py-1.5 focus:outline-none focus:border-brand-1 hover:bg-white/5 transition-colors cursor-pointer appearance-none">
                <option value="llama-3">Llama 3 (Local)</option>
                <option value="mistral-instruct">Mistral Instruct</option>
                <option value="gemini-1-5-pro">Gemini 1.5 Pro</option>
                <option value="gpt-4o">GPT-4o</option>
              </select>
              <div className="absolute inset-y-0 right-2 flex items-center pointer-events-none opacity-50 group-hover:opacity-100 transition-opacity">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m6 9 6 6 6-6"/></svg>
              </div>
            </div>
          </div>
          
          {isLoading ? (
            <button 
              className="p-2 rounded-full bg-brand-2 text-white hover:bg-brand-1 transition-colors"
              onClick={() => setIsLoading(false)} // In a real app, this would abort the fetch
            >
              <Square size={16} className="fill-current" />
            </button>
          ) : (
            <button 
              onClick={handleSubmit}
              disabled={!input.trim()}
              className="p-2 rounded-full bg-surface border border-border/50 text-text-primary hover:bg-white/10 disabled:opacity-50 disabled:hover:bg-surface transition-colors"
            >
              <ArrowUp size={18} />
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
