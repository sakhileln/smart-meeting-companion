from typing import List, Dict, Any
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

class MeetingSummary(BaseModel):
    summary: str
    key_points: List[str]
    action_items: List[Dict[str, str]]  # List of {description: str, assignee: str, due_date: str}

def generate_meeting_summary(transcript: str) -> MeetingSummary:
    """
    Generate a summary, key points, and action items from a meeting transcript.
    Uses OpenAI's GPT model to analyze the transcript.
    """
    if not transcript.strip():
        raise ValueError("Transcript cannot be empty")
    
    try:
        # Prepare the prompt for the model
        prompt = f"""You are an AI assistant that helps summarize meetings and extract action items. 
        Given the following meeting transcript, please provide:
        1. A concise summary of the meeting (2-3 paragraphs)
        2. 3-5 key points discussed
        3. Action items with assignees and due dates (format as a JSON array of objects with 'description', 'assignee', 'due_date' fields)
        
        Transcript:
        {transcript}
        
        Please format your response as a JSON object with the following structure:
        {{
            "summary": "...",
            "key_points": ["...", "..."],
            "action_items": [
                {{"description": "...", "assignee": "...", "due_date": "..."}},
                ...
            ]
        }}"""
        
        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes meetings and extracts action items."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        
        # Extract the content from the response
        result = response.choices[0].message.content.strip()
        
        # Parse the JSON response
        import json
        summary_data = json.loads(result)
        
        return MeetingSummary(**summary_data)
        
    except Exception as e:
        raise Exception(f"Error generating meeting summary: {str(e)}")

async def process_meeting_summary(transcript: str) -> dict:
    """
    Process a meeting transcript to generate a summary, key points, and action items.
    """
    try:
        # Generate the meeting summary
        meeting_summary = generate_meeting_summary(transcript)
        
        # Format the response
        return {
            "summary": meeting_summary.summary,
            "key_points": meeting_summary.key_points,
            "action_items": meeting_summary.action_items,
            "success": True
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }
