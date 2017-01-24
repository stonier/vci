# VCS Extras

## VCI

Extension to vcstool that allows finding/fetching from a `.repos` index.
This is a nice way of collecting the locations of all the `.repos`
you use, from both your projects and others, without having to remember
long and forgettable url's.

### Install

Install from either pypi (`pip install vcs_extras`) or from
[ppa](https://launchpad.net/~d-stonier/+archive/ubuntu/snorriheim) for xenial.

### Index

A simple example of an index:

```YAML
# repos used only as helpers, use a '_' convention for sorting
_catkin: 'kinetic/catkin.repos'
# using an alias
catkin: [_catkin]
# a relative path
ecl: 'kinetic/ecl.repos'
# a url
ecl_tools: 'https://raw.github.com/stonier/vcs_extras/repos/kinetic/ecl_tools.repos'
```

The default index used to get things started can be found
[here](https://github.com/stonier/vcs_extras/blob/repos/kinetic.yaml) which has
more detailed comments illustrating the various mechanisms used to define key-location
pairs.

To point `vci` at your own index, make use of the config command;

```bash
# an index in a public github repository
vci config --set https://github.com/me/my_repo/blob/master/my_index.yaml
# an index on your filesystem (perhaps a cloned private github repo)
vci config --set file:///home/me/my_repo/my_index.yaml
```

To list the contents of your index:

```bash
vci list
```

### Pipe into VCS Import

The `vci find` command can be piped into vcs as follows to download or update
your workspace:

```bash
vci find ecl | vcs import
```

## Dev Notes

For testing and development, run in a virtual env wrapper via:

```
source setup.bash
```
