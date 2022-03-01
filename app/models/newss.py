class Newss:

    def __init__(self,urlToImage,title,description,url,time,content):
        self.urlToImage=urlToImage
        self.title=title
        self.description=description
        self.url=url
        self.time=time
        self.content=content

        

class Sources:

    def __init__(self,id,name,description,url,language,country):
        '''
        
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.country = country
        