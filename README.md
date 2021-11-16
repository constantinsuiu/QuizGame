## New Branch - quiz_refactor_01
1. I created a new branch to help. You may or may not agree with the changes I made, and a seperate branch is a great approach.

## Database Entity Relational Diagram(ERD)
I created an ERD using Django-Extension, I think it is important to have a clear understanding of the database.

## General Points:
1. I recommend that you set your editor to add a blank line automatically, see users/forms.py, Python
W292 - no newline at end of file. If you need a recommended guide for your editor just let me know. VS Code, Sublime Text, etc should have Python linting enabled, again if you need help with this please let me know.

2. Django has specific conventions for data, the best approach is to use Fixtures, [Providing initial data for models]( https://docs.djangoproject.com/en/3.2/howto/initial-data/). For larger projects with massive data, a direct import using psql using a datadump file would be more appropriate. PostgreSQL has tools for this pg_dump + psql.

3. Best practise dictates that migrations should be included in the GitHub repo, as explained in the Django documentation on [Migrations](https://docs.djangoproject.com/en/3.2/topics/migrations/)
    "The migration files for each app live in a “migrations” directory inside of that app, and are designed to be committed to, and distributed as part of, its codebase. You should be making them once on your development machine and then running the same migrations on your colleagues’ machines, your staging machines, and eventually your production machines."

4. Pipenv is generally not recommended, its history is irradite and numerous production level projects have fallen victim to its problems. See this discussion for example, [If this project is dead, just tell us #4058 ](https://github.com/pypa/pipenv/issues/4058). In your case I used pip + requirements.txt. Currently the tool [Poetry](https://python-poetry.org/docs/) is considered the actual best approach, I have just started using it myself.

5. For PostgreSQL I use a tool developed by Jacob Kaplan-Moss, the co-creator of Django. The tool [DJ-Database-URL](https://github.com/jacobian/dj-database-url). You can see its usage in my branch settings.py and the .env/.env.sample.
