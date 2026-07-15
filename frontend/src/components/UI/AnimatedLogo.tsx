import { motion } from 'framer-motion';
import { Sparkles } from 'lucide-react';
import { cn } from '../../utils/cn';

export const AnimatedLogo = ({ className }: { className?: string }) => {
  return (
    <div className={cn("flex items-center gap-2", className)}>
      <motion.div
        animate={{ 
          rotate: [0, 15, -15, 0],
          scale: [1, 1.1, 1]
        }}
        transition={{ 
          duration: 4, 
          repeat: Infinity,
          ease: "easeInOut"
        }}
      >
        <Sparkles size={24} style={{ color: 'var(--color-brand-1)' }} />
      </motion.div>
      <span className="text-xl font-bold tracking-tight text-gradient">
        ObsiZen
      </span>
    </div>
  );
};
