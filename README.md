# Start-Work

<div style="display: flex; justify-content: center" >

[
  <kbd
    style="
      display: flex;
      padding: 8px;
      border-top-right-radius: 0;
      border-bottom-right-radius: 0;
    "
    >
    <img
      src="assets/links/github.svg"
      height="25"
      style="margin-right: 8px;"
    />
    <span
      style="
        display: flex;
        flex-direction: column;
        justify-content: center;
        font-size: 14px;
      "
    >
      Github
    </span>
  </kbd>
](https://github.com/JorbFreire/startwork)

[
  <kbd
    style="
      display: flex;
      padding: 8px;
      border-top-left-radius: 0;
      border-bottom-left-radius: 0;
    "
    >
    <img
      src="https://pypi.org/static/images/logo-small.2a411bc6.svg"
      height="25"
      style="margin-right: 8px;"
    />
    <span
      style="
        display: flex;
        flex-direction: column;
        justify-content: center;
        font-size: 14px;
      "
    >
      Published at PyPi
    </span>
  </kbd>
](https://pypi.org/project/startwork/)

</div>
Small CLI to easier start and swap between projects in different stacks.

## motivation

It's not hard to set up and run most modern software projects.

Usually, we just have to run two something like `pip install -r requirements.txt`
 and `flask run` or something similar. The real problem comes we you have to
 constantly switch contexts, even worse when working with multiple projects in
 multiple languages with totally different setups a couple of times a day.

[Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) are great tools to handle this problem. Start Work
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
