import streamlit as st
import openai
import pandas as pd
import time
from kaggle.api.kaggle_api_extended import KaggleApi
from googlesearch import search

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('https://media.istockphoto.com/id/1663010058/vector/technology-abstract-futuristic-background-for-internet-business-big-data-concept.jpg?s=612x612&w=0&k=20&c=k4uMvZGxyuM1IFslhIYcjqcUnMv_qNTeGkL4wGEe4LI=');
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Market Research & Use Case Generation Agent")
st.image("group-of-businesswomen-during-a-meeting.webp",width=550)

# Setting Up OpenAI API Key
openai.api_key = "Your API key"
if not openai.api_key:
    st.warning("OpenAI API key is missing. Please configure it as an environment variable.")

st.title("AI & GenerativeAI Use Case Research")
st.image("https://imgs.search.brave.com/ukA60C6C2Cq2US-Sd-fd_8wOn8DT5YrTBgt0QN2tJSQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90MTA1/ODk5NzgucC5jbGlj/a3VwLWF0dGFjaG1l/bnRzLmNvbS90MTA1/ODk5NzgvOGM5NmM4/ZmQtYjc4ZC00MGZj/LWI0NTItOThlOGU4/YTFmYzk4L2ltYWdl/LnBuZw", width=550)

# Predefined Companies with Multiple Industries
companies = {
    "Google": ["Technology", "Advertising", "Cloud Computing", "AI & ML", "Consumer Electronics", "Autonomous Vehicles"],
    "Microsoft": ["Technology", "Cloud Computing", "Software Development", "Gaming", "AI & ML", "Enterprise Solutions"],
    "Amazon": ["E-commerce", "Cloud Computing", "Logistics", "AI & ML", "Retail", "Consumer Electronics"],
    "Tesla": ["Automotive", "Energy", "AI & ML", "Batteries", "Solar Power", "Transportation"],
    "Meta": ["Social Media", "AI & ML", "VR & AR", "Advertising", "Consumer Technology", "Data Analytics"],
    "IBM": ["Technology", "AI & ML", "Cloud Computing", "Blockchain", "Quantum Computing", "Enterprise Solutions"],
    "Intel": ["Semiconductors", "AI & ML", "Cloud Computing", "Autonomous Vehicles", "IoT", "Gaming"],
    "Apple": ["Consumer Electronics", "Software Development", "Retail", "AI & ML", "Health Technology", "Wearables"],
    "Samsung": ["Electronics", "Semiconductors", "AI & ML", "Displays", "Consumer Technology", "Home Appliances"],
    "Oracle": ["Enterprise Software", "Cloud Computing", "Database Management", "AI & ML", "ERP Solutions", "HR Technology"],
    "Cisco": ["Networking", "Cybersecurity", "Cloud Computing", "IoT", "AI & ML", "Enterprise Solutions"],
    "Salesforce": ["Cloud Computing", "CRM", "AI & ML", "Marketing Automation", "Analytics", "Enterprise Solutions"],
    "Adobe": ["Software", "Digital Media", "Creative Tools", "AI & ML", "Marketing", "Cloud Computing"],
    "Netflix": ["Entertainment", "Streaming", "AI & ML", "Content Production", "Advertising", "Data Analytics"],
    "Airbnb": ["Hospitality", "Travel", "Real Estate", "AI & ML", "Marketplace", "Analytics"],
    "Uber": ["Transportation", "Logistics", "AI & ML", "Ride-sharing", "Autonomous Vehicles", "Delivery"],
    "Zoom": ["Communication", "Video Conferencing", "AI & ML", "Enterprise Solutions", "Collaboration Tools", "Cloud Computing"],
    "Spotify": ["Music Streaming", "AI & ML", "Content Discovery", "Advertising", "Data Analytics", "Entertainment"],
    "Snapchat": ["Social Media", "AI & ML", "Advertising", "Content Creation", "AR & VR", "Consumer Technology"],
    "SpaceX": ["Aerospace", "Space Exploration", "Satellites", "AI & ML", "Energy", "Transportation"]
}

# Dropdown for selecting a company with an initial "Choose the company" option
selected_company = st.selectbox("Choose a company or select 'Other' to enter the company and industry names:", ["Choose the company"] + list(companies.keys()) + ["Other"])

if selected_company == "Other":
    company_name = st.text_input("Enter the company name:")
    industry_name = st.text_input("Enter the industry name:")
