<p align="center"><a href="#" target="_blank" rel="noopener noreferrer"> <img src="https://image.ibb.co/evGJH7/Artboard_1_3x.png" alt="Recommender Service logo"></a></p>

<h2 align="center">Introduction</h2>
You see the 'P2EM' in the Logo above? Do you have any idea what that means?

Let me help you.

P2EM refers to _"Plan to Embarass Myself"_

To understand the background story, read my article, \*
<a href="https://codeburst.io/how-i-plan-to-embarrass-myself-by-attempting-to-learn-12-incredibly-hard-skills-one-a-month-622ab0acc05b" target="_blank" rel="noopener noreferrer">How I Plan to Embarass Myself ...</a>

Hey, read it :)

<h2 align="center">What does this do?</h2>
If you read the article above, you should get a sense of what this is about.

The service (largely written in Python) recommends movies based on a user's previous movie ratings using Machine Learning.

Oops. That was a mouthful.

<h2 align="center">Where can I try this out? </h2>
I'm currently building out a web client where you can try this.

I'll have the link here, when there's something pretty for you to see :)

<h2>How do I run the app locally?</h2>
Yeah, I've got your back.

1.  Clone the repo

```bash
git clone https://github.com/ohansemmanuel/recommender-service.git
```

2.  Create a .env file

```bash
cd recommender-service
touch .env
```

3.  The env file requires 4 important variables

```env
JWT_SECRET_KEY
USERNAME
PASSWORD
USER_ID
```

* JWT_SECRET_KEY is required by Flask-JWT for some encryption.

* USERNAME and PASSWORD will be used to access authorized resources. These should be **unique strings**.

* USER_ID is required, just like the username and password. This should be an **Integer**

4.  Install the app dependencies

```bash
pip install
```

5.  If you have some experience with Python development, you may need to have the app loaded from a virtual environment.

### Does this explanation suck?

I'll refactor pretty soon. Still writing out the code. It never gets completed, does it? :(
