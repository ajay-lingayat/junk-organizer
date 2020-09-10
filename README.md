# junk-organizer

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
 Junk.organize('path/to/you/folder/')
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
