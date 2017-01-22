# VCS Find

Extension to vcstool that allows finding/fetching from a `.repos` index.

# Dev Notes

## Setup

Run in a virtual env wrapper via:

```
source setup.bash
```

## Details

Would have been nice just to extend vcs' command line just like catkin tools has
been designed, but it hasn't been designed with entry points. Instead the vci
tool here is just configured to 'work nicely with' the vcs command.