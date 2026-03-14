from fpdf import FPDF
import os

def export_session_to_pdf(messages):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)
        
        pdf.cell(200, 10, text="Math Mentor - Session History", new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.ln(10)
        
        for msg in messages:
            if msg["role"] == "user":
                pdf.set_font("Helvetica", 'B', 12)
                text = f"User: {msg['content']}".encode('latin-1', 'replace').decode('latin-1')
                pdf.multi_cell(0, 10, text=text)
            else:
                pdf.set_font("Helvetica", '', 12)
                content = msg['content'].replace("**", "")
                text = f"Mentor: {content}".encode('latin-1', 'replace').decode('latin-1')
                pdf.multi_cell(0, 10, text=text)
            pdf.ln(5)
            
        os.makedirs("exports", exist_ok=True)
        filepath = "exports/session_notes.pdf"
        pdf.output(filepath)
        return filepath
    except Exception as e:
        print(f"Error exporting PDF: {e}")
        raise e
