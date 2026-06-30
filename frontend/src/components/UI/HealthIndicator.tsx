import { motion } from 'framer-motion';
import type { BackendHealth } from '../../types';
import { cn } from '../../utils/cn';

interface Props {
  health: BackendHealth;
  className?: string;
}

export const HealthIndicator = ({ health, className }: Props) => {
  const isOnline = health.status === 'online';
  const isChecking = health.status === 'checking';

  return (
    <div className={cn("flex items-center gap-2 text-xs", className)}>
      <div className="relative flex h-2.5 w-2.5">
        {isOnline && (
          <motion.span
            animate={{ scale: [1, 1.5, 1], opacity: [0.5, 0, 0.5] }}
            transition={{ duration: 2, repeat: Infinity }}
            className="absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"
          ></motion.span>
        )}
        <span className={cn(
          "relative inline-flex rounded-full h-2.5 w-2.5",
          isOnline ? "bg-green-500" : isChecking ? "bg-yellow-500" : "bg-red-500"
        )}></span>
      </div>
      <span className="text-text-secondary capitalize">
        {health.status} {health.latency ? `${health.latency}ms` : ''}
      </span>
    </div>
  );
};
