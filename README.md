# I-can-do-machine-learning

```
                   ##        .
             ## ## ##       ==
          ## ## ## ##      ===
      /""""""""""""""""\___/ ===
 ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
      \______ o          __/
        \    \        __/
         \____\______/
         |          |
      __ |  __   __ | _  __   _
     /  \| /  \ /   |/  / _\ |
     \__/| \__/ \__ |\_ \__  |
```

## 1. Introduction

Docker is an open source containerization technology.

> A container runs natively on Linux and shares the kernel of the host machine with other containers. It runs a discrete process, taking no more memory than any other executable, making it lightweight.

<table align="center">
  <tbody>
    <tr>
      <td>
        <img src="res/container.png" width=300>
      </td>
      <td>
        <img src="res/vm.png" width=300>
      </td>
    </tr>
  </tbody>
</table>

> By contrast, a virtual machine (VM) runs a full-blown “guest” operating system with virtual access to host resources through a hypervisor. In general, VMs incur a lot of overhead beyond what is being consumed by your application logic.

## 2. Try it out

Install docker: https://docs.docker.com/install

Create a virtual environment and install the project dependencies:

    make install && pipenv shell

Install the project in `editable/develop` mode:

    make dev

Make sure that the project is correctly installed:

    make lint && make test

Build a docker image:

    make dockerize

Run the project in a container:

    make run

Open the project at http://localhost:8000