elif selected_company != "Choose the company":
    company_name = selected_company
    # Dropdown for selecting an industry from the company's industries
    industry_name = st.selectbox("Select an industry:", companies[selected_company])
else:
    company_name = None
    industry_name = None

if st.button("Click here to Generate AI Research Report"):
    if not company_name or not industry_name:
        st.warning("Please provide both the company name and the industry name.")
    else:
        st.write("Please Wait! It is Researching AI trends and company insights.....")

        # Agent 1: Web Searching for Company and Industry Trends
        def search_web(query, num_results=3):
            """It Will Performs Google search and return a list of result links."""
            results = []
            try:
                for result in search(query, num_results=num_results):
                    results.append(result)
                    time.sleep(1)  
            except Exception as e:
                st.warning(f" Web search failed: {e}")
            return results

        # Generate search queries
        industry_query = f"AI trends in {company_name} {industry_name} site:forbes.com OR site:venturebeat.com OR site:{company_name.lower()}.com"
        company_query = f"{company_name} AI strategy site:{company_name.lower()}.com OR site:businessinsider.com"

        # Perform web search
        industry_trends = search_web(industry_query)
        company_focus = search_web(company_query)

        st.success("✅ Successfully Completed Company and Industry Research.!")

        # Agent 2: Generate AI Use Cases with OpenAI
        st.write(" Please Wait! It is Generating AI Use Cases Of a Company.....")
        prompt = (
            f"Based on the latest AI trends in {industry_name} and the business focus of {company_name}, "
            "suggest top AI and Generative AI use cases that can improve operations, customer experience, and efficiency. "
            "Provide a concise list."
        )
        try:
            response = openai.ChatCompletion.create(
                model="your GPT Model",
                messages=[{"role": "user", "content": prompt}]
            )
            use_cases = response['choices'][0]['message']['content'].strip().split("\n")
        except Exception as e:
            st.warning(f" OpenAI API call failed: {e}")
            use_cases = []

        if not use_cases:
            st.warning("No AI use cases are generated. Check your OpenAI API key or response.")
            use_cases = ["N/A"]

        st.success("✅ Successfully Generated AI Use Cases!")

        # Agent 3: Collect AI Dataset Resources from Kaggle
        st.write("Please Wait! Searching for relevant AI datasets on Kaggle...")

        # Initialize Kaggle API
        try:
            api = KaggleApi()
            api.authenticate()
        except Exception as e:
            st.warning(f"Kaggle authentication failed: {e}")
            api = None

        datasets = []

        if api:
            for use_case in use_cases:
                if use_case.strip() != "N/A":
                    query = " ".join(use_case.split()[:3])  # Extract first 3 words for better search
                    try:
                        kaggle_results = api.dataset_list(search=query, sort_by="votes")
                        dataset_links = [f"https://www.kaggle.com/datasets/{dataset.ref}" for dataset in kaggle_results[:3]]
                        datasets.append(", ".join(dataset_links) if dataset_links else "No dataset found")
                    except Exception:
                        datasets.append("No dataset found")
                else:
                    datasets.append("N/A")  # Keep alignment

        st.success("✅ Successfully Completed Dataset Collections!")

        #Final Data Structure
        use_cases_data = {
            "Use Cases": [uc.split(":")[0] if ":" in uc else uc for uc in use_cases],  
            "Description": use_cases,  
            "Reference": datasets
        }

        # Generating Excel Report
        st.write("📄 Please Wait! It Is Generating Final Report in Excel Format.....")

        use_cases_df = pd.DataFrame(use_cases_data)
        industry_trends_df = pd.DataFrame(industry_trends, columns=["Industry Trends Links"])
        company_focus_df = pd.DataFrame(company_focus, columns=["Company Focus Area Links"])

        output_file_path = f"AI_Use_Case_Report_{company_name}.xlsx"
        with pd.ExcelWriter(output_file_path, engine="xlsxwriter") as writer:
            use_cases_df.to_excel(writer, sheet_name="Use Cases Feasibility Check", index=False)
            industry_trends_df.to_excel(writer, sheet_name="References of Articles_Resource", index=False)
            company_focus_df.to_excel(writer, sheet_name="Company Focus Areas", index=False)

        st.success(f"✅ Successfully Generated the Reported File: {output_file_path}")

        # Download Button
        with open(output_file_path, "rb") as file:
            st.download_button(label="📥Click here to Download Your AI Research Report", data=file, file_name=output_file_path)

            st.success("You have Successfully Completed Your AI Research Process...!")
            st.success("Refresh Page and enter Another Company and Industry For Research...!")
