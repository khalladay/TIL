# How to fix a mistyped password in Git (on windows)

I tried to clone a repo from a locally hosted server and mistyped my password. Subsequent attempts to clone yeilded an "Authentication Error" instead of re-prompting for my password. 

To fix, open up the windows credential manager (press windows key, type credential, you'll see it), and modify the credential associated with the server you're cloning from. Then reclone with git and you should be good to go. 
