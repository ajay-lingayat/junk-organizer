# junk-organizer

[![Downloads](https://pepy.tech/badge/junk-organizer-yellow.svg)](https://pepy.tech/project/junk-organizer)
[![Downloads](https://pepy.tech/badge/junk-organizer/month)](https://pepy.tech/project/junk-organizer/month)
[![Downloads](https://pepy.tech/badge/junk-organizer/week)](https://pepy.tech/project/junk-organizer/week)

## Requirements
```
 python>=3.0
```

## Installation
```
 pip install junk-organizer
```

## Usage

### Organize a single folder
```python
 from JunkOrganizer import Organizer
 Junk = Organizer()
 Junk.organize('path/to/the/folder/')
```

Output
```
 folder 'path/to/the/folder' has been organized!
```

### Organize multiple folders
Pass a list of all folders that you want organize to the organize_more method. 

```python
 folders = [
   'path/to/a/folder/', 
   'path/to/another/folder/', 
   'path/to/one_more/folder/'
 ]
 Junk.organize_more(folders) 
```

Output
```
 Organizing folders...
 folder 'path/to/a/folder' has been organized! 
 folder 'path/to/another/folder' has been organized! 
 folder 'path/to/one_more/folder' has been organized! 
```

## Upcoming Updates
- Organize more files with more extensions. 
- And many more.
