:orphan:

.. _midterm:

Midterm test preparation
========================

The midterm programming test is worth 20% of the course. The format
of this test is deliberately similar to the programming exam in May that makes
up the other 80% of the assessment. This test therefore provides both some feedback
on how you are progressing in the course, and an opportunity to practice for the
end of term exam. This is a programming module, so the midterm test will consist
of programming exercises. The content which will be examined in the test is
everything covered up to and including chapter 6. There won't be any new concepts
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

.. The test will work using GitHub Classroom. The link to accept the test
.. "assignment" will be distributed at the start time of the test, simultaneously
.. as an announcement on Blackboard, and in the Ed forum. The test repository
.. will contain a file :file:`README.rst` containing the questions, skeleton code
.. appropriate to the questions, and tests. GitHub shows :file:`README.rst` files on
.. the repository web page, and the instructions will be easier to read there since
.. any links will be clickable.

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

.. Using Git in the test
.. ---------------------

.. You should accept the test from GitHub Classroom, and clone the test repository
.. into the folder you created for the course, just like you have been doing for
.. the exercise repositories. This will help ensure that you are programming in
.. the same environment you have been using all along, and therefore avoid any
.. unfortunate misconfiguration surprises in the test.

.. This is a test of programming as a whole, so using Git correctly is a part of
.. the test. This has some consequences for how you should go about the test:

.. 1. Commit *and* push your work as you go along. Do not rely on committing once
..    at the end of the test. You will be marked on what you have pushed to GitHub
..    at the end of the test period. If the first time that you try to push
..    something to GitHub is at the end of the test time, and something goes wrong, then
..    you will receive 0% for the test, because you will not have pushed any
..    answers.
.. 2. Don't forget to `git add` any files you need to create. If you don't add them
..    to the repository, they won't be pushed and therefore they won't be marked.

.. .. warning::

..     If you commit and push often as you go through the test then not only will
..     you know that you have some marks in the bank already, but you will have a
..     record of what you had done at each point in time. In the unlikely event of a failure outside your
..     control, such as your network failing or GitHub going down, it will be very
..     easy to assign the correct marks to students who have already pushed a large
..     part of their work to GitHub. At the other extreme, it will be difficult to
..     ascribe any credit at all to students with no pushed work who then push a
..     single commit to GitHub after the time has expired.

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

    Obtain the `practice problem from GitHub Classroom
    <https://classroom.github.com/a/whZ5Hmzx>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

    Note that these instructions are only applicable to the practice problems.
    The test this year will be conducted using a new system.

.. proof:exercise::

    Obtain the `practice problem from GitHub Classroom
    <https://classroom.github.com/a/BIoMj_-E>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

    Note that these instructions are only applicable to the practice problems.
    The test this year will be conducted using a new system.

.. proof:exercise::

    Obtain the `practice problem from GitHub Classroom
    <https://classroom.github.com/a/jVHNwYHx>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

    Note that these instructions are only applicable to the practice problems.
    The test this year will be conducted using a new system.

.. proof:exercise::

    Obtain the `practice problem from GitHub Classroom
    <https://classroom.github.com/a/6bPHF9F7>`__. Follow the instructions in
    the README file that will be displayed on GitHub on your copy of the page.

    Note that these instructions are only applicable to the practice problems.
    The test this year will be conducted using a new system.

.. Exam preparation
.. ----------------

.. The final exam will be similar in format to the :ref:`midterm test <midterm>`, so all
.. of the advice about preparing applies there too. As with all second year
.. elective modules, the exam will comprise four questions, each marked out of 20.

.. As with everything in this course, the one thing you can do to effectively
.. prepare for the exam is to program. You should complete any of the exercises in
.. the course that you have not yet done, and more exercises are given below.

.. Exam scope
.. ~~~~~~~~~~

.. Everything we have covered in the course up to and including week 11
.. (chapter 10) will be fully examinable. 

.. .. Allowed materials
.. .. ~~~~~~~~~~~~~~~~~

.. .. 1. You may take the exam using your own laptop or a College PC.
.. .. 2. You may consult static websites such as https://python.org, and the course
.. ..    text https://object-oriented-python.github.io. If you wish, you may use
.. ..    search engines without embedded conversational AI capabilities such as
.. ..    Google.
.. .. 3. You must not attempt to communicate with anyone other than an invigilator.
.. ..    This includes, but is not limited to:

.. ..    a. sending or receiving emails,

.. ..    b. sending or receiving instant messages on any platform, and

