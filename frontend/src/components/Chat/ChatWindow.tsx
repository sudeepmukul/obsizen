import { useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useStore } from '../../store/useStore';
import { MessageBubble } from './MessageBubble';
import { ThinkingIndicator } from './ThinkingIndicator';
import { QuickPrompts } from '../Input/QuickPrompts';
import { ChatInput } from '../Input/ChatInput';

export const ChatWindow = () => {
  const { messages, isLoading, addMessage, setIsLoading } = useStore();
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleQuickPrompt = async (prompt: string) => {
    const userMessage = {
      id: Date.now().toString(),
      role: 'user' as const,
      content: prompt,
    };
    addMessage(userMessage);
    setIsLoading(true);

    import('../../services/chat').then(({ chatService }) => {
      chatService.sendMessage(prompt, messages).then((response) => {
        addMessage(response);
        setIsLoading(false);
      });
    });
  };

  return (
    <div className="flex flex-col h-screen flex-1 relative bg-bg-primary overflow-hidden z-0">
      {/* Breathing glowing background */}
      <div className="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-glow opacity-30 rounded-full mix-blend-screen pointer-events-none" />

      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto scroll-smooth pb-32 relative z-10">
        <AnimatePresence>
          {messages.length === 0 ? (
            <motion.div 
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="flex flex-col items-center justify-center h-full px-4 pt-20"
            >
              <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-text-primary mb-4 text-center pb-2">
                Ask your Vault
              </h1>
              <p className="text-text-secondary text-lg mb-8 text-center">
                Your local-first AI Second Brain is ready.
              </p>
              <QuickPrompts onSelect={handleQuickPrompt} />
            </motion.div>
          ) : (
            <div className="flex flex-col pt-8">
              {messages.map((message) => (
                <motion.div
                  key={message.id}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                >
                  <MessageBubble message={message} />
                </motion.div>
              ))}
              {isLoading && (
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                >
                  <ThinkingIndicator />
                </motion.div>
              )}
              <div ref={messagesEndRef} className="h-4" />
            </div>
          )}
        </AnimatePresence>
      </div>

      {/* Input Area */}
      <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-bg-primary via-bg-primary to-transparent pt-10 pb-6 px-4 z-20">
        <ChatInput />
      </div>
    </div>
  );
};
