### Document Stores

- Select document stores
- Create New
- Choose file loader (PDF)
- Upload file
- Choose the text splitter
- Upload and test the chunks
- Click process

### Upsert into Vector DB

- Start upsert
- Choose the embedding (OpenAPI-small)
- Choose vectorstores (Pinecone)
- Visit Pinecone website
- Create an index
    - name
    - configuration (OpenAI-small)
    - Choose the chunk size (1536)
    - AWS zone
    - Create
- Create API and use in Flowise

### Build the Flowise Project

- Refer 32-flowise-rag\01-complete-project.png