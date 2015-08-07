# docker-galaxy-stable-toolshed - AAFC flavour
Galaxy Docker with empty dev toolshed enabled. This Dockerfile builds on smithcr/docker-galaxy-stable-toolshed, which in turn builds on bgruening/docker-galaxy-stable. 

## Set up

You will need to have installed:
* git (to check this project out)
* Docker (preferably version 1.7 and up)
* If you're using a Mac, Docker does not run natively on it. Intall boot2docker VM. See very good Docker documentation on this: https://docs.docker.com/installation/mac/

When cloning this project, make sure that you use --recursive option to bring in all dependent projects:
`git clone --recursive https://github.com/AAFC-MBB/docker-galaxy-stable-toolshed.git`

If you'd like to change galaxy toolshed admin user name, password, and/or email, edit user_info.xml file. Defaults are:
`email: toolshed@galaxy.org`
`user name: galaxyuser`
`pass:  toolshed`

To build a docker image, :
`docker build -t aafc-mbb/galaxy-stable-toolshed .`

Create and run the container:
`docker run -d -p 8080:80 -p 9009:9009 -v <some host directory>:/export smithcr/galaxy-stable-toolshed`


