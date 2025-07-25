import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from mcp_use import MCPAgent, MCPClient

# Optional: Load API keys from .env
load_dotenv()

# MCP server config: the "everything" bash server
mcp_shell_config = {
    "mcpServers": {
        "shell": {
            "command": "docker",
            "args": [
                "run", "--rm", "-i",
                "-e", "MCP_SHELL_LOG_LEVEL=info",
                "-e", "MCP_SHELL_SEC_CONFIG_FILE=/app/security.yaml",
                "-v", "/home/mehrdad/Main/ODU/ODU Research/Cyber/MCP/mcp-shell/security.yaml:/app/security.yaml:ro",
                "mcp-shell:latest"
            ]
        }
    }
}


async def main():
    # Initialize MCP client
    client = MCPClient(config=mcp_shell_config)

    # Choose your LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # Create an agent
    agent = MCPAgent(llm=llm, client=client, max_steps=10, system_prompt="""
You are a cybersecurity assistant that uses tools to solve Capture The Flag (CTF) web challenges.
You must prefer running shell commands over guessing.
Always explain the reasoning behind the tools and commands you use.
If a command fails, try an alternative or describe what went wrong.
""")

    # Run a task (e.g., use curl or gobuster)
    # result = await agent.run(
    #     """execute the command 'curl http://titan.picoctf.net:63704/' and tell me what you see. the flag might
    #     be encoded so if you find sth encoded, decode it to see it is the flag or not"""
    # )
    result = await  agent.run("""execute the command 'curl http://titan.picoctf.net:61003/' and tell me what you see.
     the flag might be encoded so if you find sth encoded, decode it to see it is the flag or not
     find the associated pages to see if there is a flag there or there is an encoding there""")

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
