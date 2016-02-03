#**About the dataset:**
##This data set includes all of the publicly-sited works in the Civic Art Collection, which includes historic monuments, murals, and artworks commissioned through the City's Public Art Program. The data set includes the following categories: artist name, title of work, medium, dimensions and location.

#Basic facts about the dataset:
###- The source of the data: https://data.sfgov.org/
###- The data's landing page: https://data.sfgov.org/Culture-and-Recreation/SF-Civic-Art-Collection/zfw6-95su
###- Direct link to the data: https://data.sfgov.org/api/views/zfw6-95su/rows.csv?accessType=DOWNLOAD
###- The data format: CSV
###- Number of rows: 692

#Description of data fields:
###\_id_ - text string with ID number of the art piece
###_rev - text string (unknown identifier)
###accession_id - float (unknown identifier)
###artist - text string with the artist of the work of art
created_at - text string with the date and time that the filing was created
###credit_line - text string with payment information on the work of art
###display_dimensions - text string with the size of the work of art
###geometry - contains a dict with the type and 			coordinates
###location_description - text string with a description of the location of the art
###medium - text string with the medium of the art
###source - text string with the data source
###title - text string with the title of the work of art
###Location 1 - text string with more information on the location of the art

#Anticipated data wrangling:
###I will probably filter the dataset to include the artist, the location description, the medium, and the title of the work of art. Also, I will split the geometry field to get just the coordinates