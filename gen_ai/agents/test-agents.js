import { 
  AgenticFramework, 
  ResearchAgent, 
  AnalysisAgent, 
  WriterAgent, 
  ReviewAgent
} from './agents.js';

// ============================================================================
// TEST SUITE FOR AGENTIC FRAMEWORK
// ============================================================================

class AgenticFrameworkTests {
  constructor() {
    this.framework = new AgenticFramework();
    this.testResults = [];
    this.passedTests = 0;
    this.failedTests = 0;
  }

  // Mock model for testing
  createMockModel(name) {
    return {
      invoke: async (messages) => ({
        content: `Test response from ${name}: ${messages[messages.length - 1].content}`
      })
    };
  }

  async runTest(testName, testFunction) {
    console.log(`🧪 Running test: ${testName}`);
    try {
      const result = await testFunction();
      this.testResults.push({ name: testName, status: 'PASSED', result });
      this.passedTests++;
      console.log(`✅ ${testName}: PASSED`);
      return result;
    } catch (error) {
      this.testResults.push({ name: testName, status: 'FAILED', error: error.message });
      this.failedTests++;
      console.log(`❌ ${testName}: FAILED - ${error.message}`);
      return null;
    }
  }

  async testAgentRegistration() {
    const mockModel = this.createMockModel("TestModel");
    
    // Test registering different types of agents
    const researchAgent = new ResearchAgent(mockModel);
    const analysisAgent = new AnalysisAgent(mockModel);
    const writerAgent = new WriterAgent(mockModel);
    const reviewAgent = new ReviewAgent(mockModel);

    this.framework.registerAgent(researchAgent);
    this.framework.registerAgent(analysisAgent);
    this.framework.registerAgent(writerAgent);
    this.framework.registerAgent(reviewAgent);

    // Verify agents are registered
    if (this.framework.agents.size !== 4) {
      throw new Error(`Expected 4 agents, got ${this.framework.agents.size}`);
    }

    // Test agent retrieval
    const retrievedAgent = this.framework.getAgent("ResearchAgent");
    if (!retrievedAgent || retrievedAgent.name !== "ResearchAgent") {
      throw new Error("Failed to retrieve registered agent");
    }

    return { registeredAgents: this.framework.agents.size };
  }

  async testAgentProcessing() {
    const mockModel = this.createMockModel("TestModel");
    const researchAgent = new ResearchAgent(mockModel);

    const testInput = "Test research query about artificial intelligence";
    const result = await researchAgent.process(testInput);

    if (!result.agent || !result.output || !result.timestamp) {
      throw new Error("Agent processing result missing required fields");
    }

    if (result.success !== true) {
      throw new Error("Agent processing should succeed with mock model");
    }

    return result;
  }

  async testToolExecution() {
    const mockModel = this.createMockModel("TestModel");
    const researchAgent = new ResearchAgent(mockModel);

    // Test web search tool
    const webSearchTool = researchAgent.tools.find(tool => tool.name === "web_search");
    if (!webSearchTool) {
      throw new Error("Web search tool not found");
    }

    const searchResult = await webSearchTool.invoke({ query: "test query", sources: 2 });
    if (!searchResult) {
      throw new Error("Web search tool failed to return result");
    }

    // Test data analysis tool
    const dataAnalysisTool = researchAgent.tools.find(tool => tool.name === "analyze_data");
    if (!dataAnalysisTool) {
      throw new Error("Data analysis tool not found");
    }

    const analysisResult = await dataAnalysisTool.invoke({ 
      data: "test data", 
      analysisType: "trend" 
    });
    if (!analysisResult) {
      throw new Error("Data analysis tool failed to return result");
    }

    return { searchResult, analysisResult };
  }

  async testWorkflowCreation() {
    const mockModel = this.createMockModel("TestModel");
    
    // Register agents
    this.framework.registerAgent(new ResearchAgent(mockModel));
    this.framework.registerAgent(new AnalysisAgent(mockModel));
    this.framework.registerAgent(new ReviewAgent(mockModel));

    // Create workflow
    const workflow = {
      execute: async (input, state) => {
        return { 
          research: { output: "Research completed" },
          analysis: { output: "Analysis completed" },
          review: { output: "Review completed" }
        };
      }
    };

    this.framework.createWorkflow("test-workflow", workflow);

    if (this.framework.workflows.size !== 1) {
      throw new Error("Workflow not created successfully");
    }

    return { workflowsCreated: this.framework.workflows.size };
  }

