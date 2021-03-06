import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here
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

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit= None)
    all_comments = submission.comments.list()
    print('len(all_comments)=',len(all_comments))

    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
   

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    submission.comments.replace_more(limit= None)
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'mb4bot':
            not_my_comments.append(comment)
    print('len of not_my_comments=', len(not_my_comments))

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)
    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        submission.reply(generate_comment())
    
        
    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        submission.comments.replace_more(limit= None)
        comments_without_replies=[]
        for comment in not_my_comments:
            authors = []
            for reply in comment.replies:
                authors.append(str(reply.author))
            if 'mb4bot' in authors:
                pass
            else:
                comments_without_replies.append(comment)

        # print('comments without replies=', comments_without_replies)
                    
       
       

        # comments_without_replies = []
        # for n_comment in not_my_comments:
        #     for reply in n_comment.replies:
        #         if str(reply.author) != 'mb4bot': 
        #             comments_without_replies.append(n_comment)
        #         elif n_comment in comments_without_replies:
        #             pass
        # print('comments without replies=', comments_without_replies)
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        #Extra credit task: Upvote every comment that contains biden
        # submission.comments.replace_more(limit= None)
        # comment_content=[]
        # for comment in all_comments:
        #     comment_content.append(str(comment.body))
        
        # for a_comment in comment_content:
        #     if 'Biden' in a_comment:
        #         comment.upvote()

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
    try:
        comment = random.choice(comments_without_replies)
        try:
            comment.reply(generate_comment())
        except praw.exceptions.APIException:
            print('deleted comment, cannot reply')
            pass
    except IndexError:
        print('all mine')
        pass
        
        
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    # submission = random.choice ()

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    
    submission = random.choice(list(reddit.subreddit('BotTown2').hot(limit=5)))

    time.sleep(1)