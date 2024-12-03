from typing import IO

from openai import OpenAI
from pypdf import PdfReader


class ResumeService:
    def __init__(self, resume: IO[bytes], api_key: str, model: str = "gpt-4o-mini"):
        self.resume = resume
        self.resume_text = self._read_resume(resume)
        self._client = OpenAI(api_key=api_key)
        self._model = model

    @staticmethod
    def _read_resume(resume: IO[bytes]) -> str:
        """

        :param resume:
        :return:
        """
        reader = PdfReader(resume)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

    def judge(self, resume_text: str) -> str:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a résumé reviewer. "
                    "Offer a constructive feedback summary of the given résumé, highlighting strong areas and weak. "
                    "Do not use more than 4 sentences."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Can you judge my résumé? Here it is:\n"
                    f"{resume_text}"
                )
            }
        ]
        response = self._client.chat.completions.create(model=self._model, messages=messages)
        msg = response.choices[0].message.content
        return msg
