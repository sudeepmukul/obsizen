import { motion } from 'framer-motion';

export const ThinkingIndicator = () => {
  return (
    <div className="flex gap-4 max-w-3xl w-full mx-auto py-6">
      <div className="flex items-center gap-2 px-4 py-3 bg-surface/30 w-fit rounded-2xl border border-border/50">
        <motion.div 
          className="w-2 h-2 rounded-full"
          style={{ backgroundColor: 'var(--color-brand-1)' }}
          animate={{ scale: [1, 1.5, 1], opacity: [0.5, 1, 0.5] }}
          transition={{ duration: 1, repeat: Infinity, delay: 0 }}
        />
        <motion.div 
          className="w-2 h-2 rounded-full"
          style={{ backgroundColor: 'var(--color-brand-2)' }}
          animate={{ scale: [1, 1.5, 1], opacity: [0.5, 1, 0.5] }}
          transition={{ duration: 1, repeat: Infinity, delay: 0.2 }}
        />
        <motion.div 
          className="w-2 h-2 rounded-full"
          style={{ backgroundColor: 'var(--color-brand-3)' }}
          animate={{ scale: [1, 1.5, 1], opacity: [0.5, 1, 0.5] }}
          transition={{ duration: 1, repeat: Infinity, delay: 0.4 }}
        />
      </div>
    </div>
  );
};
