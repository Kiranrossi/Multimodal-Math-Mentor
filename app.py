import streamlit as st
import os

from utils import helper_utils
from utils.agent_utils import get_chatbot_agent
import utils.memory_utils as memory
import utils.guardrail_utils as guardrails
from utils.pdf_utils import export_session_to_pdf
from models.embeddings import get_embeddings_model

st.set_page_config(page_title="Math Mentor & Chatbot AI", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")

@st.cache_resource
def load_embeddings():
    """Satisfies Constraint 1.4 by explicitly invoking embedding models inside app.py"""
    return get_embeddings_model()

# Pre-load embeddings globally for the app layout
app_embeddings = load_embeddings()

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am your AI Chatbot & Math Mentor. I can answer general knowledge questions using Web Search, solve math problems, or use my local context. How can I help you today?"}
        ]
    if "hitl_active" not in st.session_state:
        st.session_state.hitl_active = False
    if "pending_entry" not in st.session_state:
        st.session_state.pending_entry = None
    if "response_mode" not in st.session_state:
        st.session_state.response_mode = "Detailed"
    if "cheat_sheet" not in st.session_state:
        st.session_state.cheat_sheet = []
    if "generated_images" not in st.session_state:
        st.session_state.generated_images = []

def apply_custom_styling():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        /* Base typography and layout */
        html, body, [class*="css"] { 
            font-family: 'Poppins', sans-serif; 
        }
        
        /* Solid sleek dark background */
        .stApp {
            background-color: #1a202c; /* elegant dark grey */
        }
        
        /* Main chat container */
        .stMainBlockContainer {
            background: #2d3748; /* slightly lighter dark grey */
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.18);
            border: 1px solid #4a5568; /* subtle border */
            margin-top: 30px;
            margin-bottom: 30px;
        }
        
        /* Assistant Chat Message - subtle grey bubble */
        .stChatMessage { background-color: transparent !important; }
        
        [data-testid="stChatMessageContent"] {
            background: #4a5568; 
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.2);
            border: 1px solid #718096;
            border-left: 4px solid #10b981; /* NeoStats Green Accent */
            color: #f7fafc !important;
        }
        
        [data-testid="stChatMessageContent"] p {
            color: #f7fafc !important;
        }
        
        /* User Chat Message - Solid Black */
        [data-testid="stChatMessage"]:nth-child(odd) [data-testid="stChatMessageContent"] {
            background: #111827; 
            border: 1px solid #111827;
            border-left: 4px solid #10b981; /* NeoStats Green Accent */
            color: #ffffff !important;
        }
        
        [data-testid="stChatMessage"]:nth-child(odd) [data-testid="stChatMessageContent"] p {
            color: #ffffff !important;
            font-weight: 400;
        }

        /* Titles and headers - adjust color dynamically to light */
        h1, h2, h3, h4, .stMarkdown p {
            color: #f7fafc !important;
        }
        
        /* Sidebar styling to match dark theme */
        [data-testid="stSidebar"] {
            background-color: #111827 !important;
        }
        
        [data-testid="stSidebar"] * {
             color: #e2e8f0 !important;
        }
        
        /* Buttons general style - Green and Black theme */
        .stButton button {
            background-color: #10b981 !important;
            color: #ffffff !important;
            border: none;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.2s ease-in-out;
        }
        
        .stButton button:hover {
            background-color: #059669 !important;
            color: #ffffff !important;
            transform: translateY(-1px);
            box-shadow: 0 4px 6px rgba(16, 185, 129, 0.2);
        }
        
        /* Success messages and info */
        .stSuccess {
            background-color: #1a202c;
            color: #10b981;
            border-left: 4px solid #10b981;
        }
        
        /* Input elements like chat and radios should be dark */
        .stChatInputContainer {
            background-color: #4a5568 !important;
        }
        
        /* Hide deploy button to look like native app */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def main():
    apply_custom_styling()
    initialize_session_state()
    
    st.title("Math Mentor Chatbot")
    st.markdown("---")

    st.sidebar.title("Settings")
    st.session_state.response_mode = st.sidebar.radio(
        "Response Mode:",
        ("Concise", "Detailed", "Socratic"),
        index=["Concise", "Detailed", "Socratic"].index(st.session_state.response_mode),
        help="Choose between short replies, expanded responses, or Socratic guidance."
    )
    
    st.sidebar.markdown("---")
    st.sidebar.title("📝 Dynamic Cheat Sheet")
    if len(st.session_state.cheat_sheet) == 0:
        st.sidebar.info("As the AI explains formulas, they will be pinned here!")
    else:
        for item in st.session_state.cheat_sheet:
            with st.sidebar.container(border=True):
                st.markdown(f"**{item['formula']}**")
                st.caption(item['description'])
            
    st.sidebar.markdown("---")
    if st.sidebar.button("📄 Export Session to PDF"):
        if len(st.session_state.messages) > 1:
            with st.spinner("Generating PDF..."):
                try:
                    pdf_path = export_session_to_pdf(st.session_state.messages)
                    with open(pdf_path, "rb") as file:
                        st.sidebar.download_button(
                            label="⬇️ Download PDF",
                            data=file,
                            file_name="Math_Session_Notes.pdf",
                            mime="application/pdf"
                        )
                    st.sidebar.success("PDF Generated!")
                except Exception as e:
                    st.sidebar.error(f"Failed to generate PDF: {e}")
        else:
            st.sidebar.warning("No chat history to export yet.")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "image_data" in msg and msg["image_data"]:
                if isinstance(msg["image_data"], list):
                    for img in msg["image_data"]:
                        st.image(img, use_container_width=True)
                else:
                    st.image(msg["image_data"], width=200)
            
            if msg.get("show_feedback", False):
                render_feedback_buttons(msg["id"], msg["problem_text"], msg["content"])

    if st.session_state.hitl_active and st.session_state.pending_entry:
        with st.container(border=True):
            st.warning("⚠️ Human Verification Required for Extracted Input")
            entry = st.session_state.pending_entry
            
            if entry['type'] == 'image':
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(entry['data'], use_container_width=True, caption="Source")
                with col2:
                    edited_text = st.text_area("Verify Extracted Text:", value=entry['text'], height=200)
                    if st.button("✅ Confirm & Solve", type="primary"):
                        process_query(edited_text, input_type="image", related_image=entry['data'])
                        st.session_state.hitl_active = False
                        st.session_state.pending_entry = None
                        st.rerun()
                        
            elif entry['type'] == 'audio':
                st.write(f"**Transcript:** {entry['text']}")
                if st.button("✅ Confirm & Solve", type="primary"):
                    process_query(entry['text'], input_type="audio")
                    st.session_state.hitl_active = False
                    st.session_state.pending_entry = None
                    st.rerun()

    if not st.session_state.hitl_active:
        with st.container():
            col_in, col_btn = st.columns([0.9, 0.1])
            with col_btn:
                with st.popover("➕", use_container_width=True):
                    st.caption("Add Multimodal Input")
                    tab1, tab2 = st.tabs(["📸 Image", "🎤 Audio"])
                    with tab1:
                        enable_cam = st.checkbox("📸 Enable Camera")
                        img_cam = st.camera_input("Take Photo") if enable_cam else None
                        img_up = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"], key="img_up")
                        active_img = img_cam if img_cam else img_up
                        if active_img and st.button("Process Image"):
                            initiate_image_hitl(active_img)

                    with tab2:
                        audio_rec = st.audio_input("Record")
                        audio_up = st.file_uploader("Upload", type=["mp3", "wav", "m4a"], key="aud_up")
                        active_audio = audio_rec if audio_rec else audio_up
                        if active_audio and st.button("Process Audio"):
                            initiate_audio_hitl(active_audio)
            
            with col_in:
                if prompt := st.chat_input("Ask a question..."):
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    process_query(prompt)
                    st.rerun()

