"use client";

import { useStream } from "@langchain/langgraph-sdk/react";
import { LoadExternalComponent, UIMessage } from "@langchain/langgraph-sdk/react-ui";

type AgentState = {
    messages: unknown[];
    ui?: UIMessage[];
};

export default function Page() {
    const stream = useStream<AgentState>({
        apiUrl: "http://localhost:2024", // Assuming LangGraph server runs here
        assistantId: "agent",
    });
    const { messages, values, submit } = stream;

    return (
        <div className="max-w-4xl mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Generative UI Chat</h1>

            <div className="space-y-4 mb-4 border p-4 rounded min-h-[300px] max-h-[600px] overflow-y-auto">
                {messages.map((message) => (
                    <div key={message.id} className={`p-3 rounded-lg ${message.type === 'human' ? 'bg-blue-100 ml-auto max-w-[80%]' : 'bg-gray-100 mr-auto max-w-[80%]'}`}>
                        <div className="font-xs text-gray-500 mb-1">{message.type === 'human' ? 'You' : 'Agent'}</div>
                        <div>{typeof message.content === 'string' ? message.content : JSON.stringify(message.content)}</div>

                        {/* Render UI components associated with this message */}
                        {values.ui
                            ?.filter((ui) => ui.metadata?.message_id === message.id)
                            .map((ui) => (
                                <div key={ui.id} className="mt-2">
                                    <LoadExternalComponent stream={stream} message={ui} />
                                </div>
                            ))}
                    </div>
                ))}
            </div>

            <form
                onSubmit={(e) => {
                    e.preventDefault();
                    const form = e.target as HTMLFormElement;
                    const input = form.elements.namedItem("input") as HTMLInputElement;
                    const value = input.value;
                    if (!value) return;

                    submit({ messages: [{ type: "human", content: value }] });
                    input.value = "";
                }}
                className="flex gap-2"
            >
                <input
                    name="input"
                    className="flex-1 p-2 border rounded"
                    placeholder="Ask about the weather..."
                />
                <button type="submit" className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                    Send
                </button>
            </form>
        </div>
    );
}