.. ..    c. posting on any web forum.

.. .. 4. You must not attempt to employ conversational AI tools such as ChatGPT,
.. ..   Microsoft Bing, or GitHub Copilot.

.. .. Using unauthorised materials or attempting to communicate with anyone other
.. .. than an invigilator are exam offences and will be dealt with under the academic
.. .. misconduct policy and procedures.

.. Support while revising
.. ~~~~~~~~~~~~~~~~~~~~~~

.. The module Ed forum will remain open throughout the revision period and we
.. will be very happy to respond to your questions. There will also be a revision
.. lecture at the start of the summer term.

.. .. Past papers
.. .. ~~~~~~~~~~~

.. .. .. proof:exercise::

.. ..     Obtain the `practice problem from GitHub Classroom
.. ..     <https://classroom.github.com/a/T2uShUW8>`__. Follow the instructions in
.. ..     the README file that will be displayed on GitHub on your copy of the page.

.. ..     .. note::

.. ..         This was the August 2021 exam.

.. .. .. proof:exercise::

.. ..     Obtain the `practice problem from GitHub Classroom
.. ..     <https://classroom.github.com/a/lHkZo7H0>`__. Follow the instructions in
.. ..     the README file that will be displayed on GitHub on your copy of the page.

.. ..     .. note::

.. ..         This was the May 2022 exam.

.. .. .. proof:exercise::

.. ..     Obtain the `practice problem from GitHub Classroom
.. ..     <https://classroom.github.com/a/6CNSDTzo>`__. Follow the instructions in
.. ..     the README file that will be displayed on GitHub on your copy of the page.

.. ..     .. note::

.. ..         This was the August 2022 exam.

.. .. .. proof:exercise::

.. ..     Obtain the `practice problem from GitHub Classroom
.. ..     <https://classroom.github.com/a/ian0yjPK>`__. Follow the instructions in
.. ..     the README file that will be displayed on GitHub on your copy of the page.

.. ..     .. note::

.. ..         This was the May 2023 exam.

.. .. .. proof:exercise::

.. ..     Obtain the `practice problem from GitHub Classroom
.. ..     <https://classroom.github.com/a/p-JqEA4w>`__. Follow the instructions in
.. ..     the README file that will be displayed on GitHub on your copy of the page.

.. ..     .. note::

.. ..         This was the January 2024 exam.


.. .. Further programming practice ideas
.. .. ----------------------------------

.. .. In addition to these exam-style questions, you can also usefully practice
.. .. programming by going beyond the specification of the exercises in the course.
.. .. The following exercises are just ideas for how to do that. They do not come
.. .. with additional code or tests.

.. .. In addition to this, there are a lot of very good exercises in
.. .. chapters 7 and 9 of `Hans Petter Langtangen, A Primer on Scientific Programming
.. .. with Python <https://link.springer.com/book/10.1007%2F978-3-662-49887-3>`__.
.. .. You can access that book by logging in with your Imperial credentials.

.. .. .. proof:exercise::

.. ..     Extend the :class:`Polynomial` class from :numref:`Chapter %s <objects>` to
.. ..     support polynomial division. Polynomial division results in a quotient and
.. ..     a remainder, so you might choose to implement :meth:`~object.__floordiv__`
.. ..     to return the quotient and :meth:`~object.__mod__` to return the remainder,
.. ..     in a manner analogous to integer division. You might also implement
.. ..     :meth:`~object.__truediv__` and have it return the quotient if the
.. ..     polynomial division is exact, but raise :class:`ValueError` if there is a
.. ..     remainder.

.. ..     .. hint::

.. ..         Don't forget that repeating code is poor style, so you might need a
.. ..         helper method to implement the actual polynomial division.
    
.. .. .. proof:exercise::

.. ..     Extend the :class:`Deque` class from :numref:`Week %s
.. ..     <abstract_data_types>` to automatically resize the ring buffer by a
.. ..     proportion of its length when it is full, and when it becomes too empty.
.. ..     You can check the behaviour of your implementation against
.. ..     :class:`collections.deque`.

.. .. .. proof:exercise::

.. ..     For a real challenge, extend the groups implementation from :numref:`Week
.. ..     %s <inheritance>` to support taking the quotient of two groups. What do the
.. ..     values and validation of a quotient group look like in code? You could
.. ..     implement :meth:`~object.__truediv__` on :class:`Group` to provide the user
.. ..     interface.

.. .. .. proof:exercise::

