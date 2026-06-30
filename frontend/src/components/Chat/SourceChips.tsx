import type { Source } from '../../types';
import { FileText } from 'lucide-react';
import { cn } from '../../utils/cn';

interface Props {
  sources: Source[];
  className?: string;
}

export const SourceChips = ({ sources, className }: Props) => {
  if (!sources || sources.length === 0) return null;

  return (
    <div className={cn("flex flex-wrap gap-2 mt-4", className)}>
      {sources.map((source) => (
        <a
          key={source.id}
          href={source.path || '#'}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-surface/50 border border-border hover:bg-surface hover:border-purple-500/50 transition-colors text-xs text-text-secondary hover:text-text-primary"
        >
          <FileText size={12} style={{ color: 'var(--color-brand-1)' }} />
          <span>{source.title}</span>
        </a>
      ))}
    </div>
  );
};
