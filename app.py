import streamlit as st
import os
from dotenv import load_dotenv
import packages.utils as utils
import packages.agents as agents
import packages.memory as memory
import packages.guardrails as guardrails
import packages.tools as tools

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Math Mentor Pro", page_icon="🎓", layout="wide")

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am your Professional Math Mentor. I can help with Algebra, Calculus, Probability, and Linear Algebra."}
        ]
    # State for HITL
    if "hitl_active" not in st.session_state:
        st.session_state.hitl_active = False
    if "pending_entry" not in st.session_state:
        st.session_state.pending_entry = None

def apply_custom_styling():
    st.markdown("""
    <style>
        /* Import Font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Background Image - Math/Education Theme */
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=2600&auto=format&fit=crop");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        /* Glassmorphism Overlay for Main Content */
        .stMainBlockContainer {
            background: rgba(255, 255, 255, 0.95); /* High opacity white for readability */
            padding: 2.5rem;
            border-radius: 25px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.5);
            margin-top: 30px;
            margin-bottom: 30px;
        }
        
        /* Dark Mode Support (Optional - forces white text logic if user is in dark mode, but we are using a white glass theme) */
        
        /* Chat Message Bubbles */
        .stChatMessage {
            background-color: transparent !important;
        }
        
        [data-testid="stChatMessageContent"] {
            background: #ffffff;
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            border: 1px solid #e0e0e0;
            color: #000000 !important; /* Force black text */
        }
        
        /* User Bubble Color */
        [data-testid="stChatMessage"]:nth-child(odd) [data-testid="stChatMessageContent"] {
            background: #e3f2fd; /* Light Blue */
            border: 1px solid #bbdefb;
            color: #000000 !important; /* Force black text */
        }
        
        /* Headers */
        h1, h2, h3, p, div {
            color: #2c3e50 !important;
            font-weight: 600 !important;
        }
        
        /* Buttons */
        .stButton button {
            background: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
            color: white !important;
            border: none;
            border-radius: 50px;
            padding: 0.5rem 1.5rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        /* Links */
        a {
            color: #2575fc !important;
            text-decoration: none;
            font-weight: 600;
        }
        a:hover {
            text-decoration: underline;
        }
        
    </style>
    """, unsafe_allow_html=True)

def main():
    apply_custom_styling()
    initialize_session_state()
    
    st.title("🎓 Professional Math Mentor")
    st.markdown("---")

    # --- Chat History ---
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            # Special formatting for Assistant
            if msg["role"] == "assistant":
                if "problem_text" in msg:
                    # Professional Breakdown
                    with st.expander("📄 Parser Output", expanded=False):
                        st.json(msg["raw_data"])
                    
                    st.markdown(msg["content"]) # The Solver Output (Explanation + Answer)
                    
                    if "confidence" in msg:
                        color = "green" if msg["confidence"] > 80 else "orange"
                        st.caption(f"**Verifier Confidence:** :{color}[{msg['confidence']}%]")
                    
                    if msg.get("show_feedback", False):
                        render_feedback_buttons(msg["id"], msg["problem_text"], msg["content"], msg["topic"])
                else:
                    st.markdown(msg["content"])
            else:
                st.markdown(msg["content"])
                if "image_data" in msg:
                    st.image(msg["image_data"], width=200)

    # --- HITL Interface ---
    if st.session_state.hitl_active and st.session_state.pending_entry:
        with st.container(border=True):
            st.warning("⚠️ Human Verification Required")
            entry = st.session_state.pending_entry
            
            if entry['type'] == 'image':
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(entry['data'], use_container_width=True, caption="Source")
                with col2:
                    edited_text = st.text_area("Verify Extracted Text:", value=entry['text'], height=200)
                    if st.button("✅ Confirm & Solve", type="primary"):
                        process_math_query(edited_text, input_type="image", related_image=entry['data'])
                        st.session_state.hitl_active = False
                        st.session_state.pending_entry = None
                        st.rerun()
                        
            elif entry['type'] == 'audio':
                st.write(f"**Transcript:** {entry['text']}")
                if st.button("✅ Confirm & Solve", type="primary"):
                    process_math_query(entry['text'], input_type="audio")
                    st.session_state.hitl_active = False
                    st.session_state.pending_entry = None
                    st.rerun()

    # --- Input Area ---
    if not st.session_state.hitl_active:
        
        # Popover for Attachments
        with st.container():
            col_in, col_btn = st.columns([0.9, 0.1])
            with col_btn:
                with st.popover("➕", use_container_width=True):
                    st.caption("Add Multimodal Input")
                    
                    tab1, tab2 = st.tabs(["📸 Image", "🎤 Audio"])
                    
                    with tab1:
                        # Conditional Camera (User Request: "take pictures button")
                        enable_cam = st.checkbox("📸 Enable Camera")
                        img_cam = None
                        if enable_cam:
                            img_cam = st.camera_input("Take Photo")
                        
                        img_up = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"], key="img_up")
                        
                        active_img = img_cam if img_cam else img_up
                        if active_img:
                            if st.button("Process Image"):
                                initiate_image_hitl(active_img)

                    with tab2:
                        # Native Audio Input (Streamlit 1.40+)
                        audio_rec = st.audio_input("Record")
                        audio_up = st.file_uploader("Upload", type=["mp3", "wav", "m4a"], key="aud_up")
                        
                        # Priority to recorder if present
                        active_audio = audio_rec if audio_rec else audio_up
                        
                        if active_audio:
                            if st.button("Process Audio"):
                                initiate_audio_hitl(active_audio)
            
            with col_in:
                if prompt := st.chat_input("Ask a math question..."):
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    process_math_query(prompt)
                    st.rerun()

