# K-Nearest-Neighbors and K-means-clustering
a basic implementation of k-nearest-neighbors

This project is a build week for Lambda School Computer Science Unit 1. It was completed durring the week of May 25th.

[Requirements can be found here](https://github.com/LambdaSchool/CS-Data-Science-Build-Week-I)

### Monday

I choose to do this implimentation because as a part of my labs project I needed to cluster earthquakes but was unable to get the sklearn implementation to work for me. I'm going to check in tomorrow (Tuesday) if I can build an algorithm that is specific to my project instead of just recreating the base model.

Today I'm going to focus on getting the general structure of the class built. MVP lays out required methods and I'm going to get those in place along with a rudimentary predict method.


### Tuesday

I ran through the basic KNN classifier yesterday so I'm going to switch to k-means clustering. I'm going to start a KMC classifier, I have an idea involving a distance matrix but its only a basic idea that will not work fully. Perhaps something along the lines of finding the lowest average with the highest distances from each other.

OK, I was totally making it harder than it needs to be. I've implemented a basic solution that works but needs improvement following the pattern:
- select K random points
- group the data around those points
- get the average distances of the groups
- use those averages as the new center
- loop until the centers don't change

Now that I have MVP for both of these algorithms I'm going to implement a solution to my labs project with earthquakes.


### Wednesday

I focused on getting quake data to line up. I started the day by using my API to pull the last month of data from each source,
then worked with my algorithm to line the data up.

My first thought was to focus the search on lat, lon, and mag. This returned good results from my data, so I pulled down all of the data from the server. For some reason when pulling it down from the server there was much less lining up, so I think something is wrong with how I'm setting up the search. I'll have to come back to this tomorrow

### Thursday

I found out that the job that got me into data Science is currently hiring and spent all day working on my application. I'm going to work on writing up a blog post this evening about my working algorithm and if I have time work a little more on the earthquakes.
