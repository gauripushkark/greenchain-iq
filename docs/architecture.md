# GreenChain IQ Architecture

## MVP Architecture

```mermaid
flowchart TD
    A[User / Sustainability Analyst] --> B[GreenChain IQ Demo App]

    B --> C[Supplier ESG Dataset]
    C --> D[Risk Scoring Logic]

    D --> E[Risk Drivers]
    E --> F[Local Knowledge Retrieval Scaffold]

    F --> G[Synthetic Policy Documents]
    G --> H[Grounded Policy Guidance]

    D --> I[Risk Classification]
    H --> J[Business Recommendations]

    I --> K[Supplier Risk Report]
    J --> K

    K --> L[Executive Summary and Responsible AI Note]
