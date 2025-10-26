import { 
  AgenticFramework, 
  ResearchAgent, 
  AnalysisAgent, 
  WriterAgent, 
  ReviewAgent,
  ResearchAnalysisWorkflow,
  ContentCreationWorkflow
} from './agents.js';
import { ChatOpenAI } from '@langchain/openai';
import { ChatAnthropic } from '@langchain/anthropic';

// ============================================================================
// DEMO CONFIGURATION
// ============================================================================

// Initialize models (using mock models for demo - replace with real API keys)
const createMockModel = (name) => ({
  invoke: async (messages) => ({
    content: `Mock response from ${name}: ${messages[messages.length - 1].content}`
  })
});

const models = {
  openai: createMockModel("OpenAI GPT-4"),
  anthropic: createMockModel("Anthropic Claude")
};

// ============================================================================
// DEMO SCENARIOS
// ============================================================================

class DemoScenarios {
  constructor(framework) {
    this.framework = framework;
  }

  async runMarketResearchDemo() {
    console.log("\n" + "=".repeat(60));
    console.log("🎯 DEMO SCENARIO 1: Market Research Analysis");
    console.log("=".repeat(60));

    const input = "Analyze the current market trends in artificial intelligence and machine learning, focusing on enterprise adoption and competitive landscape";

    console.log(`📝 Input: ${input}\n`);

    try {
      const result = await this.framework.executeWorkflow("research-analysis", input);
      
      console.log("\n📊 RESULTS:");
      console.log("-".repeat(40));
      console.log("Research Phase:", result.research?.output || "Completed");
      console.log("Analysis Phase:", result.analysis?.output || "Completed");
      console.log("Review Phase:", result.review?.output || "Completed");
      
      return result;
    } catch (error) {
      console.error("❌ Error in market research demo:", error.message);
      return null;
    }
  }

  async runContentCreationDemo() {
    console.log("\n" + "=".repeat(60));
    console.log("✍️ DEMO SCENARIO 2: Content Creation Pipeline");
    console.log("=".repeat(60));

    const input = "Create a comprehensive report on the future of quantum computing, including technical developments, market opportunities, and strategic recommendations";

    console.log(`📝 Input: ${input}\n`);

    try {
      const result = await this.framework.executeWorkflow("content-creation", input);
      
      console.log("\n📊 RESULTS:");
      console.log("-".repeat(40));
      console.log("Research Phase:", result.research?.output || "Completed");
      console.log("Analysis Phase:", result.analysis?.output || "Completed");
      console.log("Writing Phase:", result.writing?.output || "Completed");
      console.log("Review Phase:", result.review?.output || "Completed");
      
      return result;
    } catch (error) {
      console.error("❌ Error in content creation demo:", error.message);
      return null;
    }
  }

  async runDataAnalysisDemo() {
    console.log("\n" + "=".repeat(60));
    console.log("📈 DEMO SCENARIO 3: Data Analysis Workflow");
    console.log("=".repeat(60));

    const input = "Analyze customer behavior data to identify patterns, trends, and opportunities for improving user engagement and retention";

    console.log(`📝 Input: ${input}\n`);

    try {
      const result = await this.framework.executeWorkflow("research-analysis", input);
      
      console.log("\n📊 RESULTS:");
      console.log("-".repeat(40));
      console.log("Research Phase:", result.research?.output || "Completed");
      console.log("Analysis Phase:", result.analysis?.output || "Completed");
      console.log("Review Phase:", result.review?.output || "Completed");
      
      return result;
    } catch (error) {
      console.error("❌ Error in data analysis demo:", error.message);
      return null;
    }
  }

  async runInteractiveDemo() {
    console.log("\n" + "=".repeat(60));
    console.log("🤖 INTERACTIVE DEMO: Multi-Agent Collaboration");
    console.log("=".repeat(60));

    const scenarios = [
      "Research the latest developments in edge computing",
      "Analyze the impact of 5G on IoT applications",
      "Create a technical white paper on blockchain scalability",
      "Evaluate the competitive landscape in cloud computing"
    ];

    for (let i = 0; i < scenarios.length; i++) {
      console.log(`\n🔄 Scenario ${i + 1}: ${scenarios[i]}`);
      console.log("-".repeat(50));
      
      try {
        const result = await this.framework.executeWorkflow("research-analysis", scenarios[i]);
        console.log(`✅ Completed scenario ${i + 1}`);
      } catch (error) {
        console.error(`❌ Error in scenario ${i + 1}:`, error.message);
      }
    }
  }
}

