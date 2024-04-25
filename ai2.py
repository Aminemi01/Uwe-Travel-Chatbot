from flask import Flask, request, jsonify
import google.generativeai as genai
from google.generativeai import GenerativeModel
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

app = Flask(__name__)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
# Replace with your actual API key
API_KEY = "not availnle IN the UK "

genai.configure(api_key=API_KEY)
model = GenerativeModel(model_name="gemini-pro")

def generate_ai_response(user_inputs):
  """
  Generates a comprehensive AI response based on user inputs for the Business Traveler AI Finder Questionnaire.

  Args:
      user_inputs (dict): A dictionary containing user input values for each questionnaire item.

  Returns:
      str: The generated AI response tailored to the user's needs.
  """

  prompt = (
      f"**Business Traveler Profile:**\n"
      f"- Business Travel Goal: {user_inputs['goal']}\n"
      f"- Industry Sector: {user_inputs['industry']}\n"
      f"- Client Engagement Preferences: {user_inputs['client_engagement']}\n"
      f"- Professional Networking Interest: {user_inputs['networking_interest']}\n"
      f"- Business Development Activities: {user_inputs['development_activities']}\n"
      f"- Expected Travel Outcome: {user_inputs['travel_outcome']}\n"
      f"- Preferred Work Environment: {user_inputs['work_environment']}\n"
      f"- Additional Needs: {user_inputs['additional_needs']}\n\n give a specific place or country"
      f"**AI Recommendation:**\n"
      f"Based on your travel goals, industry sector, and preferences, here's a tailored "
      f"recommendation for your business trip:\n"
  )

  # Leverage Gemini API to generate specific recommendations based on user inputs
  # (Note: This section requires further customization for more specific recommendations)
  response = model.generate_content(contents=[{"parts": [{"text": prompt}]}])
  generated_text = response.candidates[0].content.parts[0].text
  # Combine user details and generated recommendations for a comprehensive response
  return (
      #f"{prompt}\n"
      f"{generated_text}\n"
  )

@app.route("/recommendations", methods=["POST"])
def process_user_input():
  user_inputs = request.get_json()
  if not user_inputs:
    return jsonify({"error": "Missing user input data."}), 400

  # Validate user inputs (optional)

  ai_response = generate_ai_response(user_inputs)
  gen_text=to_markdown(ai_response)
  print(gen_text._repr_markdown_())
  return jsonify({"response": ai_response})

if __name__ == "__main__":
  app.run(debug=True)
