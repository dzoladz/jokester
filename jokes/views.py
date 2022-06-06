from django.shortcuts import render
from pathlib import Path
import random


# Create your views here.
def index(request):
    jokes = []
    with open(Path(Path(__file__).parent / 'jokes.txt')) as file:
        lines = file.readlines()
        question = 'Where is the slipperiest part of the library?'
        answer = 'The non-friction section.'

        for line in lines:
            line.strip()
            if line.startswith('Q:'):
                question = line.split('Q:')[1]
            elif line.startswith('A:'):
                answer = line.split('A:')[1]

            joke = f'{question.strip()} {answer.strip()}'
            jokes.append(joke)

    joke = jokes[random.randint(0, len(jokes) - 1)]

    return render(request, 'base.html', {'joke': joke})
