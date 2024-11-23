from openai import OpenAI

client = OpenAI()

def analyze_dataset_with_gpt(data_json: str, user_request: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a data analyst. Here's the dataset in JSON format: \n{data_json}\n"
                },
                {
                    "role": "user",
                    "content": user_request,
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"