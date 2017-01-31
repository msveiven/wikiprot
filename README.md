# wikiprot

Instructions on creating the wikiprotocols website:
1. Clone this repository to desktop
2. Create structure of website with directories, but always make directories inside "Scanners" which is inside the "wikiprot" directory (e.g. Scanners>UMC_Skyra>neuro). The directories should be inside a GitHub folder which is inside your Documents folder
3. Once structure of website is completed, move all .xml files to their appropriate directory (e.g. neuro)
4. Run websiteCreator.py with no argument in ~/Documents/GitHub/wikiprot/Scanners
5. Push desktop repository to github. Push to this url: https://msveiven.github.io/wikiprot/ 
 Follow this link for help on pushing desktop: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

Note: the repository must be in a GitHub folder on your desktop
Tip: When updating the site, remove all of the files except for the html files that contain the tables you have already 
made and the xml files that you want to make new tables with. Removing the xml files that already have tables will save time when 
running the webpageCreator.py script
