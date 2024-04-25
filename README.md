# Business Traveler AI Chatbot

## Overview
The Business Traveler AI Chatbot offers personalized travel recommendations for business professionals. Built with Flask and utilizing Google's Gemini-Pro AI model, it is designed to enhance the business travel planning process by providing tailored advice based on user inputs.

## Prerequisites
- Python 3.x+
- Flask framework
- Access to Google GenerativeAI services (Note: Gemini API is not available in the UK)

## Technologies Used
- *Flask*: A micro web framework for Python, used for building the web server.
- *Google GenerativeAI (Gemini-Pro model)*: Used to generate dynamic travel recommendations.

## Getting Started
1. Ensure Python and Flask are installed on your system.
2. Clone the project to your local machine.
3. Install necessary Python libraries listed in requirements.txt.
4. Configure environment variables including the API key (not functional in the UK).

## API and External Integrations
This application integrates the Gemini API to generate travel recommendations. Due to restrictions, the Gemini API is currently unavailable in the UK, affecting the chatbot's functionality in this region.

## Project Structure
- app.py: Main Flask application file where routes and configurations are defined.
- requirements.txt: File listing all dependencies necessary to run the project.
- templates/: Directory containing HTML templates for the web interface.

## Note
The application was developed to provide business travelers with AI-powered insights. Due to API geographic restrictions, i can not try the chatbot in the UK you may experience limited functionality. because i build it in home country when i come back i was not able to lunch it.

