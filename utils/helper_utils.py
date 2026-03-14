import os
import base64
from groq import Groq
from config.config import app_config
import io

def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode('utf-8')

def analyze_image(image_file):
    client = Groq(api_key=app_config.GROQ_API_KEY)
    
    try:
        base64_image = encode_image(image_file)
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
            max_tokens=1024,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Vision API failed ({e}), falling back to EasyOCR.")
        return analyze_image_with_easyocr(image_file)

def analyze_image_with_easyocr(image_file):
    try:
        import easyocr
        import numpy as np
        from PIL import Image
        
        image_file.seek(0) 
        image = Image.open(image_file)
        image_np = np.array(image)
        
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(image_np, detail=0)
        return " ".join(result)
    except Exception as e:
        return f"Error analyzing image with EasyOCR: {str(e)}"

def transcribe_audio(audio_file):
    client = Groq(api_key=app_config.GROQ_API_KEY)
    
    try:
        transcription = client.audio.transcriptions.create(
            file=(audio_file.name, audio_file.read()),
            model="whisper-large-v3",
            prompt="Transcribe this question clearly.",
            response_format="text"
        )
        return transcription
    except Exception as e:
        return f"Error transcribing audio: {str(e)}"
