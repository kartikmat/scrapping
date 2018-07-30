from bs4 import BeautifulSoup

html_doc ="""
<!DOCTYPE html><html lang="en">
 <head>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css">

  <style>
    #content,
    #authorize-button,
    #signout-button {
      display: none
    }
  </style>
  <title>Caption Searcher</title>
</head>
<body>
  <nav class="black">
    <div class="nav-wrapper">
      <div class="container">
        <a href="#!" class="brand-logo">Caption Searcher</a>
      </div>
    </div>
  </nav>
  <br>
  <section>
    <div class="container">
      <p id="output"></p>
      <p>Log In With Google</p>
      <button class="btn red" id="authorize-button">Log In</button>
      <button class="btn red" id="signout-button">Log Out</button>
      <br>
      <div id="content">
        <div class="row">
          <div class="col s6">
            <form id="channel-form">
              <div class="input-field col s6">
                <input type="text" placeholder="Enter Channel Name" id="channel-input">
                <input type="text" placeholder="Enter keyword" id="keyword">
                <input type="submit" value="Get Channel Data" class="btn grey">
              </div>
            </form>
          </div>
          <div id="channel-data" class="col s6"></div>
        </div>
        <div class="row" id="video-container"></div>
      </div>
    </div>

  </section>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/js/materialize.min.js"></script>

  <script src="main.js"></script>
  <script async defer src="https://apis.google.com/js/api.js" onload="this.onload=function(){};handleClientLoad()" onreadystatechange="if (this.readyState === 'complete') this.onload()">
  </script>
</body>

</html>"""

soup = BeautifulSoup(html_doc,'html.parser')

#direct
#print(soup.body)
#print(soup.head)
#print(soup.head.title)

# find()
#el= soup.find('div')

# find_all() or findAll()
#el=soup.findAll('div')[1]

#el= soup.find(id='channel-data')
#el= soup.find(class_='row')
#el= soup.find(attrs={"href":"#!"})



#select
#el=soup.select('#channel-data')[0]
#el = soup.select('.row')


# getText()
#el=soup.find(id='output').getText()

#for row in soup.select('.row'):
#      print(row.getText())

#Navigation
#el= soup.body.contents[1].contents[1].nextSibling()
#el= soup.body.contents[1].contents[1].nextSibling().nextSibling()

#el= soup.body.contents[1].contents[1].find_next_sibling()
#el= soup.find(id='channel-data').find_previous_sibling()
#el= soup.find(class_='row').find_parent()
#el= soup.find('h3').find_next_sibling('p')


print(el)
