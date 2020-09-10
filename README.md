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
 Junk.organize('C:/user/Ajay/Desktop/Web/')
```
### Organize multiple folders
Pass A list of all folders that you want organize. 

```python
 folders = [
   'C:/user/Ajay/Desktop/Web/', 
   'C:/user/Ajay/Desktop/codes/'
 ]
 Junk.organize_more(folders) 
```
