# Notes

## make2graph

```
$ make -Bnd | ~/src/external/makefile2graph/make2graph | dot -Tpng -o dag.png
```

## CMake

```
$ cmake -S . -B build
$ cd build
$ make
```

## meson

```
$ meson build .
$ cd build
$ ninja
```
