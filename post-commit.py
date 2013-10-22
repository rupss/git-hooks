#!/usr/bin/env python

import subprocess

def execute_git_command(args):
	pr = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return pr.communicate()

def main():
	(commit_id, error) = execute_git_command(['git', 'rev-parse', 'HEAD'])
	(files, error) = execute_git_command(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit_id])
	print files

if __name__ == "__main__":
	main()