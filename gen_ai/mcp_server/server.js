#!/usr/bin/env node

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import { z } from 'zod';

// Simple MCP Server Demo
class SimpleMCPServer {
  constructor() {
    this.server = new Server(
      {
        name: 'simple-mcp-demo',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupHandlers();
  }

  setupHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [
          {
            name: 'calculate',
            description: 'Perform basic mathematical calculations',
            inputSchema: {
              type: 'object',
              properties: {
                expression: {
                  type: 'string',
                  description: 'Mathematical expression to evaluate (e.g., "2 + 3 * 4")',
                },
              },
              required: ['expression'],
            },
          },
          {
            name: 'get_current_time',
            description: 'Get the current date and time',
            inputSchema: {
              type: 'object',
              properties: {},
            },
          },
          {
            name: 'echo',
            description: 'Echo back the input message',
            inputSchema: {
              type: 'object',
              properties: {
                message: {
                  type: 'string',
                  description: 'Message to echo back',
                },
              },
              required: ['message'],
            },
          },
          {
            name: 'generate_random_number',
            description: 'Generate a random number within a specified range',
            inputSchema: {
              type: 'object',
              properties: {
                min: {
                  type: 'number',
                  description: 'Minimum value (default: 0)',
                  default: 0,
                },
                max: {
                  type: 'number',
                  description: 'Maximum value (default: 100)',
                  default: 100,
                },
              },
            },
          },
        ],
      };
    });

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      try {
        switch (name) {
          case 'calculate':
            return await this.handleCalculate(args);
          case 'get_current_time':
            return await this.handleGetCurrentTime();
          case 'echo':
            return await this.handleEcho(args);
          case 'generate_random_number':
            return await this.handleGenerateRandomNumber(args);
          default:
            throw new Error(`Unknown tool: ${name}`);
        }
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Error: ${error.message}`,
            },
          ],
          isError: true,
        };
      }
    });
  }

  async handleCalculate(args) {
    const { expression } = args;
    
    // Simple expression evaluator (for demo purposes)
    // In production, you'd want more robust expression parsing
    try {
      // Basic safety check - only allow numbers, operators, and parentheses
      if (!/^[0-9+\-*/().\s]+$/.test(expression)) {
        throw new Error('Invalid characters in expression');
      }
      
      const result = Function(`"use strict"; return (${expression})`)();
      
      return {
        content: [
          {
            type: 'text',
            text: `Calculation: ${expression} = ${result}`,
          },
        ],
      };
    } catch (error) {
      throw new Error(`Invalid expression: ${error.message}`);
    }
  }

  async handleGetCurrentTime() {
    const now = new Date();
    return {
      content: [
        {
          type: 'text',
          text: `Current time: ${now.toISOString()}\nFormatted: ${now.toLocaleString()}`,
        },
      ],
    };
  }

  async handleEcho(args) {
    const { message } = args;
    return {
      content: [
        {
          type: 'text',
          text: `Echo: ${message}`,
        },
      ],
    };
  }

  async handleGenerateRandomNumber(args) {
    const { min = 0, max = 100 } = args;
    
    if (min >= max) {
      throw new Error('Minimum value must be less than maximum value');
    }
    
    const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;
    
    return {
      content: [
        {
          type: 'text',
          text: `Random number between ${min} and ${max}: ${randomNumber}`,
        },
      ],
    };
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Simple MCP Server running on stdio');
  }
}

// Start the server
const server = new SimpleMCPServer();
server.run().catch(console.error);