// ============================================================================
// MONITORING AND ANALYTICS
// ============================================================================

class FrameworkMonitor {
  constructor(framework) {
    this.framework = framework;
    this.metrics = {
      totalExecutions: 0,
      successfulExecutions: 0,
      failedExecutions: 0,
      averageExecutionTime: 0,
      agentUtilization: {}
    };
  }

  startMonitoring() {
    console.log("📊 Starting framework monitoring...");
    this.startTime = Date.now();
  }

  stopMonitoring() {
    const endTime = Date.now();
    const totalTime = endTime - this.startTime;
    
    console.log("\n📈 FRAMEWORK METRICS:");
    console.log("=".repeat(40));
    console.log(`Total Execution Time: ${totalTime}ms`);
    console.log(`Total Workflows: ${this.framework.getHistory().length}`);
    console.log(`Registered Agents: ${this.framework.agents.size}`);
    console.log(`Available Workflows: ${this.framework.workflows.size}`);
    
    // Agent utilization
    console.log("\n🤖 Agent Utilization:");
    this.framework.agents.forEach((agent, name) => {
      console.log(`  ${name}: Active`);
    });
  }

  logExecution(workflowName, duration, success) {
    this.metrics.totalExecutions++;
    if (success) {
      this.metrics.successfulExecutions++;
    } else {
      this.metrics.failedExecutions++;
    }
    
    console.log(`⏱️ ${workflowName}: ${duration}ms (${success ? '✅' : '❌'})`);
  }
}

// ============================================================================
// MAIN DEMO EXECUTION
// ============================================================================

async function runDemo() {
  console.log("🚀 Starting LangGraph Agentic Framework Demo");
  console.log("=".repeat(60));

  // Initialize framework
  const framework = new AgenticFramework();
  const monitor = new FrameworkMonitor(framework);

  // Register agents
  console.log("\n🔧 Initializing Agents...");
  framework.registerAgent(new ResearchAgent(models.openai));
  framework.registerAgent(new AnalysisAgent(models.anthropic));
  framework.registerAgent(new WriterAgent(models.openai));
  framework.registerAgent(new ReviewAgent(models.anthropic));

  // Create workflows
  console.log("\n🔄 Setting up Workflows...");
  framework.createWorkflow("research-analysis", new ResearchAnalysisWorkflow(framework));
  framework.createWorkflow("content-creation", new ContentCreationWorkflow(framework));

  // Start monitoring
  monitor.startMonitoring();

  // Run demo scenarios
  const demos = new DemoScenarios(framework);
  
  try {
    await demos.runMarketResearchDemo();
    await demos.runContentCreationDemo();
    await demos.runDataAnalysisDemo();
    await demos.runInteractiveDemo();
  } catch (error) {
    console.error("❌ Demo execution error:", error);
  }

  // Stop monitoring and show results
  monitor.stopMonitoring();

  // Show framework state
  console.log("\n📋 FRAMEWORK STATE:");
  console.log("=".repeat(40));
  console.log("State:", JSON.stringify(framework.getState(), null, 2));
  
  console.log("\n📚 EXECUTION HISTORY:");
  console.log("=".repeat(40));
  framework.getHistory().forEach((entry, index) => {
    console.log(`${index + 1}. ${entry.workflow} - ${entry.timestamp}`);
  });

  console.log("\n🎉 Demo completed successfully!");
  console.log("=".repeat(60));
}

// ============================================================================
// ERROR HANDLING AND UTILITIES
// ============================================================================

class ErrorHandler {
  static handleAgentError(agentName, error) {
    console.error(`❌ Agent ${agentName} error:`, error.message);
    return {
      agent: agentName,
      error: error.message,
      timestamp: new Date().toISOString(),
      recovered: false
    };
  }

  static handleWorkflowError(workflowName, error) {
    console.error(`❌ Workflow ${workflowName} error:`, error.message);
    return {
      workflow: workflowName,
      error: error.message,
      timestamp: new Date().toISOString(),
      recovered: false
    };
  }

  static async retryOperation(operation, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
      try {
        return await operation();
      } catch (error) {
        if (i === maxRetries - 1) throw error;
        console.log(`🔄 Retry ${i + 1}/${maxRetries}...`);
        await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
      }
    }
  }
}

// ============================================================================
// EXPORT FOR TESTING
// ============================================================================

export {
  DemoScenarios,
  FrameworkMonitor,
  ErrorHandler,
  runDemo
};

// Run demo if this file is executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
  runDemo().catch(console.error);
}
