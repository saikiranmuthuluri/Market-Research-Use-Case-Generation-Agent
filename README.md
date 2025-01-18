# Market-Research-Use-Case-Generation-Agent
Multi-Agent architecture system that generates relevant AI and Generative AI (Generative AI) use cases for a given Company or Industry.

This project provides an interactive web application to perform market research, generate AI and Generative AI use cases, and collect relevant datasets for various industries. Using a combination of Streamlit, OpenAI, Kaggle API, and Google Search, the application creates comprehensive Excel reports tailored to specific companies and industries.

**Key Features**

**Company and Industry Research:**

  Users can select predefined companies and industries or input their own.
  The app uses web scraping and Google search to fetch the latest trends and insights.

**Generative AI Use Case Creation:**

  Leveraging OpenAI GPT models, the app generates actionable AI and Generative AI use cases aligned with the selected company and 
  industry.

**AI Dataset Retrieval:**

  The app integrates with Kaggle API to search for relevant datasets for the use cases, ensuring practical implementation resources.

**Report Generation:**

**Generates a detailed Excel report containing:**

  AI use cases and their descriptions.
  Links to industry trends and company focus areas.
  Kaggle dataset references for further analysis.
  
**Custom Styling:**

  The app features a user-friendly interface with a sleek background for enhanced user experience.

**Flowchart**

**The application workflow can be summarized as:**

  Understanding the problem statement.
  Researching the problem statement using multiple resources.
  Writing code to automate the research process.
  Setting up APIs (OpenAI, Kaggle) and libraries.
  Selecting or entering company and industry names.
  
**Using agents to:**

  Search for trends and insights online.
  Generate AI use cases via OpenAI.
  Collect relevant datasets from Kaggle.
  Compiling and generating the final Excel report.
  Providing the report as a downloadable file.

**Technology Stack**

  Frontend: Streamlit for the web interface.
  
**Backend:**

  OpenAI API for Generative AI use case generation.
  Kaggle API for dataset retrieval.
  Google Search for web scraping insights.
  
**Libraries:**
  pandas for data manipulation.
  time for managing delays.
  xlsxwriter for Excel report generation.
  
**Styling:** Embedded custom HTML and CSS for dynamic visuals.  

**Usage Instructions**

  Open the web app and select a company and its relevant industry from the dropdown menu.

**Click the Generate AI Research Report button to start:**

  Researching AI trends and insights.
  Generating AI and Generative AI use cases.
  Collecting relevant datasets.
  Download the generated Excel report containing:
  AI use cases with cross-functional benefits.
  Web links for further reading.
  Dataset references from Kaggle.
