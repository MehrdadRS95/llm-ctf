import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from mcp_use import MCPAgent, MCPClient

# Optional: Load API keys from .env
load_dotenv()

# MCP server config: the "everything" bash server
everything_server = {
    "mcpServers": {
        "everything": {
            "type": "external",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-everything"]
        }
    }
}


async def main():
    # Initialize MCP client
    client = MCPClient(config=everything_server)

    # Choose your LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # Create an agent
    agent = MCPAgent(llm=llm, client=client, max_steps=10)

    # Run a task (e.g., use curl or gobuster)
    # result = await agent.run(
    #     """execute the command 'curl http://titan.picoctf.net:63704/' and tell me what you see. the flag might
    #     be encoded so if you find sth encoded, decode it to see it is the flag or not"""
    # )
    result = await  agent.run("""search the web to see what are the best fastfood restaurants in Norfolk,
     give their google ratings""")

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
