# Covid-19 Tracker

Welcome to my Covid-19 tracker created using HTML5, CSS, Javascript, Python and MongoDB. This 
a simple yet effective database used to store covid-19 experiences.

I want users to be able to log any details/ experiences with covid-19. This will be benificial 
to the user if they were to run into any health issues and needed to reflect on what may have 
caused it. A safe, easy way to store your data online.

## Design Process 

When i initally thought about creating my Covid-19 Tracker, I sketched some ideas down onto my IPad. 
My original design was going to be 5 pages. I then learned how to impliment the functionality where 
would only be visable to users who wre logged in/ out. From learning this, I relaised i could expand 
my site further making sections of it only accessable to some such as edit pages and manage documents.

## Wireframes/ Mock ups

- These are all found within the assets folder. Please go to assets > wireframes.

## User Experience

### User Stories

* I want to be able to store information.
* I want to be able to read different peoples documents if permitted to.
* I want to be able to update my information or delete it if needed.
* I dont want other people to be able to update or delete my entries.
* I want an easy navigation layout for the website.

These needs are met by;

* A simple yet effective styled form for creating documents.
* A straight forward documents section where documents are easily accessable.
* An edit page which allows users to access their previous entires for updating.
* A simple yet effective navigation bar that will not break from clicking between pages in any 
order. And, adapts to screen size.

### Strategy Plane 

##### Website Goals;

* A safe way to store documents.
* Create an easy to use website.
* Use simple yet effective ways to impliment javascript for interactivity.
* Create a website that would be effective in all age groups.
* Easy CRUD functionality.

### Scope Plane 

This website is designed over 7 pages. The home page contains 
a clear about message which informs users of websites purpose 
and documents for users to read. The website uses a database to 
store information. overall, the entire site enables CRUD functionality.
The Navbar is has JQuery implemented for ease of access from different screen sizes.


### Structure Plane 

The aim of the structure is to allow users to navigate through the site with ease. 
The home page contains a description on what the site is about, documents for the user to read.
The create a document page provides an easy to use form for the user including a calender 
format to pick a date from.

### Skeleton Plane 

1. 7 different pages with easy access to all.
2. Document structure that changed based on device being used.
3. A dropdown navagtion icon for smaller screens.

### Surface Plane

When creating this project, I thought intensly about colours that would be good for user experience.
The colours for the main site are subtle coulours that go well together along with a bold primary colour. The 
input field cards were a subtle grey which is easy on the eys for every user. I want the user to feel as if they 
feel welcomed to the site.

## Features

dropdown icon - Easy navagtion for smaller devices where all pages may not fit onto the screen.

Call to action buttons - easy navigation for user from and to any page on the website.

Create a document form - a simple form which will allow any user to make an entry to the database

A flash message - a flash message which informs the user of completion, error encounters when submitting a form.

links to socials - easy to use icons at the bottom of every page for additional navagation/ support.

### Features left to implement

*links to socials - easy to use icons at the bottom of every page for additional navagation/ support.

*Support page - a page in which the user can receive help/ report upon a form completion.

* A function which allows users to view only personal entries via profile page.

* I would have liked to of changed the layout of manage document cards for smaller devices.

## Technologies used

