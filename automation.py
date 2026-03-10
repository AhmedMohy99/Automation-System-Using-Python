import os
import json
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_marketing_bundle(topic):
    print(f"🚀 Generating automation bundle for: {topic}")
    
    prompt = f"""
    Act as a senior marketing strategist for We-Wave-Agency. 
    Create a marketing bundle for the topic: '{topic}'.
    Include:
    1. A 300-word SEO Blog Post.
    2. A catchy Instagram Caption with hashtags.
    3. A professional LinkedIn post.
    Return the result in strictly JSON format with keys: 'blog', 'instagram', 'linkedin'.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )

    content = json.loads(response.choices[0].message.content)
    
    # Save to a local "database" file automatically
    with open('campaign_vault.json', 'a') as f:
        json.dump({topic: content}, f)
        f.write('\n')
        
    return content

# Example trigger
# bundle = generate_marketing_bundle("Why one-stop marketing agencies beat freelancers")
