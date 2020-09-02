# Image resizer

Python image editor

## Install dependencies

```shell
pip install -r requirements.txt
```

## Run application

```shell
python main.py
```

## Lint all py files

```shell
sh linter.sh
```

## Create Windows executable

```shell
pyinstaller --noconsole --onefile main.py
```

## Create new file pylintrc

```shell
pylint --generate-rcfile > ./nothing.pylintrc
```


## References

* [Image Processing in Python with Pillow](https://auth0.com/blog/image-processing-in-python-with-pillow)
* https://stackoverflow.com/questions/40292705/tkinter-file-pattern-set-in-a-file-dialog

<!--

## Create tag

```shell
gac Message # Add and commit
git tag -a -m "Message" v0.1
git push --follow-tags
```

-->
