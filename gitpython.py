
# start writing shebang statement
# https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

from git import Repo

# the problem statement was to update the git repo in current directory, but you are hardcoding the path here
# also the path you hardcoded does not exist on system of user, so the script is useless for user
# you could've provided the facility to provide path from outside as well
repo = Repo('/home/di.garg/sample')
assert repo.bare == False
repo.remotes.origin.pull()

# redundant -- calling pull function twice
# this statement prints =====> [<git.remote.FetchInfo object at 0x7fd6e7c3ef50>]
# which is not helpful for user
print(repo.remotes.origin.pull())