  async testWorkflowExecution() {
    const mockModel = this.createMockModel("TestModel");
    
    // Register agents
    this.framework.registerAgent(new ResearchAgent(mockModel));
    this.framework.registerAgent(new AnalysisAgent(mockModel));
    this.framework.registerAgent(new ReviewAgent(mockModel));

    // Create and register workflow
    const workflow = {
      execute: async (input, state) => {
        return { 
          research: { output: `Research for: ${input}` },
          analysis: { output: `Analysis of: ${input}` },
          review: { output: `Review of: ${input}` }
        };
      }
    };

    this.framework.createWorkflow("test-execution", workflow);

    // Execute workflow
    const testInput = "Test workflow execution";
    const result = await this.framework.executeWorkflow("test-execution", testInput);

    if (!result.research || !result.analysis || !result.review) {
      throw new Error("Workflow execution missing expected outputs");
    }

    return result;
  }

  async testStateManagement() {
    // Test initial state
    const initialState = this.framework.getState();
    if (initialState === undefined) {
      throw new Error("Initial state should be defined");
    }

    // Test state modification
    this.framework.state.testProperty = "test value";
    const modifiedState = this.framework.getState();
    if (modifiedState.testProperty !== "test value") {
      throw new Error("State modification failed");
    }

    return { initialState, modifiedState };
  }

  async testHistoryTracking() {
    const mockModel = this.createMockModel("TestModel");
    
    // Register agents and create workflow
    this.framework.registerAgent(new ResearchAgent(mockModel));
    this.framework.registerAgent(new AnalysisAgent(mockModel));
    this.framework.registerAgent(new ReviewAgent(mockModel));

    const workflow = {
      execute: async (input, state) => ({ result: "test" })
    };

    this.framework.createWorkflow("test-history", workflow);

    // Execute workflow to generate history
    await this.framework.executeWorkflow("test-history", "test input");

    const history = this.framework.getHistory();
    if (history.length === 0) {
      throw new Error("History not being tracked");
    }

    const lastEntry = history[history.length - 1];
    if (!lastEntry.workflow || !lastEntry.timestamp) {
      throw new Error("History entry missing required fields");
    }

    return { historyLength: history.length, lastEntry };
  }

  async testErrorHandling() {
    const mockModel = this.createMockModel("TestModel");
    const researchAgent = new ResearchAgent(mockModel);

    // Test agent error handling
    const errorResult = await researchAgent.process(null);
    if (errorResult.success !== false) {
      throw new Error("Agent should handle errors gracefully");
    }

    if (!errorResult.error) {
      throw new Error("Error result should include error message");
    }

    return errorResult;
  }

  async testMultiAgentCollaboration() {
    const mockModel = this.createMockModel("TestModel");
    
    // Register multiple agents
    const researchAgent = new ResearchAgent(mockModel);
    const analysisAgent = new AnalysisAgent(mockModel);
    const writerAgent = new WriterAgent(mockModel);
    const reviewAgent = new ReviewAgent(mockModel);

    this.framework.registerAgent(researchAgent);
    this.framework.registerAgent(analysisAgent);
    this.framework.registerAgent(writerAgent);
    this.framework.registerAgent(reviewAgent);

    // Test sequential processing
    const testInput = "Multi-agent collaboration test";
    
    const researchResult = await researchAgent.process(testInput);
    const analysisResult = await analysisAgent.process(researchResult.output);
    const writingResult = await writerAgent.process(analysisResult.output);
    const reviewResult = await reviewAgent.process(writingResult.output);

    // Verify all agents processed successfully
    const results = [researchResult, analysisResult, writingResult, reviewResult];
    const failedResults = results.filter(r => !r.success);
    
    if (failedResults.length > 0) {
      throw new Error(`${failedResults.length} agents failed in collaboration test`);
    }

    return { 
      collaborationSuccess: true, 
      agentsProcessed: results.length,
      finalOutput: reviewResult.output
    };
  }

  async runAllTests() {
    console.log("🧪 Starting Agentic Framework Test Suite");
    console.log("=".repeat(50));

    await this.runTest("Agent Registration", () => this.testAgentRegistration());
    await this.runTest("Agent Processing", () => this.testAgentProcessing());
    await this.runTest("Tool Execution", () => this.testToolExecution());
    await this.runTest("Workflow Creation", () => this.testWorkflowCreation());
    await this.runTest("Workflow Execution", () => this.testWorkflowExecution());
    await this.runTest("State Management", () => this.testStateManagement());
    await this.runTest("History Tracking", () => this.testHistoryTracking());
    await this.runTest("Error Handling", () => this.testErrorHandling());
    await this.runTest("Multi-Agent Collaboration", () => this.testMultiAgentCollaboration());

    this.printTestSummary();
  }

