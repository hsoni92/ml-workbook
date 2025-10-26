#!/usr/bin/env node

import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

// Get the current directory
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Simple MCP Client Demo using direct JSON-RPC communication
class SimpleMCPClient {
  constructor() {
    this.serverProcess = null;
    this.requestId = 0;
  }

  async connect() {
    try {
      console.log('🚀 Starting MCP server...');
      
      // Spawn the MCP server as a child process
      this.serverProcess = spawn('node', [join(__dirname, 'server.js')], {
        stdio: ['pipe', 'pipe', 'pipe'],
      });

      // Handle server process errors
      this.serverProcess.on('error', (error) => {
        console.error('❌ Server process error:', error.message);
      });

      this.serverProcess.stderr.on('data', (data) => {
        console.log('Server:', data.toString().trim());
      });

      // Wait a moment for the server to start
      await new Promise(resolve => setTimeout(resolve, 500));

      console.log('✅ MCP server started');
    } catch (error) {
      console.error('❌ Connection failed:', error.message);
      throw error;
    }
  }

  async sendRequest(method, params = {}) {
    return new Promise((resolve, reject) => {
      const request = {
        jsonrpc: '2.0',
        id: ++this.requestId,
        method: method,
        params: params
      };

      let responseData = '';
      
      const onData = (data) => {
        responseData += data.toString();
        
        // Try to parse complete JSON responses
        const lines = responseData.split('\n');
        for (const line of lines) {
          if (line.trim()) {
            try {
              const response = JSON.parse(line);
              if (response.id === request.id) {
                this.serverProcess.stdout.removeListener('data', onData);
                resolve(response);
                return;
              }
            } catch (e) {
              // Not a complete JSON response yet
            }
          }
        }
      };

      this.serverProcess.stdout.on('data', onData);
      
      // Send the request
      this.serverProcess.stdin.write(JSON.stringify(request) + '\n');
      
      // Timeout after 5 seconds
      setTimeout(() => {
        this.serverProcess.stdout.removeListener('data', onData);
        reject(new Error('Request timeout'));
      }, 5000);
    });
  }

  async listTools() {
    try {
      const response = await this.sendRequest('tools/list');
      
      console.log('\n📋 Available Tools:');
      response.result.tools.forEach((tool, index) => {
        console.log(`${index + 1}. ${tool.name}: ${tool.description}`);
      });
      
      return response.result.tools;
    } catch (error) {
      console.error('❌ Error listing tools:', error.message);
      return [];
    }
  }

  async callTool(toolName, args = {}) {
    try {
      const response = await this.sendRequest('tools/call', {
        name: toolName,
        arguments: args
      });

      console.log(`\n🔧 Tool: ${toolName}`);
      console.log(`📥 Input: ${JSON.stringify(args)}`);
      console.log(`📤 Output: ${response.result.content[0].text}`);
      
      return response.result;
    } catch (error) {
      console.error(`❌ Error calling tool ${toolName}:`, error.message);
      return null;
    }
  }

  async runDemo() {
    try {
      await this.connect();
      
      console.log('\n🚀 Starting MCP Demo...\n');
      
      // List available tools
      await this.listTools();
      
      // Demo 1: Calculate
      console.log('\n' + '='.repeat(50));
      console.log('DEMO 1: Mathematical Calculation');
      console.log('='.repeat(50));
      await this.callTool('calculate', { expression: '2 + 3 * 4' });
      await this.callTool('calculate', { expression: '(10 + 5) / 3' });
      
      // Demo 2: Get current time
      console.log('\n' + '='.repeat(50));
      console.log('DEMO 2: Get Current Time');
      console.log('='.repeat(50));
      await this.callTool('get_current_time');
      
      // Demo 3: Echo
      console.log('\n' + '='.repeat(50));
      console.log('DEMO 3: Echo Message');
      console.log('='.repeat(50));
      await this.callTool('echo', { message: 'Hello from MCP!' });
      await this.callTool('echo', { message: 'This is a simple demo' });
      
      // Demo 4: Random number generation
      console.log('\n' + '='.repeat(50));
      console.log('DEMO 4: Random Number Generation');
      console.log('='.repeat(50));
      await this.callTool('generate_random_number', { min: 1, max: 10 });
      await this.callTool('generate_random_number', { min: 50, max: 100 });
      await this.callTool('generate_random_number'); // Use defaults
      
      console.log('\n✅ Demo completed successfully!');
      
    } catch (error) {
      console.error('❌ Demo failed:', error.message);
    } finally {
      if (this.serverProcess) {
        this.serverProcess.kill();
      }
    }
  }
}

// Run the demo
const demo = new SimpleMCPClient();
demo.runDemo().catch(console.error);