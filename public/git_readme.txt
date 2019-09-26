
Learn how to create a git repo
Learn how to place a file in a git repo
Learn how to clone a git repo
Learn what to put in ~/.gitconfig
Learn how to push a git repo to github.com
Learn how to fork a git repo on github.com
Learn how to create a branch in a git repo
Learn how to navigate branches in a git repo
Learn how to quickly recover from broken git repo
Learn how to submit a pull request on a git repo

ooooooo
Learn how to create a git repo

I use two ways to create a git repository (a repo).

The most common way I create a repo is to clone a repo from github.com with syntax like this:

cd ~
rm -rf try-tf
git clone https://github.com/jasonbaldridge/try-tf

The above syntax will create a repo at this location:

~/try-tf/

Occasionally I will create a git repo from scratch with syntax like this:

cd ~
mkdir my_repo
cd    my_repo
echo  I like my_repo. > README.md
git init
git add .
git commit -am 'This repo will help me learn git.'

ooooooo
Learn how to place a file in a git repo

It is easy to place a file in a git repo.

I use syntax like this:

cd ~/my_repo
echo Dan was here. > dan.txt
git add .
git commit -am 'dan.txt will help me learn git.'


oooooooo
Learn how to clone a git repo

I use 4 types of syntax to clone a repo.

1.
I can clone a repo from github.com with syntax like this:

cd ~
rm -rf try-tf
git clone https://github.com/jasonbaldridge/try-tf

I use the syntax above if I only want a copy of the repo so I can use it.

2.
The syntax below is useful if want a copy of the repo so I can enhance it:

cd ~
rm -rf try-tf
git clone git@github.com:jasonbaldridge/try-tf.git

The above syntax will work okay if I have my public-ssh-key registered in the github account.

3.
The syntax below is useful if want a copy of a repo from another host rather than github.com:

cd ~
rm -rf try-tf
git clone joe@otherhost.com:/var/gitrepos/try-tf

4.
The syntax below is useful if want a copy of a repo already on my laptop:

cd /home/dan
git clone /home/dan/my_repo /tmp/my_repo_backup

I often use the 4th idea if I want to create a clone of an important
repo so I can run experiments on the clone without disturbing the original.

ooooooooooooo
Learn what to put in ~/.gitconfig

My ~/.gitconfig file looks like this:

[user]
	name = Dan Bikle
	email = dan.bikle101@yahoo.com
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true

[github]
	user = bikle101

[alias]
	br = branch
	st = status
        ci = commit
        co = checkout

I find that the alias syntax is useful.

For example it allows me to replace this shell command:

git checkout

with this shell command:

git co


oooooooooooooo
Learn how to push a git repo to github.com

If I clone a repo from github.com, then it is easy to push that same repo to github.com.

Here is some demo syntax:

cd ~
git clone git@github.com:someuser101/the_repo.git
cd the_repo
echo 'Dan was here.' > dan.txt
git add .
git commit -am 'A demo'
git push origin master

oooooooooooooo
Learn how to fork a git repo on github.com

When I want to fork a repo on github.com, I use the web site.

First I login to github.com.

Then I find the repo I want to fork.

Then I find the fork button and click it.

I should then find a new repo in my github.com account.

Typically at that point I clone the forked-repo to my laptop and start enhancing it.

The main reason I fork a repo is so that I can enhance it.

If I just want to use a repo, I clone it.


ooooooooooooooo
Learn how to create a branch in a git repo

When I create a git repo on my laptop, git will put me in the master branch.

The syntax below shows how to create the dan branch:

cd ~
mkdir some_repo
cd    some_repo
echo  hello > readme.txt
git init
git add .
git commit -am hello
git status
git checkout -b dan
git status


oooooooooooo
Learn how to navigate branches in a git repo

The syntax below shows how to create the dan branch:

cd ~
mkdir da_repo
cd    da_repo
echo  hello > readme.txt
git init
git add .
git commit -am hello
git status
git checkout -b dan
git status

