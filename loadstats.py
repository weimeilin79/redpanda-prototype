import pandas as pd
import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Set your OpenAI API key


# Initialize the LLM with LangChain
llm = ChatOpenAI(
    openai_api_key = ' YOUR_API_KEY ',
    model_name="gpt-4o",
    temperature=0.0)

# Define a prompt template for analyzing CSV data
prompt = PromptTemplate(
    input_variables=["data"],
    template="""Here's a potential customer of redpanda and how they are using the Redpanda clusters, 
    it contains the Configuration JSON fields such as: 
    callhome_cluster_age_days: The age of the cluster in days based on call home data.
    console_cluster_age_days: The age of the cluster in days as recorded in the console.
    callhome_topic_count: The total number of topics in the cluster as reported by call home.
    console_topic_count: The total number of topics in the cluster according to the console.
    callhome_partition_count: The total number of partitions across topics, as reported by call home.
    console_partition_count: The total number of partitions in the console data.
    callhome_cpu_count: The number of CPUs in the cluster according to call home data.
    callhome_origin_company: The name of the company or organization originating the cluster's data.
    license_status: The status of the license for the cluster (e.g., valid, expired).
    license_org_name: The organization name associated with the license.
    enterprise_features_used: A list or indicator of enterprise features actively in use within the cluster.
    rbac_usage_days: Number of days that role-based access control (RBAC) has been used in the cluster.
    audit_usage_days: Number of days audit logging has been active in the cluster.
    cloud_storage_usage_days: Number of days cloud storage features have been utilized.
    continuous_partition_autobalancing_usage_days: Number of days that continuous partition autobalancing has been enabled.
    : {data}
    
    Based on the following sales play strategies:
    : {sales_content}
    

    Analyze this unpaying customer based on its industry, why they need streaming data,
    and generate a targeted sales plan to up-sell Redpanda's enterprise features that they are already using.
    And also provide a summary of the customer's usage of Redpanda clusters and the potential value of the up-sell.
    Also suggest questions to ask the customer in the first meeting to understand their needs better, and how to position Redpanda as a solution.
    make sure it is comprehensive a analysis and sales plan.
    """
)

# Define the LLM Chain with the prompt and LLM
chain = prompt | llm

def load_csv_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    # Convert to JSON format to send to LLM
    data_json = df.to_json()
    return data_json

def load_salesplay_docs(folder_path):
    sales_content = ""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            sales_content += file.read() + "\n"
    return sales_content

# Function to analyze the CSV data with ChatGPT via LangChain
def analyze(file_path, sales_folder):
    # Load and format data
    data = load_csv_data(file_path)

    # Load sales play documents
    sales_content = load_salesplay_docs(sales_folder)
    # Generate the analysis
    response = chain.invoke({"data": data, "sales_content": sales_content})
    content = response.content
    # Format the content by adding clear sections
    formatted_content = "\n===== Customer Analysis and Sales Plan =====\n"
    formatted_content += content.replace("##", "\n##").replace("# ", "").replace("**", "").replace("\n\n", "\n")  # Adjust heading levels and add extra line breaks

    return formatted_content

# Example usage
if __name__ == "__main__":
    file_path = 'pfizer.csv'
    sales_folder = 'sales_play_doc'
    analysis = analyze(file_path,sales_folder)
    print(analysis)