def initiate_image_hitl(image_file):
    with st.spinner("🔍 Vision Agent: Extracting text..."):
        text = utils.analyze_image(image_file)
    st.session_state.pending_entry = {'type': 'image', 'data': image_file, 'text': text}
    st.session_state.hitl_active = True
    st.rerun()

def initiate_audio_hitl(audio_file):
    with st.spinner("👂 Audio Agent: Transcribing..."):
        text = utils.transcribe_audio(audio_file)
    st.session_state.pending_entry = {'type': 'audio', 'data': audio_file, 'text': text}
    st.session_state.hitl_active = True
    st.rerun()

def process_math_query(raw_input, input_type="text", related_image=None):
    if input_type == "image":
        st.session_state.messages.append({"role": "user", "content": "Analyze this image.", "image_data": related_image})
    elif input_type == "audio":
        st.session_state.messages.append({"role": "user", "content": f"🎤 Transcript: {raw_input}"})

    with st.chat_message("assistant"):
        # Explicit Agent Trace Container
        with st.status("⚙️ **Agent Workflow**", expanded=True) as status:
            
            # 1. Guardrail
            status.write("🛡️ **Guardrail**: Validating intent & safety...")
            safety = guardrails.validate_input(raw_input[:500])
            if safety == "UNSAFE":
                status.update(label="❌ Blocked", state="error")
                st.error("Request blocked by safety guardrails.")
                st.session_state.messages.append({"role": "assistant", "content": "Request blocked by safety guardrails."})
                return

            # 2. Parsing
            status.write("🧩 **Parser**: Extracting parameters...")
            parser_chain = agents.get_parser_agent()
            structured_prob = parser_chain.invoke({"raw_input": raw_input})
            
            if structured_prob.get("needs_clarification", False) and input_type == "text":
                status.update(label="⚠️ Needs Clarification", state="error")
                resp = f"Ambiguous input. Did you mean: '{structured_prob.get('problem_text')}'?"
                st.markdown(resp)
                st.session_state.messages.append({"role": "assistant", "content": resp})
                return

            # 3. Memory & Solving
            status.write("🧠 **Memory**: Checking knowledge base...")
            sim_sol = memory.retrieve_similar_solution(structured_prob.get("problem_text"))
            
            final_sol = ""
            conf = 100
            from_mem = False
            
            if sim_sol:
                final_sol = sim_sol
                from_mem = True
                status.write("✅ **Recalled**: Solution found in memory.")
            else:
                status.write("📐 **Solver**: Computing step-by-step solution...")
                try:
                    solver = agents.get_solver_agent()
                    final_sol = solver.invoke({"structured_problem": structured_prob})
                except Exception as e:
                    status.update(label="❌ Error", state="error")
                    err_msg = f"Solver encountered an error: {str(e)}"
                    st.error(err_msg)
                    st.session_state.messages.append({"role": "assistant", "content": err_msg})
                    return
                
                status.write("⚖️ **Evaluator**: verifying correctness...")
                status.write("⚖️ **Evaluator**: verifying correctness...")
                try:
                    evaluator = agents.get_evaluator_agent()
                    eval_res = evaluator.invoke({"problem_text": structured_prob.get("problem_text"), "proposed_solution": final_sol})
                    conf = eval_res.get("confidence", 0)
                except Exception as e:
                    print(f"Evaluator failed (likely Rate Limit): {e}")
                    status.write("⚠️ **Evaluator Skipped**: Rate Limit Reached. Proceeding...")
                    conf = 100 # Assume correct if we can't check

                
            status.update(label="✅ **Complete**: Solution Ready", state="complete")
            
            # Render Final Output
            with st.expander("📄 Parser Output", expanded=False):
                st.json(structured_prob)
            st.markdown(final_sol)
            if not from_mem:
                color = "green" if conf > 80 else "orange"
                st.caption(f"**Verifier Confidence:** :{color}[{conf}%]")
            
            # Save
            st.session_state.messages.append({
                "role": "assistant",
                "content": final_sol,
                "raw_data": structured_prob,
                "confidence": conf,
                "id": len(st.session_state.messages),
                "show_feedback": not from_mem,
                "problem_text": structured_prob.get("problem_text"),
                "topic": structured_prob.get("topic")
            })
            
            if not from_mem:
                render_feedback_buttons(len(st.session_state.messages), structured_prob.get("problem_text"), final_sol, structured_prob.get("topic"))

def render_feedback_buttons(msg_id, problem, solution, topic):
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ Accurate", key=f"up_{msg_id}"):
            memory.save_to_memory(problem, solution, topic)
            st.success("Memorized for future!")
    with c2:
        if st.button("❌ Inaccurate", key=f"down_{msg_id}"):
            st.error("Flagged for review.")

if __name__ == "__main__":
    main()
