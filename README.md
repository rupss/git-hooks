post-commit.py is a post-commit Git hook that I wrote that replaces tabs with 4 spaces in the modified files, and then adds these files without tabs back to the commit. 

SETUP: 

- Copy post-commit.py to your .git/hooks directory. 
- Change the name from post-commit.py to post-commit
- Make the file executable (chmod +x post-commit)

It should then run after you make a new commit.

PROBLEMS: 

Don't use this if you have uncommitted hunks in your files, since this script adds the file directly.