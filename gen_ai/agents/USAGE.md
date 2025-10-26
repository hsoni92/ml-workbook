# LangGraph Agentic Framework Demo - Usage Guide

## 🚀 Quick Start

### 1. Installation
```bash
cd gen_ai
npm install
```

### 2. Environment Setup
Copy the environment template and add your API keys:
```bash
cp env.example .env
# Edit .env with your actual API keys
```

### 3. Run Demos

#### Basic Demo
```bash
npm run demo
```

#### Comprehensive Demo
```bash
node comprehensive-demo.js
```

#### Test Suite
```bash
npm test
```

## 📁 File Structure

```
gen_ai/
├── agents.js              # Core framework and agents
├── demo.js                # Basic demo scenarios
├── comprehensive-demo.js   # Advanced business intelligence demo
├── test-agents.js         # Test suite and benchmarks
├── package.json           # Dependencies and scripts
├── README.md              # Framework documentation
└── env.example            # Environment configuration template
```

## 🤖 Available Agents

### ResearchAgent
- **Purpose**: Gathers information from various sources
- **Tools**: Web search, data analysis
- **Use Cases**: Market research, competitive analysis

### AnalysisAgent
- **Purpose**: Processes data and generates insights
- **Tools**: Statistical analysis, insight generation
- **Use Cases**: Data interpretation, pattern recognition

### WriterAgent
- **Purpose**: Creates structured content
- **Tools**: Content generation, formatting
- **Use Cases**: Report writing, documentation

### ReviewAgent
- **Purpose**: Quality assurance and validation
- **Tools**: Quality checks, data validation
- **Use Cases**: Content review, output validation

### BusinessAnalystAgent (Advanced)
- **Purpose**: Business intelligence and financial analysis
- **Tools**: Financial analysis, risk assessment, ROI calculation
- **Use Cases**: Strategic planning, investment analysis

## 🔄 Available Workflows

### Research Analysis Workflow
- Research → Analysis → Review
- **Use Case**: Market research and data analysis

### Content Creation Workflow
- Research → Analysis → Writing → Review
- **Use Case**: Content generation and documentation

### Business Intelligence Workflow
- Market Research → Competitor Analysis → Trend Analysis → Strategic Recommendations → Executive Summary → Quality Review
- **Use Case**: Comprehensive business intelligence

## 💡 Usage Examples

### Basic Agent Usage
```javascript
import { AgenticFramework, ResearchAgent } from './agents.js';

const framework = new AgenticFramework();
const researchAgent = new ResearchAgent(model);
framework.registerAgent(researchAgent);

const result = await researchAgent.process("Research AI trends");
console.log(result.output);
```

### Workflow Execution
```javascript
import { ResearchAnalysisWorkflow } from './agents.js';

const workflow = new ResearchAnalysisWorkflow(framework);
framework.createWorkflow("my-workflow", workflow);

const result = await framework.executeWorkflow("my-workflow", "Analyze market trends");
```

### Custom Agent Creation
```javascript
import { BaseAgent } from './agents.js';

class CustomAgent extends BaseAgent {
  constructor(model) {
    super("CustomAgent", "description", model);
    this.addTool(this.createCustomTool());
  }
  
  createCustomTool() {
    return tool(
      async ({ input }) => {
        return `Processed: ${input}`;
      },
      {
        name: "custom_tool",
        description: "Custom tool description",
        schema: z.object({
          input: z.string().describe("Input parameter")
        })
      }
    );
  }
}
```

## 🔧 Configuration

### Model Setup
Replace mock models with real API models:

```javascript
// OpenAI
const openaiModel = new ChatOpenAI({
  model: "gpt-4",
  apiKey: process.env.OPENAI_API_KEY
});

// Anthropic
const anthropicModel = new ChatAnthropic({
  model: "claude-3-sonnet-20240229",
  apiKey: process.env.ANTHROPIC_API_KEY
});
```

### Custom Workflows
Create custom workflows by extending the base pattern:

```javascript
class CustomWorkflow {
  constructor(framework) {
    this.framework = framework;
    this.graph = this.createGraph();
  }
  
  createGraph() {
    const graph = new StateGraph({
      channels: {
        input: { value: (x) => x },
        step1: { value: (x) => x },
        step2: { value: (x) => x },
        output: { value: (x) => x }
      }
    });
    
    // Add nodes and edges
    graph.addNode("step1", async (state) => {
      // Your logic here
    });
    
    graph.addEdge(START, "step1");
    graph.addEdge("step1", END);
    
    return graph.compile();
  }
  
  async execute(input, state) {
    return await this.graph.invoke({ input });
  }
}
```

## 📊 Monitoring and Debugging

### Framework Monitoring
```javascript
const monitor = new FrameworkMonitor(framework);
monitor.startMonitoring();

// Your workflow executions

monitor.stopMonitoring();
```

### Error Handling
```javascript
try {
  const result = await framework.executeWorkflow("workflow-name", input);
} catch (error) {
  console.error("Workflow error:", error.message);
  // Implement retry logic or fallback
}
```

## 🧪 Testing

### Run All Tests
```bash
npm test
```

### Individual Test Categories
```javascript
import { AgenticFrameworkTests } from './test-agents.js';

const testSuite = new AgenticFrameworkTests();
await testSuite.testAgentRegistration();
await testSuite.testWorkflowExecution();
```

### Performance Benchmarks
```javascript
import { PerformanceBenchmarks } from './test-agents.js';

const benchmarks = new PerformanceBenchmarks();
await benchmarks.benchmarkAgentPerformance();
await benchmarks.benchmarkWorkflowPerformance();
```

## 🎯 Best Practices

1. **Agent Design**: Keep agents focused on specific tasks
2. **Tool Creation**: Make tools reusable and well-documented
3. **Error Handling**: Implement robust error recovery
4. **State Management**: Use framework state for persistence
5. **Monitoring**: Track agent performance and workflow metrics
6. **Testing**: Write comprehensive tests for all components

## 🔮 Extending the Framework

### Adding New Agent Types
1. Extend `BaseAgent` class
2. Implement required methods
3. Add custom tools
4. Register with framework

### Creating Custom Workflows
1. Define workflow structure
2. Add nodes for each step
3. Define edges between nodes
4. Implement execution logic

### Integrating External Services
1. Create tools for external APIs
2. Add authentication handling
3. Implement rate limiting
4. Add error recovery

## 📞 Support

For questions or issues:
1. Check the test suite for examples
2. Review the comprehensive demo
3. Examine the core framework code
4. Create custom agents and workflows

## 🎉 Demo Scenarios

The framework includes several demo scenarios:

1. **Market Research**: Analyze industry trends and competitors
2. **Content Creation**: Generate comprehensive reports
3. **Data Analysis**: Process and interpret datasets
4. **Business Intelligence**: Strategic analysis and recommendations
5. **Multi-Agent Collaboration**: Coordinated workflows

Each demo showcases different aspects of the framework and can be used as templates for your own implementations.
