Nothing to see here now, but will soon be some documentation on a data visualization project for the BikeShare Data challenge. All data can be downloaded from the [BikeShare Data Challenge](http://bayareabikeshare.com/datachallenge) website.

Questions to ask of the data:


   * What days/times do the most/least bike rides occur
   * 
      * how does that correlate to:
      * 
         * temperature
         * precipitation
         * station location
   * Cycling time by distance (ie is it similar across distances, or are there faster cyclists)
   * 
      * how long on average does it take someone to reach their destination on a bikeshare
   * usage by bike #
   * 
      * how many trips did each bike take
      * fastest and slowest bikes
   * how many subscribers vs customers - breakdown over time (ie can we infer that customers became subscribers)
   * most popular bike stations
   * 
      * by bike pickup
      * by bike return
   * where do bike sharers live
   * 
      * how does this correlate to where they pickup/dropoff bikes
   * ridership on launch date (8/29/13)
   * rebalancing data: 
   * 
      * which stations are the most popular
      * mean time to refill bikes (which stations get the most love)

How to store and analyze this data
4 spreadsheets
could either do sql and 4 tables, relate to one another, or 4 collections with each record as a document;
Also can run scripts that do aggregations across the csv files and store the results in a database (redis?)
either way, store aggregations in a results database so we can read from that for our visualization