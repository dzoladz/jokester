from django.shortcuts import render
import random


# Create your views here.
def index(request):
    jokes = [
        ['Why did the heart specialist recommend that his patients go to the library?', 'He heard they are good for circulation.'],
        ['Why does Dracula go to the library?', 'To sink his teeth into a good book.'],
        ['How do librarians flirt?', 'They ask for your call number.'],
        ['Where is the slipperiest part of the library?', 'The non-friction section.'],
        ['How do the books stay warm in the library?', 'They wear book jackets.'],
        ['Why can’t librarians finish mystery books?', 'They keep reading between the lines.'],
        ['What advice do you often get from a librarian?', 'Believe in your shelf.'],
        ['Why did the ghost keep coming back to the library?', 'Because he went through his books too quickly.'],
        ['What did the librarian tell the person who checked out 100 books?', 'Don’t overdue it.'],
        ['Where does the library keep books about conspiracies?', 'Right behind you.'],
        ['Why did the local library ban drinks?', 'Because a person poured some milk on the serials.'],
        ['Why do librarians love good jokes about books?', 'They always get the reference.'],
        ['Why don\'t modern libraries keep dystopian books?', 'Because they are so 1984.'],
        ['What did the cops say when the librarian died after a book fell on top of her head?', 'She had her shelf to blame.'],
        ['What does a librarian wish someone on their birthday?', 'Many many happy returns.'],
        ['What do librarians say?', 'I have not metadata I did not find likable.'],
        ['What do people who cannot part with their library books say?', 'My love is overdue.'],
        ['Why are libraries the tallest buildings in the world?', 'Because they have so many stories.']
    ]

    i = random.randint(0, len(jokes) - 1)
    question, answer = jokes[i]
    joke = f'{question.strip()} {answer.strip()}'

    return render(request, 'base.html', {'joke': joke})
