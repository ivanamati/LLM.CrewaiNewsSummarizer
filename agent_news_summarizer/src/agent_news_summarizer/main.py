#!/usr/bin/env python
import sys
from crew import LatesstAiDevelopmentCrew


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI & LLM news for developers'
    }
    print(LatesstAiDevelopmentCrew().crew().kickoff(inputs=inputs))

run()
