
from clarifai.client.workflow import Workflow
# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/tm4w051o5ex8/App-with-Llama-2/workflows/workflow-e91f74"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="9de120c41db54852aa3297d7aa9af4e7"
)
result = text_classfication_workflow.predict_by_bytes(b"Who's your daddy?", input_type="text")
print(result.results[0].outputs[0].data)




