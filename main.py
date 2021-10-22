import praw

reddit = praw.Reddit(
    client_id="CUlMAgLt1nnsCb9-5wEQww",
    client_secret="d6Q0qATAETX5tmzGM96m9GGdcBq1DA",
    password="Magha@702",
    user_agent="testscript by u/RagingBox08",
    username="RagingBox08",
)
def getNewPost(rslash):
    # rslash = input("enter the name of the subreddit: ")
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    for submission in subreddit.new(limit=5):
        print(submission.url)
        return submission.url, subreddit.title

def getHotPost(rslash):
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    c  = 0
    for submission in subreddit.hot(limit = 6):
        if c == 0:
            c +=1
            continue
        print(submission.url)
        return submission.url, subreddit.title

def getTopPost(rslash):
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    for submission in subreddit.top(limit= 10):
        print(submission.title)
        print(submission.url)
        return submission.url,subreddit.title

subreddit = reddit.subreddit('ImaginaryNetwork')
print(subreddit.title)
for submission in subreddit(limit = 5):
    print(submission.title)
    print()
# print(reddit.user.me())