# VCI

Works with vcstool to find/fetch from a `.repos` index.
This is a great way of collecting the locations of all the `.repos`
you use, from both your projects and others, without having to remember
long and forgettable url's.

## Quick Demo

```
$ vci config --set-default

URL : https://raw.githubusercontent.com/stonier/vci/repos/kinetic.yaml

$ vci list

https://raw.githubusercontent.com/stonier/vci/repos/kinetic.yaml

    _catkin: kinetic/catkin.repos
    catkin: ['_catkin']
    ecl: kinetic/ecl.repos
    ecl_tools: https://raw.github.com/stonier/vci/repos/kinetic/ecl_tools.repos
    ros-tutorials: kinetic/ros_tutorials.repos

$ vci find catkin

repositories:
  catkin: {type: git, url: 'https://github.com/ros/catkin.git', version: kinetic-devel}
  cmake_modules: {type: git, url: 'https://github.com/ros/cmake_modules.git', version: 0.4-devel}
  gtest: {type: git, url: 'https://github.com/google/googletest.git', version: release-1.8.0}

$ mkdir -p ~/catkin_ws/src; cd ~/catkin_ws/src
$ vci find catkin | vcs import

...
=== ./catkin (git) ===
Cloning into '.'...
Already on 'kinetic-devel'
Your branch is up-to-date with 'origin/kinetic-devel'.
=== ./cmake_modules (git) ===
Cloning into '.'...
Already on '0.4-devel'
Your branch is up-to-date with 'origin/0.4-devel'.
=== ./gtest (git) ===
Cloning into '.'...
Note: checking out 'release-1.8.0'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at ec44c6c... Merge pull request #821 from mazong1123/master

$ cd ~/catkin_ws
$ catkin init
$ catkin build
...
```

## Install

Install from either pypi (`pip install vci`) or from
[ppa](https://launchpad.net/~d-stonier/+archive/ubuntu/snorriheim) for xenial.

## Subcommands

```
$ vci --help
usage: vci [-h] [-v] {find,config,list} ...

version control index handling

optional arguments:
  -h, --help          show this help message and exit
  -v, --version       show program's version number and exit

commands:
  {find,config,list}  valid commands for vci interactions
    find              search and retrieve from the version control index
    config            manage the version control index list
    list              display each key, url in the current index

And his noodly appendage reached forth to tickle the blessed...
```

## The Default Index

The default index contains a few ROS 1 kinetic repositories that
are useful for illustrating this tool:

```bash

$ vci list

https://raw.githubusercontent.com/stonier/vci/repos/kinetic.yaml

    _catkin: kinetic/catkin.repos
    catkin: ['_catkin']
    ecl: kinetic/ecl.repos
    ecl_tools: https://raw.github.com/stonier/vci/repos/kinetic/ecl_tools.repos
    ros_tutorials: ['_catkin', 'kinetic/ros_tutorials.repos']
```

Here you can see there is a convention applied via leading underscores
to indicate keys that should not be used directly, and a mechanism for
composing new keys from a list of other keys.
The [index yaml](https://raw.githubusercontent.com/stonier/vci/repos/kinetic.yaml)
includes considerably more detail and examples in the comments that elucidate the
contents of an index file.

## Switching the Index

Point `vci` at the pre-prepared ros2 index:

```bash
$ vci config --set https://raw.githubusercontent.com/stonier/vci/repos/ros2.yaml
$ vci list

https://raw.githubusercontent.com/stonier/vci/repos/ros2.yaml

    core: https://raw.githubusercontent.com/ros2/ros2/release-latest/ros2.repos
```

## Import from the Index

The `vci find` command can be piped into `vcs import` as follows to import
sources into your workspace:

```bash
$ vci config --set-defaults
$ mkdir ecl_ws; cd ecl_ws
$ vci find ecl | vcs import
```

## Create Your Own Index

For getting started quickly, start your own public repository or branch on
github in the same vein as [vci/repos](https://github.com/stonier/vci/tree/repos).
Refer to [kinetic.yaml](https://raw.githubusercontent.com/stonier/vci/repos/kinetic.yaml)
for detailed examples and tips on creating your own index yaml file. Once created,
simply point vci at it with the `vci config --set <url>` command.

Note that the index does not have to be on github. It could just as easily be hosted
on a file server or on your local machine.

## Hosting the Index Locally

If you need operation offline or simply want speedier acess, you can point
vci at a local index. If offline, this does require that all .repo references
are relative paths.

```bash
# clone vci's index branch
$ git clone https://github.com/stonier/vci.git /mnt/work/vci
$ cd /mnt/work/vci
$ git checkout repos

# point vci at it
$ vci config --set file:///mnt/work/vci/kinetic.yaml
```

# Dev Notes

For testing and development, run in a virtual env wrapper via:

```
source setup.bash
```
