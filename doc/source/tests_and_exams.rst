How to do this course
---------------------

Programming, like mathematics, is a practical, problem solving discipline. It's
not possible to learn to program just by reading notes and watching lectures. To
learn to program you need to put the content of the course into practice by
writing code. The structure of this course is designed to help you to really
understand new concepts in programming by putting them into practice. Each week,
we run through the same cycle:

1. Read the notes
2. Watch the videos
3. Do the quiz
4. Write the code

The notes
.........

All of the new material we cover in this course is presented in these notes.
Each chapter contains the material for one week of term, so in week :math:`n`,
you work through chapter :math:`n`. The notes always the starting point for your work.
Each chapter will introduce new concepts in programming, often tied back to
related mathematical concepts, and always illustrated by practical code
examples. Python has excellent `official online documentation
<https://docs.python.org/3/>`_, and we link to that throughout the text.
External links show up in orange while :ref:`internal links to other parts of
the notes <introduction>` are red. Sometimes we introduce counterexamples:
illustrations of code errors or bad implementation ideas. These will be flagged
with a big red cross:

.. container:: badcode

    .. code-block:: python3

        print "Hello World"

Conversely, if it's necessary in context to highlight which approach is the
correct one, the code will come with a big green tick:

.. container:: goodcode

    .. code-block:: python3

        print("Hello World")

At the end of each chapter there is a glossary containing key new concepts
introduced in that chapter. Always check the glossary and convince yourself that
you understand all the terms introduced there, this is a good check on whether
you have understood the chapter as a whole. However, there is more to learning
new concepts than just the vocabulary, so don't be tempted to skip reading the
chapter and just jump to the glossary!

The chapters broadly alternate between introducing new programming concepts,
such as :ref:`objects <objects>`, :ref:`abstract data types
<abstract_data_types>`, or :ref:`inheritance <inheritance>`, and
covering various aspects of the craft of programming, such as :ref:`style
<inheritance>` and :ref:`debugging <debugging>`. In this way the course combines specific programming knowledge
with more general coding skills.

The videos
..........

Throughout the notes are links to videos. These aren't typical lecture videos in
that they're not primarily focussed on delivering the new ideas in the course.
In particular, the videos don't set out to duplicate the delivery of the
material in the notes. Instead, the videos focus on putting the concepts into
practice, often by showing live coding sessions. Usually you'll want to watch
the video for a given section *after* reading the corresponding notes.

The quizzes
...........

Towards the end of each chapter is a link back to a quiz on Imperial's
Blackboard system. The quizzes are designed to allow you to convince yourself
that you've understood the material in the chapter. Sometimes they will simply
be multiple choice questions testing your understanding of the material, but
sometimes you will need to open up Python and try things out in order to work
out the right answer. The quizzes do not contribute to your module grade, but how
well you are doing on them is an indication of your progress on the module.

The exercises
.............

As we've already noted, really learning to program better is only achieved by
writing code. The core of each week's activities is therefore to put the new
concepts and programming structures you've learned into practice. The
programming exercises are given at the end of each chapter, just before the
glossary. Each time there will be a skeleton code available from
:ref:`GitHub Classroom <fons:github_classroom_exercise>` which provides the starting
point. Sometimes you might be asked to complete a piece of code while on other
occasions you'll need to write a whole Python module from scratch. Each set of
exercises will come with a matching set of tests. These are small programs which
check whether your code produces the correct responses to a range of inputs.
Tests like this provide immediate feedback and enable you to know how you are
doing without having to wait for code to be submitted and marked.

.. note::

    Solutions to exercises will not be issued. The notes and accompanying
    example code contain examples of the same programming constructs that the
    exercises require you to implement, and the tests provide a mechanism to
    know when you have a correct answer. There are also help mechanisms via the
    course forum and the lab sessions. Issuing solutions to problems would
    simply encourage students to study the solutions rather than write code, and
    the only way to learn to program is to write code.

Assessment
..........

The weekly quiz and exercises are not assessable: they are formative activities
designed to help you learn the module. Instead, the module will be assessed by
two controlled programming assessments, effectively programming exams. The first
programming assessment will be held in week 7 and will be worth 20% of the
marks for the course. This provides an opportunity to receive feedback in the
middle of the term, and is a practice for the main exam. The :ref:`course contents for
week 7 <midterm>` will comprise practice programming exercises for this midterm test.
The second programming assessment will be held in the main May exam period and
will count for the other 80% of the course.

