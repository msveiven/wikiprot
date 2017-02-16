# wikiprot

Instructions on creating the wikiprotocols website:
1. Clone this repository to desktop
2. To begin using Protparser, you need to open a terminal window and define an environment variable called WIKIPROTPATH which is set to the location Protparser was installed, and then source the setup script. Sourcing Protparser needs to be done every time you open a new terminal window. Or, you can add the two lines below to your default setup file (.bashrc or .cshrc) and Protparser will be sourced automatically everytime you open a new window. You can set this enviornmental variable equal to whichever directory you downloaded wikiprot files and scripts to. Below is an example of how this can be done if you downloaded wikiprot to /usr/local:

For Linux users:

bash:

     $> export WIKIPROTPATH=/usr/local/wikiprot
       
tcsh:

     $> setenv WIKIPROTPATH /usr/local/wikiprot

For Mac:

     $> export WIKIPROTPATH=/Applications/wikiprot
     
3. Next you will create the structure of your website. To do this, first go inside of the Scanners directory within the wikiprot directory. Next, add a directory for the scanner you are using (e.g. TestScanner). Within this scanner directory, add another directory for a catergory if you so choose (e.g. neuro or body). You can repeat this process for as many scanners and catergories that you choose.
4. Once structure of website is completed, move all .xml files to their appropriate directory (e.g. neuro)
5. Run websiteCreator.py with no argument in ~/Documents/GitHub/wikiprot/Scanners. Run like this: "python PATH/TO/STORED/SCRIPTS/websiteCreator.py"
6. Push desktop repository to github. Push to this url: https://msveiven.github.io/wikiprot/ 
 Follow this link for help on pushing desktop: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

Note: the repository must be in a GitHub folder on your desktop
Tip: When updating the site, remove all of the files except for the html files that contain the tables you have already 
made and the xml files that you want to make new tables with. Removing the xml files that already have tables will save time when 
running the webpageCreator.py script.
