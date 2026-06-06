# Add references
import asyncio
from typing import cast
from dotenv import load_dotenv
from agent_framework import Message
from agent_framework.azure import AzureAIAgentClient
from agent_framework.orchestrations import SequentialBuilder
from azure.identity import InteractiveBrowserCredential
# from azure.identity import AzureCliCredential
import warnings
warnings.filterwarnings(
    "ignore",
    message="response_mode='form_post' is recommended for better security"
)


load_dotenv()

async def main():
    # Agent instructions
    summarizer_instructions="""
    Summarize the customer's feedback in one short sentence. Keep it neutral and concise.
    Example output:
    App crashes during photo upload.
    User praises dark mode feature.
    """

    classifier_instructions="""
    Classify the feedback as one of the following: Positive, Negative, or Feature request.
    """

    action_instructions="""
    Based on the summary and classification, suggest the next action in one short sentence.
    Example output:
    Escalate as a high-priority bug for the mobile team.
    Log as positive feedback to share with design and marketing.
    Log as enhancement request for product backlog.
    """

    # Create the chat client
    credential = InteractiveBrowserCredential()
    async with (
        AzureAIAgentClient(credential=credential) as chat_client,
    ):
    

        # Create agents
        summarizer = chat_client.as_agent(
            instructions=summarizer_instructions,
            name="summarizer",
        )

        classifier = chat_client.as_agent(
            instructions=classifier_instructions,
            name="classifier",
        )

        action = chat_client.as_agent(
            instructions=action_instructions,
            name="action",
        )
    
        # Alternative feedback example:
        #  """I reached out to your customer support yesterday because I couldn't access my account. 
        # The representative responded almost immediately, was polite and professional, and fixed the 
        # issue within minutes. Honestly, it was one of the best support experiences I've ever had."""

        # Initialize the current feedback
        feedback = """
        The dashboard is fast and easy to use, and I appreciate the clean layout.
        However, I often struggle to find historical reports because there is no advanced search option.
        Adding filters and saved searches would make the platform much more efficient.
        """

        # Build sequential orchestration
        workflow = SequentialBuilder(participants=[summarizer, classifier, action]).build()
    
        # Run and collect outputs
        outputs: list[list[Message]] = []
        async for event in workflow.run(f"Customer feedback: {feedback}", stream=True):
            if event.type == "output":
                outputs.append(cast(list[Message], event.data))
    
    
        # Display outputs
        if outputs:
            for i, msg in enumerate(outputs[-1], start=1):
                name = msg.author_name or ("assistant" if msg.role == "assistant" else "user")
                print(f"{'-' * 60}\n{i:02d} [{name}]\n{msg.text}")
    

if __name__ == "__main__":
    asyncio.run(main())