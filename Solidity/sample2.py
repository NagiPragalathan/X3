import langchain
from langchain_community.llms import ChatOpenAI  # Use langchain_community
from dotenv import load_dotenv
import os

load_dotenv()

# Set up OpenAI with your API key
llm = ChatOpenAI(api_key="YOUR_OPENAI_API_KEY")

def pseudocode_to_solidity(pseudocode):
    """
    Attempts to generate Solidity code from pseudocode using LangChain and OpenAI.

    Args:
        pseudocode (str): The pseudocode to be translated.

    Returns:
        str: The generated Solidity code, or an error message if unsuccessful.
    """

    prompt = f"Convert the following pseudocode to Solidity:\n{pseudocode}"
    response = llm.run(prompt)

    if response.success:
        return response.text
    else:
        return "Error: Failed to generate Solidity code."

# Example usage
pseudocode = """
# Declare a contract named Storage
contract Storage {
  uint storedData;

  # Function to set a value
  function setValue(uint x) public {
    storedData = x;
  }

  # Function to retrieve the value
  function getValue() public view returns (uint) {
    return storedData;
  }
}
"""

solidity_code = pseudocode_to_solidity(pseudocode)
print(solidity_code)
