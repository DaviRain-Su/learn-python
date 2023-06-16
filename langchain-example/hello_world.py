from langchain.llms import OpenAI
llm = OpenAI(openai_api_key="OPENAI_API_KEY")
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))
