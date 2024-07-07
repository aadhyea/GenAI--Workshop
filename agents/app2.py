# from langchain_cohere import ChatCohere
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain.chains import SequentialChain
# from dotenv import load_dotenv
# load_dotenv()
# import os


# COHERE_API_KEY = os.getenv('COHERE_API_KEY')
# os.environ['OPENAI_API_KEY'] = 'API'

# llm = ChatCohere(temperature=0.7)

# def generate_restaurant_name_and_items(cuisine):
#     # Chain 1: Restaurant Name
#     prompt_template_name = PromptTemplate(
#         input_variables=['cuisine'],
#         template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
#     )

#     name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

#     # Chain 2: Menu Items
#     prompt_template_items = PromptTemplate(
#         input_variables=['restaurant_name'],
#         template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated string"""
#     )

#     food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

#     chain = SequentialChain(
#         chains=[name_chain, food_items_chain],
#         input_variables=['cuisine'],
#         output_variables=['restaurant_name', "menu_items"]
#     )

#     response = chain({'cuisine': cuisine})

#     return response

# if __name__ == "__main__":
#     print(generate_restaurant_name_and_items("Italian"))



from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your Cohere API key
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
os.environ['COHERE_API_KEY'] = 'API'

# Initialize the Cohere LLM
llm = ChatCohere(api_key=COHERE_API_KEY)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}. Return it as a comma separated string"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    response = chain({'cuisine': cuisine})

    return response

if __name__ == "_main_":
    print(generate_restaurant_name_and_items("Italian"))