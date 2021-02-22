.. _midterm:

Midterm test preparation
========================

This week you will take a programming test worth 20% of the course. The format
of this test is deliberately similar to the programming exam in May that makes
up the other 80% of the assessment. This test therefore provides both some feedback
on how you are progressing in the course, and an opportunity to practice for the
end of term exam. This is a programming module, so the midterm test will consist
of programming exercises. The content which will be examined in the test is
everything covered up to and including week 6. There won't be any new concepts
introduced during the test, however the questions may suggest that you use
Python modules, classes, or functions that haven't previously been introduced in
the course. These will always be similar in character to ones that have
previously been mentioned, and the test instructions will explicitly link to the
Python documentation for any features they suggest.

Test format
-----------

The final exam will be two hours long and comprise 4 questions, each of which
will be marked out of 20. The midterm test will be 40 minutes long, so to keep
the question format consistent with the final exam, there will a single
question. The extra 10 minutes is to give you some flexibility, because in the
final exam you could spend more time on some questions than others. The
question will be subdivided into identified parts with a specified number of
marks associated with each.

The test will work using GitHub Classroom. The link to accept the test
"assignment" will be distributed at the start time of the test, simultaneously in the
course Teams channel, by email, and in the Piazza forum. The test repository
will contain a file :file:`README.rst` containing the questions, skeleton code
appropriate to the questions, and tests. GitHub shows :file:`README.rst` files on
the repository web page, and the instructions will be easier to read there since
any links will be clickable.

The mark scheme
---------------

Of the 20 marks for each question, 4 will be explicitly for basic style. 2 marks
will be for passing flake8 with no errors. If there are only a handful of minor
flake8 errors then you will receive 1 mark, and if there are more than that you
will receive 0. flake8 is an imperfect tool, so the marker will check the output
of flake8 and disregard any false positives. The other 2 marks will be allocated
on a similar basis for basic style matters that flake8 cannot check, such as
conforming with naming conventions and commenting appropriately.

The remaining 16 marks will be allocated to the various parts of the questions. As with a
written maths test, getting the correct final answer is necessary but not
sufficient. A full marks answer to a question will be functionally correct, have
optimal :term:`algorithmic complexity`, and be elegant and readable. The tests
provided are an aid to writing correct code: passing the tests does not prove
that your answer is correct. For example, your code could produce the correct
output in the cases tested but nonetheless fail to implement the specification in
the question. For the avoidance of doubt, a correct answer is one which
correctly implements the specification, not simply one which passes the tests
provided. 

As a rough guide, a solution which produced the correct output but was very
inelegantly written (for example taking many too many steps to achieve simple
functionality) and which used a suboptimal algorithm could be expected to earn
half of the marks available for a question.

Using git in the test
---------------------

You should accept the test from GitHub classroom, and clone the test repository
into the folder you created for the course, just like you have been doing for
the exercise repositories. This will help ensure that you are programming in
the same environment you have been using all along, and therefore avoid any
unfortunate misconfiguration surprises in the test.

This is a test of programming as a whole, so using git correctly is a part of
the test. This has some consequences for how you should go about the test:

1. Commit *and* push your work as you go along. Do not rely on committing once
   at the end of the test. You will be marked on what you have pushed to GitHub
   at the end of the test period. If the first time that you try to push
   something to GitHub is at the end of the test time, and something goes wrong, then
   you will receive 0% for the test, because you will not have pushed any
   answers.
2. Don't forget to `git add` any files you need to create. If you don't add them
   to the repository, they won't be pushed and therefore they won't be marked.

.. warning::

    If you commit and push often as you go through the test then not only will
    you know that you have some marks in the bank already, but you will have a
    record of what you had done at each point in time. In the unlikely event of a failure outside your
    control, such as your network failing or GitHub going down, it will be very
    easy to assign the correct marks to students who have already pushed a large
    part of their work to GitHub. At the other extreme, it will be difficult to
    ascribe any credit at all to students with no pushed work who then push a
    single commit to GitHub after the time has expired.

Preparing for the test
----------------------

The way to prepare for the test is to program. In the first instance, you should
make sure you have completed all of the programming exercises for the previous
weeks. Ensure that you can run and pass all the tests locally on your machine,
and also ensure that you have pushed everything to GitHub and that the tests
show as passing there.

Once you've gone through the previous exercises, you should attempt the practice
questions here. Each of these is a question similar in format and length to the
questions on the exam. Just like on the exam, the question is specified in the
:file:`README.rst` file in the exercise repository. When you first attempt each
of these exercises, you should set yourself a 40 minute timer and see what you
can get done (and committed and pushed!) in the time you would have in the test.
After that, if you haven't finished, then go on and finish the exercise.
Programming is a practical discipline, and finishing one exercise will make you
faster and more capable when you attempt the next one.

Exercises
---------

.. proof:exercise::

    Obtain the `first practice problem from GitHub Classroom
    <https://classroom.github.com/a/wNgTuHeo>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

.. note::

    Do not forget to commit and push as you go. Do not leave this until the end
    of the test.

.. proof:exercise::

    Obtain the `second practice problem from GitHub Classroom
    <https://classroom.github.com/a/fQmijiXp>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

Midterm test instructions
-------------------------

1.  The midterm test will start at 0900 UTC (London time) on Friday 26 February 2021 and will run for 40
    minutes. Students with additional time will be contacted about this separately.
2.  The test will take the form of a GitHub classroom assignment, just like all of
    the exercises. The URL to accept the assignment will be posted at the start
    of the test on the `module Team <https://teams.microsoft.com/l/team/19%3ae96b9a199b15419281f55f454d240249%40thread.tacv2/conversations?groupId=1b12939c-d8c9-4e4d-a291-0ff35d57869f&tenantId=2b897507-ee8c-4575-830b-4f8267c3d307>`__, as Blackboard announcement, and posted on
    Piazza. Of these, the Team is the most instant form of communication so you
    are advised to look there and use the other sources as a backup.
3.  The test instructions are in the :file:`README.md` in the repository.
    GitHub will show this to you on the repository website. The instructions
    are very similar to those for the practice problems above, so you should
    make sure you have tried those in advance of the test.
4.  You submit your work by committing and pushing to the repository on GitHub
    created when you accept the GitHub Classroom assignment. You must commit and
    push as you go along. **There is no additional upload time at the end of the test period.**
5.  If you have a problem during the midterm test, you should post a question
    `on Piazza <https://piazza.com/class/kjob8in6eox1bp>`__. During the test,
    Piazza will be configured so that student posts can only be seen by the
    instructors. Other than this difference you should follow `the instructions
    on what to do in case of problems <_static/If_you_have_a_problem.pdf>`__ 
    provided by the maths exams office in their
    email of 11 February. In particular, if those instructions require you to
    `email the exam team <mailto:maths.exams@imperial.ac.uk>`__ after the test
    then you should do so. Posting on Piazza is only a mechanism for getting
    immediate help during the exam.
6.  The usual `academic integrity rules for remote assessments <_static/Academic_Integrity.pdf>`__ 
    apply. In
    particular, you may consult any resource published on the internet, but you may
    not seek help from anyone else, whether in person, by email, chat message,
    forum post or any other means.
