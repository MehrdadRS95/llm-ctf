import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from mcp_use import MCPAgent, MCPClient

# Configuration to use the "everything" server via npx
everything_server = {
    "mcpServers": {
        "everything": {
            "type": "external",  # Optional but clearer
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-everything"]
        }
    }
}


async def main():
    load_dotenv()

    # Start the MCP client
    client = MCPClient(config=everything_server)

    # Use GPT-4o as the language model
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # Create the MCPAgent with access to tools
    agent = MCPAgent(llm=llm, client=client, max_steps=10)

    # Ask the agent to use curl on the GitHub page
    result = await agent.run(
        "Use curl to fetch the page https://github.com/mcp-use/mcp-use/blob/main/examples/mcp_everything.py",
    )

    print(f"\nResult:\n{result}")


if __name__ == "__main__":
    asyncio.run(main())
