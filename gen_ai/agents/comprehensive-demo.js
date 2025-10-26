import {
  AgenticFramework,
  BaseAgent,
  ResearchAgent,
  AnalysisAgent,
  WriterAgent,
  ReviewAgent,
  ResearchAnalysisWorkflow,
  ContentCreationWorkflow
} from './agents.js';
import { ChatOpenAI } from '@langchain/openai';
import { ChatAnthropic } from '@langchain/anthropic';
import { tool } from '@langchain/core/tools';
import { z } from 'zod';

// ============================================================================
// REAL-WORLD EXAMPLE: BUSINESS INTELLIGENCE WORKFLOW
// ============================================================================

class BusinessIntelligenceWorkflow {
  constructor(framework) {
    this.framework = framework;
    this.graph = this.createGraph();
  }

  createGraph() {
    const graph = new StateGraph({
      channels: {
        input: { value: (x) => x },
        marketResearch: { value: (x) => x },
        competitorAnalysis: { value: (x) => x },
        trendAnalysis: { value: (x) => x },
        strategicRecommendations: { value: (x) => x },
        executiveSummary: { value: (x) => x },
        output: { value: (x) => x }
      }
    });

    // Add nodes for each step
    graph.addNode("marketResearch", async (state) => {
      console.log("🔍 Market Research Agent: Analyzing market conditions...");
      const researchAgent = this.framework.getAgent("ResearchAgent");
      const result = await researchAgent.process(`Market research for: ${state.input}`);
      return { marketResearch: result };
    });

    graph.addNode("competitorAnalysis", async (state) => {
      console.log("🏢 Competitor Analysis Agent: Evaluating competitive landscape...");
      const analysisAgent = this.framework.getAgent("AnalysisAgent");
      const result = await analysisAgent.process(`Competitor analysis based on: ${state.marketResearch.output}`);
      return { competitorAnalysis: result };
    });

    graph.addNode("trendAnalysis", async (state) => {
      console.log("📈 Trend Analysis Agent: Identifying market trends...");
      const analysisAgent = this.framework.getAgent("AnalysisAgent");
      const result = await analysisAgent.process(`Trend analysis for: ${state.input}`);
      return { trendAnalysis: result };
    });

    graph.addNode("strategicRecommendations", async (state) => {
      console.log("💡 Strategic Recommendations Agent: Generating strategic insights...");
      const writerAgent = this.framework.getAgent("WriterAgent");
      const context = `${state.marketResearch.output}\n${state.competitorAnalysis.output}\n${state.trendAnalysis.output}`;
      const result = await writerAgent.process(`Strategic recommendations based on: ${context}`);
      return { strategicRecommendations: result };
    });

    graph.addNode("executiveSummary", async (state) => {
      console.log("📋 Executive Summary Agent: Creating executive summary...");
      const writerAgent = this.framework.getAgent("WriterAgent");
      const context = `${state.strategicRecommendations.output}`;
      const result = await writerAgent.process(`Executive summary of: ${context}`);
      return { executiveSummary: result };
    });

    graph.addNode("qualityReview", async (state) => {
      console.log("✅ Quality Review Agent: Final quality check...");
      const reviewAgent = this.framework.getAgent("ReviewAgent");
      const result = await reviewAgent.process(`Review business intelligence report: ${state.executiveSummary.output}`);
      return { qualityReview: result };
    });

    // Define workflow edges
    graph.addEdge(START, "marketResearch");
    graph.addEdge("marketResearch", "competitorAnalysis");
    graph.addEdge("marketResearch", "trendAnalysis");
    graph.addEdge("competitorAnalysis", "strategicRecommendations");
    graph.addEdge("trendAnalysis", "strategicRecommendations");
    graph.addEdge("strategicRecommendations", "executiveSummary");
    graph.addEdge("executiveSummary", "qualityReview");
    graph.addEdge("qualityReview", END);

    return graph.compile();
  }

  async execute(input, state) {
    return await this.graph.invoke({ input });
  }
}

// ============================================================================
// ADVANCED AGENT: CUSTOM BUSINESS ANALYST
// ============================================================================

class BusinessAnalystAgent extends BaseAgent {
  constructor(model) {
    super(
      "BusinessAnalystAgent",
      "a specialized business analyst that evaluates market opportunities, financial metrics, and strategic positioning",
      model
    );
    this.addTool(this.createFinancialAnalysisTool());
    this.addTool(this.createRiskAssessmentTool());
    this.addTool(this.createROICalculatorTool());
  }

