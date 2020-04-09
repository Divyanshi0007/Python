from git import Repo
repo = Repo('/home/di.garg/sample')
assert repo.bare == False
repo.remotes.origin.pull()
print(repo.remotes.origin.pull())