# Start-Work

<!-- badges start -->
![GitHub repo size](https://img.shields.io/github/repo-size/JorbFreire/startwork?style=plastic)
[![Publish](https://github.com/JorbFreire/startwork/workflows/Publish/badge.svg)](https://github.com/JorbFreire/startwork/actions?query=workflow:"Publish")
[![GitHub release](https://img.shields.io/github/release/JorbFreire/startwork?include_prereleases=&sort=semver&color=blue)](https://github.com/JorbFreire/startwork/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
![OS - Linux](https://img.shields.io/badge/OS-Linux-blue?logo=linux&logoColor=white)
[![dependency - StartWork](https://img.shields.io/badge/dependency-StartWork-blue?logo=python&logoColor=white)](https://pypi.org/project/StartWork)
[![Github](https://img.shields.io/badge/Github-purple?logo=github)](https://github.com/JorbFreire/startwork)
<!-- badges end -->

Small CLI to easier start and swap between projects in different stacks.

## motivation

It's not hard to set up and run most modern software projects.

Usually, we just have to run two something like `pip install -r requirements.txt`
 and `flask run` or something similar. The real problem comes we you have to
 constantly switch contexts, even worse when working with multiple projects in
 multiple languages with totally different setups a couple of times a day.

[Docker](https://www.docker.com/) and [DockerCompose](https://docs.docker.com/compose/) are great tools to handle this problem. Start Work
 should not be a replacement for Docker either Docker compose and shall even
 work with both.

With Start-Work will be easier to switch between projects from any folder and
 get your development environment up and running only by selecting the project
 you wanna work on, and when some of these projects for some reason don't allow 
 Docker, Start-Work will also try to identify which tools you are using and run
 it for you.

## Installation

Just run:
```bash
pip install startwork
```

It's done, the installation can be verified with:
```bash
work --version
```

## CLI Options


```bash
work
```
Will display a list and let you select one of your saved projects

<br />

```bash
work create
```
Will guide you with a couple of questions to save a new project.

<br />

```bash
work delete
```
Will display a list and let delete one of your saved projects.

Note: it will not remove the project from your computer, only from the list on
 Start-Work

<br />

```bash
work --version
```
Show current version

<br />

```bash
work --help
```
Show currently available CLI options

## Next goals

- [ ] Handle multiple environments in a single folder
  - [ ] Detect multiple environments
  - [ ] Let you choose the environment that will be run
  - [ ] Let you mark multiple to run at the same time


- [ ] Handle multiple folders
  - [ ] When not matched by any setup pattern, check inside the first children's folders
  - [ ] When multiple children folders match, let you choose one folder
  - [ ] Let you mark multiple folders to run at the same time

- [ ] Handle multiple folders AND multiple environments at the same call
- [ ] Write fully covered end-to-end tests
