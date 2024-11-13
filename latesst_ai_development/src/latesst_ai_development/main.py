#!/usr/bin/env python
import sys
from crew import LatesstAiDevelopmentCrew


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI & LLM latest news'
    }
    print(LatesstAiDevelopmentCrew().crew().kickoff(inputs=inputs))

run()
