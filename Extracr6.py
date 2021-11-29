
import praw
import random
import datetime
import time

madlibs = [
    "[GREEN] is the [BEST] [COLOR]. [LOTS] of [STUFF] are green like [SALAD].", "[EVERYONE] [SHOULD] [LIKE] the [COLOR] green."
    "I [LOVE] [GREEN].", "[GREEN] is a [GREAT] color. There should be [BOOKS] dedicated to why [GREEN] is such a [GREAT] color.", 
    "[GREEN] should be the only [COLOR] used in art. There is no need for any other [COLOR] as long as [GREEN] exists", 
    "[EVERYTHING] should be [GREEN]. If [SOMETHING] is not [GREEN], then it probably is not [COOL]",
    "[GREEN] should be implented into [SCHOOL] curriculum. There should be [CLASSES] on why [GREEN] is a [GREAT][COLOR]"
]

replacements = {
    'GREEN' : ['the color green', 'green', 'the colour green'],
    'GREAT' : ['great', 'magnificent', 'fantastic', 'wonderful', 'amazing'],
    'BEST'  : ['greatest', 'best', 'most fantastic', 'most magnificent'],
    'BOOKS' : ['articles', 'journals','studies','research'],
    'SALAD' : ['plants', 'pickles', 'leaves', 'frogs', 'spinach'],
    'LOTS'  : ['lots', 'a whole lot', 'ridiculous amounts'],
    'STUFF' : ['stuff', 'things', 'fun things'],
    'COLOR' : ['hue','tone','color'],
    'EVERYONE' : ['Everyone', 'Everybody on planet earth', 'People everywhere', 'You'],
    'SHOULD' : ['should', 'must', 'needs to'],
    'BECOME' : ['become', 'turn into', 'try to be'],
    'LIKE' : ['enjoy', 'be keen to ', 'admire'],
    'EVERYTHING':['Everything', 'every object', 'all matter'],
    'SOMETHING':['an object', 'something', 'an item'],
    'COOL': ['awesome', 'magnificent', 'stupendous'],
    'CLASSES': ['courses', 'lectures', 'presentations'],
    'SCHOOL': ['school', 'college', 'university', 'highschool'],
    'LOVE': ['adore', 'enjoy', 'am apreciative of']
    }

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    
    o_sentence = random.choice(madlibs)
    for t in replacements.keys():
        o_sentence = o_sentence.replace('['+t+']', random.choice(replacements[t]))
    return o_sentence

# connect to reddit 
reddit = praw.Reddit('bot', user_agent= 'mb4bot')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTown2/comments/r2yref/green_thread/?'
submission = reddit.submission(url=submission_url)

submission.comment_sort = "new"
comments = submission.comments.list()
for comment in comments:
    if comment == comments[0]:
        comment.reply(generate_comment())