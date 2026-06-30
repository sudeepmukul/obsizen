import { motion } from 'framer-motion';

const SUGGESTIONS = [
  "Summarize today's notes",
  "What am I learning lately?",
  "Find startup ideas",
  "What projects am I working on?",
];

interface Props {
  onSelect: (prompt: string) => void;
}

export const QuickPrompts = ({ onSelect }: Props) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-3 w-full max-w-2xl mx-auto mt-8">
      {SUGGESTIONS.map((suggestion, i) => (
        <motion.button
          key={suggestion}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: i * 0.1 }}
          onClick={() => onSelect(suggestion)}
          className="text-left p-4 rounded-xl glass hover:bg-surface transition-colors border-border/50 hover:border-brand-2/50 text-text-secondary hover:text-text-primary text-sm"
        >
          {suggestion}
        </motion.button>
      ))}
    </div>
  );
};
