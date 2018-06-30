QUESTIONS = {
    "HELP": {
        "question": "Do you want to start a new session?",
        "response_type": "text",
        "following_stage": "NAME",
        "collect_answer": False
    },
    "NAME": {
        "question": "What is your name?",
        "response_type": "text",
        "following_stage": "ANUMBER",
        "collect_answer": True
    },
    "ANUMBER": {
        "question": "What is your anumber?",
        "response_type": "text",
        "following_stage": "HELP",
        "collect_answer": True
    }
}

ANSWER_TEMPLATE = {
    "NAME": None,
    "ANUMBER": None
}