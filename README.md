## Tasks

1. Create docker image which prints random text to output.
2. Create docker image which prints random text to output. Image (when run) accepts one arg which is length of the output text.
3. Create docker image which prints random text to output. Image (when run) accepts two args. First one is the length of the output text, the second one is the exit code.
4. Publish image to any public container repository (dockerhub)
5. Store dockerfiles in a public git repo (github/gitlab)
6. Create pipeline in gitlab/github which does following on each change:
* build image from dockerfile
* tag image with commit hash
* push image to public container repository
