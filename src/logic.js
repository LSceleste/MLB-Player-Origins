d3.csv("../data/final.csv", function(error, playerData) {
    if (error) return console.warn(error);
  
    console.log(playerData);
  
    // log a list of player last names to test
    var names = playerData.map(data => data.nameLast);
    console.log("nameLast", names);
  
    // Cast each hours value in tvData as a number using the unary + operator
    playerData.forEach(function(data) {
      data.latitude = +data.latitude;
      data.longitude = +data.longitude;
    //console.log("Latitude:", data.latitude, "Longitude:", data.longitude);
      //console.log("Longitude", data.longitude);
    });


var myMap = L.map("map", {
    //Center coordinates are for Cooperstown NY, home of the Baseball Hall of Fame
    //center: [42.7006, -74.9243], changed these for initial positioning in map.
    center: [.9631, 19.0208],
    zoom: 2.48
    });
  
  // Adding tile layer to the map
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(myMap);
 
  
 
 
  

  
    var markers = L.markerClusterGroup();
  
    // Loop through data to add markers
    for (var i = 0; i < playerData.length; i++) {
         // Add a new marker to the cluster group and bind a pop-up
        markers.addLayer(L.marker([playerData[i]["latitude"], playerData[i]["longitude"]])
          //This is where we ADD what info we want displayed plus html tags to style info
            .bindPopup("<h3>" + "Player: " + "<h4>" + playerData[i].nameFirst + " " +
            playerData[i].nameLast + "</h4>" + "</h3><hr>" + "<h3>" + "Birth Place: " + 
            "</h3>" + "<h4>" + playerData[i].birthCity + ", " + playerData[i].country_iso_code + "</h4><hr>" + 
            "<h3>" + "Birth Year: " + "<h4>" + playerData[i].birthYear + "</h4></p>"));
      }
  
    
  
    // Add our marker cluster layer to the map
    myMap.addLayer(markers);
});
// Birthplace: "United States Denver"
// birthCity: "Denver"
// birthCountry: "United States"
// birthYear: "1981.0"
// city_name: "Denver"
// continent_code: ""
// country_iso_code: "US"
// country_name: "United States"
// deathCity: ""
// deathCountry: ""
// deathYear: ""
// geoname_id: "4463523.0"
// latitude: 35.4837
// longitude: -80.9898
// nameFirst: "David"
// nameLast: "Aardsma"
// playerID: "aardsda01"
// registered_country_geoname_id: "6252001.0"

//1. load csv into sqlite database
//2. retrieve data (creating routes in order to do this)
//3. execute routes in javascript