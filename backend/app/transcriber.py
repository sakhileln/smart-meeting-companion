import whisper
import os
from typing import Optional
from fastapi import UploadFile, HTTPException, status
import uuid

class AudioTranscriber:
    def __init__(self, model_size: str = "base"):
        self.model = whisper.load_model(model_size)
        self.upload_dir = "uploads/"
        os.makedirs(self.upload_dir, exist_ok=True)
    
    async def save_upload_file(self, file: UploadFile) -> str:
        """Save uploaded file to disk and return the file path"""
        file_extension = os.path.splitext(file.filename)[1] if file.filename else ".wav"
        file_name = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(self.upload_dir, file_name)
        
        try:
            contents = await file.read()
            with open(file_path, "wb") as f:
                f.write(contents)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error saving file: {str(e)}"
            )
        finally:
            await file.close()
            
        return file_path
    
    async def transcribe_audio(self, file_path: str) -> str:
        """Transcribe audio file to text using Whisper"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found: {file_path}")
            
        try:
            # Load audio and pad/trim it to fit 30 seconds
            audio = whisper.load_audio(file_path)
            audio = whisper.pad_or_trim(audio)
            
            # Make log-Mel spectrogram and move to the same device as the model
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
            
            # Detect the spoken language
            _, probs = self.model.detect_language(mel)
            detected_lang = max(probs, key=probs.get)
            
            # Decode the audio
            options = whisper.DecodingOptions(fp16=False)
            result = whisper.decode(self.model, mel, options)
            
            return result.text
            
        except Exception as e:
            raise Exception(f"Error during transcription: {str(e)}")
    
    async def process_meeting_audio(self, file: UploadFile) -> dict:
        """Process meeting audio: save file and transcribe"""
        # Save the uploaded file
        file_path = await self.save_upload_file(file)
        
        try:
            # Transcribe the audio
            transcript = await self.transcribe_audio(file_path)
            
            return {
                "file_path": file_path,
                "transcript": transcript,
                "success": True
            }
            
        except Exception as e:
            # Clean up the file if there was an error
            if os.path.exists(file_path):
                os.remove(file_path)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error processing audio: {str(e)}"
            )