  printTestSummary() {
    console.log("\n📊 TEST SUMMARY");
    console.log("=".repeat(50));
    console.log(`Total Tests: ${this.passedTests + this.failedTests}`);
    console.log(`Passed: ${this.passedTests} ✅`);
    console.log(`Failed: ${this.failedTests} ❌`);
    console.log(`Success Rate: ${((this.passedTests / (this.passedTests + this.failedTests)) * 100).toFixed(1)}%`);

    if (this.failedTests > 0) {
      console.log("\n❌ FAILED TESTS:");
      this.testResults
        .filter(test => test.status === 'FAILED')
        .forEach(test => {
          console.log(`  - ${test.name}: ${test.error}`);
        });
    }

    console.log("\n🎉 Test suite completed!");
  }
}

// ============================================================================
// PERFORMANCE BENCHMARKS
// ============================================================================

class PerformanceBenchmarks {
  constructor() {
    this.framework = new AgenticFramework();
    this.benchmarks = [];
  }

  createMockModel(name) {
    return {
      invoke: async (messages) => {
        // Simulate processing time
        await new Promise(resolve => setTimeout(resolve, Math.random() * 100));
        return {
          content: `Benchmark response from ${name}: ${messages[messages.length - 1].content}`
        };
      }
    };
  }

  async benchmarkAgentPerformance() {
    console.log("⚡ Running Agent Performance Benchmarks");
    console.log("-".repeat(40));

    const mockModel = this.createMockModel("BenchmarkModel");
    const researchAgent = new ResearchAgent(mockModel);

    const iterations = 10;
    const times = [];

    for (let i = 0; i < iterations; i++) {
      const startTime = Date.now();
      await researchAgent.process(`Benchmark test ${i}`);
      const endTime = Date.now();
      times.push(endTime - startTime);
    }

    const avgTime = times.reduce((a, b) => a + b, 0) / times.length;
    const minTime = Math.min(...times);
    const maxTime = Math.max(...times);

    console.log(`Average processing time: ${avgTime.toFixed(2)}ms`);
    console.log(`Min processing time: ${minTime}ms`);
    console.log(`Max processing time: ${maxTime}ms`);

    return { avgTime, minTime, maxTime, iterations };
  }

  async benchmarkWorkflowPerformance() {
    console.log("⚡ Running Workflow Performance Benchmarks");
    console.log("-".repeat(40));

    const mockModel = this.createMockModel("BenchmarkModel");
    
    // Register agents
    this.framework.registerAgent(new ResearchAgent(mockModel));
    this.framework.registerAgent(new AnalysisAgent(mockModel));
    this.framework.registerAgent(new ReviewAgent(mockModel));

    // Create workflow
    const workflow = {
      execute: async (input, state) => {
        await new Promise(resolve => setTimeout(resolve, Math.random() * 200));
        return { 
          research: { output: "Benchmark research" },
          analysis: { output: "Benchmark analysis" },
          review: { output: "Benchmark review" }
        };
      }
    };

    this.framework.createWorkflow("benchmark-workflow", workflow);

    const iterations = 5;
    const times = [];

    for (let i = 0; i < iterations; i++) {
      const startTime = Date.now();
      await this.framework.executeWorkflow("benchmark-workflow", `Benchmark ${i}`);
      const endTime = Date.now();
      times.push(endTime - startTime);
    }

    const avgTime = times.reduce((a, b) => a + b, 0) / times.length;
    const minTime = Math.min(...times);
    const maxTime = Math.max(...times);

    console.log(`Average workflow time: ${avgTime.toFixed(2)}ms`);
    console.log(`Min workflow time: ${minTime}ms`);
    console.log(`Max workflow time: ${maxTime}ms`);

    return { avgTime, minTime, maxTime, iterations };
  }

  async runAllBenchmarks() {
    console.log("🚀 Starting Performance Benchmarks");
    console.log("=".repeat(50));

    const agentBenchmark = await this.benchmarkAgentPerformance();
    const workflowBenchmark = await this.benchmarkWorkflowPerformance();

    console.log("\n📈 BENCHMARK SUMMARY");
    console.log("=".repeat(50));
    console.log(`Agent Performance: ${agentBenchmark.avgTime.toFixed(2)}ms avg`);
    console.log(`Workflow Performance: ${workflowBenchmark.avgTime.toFixed(2)}ms avg`);
  }
}

// ============================================================================
// MAIN TEST EXECUTION
// ============================================================================

async function runTests() {
  const testSuite = new AgenticFrameworkTests();
  const benchmarks = new PerformanceBenchmarks();

  await testSuite.runAllTests();
  await benchmarks.runAllBenchmarks();
}

// Export for use in other files
export { AgenticFrameworkTests, PerformanceBenchmarks, runTests };

// Run tests if this file is executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
  runTests().catch(console.error);
}
