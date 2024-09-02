
import google.generativeai as genai

def assitant(qst):
  genai.configure(api_key="your gemini API key")

  # Set up the model
  generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens":64,
  }
  """256"""
  """2048"""
  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]

  model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

  convo = model.start_chat(history=[
    {
      "role": "user",
      "parts": ["the capital of algeria"]
    },
    {
      "role": "model",
      "parts": ["Algiers"]
    },
    {
      "role": "user",
      "parts": ["today's date"]
    },
    {
      "role": "model",
      "parts": ["March 2, 2023"]
    },
    {
      "role": "user",
      "parts": ["we are actually april 1st"]
    },
    {
      "role": "model",
      "parts": [
        "As an AI language model, I do not have real-time information about the current date. My knowledge is based on the data I was trained on, which may not be up-to-date. To get the most accurate information, I recommend checking a reliable calendar or news source."]
    },
    {
      "role": "user",
      "parts": ["what is the factorial of 10"]
    },
    {
      "role": "model",
      "parts": ["3,628,800\n\n**Calculation:**\n\n10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3,628,800"]
    },
    {
      "role": "user",
      "parts": ["what is the smallest known star"]
    },
    {
      "role": "model",
      "parts": [
        "The smallest known star is **EBLM J0555-57Ab**, located about 600 light-years from Earth. It is slightly larger than Saturn in size, with a radius of about 0.84 times that of Jupiter. \n\nDespite its small size, it is still a true star, meaning it undergoes nuclear fusion in its core."]
    },
    {
      "role": "user",
      "parts": ["is there really a star with a diameter of 20km"]
    },
    {
      "role": "model",
      "parts": [
        "No, there is no known star with a diameter of only 20 kilometers. The smallest known star, EBLM J0555-57Ab, has a diameter of about 120,000 kilometers, which is still significantly larger than 20 kilometers.\n\nStars are massive celestial objects that typically have diameters ranging from hundreds of thousands to millions of kilometers. A star with a diameter of only 20 kilometers would be far too small to sustain nuclear fusion in its core, which is the defining characteristic of a star."]
    },
  ])

  convo.send_message(qst)
  ans = convo.last.text
  return ans
