import ReactMarkdown from 'react-markdown';
import type { Message } from '../../types';
import { SourceChips } from './SourceChips';
import { AnimatedLogo } from '../UI/AnimatedLogo';

export const AssistantMessage = ({ message }: { message: Message }) => {
  return (
    <div className="flex gap-4 max-w-3xl w-full mx-auto py-6">
      <div className="flex-shrink-0 mt-1">
        <AnimatedLogo className="[&>span]:hidden" />
      </div>
      <div className="flex-1 space-y-4 overflow-hidden">
        <div className="prose prose-invert max-w-none text-text-primary prose-p:leading-relaxed prose-pre:bg-surface prose-pre:border prose-pre:border-border">
          <ReactMarkdown>{message.content}</ReactMarkdown>
        </div>
        {message.sources && <SourceChips sources={message.sources} />}
      </div>
    </div>
  );
};