The instructions and skeleton code for the programming exercises will be
released at a fixed time on GitHub Classroom, and the code which you have
committed to GitHub by the end of the allotted time will be marked.

The exam questions will be similar to the weekly exercises in the course,
and may include new programmes to write from specification, modifications or
extensions to be made to code which is provided, and debugging exercises in
which defective code is provided which you need to correct. Marks will be
allocated both for the functional correctness of the code written, and for
good style and following Python coding conventions.


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



Exam preparation
----------------

The exam will be similar in format to the :ref:`midterm test <midterm>`, so all
of the advice about preparing applies there too. As with all second year
elective modules, the exam will comprise four questions, each marked out of 20.

As with everything in this course, the one thing you can do to effectively
prepare for the exam is to program. You should complete any of the exercises in
the course that you have not yet done, and more exercises are given below.

Exam scope
~~~~~~~~~~

Everything we have covered in the course up to and including week 10 will be
fully examinable. The week 11 material is not examinable with the
following exceptions:

1. You may need to use :term:`abstract base classes <abstract base class>` from
   the standard library to check the type of variables. This is simply what you
   have been doing all term, for example using :class:`numbers.Number` to check
   that a value is numeric.
2. The skeleton code may include :term:`abstract base classes <abstract base
   class>` from which your classes may need to inherit. This is actually a help
   to you in the exam, because the :term:`abstract methods <abstract method>`
   will provide information about what you need to implement, and a helpful
   error message if you haven't done so.

Support while revising
~~~~~~~~~~~~~~~~~~~~~~

The module Piazza forum will remain open throughout the revision period and we
will be very happy to respond to your questions. There will also be a live
revision session during week 1 of summer term in the module team. This will be
an opportunity to ask individual questions just like in the labs. If enough
people attend then I will also run a group Q & A session.

Practice questions
~~~~~~~~~~~~~~~~~~

Some specifically-designed practice questions are presented below. In addition to this, there are a lot of very good exercises in
chapters 7 and 9 of `Hans Petter Langtangen, A Primer on Scientific Programming
with Python <https://link.springer.com/book/10.1007%2F978-3-662-49887-3>`__.
You can access that book by logging in with your Imperial credentials.

The first two questions are in exam format. 

.. proof:exercise::

    Obtain the `practice problem from GitHub Classroom
    <https://classroom.github.com/a/HdgipMxw>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

    .. note::

        This exercise is fully set up as an exam question, including provisional
        points on the autotests. It should be doable in 30 minutes, though the
        level of programming is a little more basic than the exam questions.

.. proof:exercise::

    Obtain the `practice problem from GitHub Classroom
    <https://classroom.github.com/a/6usAsES4>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

    .. note::

        This exercise is at the level of an exam question, though longer. An
        actual exam question would be pruned back to be achievable in 30
        minutes. Here the complete exercise is presented because the main thing
        you need to do is practice programming, and cutting out material
        doesn't help with that. Marks are not given as the question is the
        wrong length, so dividing 20 marks over the question would just be
        misleading

In addition to these exam-style questions, you can also usefully practice
programming by going beyond the specification of the exercises in the course.
The following exercises are just ideas for how to do that. They do not come
with additional code or tests.

.. proof:exercise::

    Extend the :class:`Polynomial` class from :numref:`Chapter %s <objects>` to
    support polynomial division. Polynomial division results in a quotient and
    a remainder, so you might choose to implement :meth:`~object.__floordiv__`
    to return the quotient and :meth:`~object.__mod__` to return the remainder,
    in a manner analogous to integer division. You might also implement
    :meth:`~object.__truediv__` and have it return the quotient if the
    polynomial division is exact, but raise :class:`ValueError` if there is a
    remainder.

    .. hint::

        Don't forget that repeating code is poor style, so you might need a
        helper method to implement the actual polynomial division.
    
.. proof:exercise::

    Extend the :class:`Deque` class from :numref:`Week %s
    <abstract_data_types>` to automatically resize the ring buffer by a
    proportion of its length when it is full, and when it becomes too empty.
    You can check the behaviour of your implementation against
    :class:`collections.deque`.

