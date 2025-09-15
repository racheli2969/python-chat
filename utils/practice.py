# find posts that contain a certain word

posts = ["green d", "Ai is Recursive d", " find AI", "AI is hidden", "AIS"]


def find_word_in_post(word, post):
    words = post.split()
    return word in words


def return_posts_with_word(word):
    selected_posts = list()

    for post in posts:
        if find_word_in_post(word, post):
            selected_posts.append(post)

    return selected_posts


words = return_posts_with_word("AI")
print(words)