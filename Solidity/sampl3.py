# Import necessary libraries (adjust for your specific LLMs)
from langchain_community.llms import OpenAI, GPT3  # Replace with actual class names
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

# Set up LLMs and memory
report_llm = GPT3(api_key="YOUR_GPT3_KEY")
explanation_llm = OpenAI(api_key="YOUR_CHATOPENAI_KEY")

# Prompt for report generation (replace with your report generation logic)
report_prompt = "..."

# Generate report text (replace with actual report generation)
report_text = "..."

# Prompt template for explanation (includes report metadata integration)
explanation_prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a helpful AI providing explanations of reports."
        ),
        MessagesPlaceholder(variable_name="report_history"),  # Placeholder for report
        HumanMessagePromptTemplate.from_template("{question} (Report: {report_metadata})"),
    ]
)

# Memory for explanation context (stores report text)
report_memory = ConversationBufferMemory(memory_key="report_history", return_messages=True)

# Chain for explanations
explanation_chain = LLMChain(
    llm=explanation_llm, prompt=explanation_prompt, verbose=True, memory=report_memory
)

# User question with report reference
question = "Can you explain the section on NLP trends in the report?"

# Generate explanation
explanation, explanation_metadata = explanation_chain({"question": question})

# Access and print results
print("Explanation Text:")
print(explanation)

print("\nExplanation Metadata:")
print(explanation_metadata)
