import gradio as gr
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from graph import graph

config = {"configurable": {"thread_id": "thread_1"}}

def call_graph(message, history):  
    result = graph.invoke(
        {"input": message, "chat_history": history},
        config=config,
    )
    return result["answer"]

app = FastAPI()

@app.get("/documentation")
async def serve_docs():
  return FileResponse("docs/doc.html")

with gr.Blocks(fill_height=True) as gr_app:  
    gr.ChatInterface(
        call_graph,
        type="messages",
        title="Promtior.ai RAG Agent",
        fill_height=True
    )

app.mount("/static", StaticFiles(directory=os.path.abspath("./static")), name="static")
app = gr.mount_gradio_app(app, gr_app, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
    print(f"Static files served from: {os.path.abspath('./static')}")

