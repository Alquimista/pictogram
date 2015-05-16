**Pictogram** - v 0.1.0
------------------------
Instagram-like image filters.

Why? Why not!,  
I think is a fun project, that's all my justification


## Platform
* Linux


## Requirements
* Python 3.4
* Wand 0.4.0
* ImageMagick


## Install
```sh
$ easy_install pictogram
```
or

```sh
$ pip install pictogram
```
or

```sh
$ hg clone https://alquimista@bitbucket.org/alquimista/pictogram
$ cd pictogram
$ python setup.py install
```

## Test
```sh
$ cd pictogram
$ py.test
```

## Usage
```python
>>> import pictogram
>>> im = pictogram.Photo(path='example.jpg')
>>> im.bord(color="#000", width=20)
>>> im.save(path='example.filtered.jpg')
>>> im.show()
```

## Source
<https://bitbucket.org/alquimista/pictogram>  


## Contact
**mail:** robertogea@openmailbox.org  
**twitter:** @elalquimista  
**Skype:** robertogea  


## Conclusion
If you like this project, please help me, fork the project and send pull
request or, contact me in twitter, skype, or mail and let me know your awesome
ideas.

Thanks,  
Roberto Gea