  createFinancialAnalysisTool() {
    return tool(
      async ({ metrics, timeframe }) => {
        return this.performFinancialAnalysis(metrics, timeframe);
      },
      {
        name: "financial_analysis",
        description: "Perform comprehensive financial analysis",
        schema: z.object({
          metrics: z.array(z.string()).describe("Financial metrics to analyze"),
          timeframe: z.string().describe("Analysis timeframe")
        })
      }
    );
  }

  createRiskAssessmentTool() {
    return tool(
      async ({ factors, context }) => {
        return this.assessRisk(factors, context);
      },
      {
        name: "risk_assessment",
        description: "Assess business and market risks",
        schema: z.object({
          factors: z.array(z.string()).describe("Risk factors to evaluate"),
          context: z.string().describe("Business context for risk assessment")
        })
      }
    );
  }

  createROICalculatorTool() {
    return tool(
      async ({ investment, returns, timeframe }) => {
        return this.calculateROI(investment, returns, timeframe);
      },
      {
        name: "roi_calculator",
        description: "Calculate return on investment",
        schema: z.object({
          investment: z.number().describe("Initial investment amount"),
          returns: z.number().describe("Expected returns"),
          timeframe: z.string().describe("Investment timeframe")
        })
      }
    );
  }

  performFinancialAnalysis(metrics, timeframe) {
    const analysis = {
      revenue: { current: 1000000, projected: 1200000, growth: 20 },
      profit: { current: 150000, projected: 200000, margin: 16.7 },
      cashFlow: { current: 80000, projected: 120000, improvement: 50 },
      debt: { current: 300000, projected: 250000, reduction: 16.7 }
    };

    return {
      timeframe,
      metrics: analysis,
      overallHealth: "Strong",
      recommendations: [
        "Maintain current growth trajectory",
        "Consider debt reduction strategies",
        "Invest in cash flow optimization"
      ],
      timestamp: new Date().toISOString()
    };
  }

  assessRisk(factors, context) {
    const riskLevels = {
      market: "Medium",
      financial: "Low",
      operational: "Medium",
      regulatory: "Low",
      competitive: "High"
    };

    const overallRisk = Object.values(riskLevels).includes("High") ? "High" : "Medium";

    return {
      context,
      riskFactors: riskLevels,
      overallRisk,
      mitigationStrategies: [
        "Diversify revenue streams",
        "Strengthen competitive positioning",
        "Implement operational safeguards"
      ],
      timestamp: new Date().toISOString()
    };
  }

  calculateROI(investment, returns, timeframe) {
    const roi = ((returns - investment) / investment) * 100;
    const annualizedROI = roi / (timeframe.includes("year") ? 1 : 12);

    return {
      investment,
      returns,
      timeframe,
      roi: roi.toFixed(2) + "%",
      annualizedROI: annualizedROI.toFixed(2) + "%",
      paybackPeriod: (investment / (returns / 12)).toFixed(1) + " months",
      recommendation: roi > 20 ? "Highly Recommended" : roi > 10 ? "Recommended" : "Consider Alternatives",
      timestamp: new Date().toISOString()
    };
  }
}

// ============================================================================
// COMPREHENSIVE DEMO EXECUTION
// ============================================================================

