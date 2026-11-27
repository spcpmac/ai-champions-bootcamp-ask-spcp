# Problem Statement
Singpass partner support teams and their integrating agencies rely on a growing repository of knowledge about authentication flows, API specifications, integration errors, configuration issues and production incidents. Today, this knowledge is scattered across Slack discussions, support tickets, technical documentation and the memories of individual engineers, making it time-consuming to retrieve relevant information, identify historical precedents and formulate accurate, consistent responses. The result is repeated investigations, escalations to engineers, and operational inefficiencies that hinder scalability as integration complexity increases. How might we unify and surface the right historical knowledge to support agents in real time, enabling faster, consistent, and trusted responses for partner integrations?

# Proposed Solution
Develop a Proof of Concept (POC) web application featuring a conversational AI chatbot powered by an LLM and Retrieval-Augmented Generation (RAG). The chatbot will leverage a knowledge base comprising historical Zendesk support tickets, the latest Singpass developer documentation and relevant Slack discussions, with all content sanitised for public consumption. Users can ask technical questions in natural language and receive contextual answers, troubleshooting guidance and references to relevant sources.

LLM + RAG is well suited for interpreting complex technical queries, retrieving information across multiple sources and synthesising relevant answers. Unlike traditional keyword searches, static FAQs or rule-based chatbots, it can understand conversational context, handle variations in how questions are phrased and draw upon historical resolutions. RAG also allows the knowledge base to be updated independently of the LLM, keeping responses aligned with the latest documentation without model retraining.

# Impact
The POC aims to reduce the time required to investigate and respond to partner enquiries, improve response accuracy and consistency, and minimise repetitive escalations to engineers. By making historical troubleshooting knowledge and technical documentation accessible through a conversational interface, support officers can resolve common issues more efficiently, while partners could eventually obtain answers through self-service.

The web application is expected to be used daily by partner support officers for technical enquiries, integration troubleshooting and response drafting. If the POC proves effective, it could be extended to external integrating partners as an always-available self-service support channel, reducing support workload and improving the overall partner experience.

# Additional Requirements
## The application should:
* Consolidate Information: Aggregate data from various official and trustworthy sources that are publicly accessible to provide a unified repository of information related to the chosen domain area.
* Personalise User Experience: Allow users to input generic, non-personally identifiable information to receive tailored guidance and information relevant to their specific scenarios.
* Enhance Understanding: Generate interactive content, including explanations, elaborations, and responses to follow-up questions, facilitating a deeper comprehension of the process.
* Present Information Effectively: Present information through a combination of formats such as text, data tables, data visualisations, and interactive forms to enhance user engagement and understanding.

## For web application:
The suggested platform for deploying the web application is Streamlit Community Cloud.
It is recommended to password protect the application.

## Documentation (As Pages within the Streamlit App)
In addition to the webpages that include the required features and functionality, your Streamlit app MUST contain the following two additional pages:
* "About Us" Page - A detailed page outlining the project scope, objectives, data sources, and features.
* "Methodology" Page - A comprehensive explanation of the data flows and implementation details, and a flowchart illustrating the process flow for each use case in the application. Each use case should have its own flowchart.