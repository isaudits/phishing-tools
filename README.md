phishing-tools
=======

Scripts to assist in generating social engineering campaigns using the
phishing frenzy social engineering tool.

-------------------------------------------------------------------------------
Matthew C. Jones, CPA, CISA, OSCP

IS Audits and Consulting, LLC - <http://www.isaudits.com/>

TJS Deemer Dana - <http://www.tjsdd.com/>

-------------------------------------------------------------------------------
### eml_to_html.py
Converts an email in .eml format into html suitable for
importing into a phishing frenzy campaign. Provides options to replace all links
with phishing frenzy URL tags as well as imbedding the tracking image tag. Also
provides the option to download all linked html images to local and replace
those links, which is useful in the event that the internet links become broken.
Output is in the .erb format which should be uploaded as the "email" with any
additional images being uploaded as "attachments."


### website_cloner.py
Scrapes a website and downloads all content, including
images to a local folder in a format suitable for uploading into a phishing
frenzy campaign. Also downloads all linked images, css, etc locally in case
internet links become broken. This practice also reduces the chance of the
site being detected as having been cloned by the original site owner since you
are not leeching images off the original site. Output is an index.php file
and any additional images, css, etc which should all be uploaded as "website."

Note that some manual cleanup is required to make sure that the linked css and
scripts are referencing properly. Also note that not all of the scripts downloaded
will be necessary for the proper functionality of the site and may have tracking
content in them.

-------------------------------------------------------------------------------
### Other notes

These scripts are a work in process, particularly the website_cloner - each time
we use it on a new site there is some small nuance or tweak that we figure out.
Please feel free to submit suggestions, modifications, or pull requests to us.
Community contribution is greatly appreciated!

Phishing Frenzy can be downloaded at <https://github.com/pentestgeek/phishing-frenzy>

-------------------------------------------------------------------------------

###License

When not otherwise specified, scripts are licensed under GPL:

This program is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later 
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
this program. If not, see <http://www.gnu.org/licenses/>.