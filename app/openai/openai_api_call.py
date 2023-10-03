import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_blog_post(articles,keywords):
    # Combine articles and keywords into a single prompt
    prompt = f"Generate a blog post on the topic of {', '.join(keywords)} using the following articles:\n\n"
    prompt += "\n\n".join(articles)
    engine_model="text-davinci-002"
    # Generate the blog post using the OpenAI API
    generated_blog_post = generate_open_api_call(prompt, engine_model)
    return generated_blog_post


def generate_open_api_call(prompt,engine_model="text-davinci-002", max_tokens=180, temperature=0.7, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise Exception("OpenAI API key not found in the .env file")
   # Initialize the OpenAI API client
    openai.api_key = api_key
    # Call the OpenAI API to generate the blog article

        # Call the OpenAI API to generate the text
    response = openai.Completion.create(
            engine=engine_model,
            prompt=prompt,
            max_tokens=max_tokens
        )
    # response = openai.Completion.create(
    #     engine=engine_model,
    #     prompt=prompt,
    #     max_tokens=max_tokens,
    #     temperature=temperature,
    #     top_p=top_p,
    #     frequency_penalty=frequency_penalty,
    #     presence_penalty=presence_penalty
    # )
    # Extract and return the generated text
    generated_text = response.choices[0].text
    return generated_text