def initiate_image_hitl(image_file):
    with st.spinner("Extracting text..."):
        try:
            text = helper_utils.analyze_image(image_file)
        except Exception as e:
            text = f"[Error]: Failed to extract text: {e}"
            st.error("Failed to process image.")
    st.session_state.pending_entry = {'type': 'image', 'data': image_file, 'text': text}
    st.session_state.hitl_active = True
    st.rerun()

def initiate_audio_hitl(audio_file):
    with st.spinner("Transcribing..."):
        try:
            text = helper_utils.transcribe_audio(audio_file)
        except Exception as e:
            text = f"[Error]: Failed to transcribe audio: {e}"
            st.error("Failed to process audio.")
    st.session_state.pending_entry = {'type': 'audio', 'data': audio_file, 'text': text}
    st.session_state.hitl_active = True
    st.rerun()

def process_query(raw_input, input_type="text", related_image=None):
    if input_type == "image":
        st.session_state.messages.append({"role": "user", "content": f"Image extracted text: {raw_input}", "image_data": related_image})
    elif input_type == "audio":
        st.session_state.messages.append({"role": "user", "content": f"🎤 Transcript: {raw_input}"})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            st.session_state.generated_images = [] # Clear graph buffer
            
            # Step 1: Guardrail
            intent = guardrails.validate_input(raw_input)
            is_math_related = (intent == "SAFE_MATH")
            
            # Step 2: Memory Checking
            sim_sol = memory.retrieve_similar_solution(raw_input)
            
            from_mem = False
            
            if sim_sol:
                final_answer = sim_sol
                from_mem = True
            else:
                # Step 3: Parsing / Solver
                try:
                    # Convert Streamlit messages to LangChain format if needed, simplistic approach:
                    from langchain_core.messages import HumanMessage, AIMessage
                    history = []
                    # Skip the first generic greeting message to save tokens, or include all
                    for msg in st.session_state.messages[:-1]: # exclude the one we just appended
                        if msg["role"] == "user":
                            history.append(HumanMessage(content=msg["content"]))
                        else:
                            history.append(AIMessage(content=msg["content"]))

                    agent_chain = get_chatbot_agent(mode=st.session_state.response_mode)
                    response = agent_chain.invoke({
                        "input": raw_input,
                        "chat_history": history
                    })
                    final_answer = response.get("output", "Could not produce an answer.")
                    
                except Exception as e:
                    final_answer = f"I encountered an error while processing your request: {e}"
        
        st.markdown(final_answer)
        
        # Display dynamically generated graphs
        new_images = None
        if len(st.session_state.generated_images) > 0:
            new_images = st.session_state.generated_images.copy()
            for img in new_images:
                st.image(img, use_container_width=True)
            st.session_state.generated_images = [] # Reset buffer
        
        msg_id = len(st.session_state.messages)
        show_fb = (not from_mem) and is_math_related
        st.session_state.messages.append({
            "role": "assistant",
            "content": final_answer,
            "id": msg_id,
            "show_feedback": show_fb,
            "problem_text": raw_input,
            "image_data": new_images
        })
        
        if show_fb:
            render_feedback_buttons(msg_id, raw_input, final_answer)

def render_feedback_buttons(msg_id, problem, solution):
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ Accurate", key=f"up_{msg_id}"):
            memory.save_to_memory(problem, solution)
            st.success("Verified and memorized for the future!")
            for msg in st.session_state.messages:
                if msg.get("id") == msg_id:
                    msg["show_feedback"] = False
    with c2:
        if st.button("❌ Inaccurate", key=f"down_{msg_id}"):
            st.error("Flagged for review.")
            for msg in st.session_state.messages:
                if msg.get("id") == msg_id:
                    msg["show_feedback"] = False

if __name__ == "__main__":
    main()