.. proof:exercise::

    For a real challenge, extend the groups implementation from :numref:`Week
    %s <inheritance>` to support taking the quotient of two groups. What do the
    values and validation of a quotient group look like in code? You could
    implement :meth:`~object.__truediv__` on :class:`Group` to provide the user
    interface.

.. proof:exercise::

    Write additional single dispatch visitor functions to extend the
    capabilities of the symbolic algebra system you wrote in :numref:`Week %s
    <trees>`. You could, for example, write a visitor which performs
    cancellation of expressions involving 1 or 0. You could implement expansion
    of brackets according to distributive laws. Finally you could canonicalise
    commutative operators such as `+` and `*` so that, for example `1 + x` is
    mapped to `x + 1`. Doing this over multiple layers of the tree
    (for example, transforming `1 + 2*x + 3*x**2` to `3*x**2 + 2*x + 1`) is an additional
    challenge.

Exam instructions
-------------------------

1.  The exam will start at 0900 UTC (London time) on Monday 24 May 2021 and will run for 
    2 hours. Students with additional time will be contacted about this separately.
2.  The exam will take the form of a GitHub classroom assignment, just like all of
    the exercises. The URL to accept the assignment will be posted at the start
    of the exam on the `module Team <https://teams.microsoft.com/l/team/19%3ae96b9a199b15419281f55f454d240249%40thread.tacv2/conversations?groupId=1b12939c-d8c9-4e4d-a291-0ff35d57869f&tenantId=2b897507-ee8c-4575-830b-4f8267c3d307>`__, as Blackboard announcement, and posted on
    Piazza. Of these, the Team is the most instant form of communication so you
    are advised to look there and use the other sources as a backup.
3.  The exam instructions are in the :file:`README.md` in the repository.
    GitHub will show this to you on the repository website. The instructions
    are very similar to those for the practice problems above, so you should
    make sure you have tried those in advance of the exam.
4.  There are 4 questions, each marked out of 20 marks. The exam is marked out
    of 80 and your attempts at all four questions will count.
5.  You submit your work by committing and pushing to the repository on GitHub
    created when you accept the GitHub Classroom assignment. You must commit as
    you go along, and it is strongly advisable to also push as you go. **Only commits
    made during the exam period will count.** Please note that you do not need a
    network connection in order to commit, so you can still do so even if you have
    network problems.
6.  The upload time at the end of the exam is only there to enable you to push
    your work. **Commits made during the upload time will not be marked.**
7.  If you have a problem during the exam, you should post a question
    `on Piazza <https://piazza.com/class/kjob8in6eox1bp>`__. During the exam,
    Piazza will be configured so that student posts can only be seen by the
    instructors. Other than this difference you should follow `the instructions
    on what to do in case of problems <_static/If_you_have_a_problem.pdf>`__ 
    provided by the maths exams office in their
    email of 11 February. In particular, if those instructions require you to
    `email the exam team <mailto:maths.exams@imperial.ac.uk>`__ after the exam
    then you should do so. Posting on Piazza is only a mechanism for getting
    immediate help during the exam.
8.  If you have a problem during the exam which prevents you from working, for
    example you cannot clone the repository or your computer crashes,  then you
    should do the following:

    a. Take note of the time when the problem starts.
    b. If possible, post `on Piazza <https://piazza.com/class/kjob8in6eox1bp>`__ to ask for help.
       If you cannot immediately post on Piazza, do so as soon as you are able. This establishes
       an external record of your issue.
    c. Take note of the time when you are able to resume work.
    d. Ensure that you commit your work before the published end time of the exam.
    e. Having committed (and, if at all possible, pushed), continue to work past the end time of the
       exam, committing at least every 5 minutes until you have recovered the time you lost.
    f. Straight after the exam submit a mitigating circumstances claim explaining the situation.

    It is critical that you have committed your work before the end of the original exam time, because
    no commitments can be made during the exam that late work will be accepted. This will be decided in
    the light of the mitigating circumstances claim.
9.  The usual `academic integrity rules for remote assessments <_static/Academic_Integrity.pdf>`__ 
    apply. In
    particular, you may consult any resource published on the internet, but you may
    not seek help from anyone else, whether in person, by email, chat message,
    forum post or any other means.
