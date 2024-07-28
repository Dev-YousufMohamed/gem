import os
import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyCzBW_4ev8G4zzcSPlu0_cRXIp_ZXnn8FQ")

model = genai.GenerativeModel('gemini-1.5-flash')

video_file_name = "/content/sample_data/abc.mp4"
video_file = genai.upload_file(path=video_file_name)

# Check whether the file is ready to be used.
while video_file.state.name == "PROCESSING":
    print('.', end='')
    time.sleep(10)
    video_file = genai.get_file(video_file.name)

if video_file.state.name == "FAILED":
  raise ValueError(video_file.state.name)

# Create the prompt.
prompt = "Summarize this video. Then create a quiz with answer key based on the information in the video."

# Make the LLM request.
print("Making LLM inference request...")
response = model.generate_content([video_file, prompt], request_options={"timeout": 600})

# Print the response, rendering any Markdown
print(response.text)
