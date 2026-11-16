from mcp.server.fastmcp import FastMCP

## Server Name
mcp=FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """_summary_
    Add to numbers
    """
    return a+b


@mcp.tool()
def multiple(a:int, b:int)->int:
    """Multiple two numbers"""
    return a*b

## the transport = "stdio" argument tells the server to:

# User standard input/output (stdin and stdout) to receive and respond to toll function calls

if __name__ == "__main__":
    mcp.run(transport="stdio")


