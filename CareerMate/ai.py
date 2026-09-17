# ---------------- imports ----------------
from ollama import chat # Import chat function from Ollama library to communicate with the AI model.


# Name of the AI model
MODEL = "gemma3"


def ask_ai(prompt):
    """
    Send a prompt to the local AI model
    and return its response.

    """

    try:

        response = chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content

    except Exception as error:

        print("\nAI request failed.")
        print(error)

        return None


def analyze_candidate(candidate):
    """
    Analyze the candidate's profile
    and provide career guidance.

    """

    prompt = f"""
You are CareerMate, a concise AI career assistant.

Analyze this candidate:

Name: {candidate['name']}
Major: {candidate['major']}
career_stage: {candidate['career_stage']}
Skills: {', '.join(candidate['skills'])}
Interests: {', '.join(candidate['interests'])}

Return ONLY the following format:

🎯 CAREER PATHS

1. Career Path
   One short sentence explaining why it fits.

2. Career Path
   One short sentence explaining why it fits.

3. Career Path
   One short sentence explaining why it fits.

📚 SKILLS TO IMPROVE

• Skill
• Skill
• Skill

🚀 NEXT STEP

One short practical recommendation.

Rules:
- Keep the entire response under 150 words.
- Be concise and specific.
- Do not include an introduction.
- Do not include a conclusion.
- Do not ask the user any questions.
- Do not say "Okay", "Sure", or "Here's an analysis".
- Do not use markdown headings with #.
- Do not add information that is not supported by the candidate's profile.

"""

    return ask_ai(prompt)


def suggest_job_titles(candidate):
    """
    Ask AI to suggest suitable job titles.

    """

    prompt = f"""
You are CareerMate, a career guidance assistant.

Based on this candidate profile:

Major: {candidate['major']}
career_stage: {candidate['career_stage']}
Skills: {', '.join(candidate['skills'])}
Interests: {', '.join(candidate['interests'])}

Suggest exactly 5 suitable job titles.

Return ONLY this format:

1. Job Title
2. Job Title
3. Job Title
4. Job Title
5. Job Title

Rules:
- Match the candidate's skills and interests.
- Consider their career_stage level.
- Keep titles realistic for their background.
- No explanations.
- No introduction.
- No conclusion.
- Do not ask questions.
"""

    return ask_ai(prompt)

def generate_interview_questions(job_title, career_stage):
    """
    Generate interview questions based on the job title
    and the candidate's career stage.
    
    """

    prompt = f"""
You are CareerMate, an interview preparation assistant.

Generate exactly 5 interview questions for:

Job Title: {job_title}
Candidate Career Stage: {career_stage}

The questions must be relevant to the specific job title.

Include a relevant mix of:
- Technical or job-specific questions
- Behavioral questions
- Problem-solving or situational questions

Important:
- If the job is technical, include relevant technical questions.
- If the job is non-technical, use job-specific questions instead of programming or technical questions.
- Match the difficulty to the candidate's career stage.
- Do not assume the candidate has advanced experience.
- Keep questions short and easy to read.

Return ONLY the 5 questions in this format:

1. Question
2. Question
3. Question
4. Question
5. Question

Rules:
- Exactly 5 questions.
- No introduction.
- No conclusion.
- No answers.
- No explanations.
- Do not ask the user anything.
"""

    return ask_ai(prompt)