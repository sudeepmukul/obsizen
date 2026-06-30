import { Sidebar } from '../components/Sidebar/Sidebar';
import { ChatWindow } from '../components/Chat/ChatWindow';

export const MainLayout = () => {
  return (
    <div className="flex h-screen w-full bg-bg-primary text-text-primary overflow-hidden font-sans">
      <Sidebar />
      <main className="flex-1 flex flex-col relative min-w-0">
        <ChatWindow />
      </main>
    </div>
  );
};