.. ..     Write additional single dispatch visitor functions to extend the
.. ..     capabilities of the symbolic algebra system you wrote in :numref:`Week %s
.. ..     <trees>`. You could, for example, write a visitor which performs
.. ..     cancellation of expressions involving 1 or 0. You could implement expansion
.. ..     of brackets according to distributive laws. Finally you could canonicalise
.. ..     commutative operators such as `+` and `*` so that, for example `1 + x` is
.. ..     mapped to `x + 1`. Doing this over multiple layers of the tree
.. ..     (for example, transforming `1 + 2*x + 3*x**2` to `3*x**2 + 2*x + 1`) is an additional
.. ..     challenge.

.. .. Exam instructions
.. .. -------------------------

.. .. 1.  The exam will start at 0900 UTC (London time) on Monday 24 May 2021 and will run for 
.. ..     2 hours. Students with additional time will be contacted about this separately.
.. .. 2.  The exam will take the form of a GitHub Classroom assignment, just like all of
.. ..     the exercises. The URL to accept the assignment will be posted at the start
.. ..     of the exam on the `module Team <https://teams.microsoft.com/l/team/19%3ae96b9a199b15419281f55f454d240249%40thread.tacv2/conversations?groupId=1b12939c-d8c9-4e4d-a291-0ff35d57869f&tenantId=2b897507-ee8c-4575-830b-4f8267c3d307>`__, as Blackboard announcement, and posted on
.. ..     Piazza. Of these, the Team is the most instant form of communication so you
.. ..     are advised to look there and use the other sources as a backup.
.. .. 3.  The exam instructions are in the :file:`README.md` in the repository.
.. ..     GitHub will show this to you on the repository website. The instructions
.. ..     are very similar to those for the practice problems above, so you should
.. ..     make sure you have tried those in advance of the exam.
.. .. 4.  There are 4 questions, each marked out of 20 marks. The exam is marked out
.. ..     of 80 and your attempts at all four questions will count.
.. .. 5.  You submit your work by committing and pushing to the repository on GitHub
.. ..     created when you accept the GitHub Classroom assignment. You must commit as
.. ..     you go along, and it is strongly advisable to also push as you go. **Only commits
.. ..     made during the exam period will count.** Please note that you do not need a
.. ..     network connection in order to commit, so you can still do so even if you have
.. ..     network problems.
.. .. 6.  The upload time at the end of the exam is only there to enable you to push
.. ..     your work. **Commits made during the upload time will not be marked.**
.. .. 7.  If you have a problem during the exam, you should post a question
.. ..     `on Piazza <https://piazza.com/class/kjob8in6eox1bp>`__. During the exam,
.. ..     Piazza will be configured so that student posts can only be seen by the
.. ..     instructors. Other than this difference you should follow `the instructions
.. ..     on what to do in case of problems <_static/If_you_have_a_problem.pdf>`__ 
.. ..     provided by the maths exams office in their
.. ..     email of 11 February. In particular, if those instructions require you to
.. ..     `email the exam team <mailto:maths.exams@imperial.ac.uk>`__ after the exam
.. ..     then you should do so. Posting on Piazza is only a mechanism for getting
.. ..     immediate help during the exam.
.. .. 8.  If you have a problem during the exam which prevents you from working, for
.. ..     example you cannot clone the repository or your computer crashes,  then you
.. ..     should do the following:

.. ..     a. Take note of the time when the problem starts.
.. ..     b. If possible, post `on Piazza <https://piazza.com/class/kjob8in6eox1bp>`__ to ask for help.
.. ..        If you cannot immediately post on Piazza, do so as soon as you are able. This establishes
.. ..        an external record of your issue.
.. ..     c. Take note of the time when you are able to resume work.
.. ..     d. Ensure that you commit your work before the published end time of the exam.
.. ..     e. Having committed (and, if at all possible, pushed), continue to work past the end time of the
.. ..        exam, committing at least every 5 minutes until you have recovered the time you lost.
.. ..     f. Straight after the exam submit a mitigating circumstances claim explaining the situation.

.. ..     It is critical that you have committed your work before the end of the original exam time, because
.. ..     no commitments can be made during the exam that late work will be accepted. This will be decided in
.. ..     the light of the mitigating circumstances claim.
.. .. 9.  The usual `academic integrity rules for remote assessments <_static/Academic_Integrity.pdf>`__ 
.. ..     apply. In
.. ..     particular, you may consult any resource published on the internet, but you may
.. ..     not seek help from anyone else, whether in person, by email, chat message,
.. ..     forum post or any other means.
