# Indentation Converter

## Introduction

Simple project that converts one kind of indentation to another. You can convert a downloaded file which is indented with arbitrary number of spaces or tabs to the type of indentation you are familiar with.

By the way, since there are many other solutions to this problem, just consider this repo a tutorial. :smile:

## Dependencies

The interpreter, Python 3, is certainly a requirement.

Besides, please make sure the Python libraries `argparse` and `regex` are installed. Simply

```shell
pip install argparse regex
```

will do.

The origin `re` library fails to meet the needs. :pensive:

## Usage

The usage is simple. The main function is inside `ind_cvt.py`, so to use it, simply typing

```shell
python ind_cvt.py --file path/to/your/file.extension
```

will do. The command create `file_cvt.extension` which contains the converted text in the same directory as the original file.

**Note**: If there's an important file with the same name, it'll overwrite it. Editing the `config.py` or giving another argument to `--appendix` will help.

By default, the command convert indentations from two spaces to four. To do other transitions, you can specify values for `--prev` and `--target`, which are the indentations to change from and to respectively.

```shell
python ind_cvt.py --file path/to/your/file.extension --prev '  ' --target '    '
```

Also, you can specify the appendix:

```shell
python ind_cvt.py --file path/to/your/file.extension --appendix '_myAppendix'
```

will produce `file_myAppendix.extension` in the same directory as your `file.extension`.

Default values for those arguments are available in `config.py`.

## ToDo

Add support for converting mixed indentations. (mixture of spaces and tabs, for example)
