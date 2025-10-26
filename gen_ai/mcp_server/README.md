# Simple MCP Server Demo

A demonstration of the Model Context Protocol (MCP) using Node.js. This simple demo shows how to create an MCP server with basic tools and a client to interact with it.

## What is MCP?

The Model Context Protocol (MCP) is a standard for connecting AI assistants to data sources and tools. It enables AI models to access external resources and perform actions through a standardized interface.

## Features

This demo includes a simple MCP server with the following tools:

- **calculate**: Perform basic mathematical calculations
- **get_current_time**: Get the current date and time
- **echo**: Echo back input messages
- **generate_random_number**: Generate random numbers within a specified range

## Installation

1. Navigate to the mcp_server directory:
```bash
cd gen_ai/mcp_server
```

2. Install dependencies:
```bash
npm install
```

## Usage

### Running the Demo

The easiest way to see the MCP server in action is to run the demo client:

```bash
npm run demo
```

This will:
1. Start the MCP server
2. Connect a client to it
3. List available tools
4. Demonstrate each tool with sample inputs

### Manual Server Testing

You can also run the server manually:

```bash
npm start
```

The server runs on stdio and can be connected to by MCP clients.

### Development Mode

For development with auto-restart:

```bash
npm run dev
```

## Demo Output

When you run `npm run demo`, you'll see output like:

```
✅ Connected to MCP server

🚀 Starting MCP Demo...

📋 Available Tools:
1. calculate: Perform basic mathematical calculations
2. get_current_time: Get the current date and time
3. echo: Echo back the input message
4. generate_random_number: Generate a random number within a specified range

==================================================
DEMO 1: Mathematical Calculation
==================================================

🔧 Tool: calculate
📥 Input: {"expression":"2 + 3 * 4"}
📤 Output: Calculation: 2 + 3 * 4 = 14

🔧 Tool: calculate
📥 Input: {"expression":"(10 + 5) / 3"}
📤 Output: Calculation: (10 + 5) / 3 = 5

==================================================
DEMO 2: Get Current Time
==================================================

🔧 Tool: get_current_time
📥 Input: {}
📤 Output: Current time: 2024-01-15T10:30:45.123Z
Formatted: 1/15/2024, 10:30:45 AM

==================================================
DEMO 3: Echo Message
==================================================

🔧 Tool: echo
📥 Input: {"message":"Hello from MCP!"}
📤 Output: Echo: Hello from MCP!

==================================================
DEMO 4: Random Number Generation
==================================================

🔧 Tool: generate_random_number
📥 Input: {"min":1,"max":10}
📤 Output: Random number between 1 and 10: 7

✅ Demo completed successfully!
```

## Code Structure

- `server.js`: The MCP server implementation with tool definitions and handlers
- `demo-client.js`: A client that demonstrates how to interact with the MCP server
- `package.json`: Project configuration and dependencies

## Extending the Demo

To add new tools to the server:

1. Add the tool definition in the `ListToolsRequestSchema` handler
2. Add a case in the `CallToolRequestSchema` handler
3. Implement the tool logic in a new handler method

Example:
```javascript
// In setupHandlers(), add to tools array:
{
  name: 'my_new_tool',
  description: 'Description of what this tool does',
  inputSchema: {
    type: 'object',
    properties: {
      param1: {
        type: 'string',
        description: 'Description of param1',
      },
    },
    required: ['param1'],
  },
}

// In CallToolRequestSchema handler, add case:
case 'my_new_tool':
  return await this.handleMyNewTool(args);

// Add handler method:
async handleMyNewTool(args) {
  const { param1 } = args;
  return {
    content: [
      {
        type: 'text',
        text: `Tool result: ${param1}`,
      },
    ],
  };
}
```

## Learn More

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP SDK for JavaScript](https://github.com/modelcontextprotocol/sdk/tree/main/typescript)
- [MCP Examples](https://github.com/modelcontextprotocol/examples)