[Materializecss](https://materializecss.com/) - This is the framework I used to construct the website.

[Stack Overflow](https://stackoverflow.com/) - I used this as a resource of skils that I needed to learn e.g jQuery, Python.

[W3Schools](https://www.w3schools.com/default.asp) - I used this as a resource for skills e.g Styling pieces of text.

[W3Docs](https://www.w3docs.com/) - I used this to learn how to style buttons and spans.

[Geeks for geeks](https://www.geeksforgeeks.org/) - I used this to learn different attributes for HTML.

[MongoDB](https://www.mongodb.com/3) - This was used to create my database.

[Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - This website was used to impliment password hashing.

[Heroku](https://www.heroku.com/) - This was used to deploy my app.

## Testing

-  The CSS was run through the https://jigsaw.w3.org/css-validator/ without any errors found.
-  The HTML was run through the https://validator.w3.org/, the errors that are found are all related to the Jinja 
templating.
-  The cornflakes(flake8) lint was installed as an extension to the development and validated the Python code 
throughout my milestone project.
-  The site was tested on three different browsers: Google Chrome, Brave and Safari.
-  The responsiveness was tested on a wide variety of devices such as iphones, tablets and desktops using the Chrome 
DevTools and http://whatismyscreenresolution.net/multi-screen-test.


## Issues 

- The manage documents cards didnt sit properly when a large description was added
- I had issues trying to get my started experiencing placeholder text to dissapear
- i had tried to set up soem defensive programming with removing a document but i could not get it to 
work unfortunately.

### Validation

The W3C Markup Validator and the W3C CSS Validator were both used to validate every page of this project.
Despite my efforts, the vaildation had issues reading Python code. all HTML5 and CSS passed seperatly.


### Device testing

During my project, I consistently checked the website compatibility with all device sizes to ensure the best user experience possible.
I ensured this by using Chromes built in developer tools.
This website works well on all device sizes although I did encounter some issues on mobile device size with the text overflow. 
This happens when you go the the create a document page on mobiles and placeholders do not sit on their inputs.

I had a number of work collegues, family and friends try the website out for feedback so that i could make improvments from early development stages
 regarding a users experience. 


#### Devices tested

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- IPhone 5/SE
- IPhone 6/7/8
- IPhone 6/7/8Plus
- IPhone X
- IPad
- IPad Pro
- Surface Duo
- Galaxy Fold

### create document

1. Go to create document page once logged in
2. Try to submit empty form, a message will appear saying _Field required_
3. if the field does not meet the required amount of characters, the field will ask 
that you input the neccessary requirements.
4. Clicking submit creates a new document which can be viewed on manage documents page with 
full CRUD functionality to creator.

### edit document

1. the edit button can only be seen by the creator of the document.
2. if the creator presses edit, the edit page forms with the input fields 
of selected document.
3. once submitted, the user can instantly see the updated document.
4. select the cancel button instead. user will be taken back to manage documents page.

### remove document

1. the creator of the document must be signed in to view this option.
2. selecting remove will remove the document from the database.

1. Game onto game page and click the tiles faster than 225ms.
2. Tiles do not crash and game does not stop working.

### Navbar

1. on a smaller device, click the navbar links in any order and they will not break.
2. certain links are hidden from signed in/ out users for user experience.
3. go onto a larger device to make sure drop down disapears and a good UI navbar appears.

## Deployment

[Covid-19 Tracker](https://covid-19-logger.herokuapp.com/)

This project of mine is deployed via Heroku through their website. There is no difference between the deployed version and the deployment version.

### Deploying a Github Repository page

####Remote Deployment
-   Go to your Github repository and open it using GitPod
-	In the terminal run the command "pip3 freeze --local > requirements.txt" to create a .txt file with all of the dependencies for Heroku
-	In the terminal run the command "echo web: python run.py > Procfile" to create a Procfile for Heroku
-	Log in to Heroku and select Create New App
-	Select the input field App Name
-	Give your app a name
-	Select the region closest to your location (ireland for me) as I am in England
-	Click Create App
-	To connect the app to your Github repository, click on the Github icon inside of the "deployment method" section
-	Here there will be a new section called "Connect to Github" - ensure your Github profile is displayed inside it
-	Insert your repository name inside the "Connect to Github" section next to where your profile is displayed
-	Click on the "Search" button, once it finds your repository click the "Connect" button
-	Click on the settings tab at the top of the page, and select "Reveal Config Var"
-	Add the variables for IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME
-	Return to the Gitpod and make sure you have pushed the requirements.txt and Procfile
-	Return to Heroku and select enable automatic deployment
-	Select your master branch under Branch Selected
-	Click on the "Deploy Branch" - wait for the app to build
-	Once the site is deployed, click view to launch the app
-	As "enable automatic deployment" has been selected, any pushes to github will be updated automatically by heroku.


## Credits

#### Content -

The Navbar have all been copied from Matrialize. I have now styled the in my own way to fit into my website.
The create document form has been copied from one of my previous peices of work but styled to fit correctly with this website 
along with added Python for functonality.

[Materializecss](https://materializecss.com/) - This is the framework I used to construct the website.

[Stack Overflow](https://stackoverflow.com/) - I used this as a resource of skils that I needed to learn e.g jQuery, Python.

[W3Schools](https://www.w3schools.com/default.asp) - I used this as a resource for skills e.g Styling pieces of text.

[W3Docs](https://www.w3docs.com/) - I used this to learn how to style buttons and spans.

[Geeks for geeks](https://www.geeksforgeeks.org/) - I used this to learn different attributes for HTML.

[MongoDB](https://www.mongodb.com/3) - This was used to create my database.

[Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - This website was used to impliment password hashing.

[Heroku](https://www.heroku.com/) - This was used to deploy my app.

#### Media

[Youtube] (https://www.youtube.com/watch?v=rfscVS0vtbw) - This is where I learnt a lot of how to implement alot of my python functionality.

#### Acknowledgments

I have taken inspiration from my previous projects that have helped me construct this one. They are on my github repository