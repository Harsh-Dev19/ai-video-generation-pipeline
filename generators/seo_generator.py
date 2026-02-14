from config import client

def generate_seo(script):
    prompt = f"""
    Based on the following script, generate:

    1. A highly clickable YouTube title (max 60 characters)
    2. A 2-paragraph SEO optimized description
    3. 15 trending hashtags

    Format:

    TITLE:
    ...

    DESCRIPTION:
    ...

    HASHTAGS:
    ...

    Script:
    {script}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
