import os
import base64
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from groq import Groq
import io

def encode_image(image_file):
    """
    Encodes a file-like object (image) to base64 string.
    """
    return base64.b64encode(image_file.getvalue()).decode('utf-8')

def analyze_image(image_file):
    """
    Analyzes an image using Groq's Vision model, falling back to EasyOCR.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return analyze_image_with_easyocr(image_file)

    client = Groq(api_key=api_key)
    
    try:
        # Encode image to base64
        base64_image = encode_image(image_file)
        
        # Try the new "Scout" model (Llama 4 Preview) found in active models list
        model_id = "meta-llama/llama-4-scout-17b-16e-instruct" 
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a Robot. You cannot solve math. You can only read text.\n\nJOB: Output the EXACT text seen in the image.\n\nNEGATIVE CONSTRAINTS (Read Carefully):\n- DO NOT solve the problem.\n- DO NOT calculate anything.\n- DO NOT add 'Step 1', 'Solution', or 'Answer'.\n- DO NOT correct typos.\n\nInput: [Image]\nOutput: [Raw Text String]"
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Transcribe this image. Return ONLY the text visible in the image."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model=model_id,
            temperature=0.0,
            max_tokens=1024, # Limiting tokens to discourage long explanations
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Vision API failed ({e}), falling back to EasyOCR.")
        return analyze_image_with_easyocr(image_file)

def analyze_image_with_easyocr(image_file):
    """
    Fallback: Analyzes an image using EasyOCR.
    """
    try:
        import easyocr
        import numpy as np
        from PIL import Image
        
        # Reset file pointer if needed or re-open
        image_file.seek(0) 
        image = Image.open(image_file)
        image_np = np.array(image)
        
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(image_np, detail=0)
        return " ".join(result)
    except Exception as e:
        return f"Error analyzing image with EasyOCR: {str(e)}"


def transcribe_audio(audio_file):
    """
    Transcribes audio using Groq's Whisper model.
    
    Args:
        audio_file: A file-like object containing the audio.
        
    Returns:
        str: The transcribed text.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Error: GROQ_API_KEY not found."

    client = Groq(api_key=api_key)
    
    # We need to save the file temporarily because Groq client expects a file path or tuple
    # Streamlit UploadedFile is file-like. Groq Python SDK handles file-like objects? 
    # Let's try passing the tuple (filename, file_obj) which is standard for requests/httpx.
    
    try:
        # Whisper model on Groq
        transcription = client.audio.transcriptions.create(
            file=(audio_file.name, audio_file.read()),
            model="whisper-large-v3",
            prompt="Transcribe this math question clearly. Use standard math terminology.",
            response_format="text"
        )
        return transcription
    except Exception as e:
        return f"Error transcribing audio: {str(e)}"
