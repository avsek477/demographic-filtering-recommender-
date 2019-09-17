# demographic-filtering-recommender-system

Demographic filtering offer generalized recommendations to every user, based on movie popularity and/or genre. One thing to note here is that such systems recommends the same movie to users with similar demographic features. Hence, tha basic idea here is to suggest movies based on popularity and critically acclaimed good movies by users based on the ratio of their votes. 

Here, Weighted rating formula is used which is,
Weighted Rating(WR) = (v/(v+m)*R) + (m/(v+m)*C)
where, 
v is the number of votes for the movie.
m is the minimum votes required to be listed in the chart.
R is the average rating of the movie. 
C is the mean vote across the whole report.

#In order to run this project, just type in this command on the root directory of the cloned project.
bash download_datasets