async function runComprehensiveDemo() {
  console.log("🚀 LangGraph Agentic Framework - Comprehensive Demo");
  console.log("=".repeat(70));

  // Initialize framework with real-world configuration
  const framework = new AgenticFramework();

  // Create mock models (replace with real API keys in production)
  const createMockModel = (name) => ({
    invoke: async (messages) => ({
      content: `[${name}] Processed: ${messages[messages.length - 1].content}`
    })
  });

  const models = {
    openai: createMockModel("GPT-4"),
    anthropic: createMockModel("Claude-3"),
    business: createMockModel("Business-Analyst")
  };

  // Register specialized agents
  console.log("\n🔧 Initializing Specialized Agents...");
  framework.registerAgent(new ResearchAgent(models.openai));
  framework.registerAgent(new AnalysisAgent(models.anthropic));
  framework.registerAgent(new WriterAgent(models.openai));
  framework.registerAgent(new ReviewAgent(models.anthropic));
  framework.registerAgent(new BusinessAnalystAgent(models.business));

  // Create advanced workflows
  console.log("\n🔄 Setting up Advanced Workflows...");
  framework.createWorkflow("business-intelligence", new BusinessIntelligenceWorkflow(framework));
  framework.createWorkflow("research-analysis", new ResearchAnalysisWorkflow(framework));
  framework.createWorkflow("content-creation", new ContentCreationWorkflow(framework));

  // Demo 1: Business Intelligence Workflow
  console.log("\n" + "=".repeat(70));
  console.log("📊 DEMO 1: Business Intelligence Workflow");
  console.log("=".repeat(70));

  const businessQuery = "Analyze the competitive landscape for AI-powered customer service solutions, including market size, key players, pricing strategies, and growth opportunities";

  try {
    const biResult = await framework.executeWorkflow("business-intelligence", businessQuery);
    console.log("\n📈 Business Intelligence Results:");
    console.log("-".repeat(50));
    console.log("Market Research:", biResult.marketResearch?.output || "Completed");
    console.log("Competitor Analysis:", biResult.competitorAnalysis?.output || "Completed");
    console.log("Trend Analysis:", biResult.trendAnalysis?.output || "Completed");
    console.log("Strategic Recommendations:", biResult.strategicRecommendations?.output || "Completed");
    console.log("Executive Summary:", biResult.executiveSummary?.output || "Completed");
    console.log("Quality Review:", biResult.qualityReview?.output || "Completed");
  } catch (error) {
    console.error("❌ Business Intelligence Demo Error:", error.message);
  }

  // Demo 2: Multi-Agent Collaboration
  console.log("\n" + "=".repeat(70));
  console.log("🤝 DEMO 2: Multi-Agent Collaboration");
  console.log("=".repeat(70));

  const collaborationQuery = "Create a comprehensive market entry strategy for a new fintech startup";

  try {
    const collabResult = await framework.executeWorkflow("research-analysis", collaborationQuery);
    console.log("\n🤝 Collaboration Results:");
    console.log("-".repeat(50));
    console.log("Research Phase:", collabResult.research?.output || "Completed");
    console.log("Analysis Phase:", collabResult.analysis?.output || "Completed");
    console.log("Review Phase:", collabResult.review?.output || "Completed");
  } catch (error) {
    console.error("❌ Collaboration Demo Error:", error.message);
  }

  // Demo 3: Content Creation Pipeline
  console.log("\n" + "=".repeat(70));
  console.log("✍️ DEMO 3: Content Creation Pipeline");
  console.log("=".repeat(70));

  const contentQuery = "Generate a technical white paper on blockchain scalability solutions for enterprise applications";

  try {
    const contentResult = await framework.executeWorkflow("content-creation", contentQuery);
    console.log("\n✍️ Content Creation Results:");
    console.log("-".repeat(50));
    console.log("Research Phase:", contentResult.research?.output || "Completed");
    console.log("Analysis Phase:", contentResult.analysis?.output || "Completed");
    console.log("Writing Phase:", contentResult.writing?.output || "Completed");
    console.log("Review Phase:", contentResult.review?.output || "Completed");
  } catch (error) {
    console.error("❌ Content Creation Demo Error:", error.message);
  }

  // Demo 4: Individual Agent Capabilities
  console.log("\n" + "=".repeat(70));
  console.log("🔧 DEMO 4: Individual Agent Capabilities");
  console.log("=".repeat(70));

  const businessAnalyst = framework.getAgent("BusinessAnalystAgent");
  if (businessAnalyst) {
    console.log("\n💼 Business Analyst Agent Demo:");
    console.log("-".repeat(50));
    
    // Test financial analysis
    const financialResult = await businessAnalyst.process("Analyze financial performance for Q4 2024");
    console.log("Financial Analysis:", financialResult.output);
    
    // Test risk assessment
    const riskResult = await businessAnalyst.process("Assess market risks for new product launch");
    console.log("Risk Assessment:", riskResult.output);
  }

  // Framework Statistics
  console.log("\n" + "=".repeat(70));
  console.log("📊 FRAMEWORK STATISTICS");
  console.log("=".repeat(70));
  console.log(`Registered Agents: ${framework.agents.size}`);
  console.log(`Available Workflows: ${framework.workflows.size}`);
  console.log(`Execution History: ${framework.getHistory().length} workflows`);
  console.log(`Framework State: ${Object.keys(framework.getState()).length} properties`);

  // Agent Capabilities Summary
  console.log("\n🤖 AGENT CAPABILITIES SUMMARY:");
  console.log("-".repeat(50));
  framework.agents.forEach((agent, name) => {
    console.log(`${name}:`);
    console.log(`  - Tools: ${agent.tools.length}`);
    console.log(`  - Description: ${agent.description}`);
  });

  console.log("\n🎉 Comprehensive Demo Completed Successfully!");
  console.log("=".repeat(70));
}

// ============================================================================
// EXPORT AND EXECUTION
// ============================================================================

export { 
  BusinessIntelligenceWorkflow, 
  BusinessAnalystAgent, 
  runComprehensiveDemo 
};

// Run comprehensive demo if this file is executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
  runComprehensiveDemo().catch(console.error);
}
