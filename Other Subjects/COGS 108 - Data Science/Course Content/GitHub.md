#Git
Version Control
- Enables multiple people to work on a single project
- Each person edits their own copy and chooses when to share that copy.
	- Independent work!
- A way to manage the evolution of a set of files
- The set of files is called a repository (repo)

## git vs GitHub
- git is the version control system.
- GitHub is the website for git repos to be published on the cloud.
- Good for collaboration, returning to a safe state, exposure for your work, and tracking others' work.
	- Search /topics/datascience-projects on GitHub for COGS 108

### Workflow
- Copy the online repo onto a local computer by cloning the repo.
- Change something in the directory.
	- Track these files with the add command. 
		- This is called "staging". Gets *ready* to apply changes to the repo.
	- Create a snapshot with the commit command.
		- Tracks who, what, and when.
		- Can add a commit message with -m option flag.
		- Commits add a hash value to make a unique ID.
			- Can return to one of these commits via the hash.
				- Specifically, git applies a **delta**, a set of changes, to the current file.
				- So changes are stored, not whole files, for efficient space usage.
			- Forwards and backwards! Older commits cannot "see" future commits, however.
	- Push these changes into the remote server to share.
- Teammate is working with an out-of-date copy...
	- Get changes with pull command.
		- If there are conflicts, must "merge" files.
		- Teammate will choose if they want the online version or their local version.
- **Branching**
	- A smaller scale of independent work.
	- Branch from a commit or the current moment.
	- Merge back onto the main branch at a commit point or the current moment!

### Contributing
- To contribute to somebody else's repo, one first **forks** the repo to create one's own GitHub repo. Then clone the forked repo onto one's computer.
	- Once completed with contributions, one submits a pull request to have the original repo possibly integrate one's changes into the original repo.
- We can file **issues** on GitHub without explicitly forking and making a pull request.

#### Personal Access Tokens
- Fine-grained passwords that allow access for a given time to a given thing for a given person.