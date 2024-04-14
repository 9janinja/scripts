#Make sure to install the gitpython library before running this script by executing "pip install gitpython".

import git
import os

class GitRepositoryManager:
    def __init__(self, repo_url, local_path):
        self.repo_url = repo_url
        self.local_path = local_path
        self.repo = None

    def clone_repository(self):
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)
        self.repo = git.Repo.clone_from(self.repo_url, self.local_path)
        print("Repository cloned successfully.")

    def create_branch(self, branch_name):
        self.repo.git.checkout('master')
        self.repo.git.checkout('-b', branch_name)
        print(f"Branch '{branch_name}' created successfully.")

    def switch_branch(self, branch_name):
        self.repo.git.checkout(branch_name)
        print(f"Switched to branch '{branch_name}'.")

    def commit_changes(self, message):
        self.repo.git.add('--all')
        self.repo.index.commit(message)
        print("Changes committed successfully.")

    def push_changes(self):
        origin = self.repo.remote(name='origin')
        origin.push()
        print("Changes pushed to remote repository.")

# Example usage:
if __name__ == "__main__":
    # Initialize GitRepositoryManager with repository URL and local path
    repo_manager = GitRepositoryManager(repo_url="https://github.com/example/repo.git", local_path="repo")

    # Clone the repository
    repo_manager.clone_repository()

    # Create a new branch
    repo_manager.create_branch(branch_name="feature-branch")

    # Switch to the new branch
    repo_manager.switch_branch(branch_name="feature-branch")

    # Make changes to files

    # Commit changes
    repo_manager.commit_changes(message="Added new feature")

    # Push changes to remote repository
    repo_manager.push_changes()
