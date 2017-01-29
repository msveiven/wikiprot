# wikiprot

Instructions on creating the wikiprotocols website:
1. Clone this repository to desktop
2. Create structure of website with directories, but always make "Scanners" inside the "wikiprot" directory first then do the 
 rest (e.g. Scanners>UMC_Skyra>neuro)
3. Once structure of website is completed, move all .xml files to their appropriate directory (e.g. neuro)
4. Run webpageCreator.py in every directory that you created except the first one (in this case wikiprot)
5. Push desktop repository to github. Follow this link for help: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

Note: the repository must be in a GitHub folder on your desktop
Tip: When updating the site, remove all of the files except for the html files that contain the tables you have already 
made and the xml files that you want to make new tables with. Removing the xml files that already have tables will save time when 
running the webpageCreator.py script
