
import os
from openai import OpenAI


class AIGateway:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = (
            OpenAI(api_key=self.api_key)
            if self.api_key else None
        )

    def is_connected(self):
        return self.client is not None

    def generate(self, prompt, model="gpt-4o-mini"):
        if not self.client:
            return {
                "success": False,
                "error": "OPENAI_API_KEY is not configured"
            }

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are PROJECT YOUTUBE AI, "
                            "an expert YouTube content assistant."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7
            )

            return {
                "success": True,
                "content": response.choices[0].message.content
            }

        except Exception as error:
            return {
                "success": False,
                "error": str(error)
            }


ai_gateway = AIGateway()
