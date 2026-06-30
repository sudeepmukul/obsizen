import type { Message } from '../../types';
import { AssistantMessage } from './AssistantMessage';

export const MessageBubble = ({ message }: { message: Message }) => {
  if (message.role === 'assistant') {
    return <AssistantMessage message={message} />;
  }

  return (
    <div className="flex gap-4 max-w-3xl w-full mx-auto py-6 justify-end">
      <div className="bg-surface border border-border/50 px-5 py-3 rounded-2xl rounded-tr-sm max-w-[80%] text-text-primary whitespace-pre-wrap">
        {message.content}
      </div>
    </div>
  );
};
