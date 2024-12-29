from openai import OpenAI
import streamlit as st
# from config import secreat_key


# page stetup 
st.set_page_config(page_title = "Streamlit Chat", page_icon = 'speech_balloon')
st.title('Chatbot')

if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False

def complete_setup():
    st.session_state.setup_complete = True


#this line checks if the setup complete session state variable 

# state is false and if it is then user will be displayed.



if not st.session_state.setup_complete:
    
# First sub header below chat bot 

    st.subheader("Personal information", divider = "rainbow")
    
    if "name" not in st.session_state:
        st.session_state["name"] = ""

    if "experience" not in st.session_state:
        st.session_state["experience"] = ""

    if "skills" not in st.session_state:
        st.session_state["skills"] = ""
    
    
    
    #Asking user's details. User name, experience, skills
    
    
    # user's name 
    
    st.session_state["name"] = st.text_input(label = "Name", max_chars = None, value =st.session_state["name"] , placeholder = "Enter your name")
    
    # input field for the experienc and field
    
    st.session_state["experience"] = st.text_area(label = "Experience", height = None, max_chars = None, value = st.session_state["experience"], placeholder = "Describe your experience")

    
    st.session_state["skills"] = st.text_area(label = "Skills", height = None, max_chars = None, value = st.session_state["skills"], placeholder = "List your skills" )
    
    
    
    
    
    
    # Creating the label to check the informations.
    
    
    # Creating a label to confirm the input of the response. To do this we will use the write method
    
    st.write(f"**Your Name**: {st.session_state['name']}")
    st.write(f"**Your Experience**: {st.session_state['experience']}")
    st.write(f"**Your Skills**: {st.session_state['skills']}")
    
    
    
    
    
    
    #Creating one more label to get the information about the   #Company and name of the Interviewee
    
    
    # Add the fields for company and position separatly.

    
    # Initializing the session state variables.

    

    st.subheader("Company" "&" "Position", divider = 'rainbow')

    if "company" not in st.session_state:
        st.session_state["company"] = "Amazon"
    if "position" not in st.session_state:
        st.session_state["position"] = "Data Scientist"
    if "level" not in st.session_state:
            st.session_state["level"] = "Junior"
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.session_state["level"] = st.radio(
            "Choose level",
            key = "visibility",
            options = ["Junior", "Mid_level", "senior"]
    
        )
    
    
    with col2:
        st.session_state["position"] = st.selectbox(
            "Choose a position",
            ("Data Scientist", "Data Engineer", "ML Engineer", "BI Analyst", "FInancial Analyst")
        )
    
    
        
        # Enter a list of company names.
    
    
    
    st.session_state["company"] = st.selectbox(
        "Choose a Company ",
        ("Amazon", "Meta", "BMW", "Apple", "Google", "Samsung")
    )
    
    
    st.write(f"**Your Information:** {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}" )
    
    if st.button("Start interview", on_click = complete_setup):
        st.write("Setup complete. Starting interview.....")
    
    


# Defining the Open AI model.



# Open AI model 

if st.session_state.setup_complete:

    # Providing the guiding box to the user as guide line 
    st.info(
        """
        Start by introducing yourself. 
        """, 
        icon= "👋"

    )


    client = OpenAI(api_key = st.secrets["secret_key"])


    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o"



    # messages in session states.


    # if "messages" not in st.session_state:
    #     st.session_state.messages = [{"role":"system", "content":f"You are an HR executive that interviews an unterviewee called {st.session_state['name']} with {st.session_state['experience']} and {st.session_state['skills']}. You should interview them for the position {level} {position} at the {company} " }]


    if "message" not in st.session_state:
        st.session_state.messages =[{
            "role":"system",
            "content":(

                f"You are an HR executive that interviews as interviewee called {st.session_state['name']}"

                f"with experience {st.session_state['experience']} and skills {st.session_state['skills']}."

                f"You should interview him for the position {st.session_state['level']} {st.session_state['position']}"

                f"at the company {st.session_state['company']}"
            )
        }]
      


    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


    
    # Creating the chat.
    



    # Creating the chat.

    if prompt := st.chat_input("Your answer. "):
        st.session_state.messages.append({"role":"user", "content":prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # chat bot response block.

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model = st.session_state["openai_model"],
                messages =[
                    {
                        "role": m["role"], "content":m["content"]
                    }
                    for m in st.session_state.messages
                ],
                stream = True, # recive the response 

            )
            response = st.write_stream(stream)
        st.session_state.messages.append({
            "role":"assistant", "content":response
        })


    # call the open AI to generate the response 



    # store the user session state and update it dynamically.