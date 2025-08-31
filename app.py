from typing import Any, Dict
from fastapi import FastAPI
from langserve import add_routes
from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

app = FastAPI(
    title="Poem Generator API",
    version="1.0.0",
)

class PoemInput(BaseModel):
    topic: str = Field(..., description="The topic to write a poem about")

class PoemOutput(BaseModel):
    poem: str = Field(..., description="The generated poem")

# Create the poem generation chain
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a poetic assistant. Write a beautiful poem."),
    ("user", "Write a poem about {topic}")
])

model = OllamaLLM(model="llama3.2:1b")

chain = (
    RunnableParallel({
        "topic": lambda x: x["topic"]
    })
    | prompt
    | model
    | RunnableLambda(lambda x: {"poem": x})
)

# Add routes with explicit input/output types
add_routes(
    app,
    chain,
    path="/poem",
    input_type=PoemInput,
    output_type=PoemOutput,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
