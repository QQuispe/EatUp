var map, infoWindow;

/* first version of google map api and markers
function createMap(){
    var options = {
        center: { lat: 39.100290, lng: -77.162480 },
        zoom: 12
    };

    map = new google.maps.Map(document.getElementById('map'), options);

    /* Get location from browser and mark map
    infoWindow = new google.maps.InfoWindow;
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (p){
            var position = {
                lat: p.coords.latitude,
                lng: p.coords.longitude
            };
            infoWindow.setPosition(position);
            infoWindow.setContent('Current Location');
            infoWindow.open(map);
        }, function () {
            handleLocationError('Geolocation service not working', map.center());
        })

    } else {
        handleLocationError('Location not available', map.center())
    }

    /* Search for location and mark map. Autocomplete.
    var input = document.getElementById('search');
    var searchBox = new google.maps.places.SearchBox(input);
    mark(searchBox);
    var input1 = document.getElementById('search1');
    var searchBox1 = new google.maps.places.SearchBox(input1);
    mark(SearchBox1);

    map.addListener('bounds_changed', function() {
        searchBox.setBounds(map.getBounds());
        searchBox1.setBounds(map.getBounds());
    });


    function mark(i){
        var markers = [];
        i.addListener('places_changed', function() {
            var places = i.getPlaces();

            if(places.length === 0)
                return;

            // clear map for future searches
            markers.forEach(function (m) {m.setMap(null); });
            markers = [];

            var bounds = new google.maps.LatLngBounds();

            places.forEach(function (p) {
                if (!p.geometry)
                    return;

                markers.push(new google.maps.Marker({
                    map: map,
                    title: p.name,
                    position: p.geometry.location
                }));

                if (p.geometry.viewport)
                    bounds.union(p.geometry.viewport);
                else
                    bounds.extends(p.geometry.location);
            });
            map.fitBounds(bounds);
        });
    }
}
*/

// current version. Does not include getting browser location
function initAutocomplete() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 39.100290, lng: -77.162480 },
        zoom: 11
        //mapTypeId: 'roadmap'
    });
    var markers = [];

    // Create the search boxs and link them to the UI elements.
    var searchBoxes = document.getElementsByClassName('form-control');
    for (var i=0; i<searchBoxes.length;i++) {
        var searchBox = new google.maps.places.SearchBox(searchBoxes[i]);
        //map.controls[google.maps.ControlPosition.TOP_LEFT].push(searchBoxes[i]);
        map.addListener('bounds_changed', function() {
            searchBox.setBounds(map.getBounds());
        });
        markers.push([]);
        searchBox.addListener('places_changed', (function(i) {
            return function() {
                processSearch(i, this)
            }
        }(i)));
    }

    function processSearch(uniqueId, searchBox) {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
            return;
           }

        // Clear out the old markers.
        markers[uniqueId].forEach(function(marker) {
        marker.setMap(null);
        });
        markers[uniqueId] = [];

        // For each place, get the icon, name and location.
        var bounds = new google.maps.LatLngBounds();
        places.forEach(function(place) {
            if (!place.geometry) {
                console.log("Returned place contains no geometry");
                return;
            }
        var icon = {
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(25, 25)
        };

        // Create a marker for each place.
        if (!markers[uniqueId]) markers.push([]);
        markers[uniqueId].push(new google.maps.Marker({
            map: map,
            title: place.name,
            position: place.geometry.location
        }));

        if (place.geometry.viewport) {
            // Only geocodes have viewport.
            bounds.union(place.geometry.viewport);
        } else {
            bounds.extend(place.geometry.location);
        }
        });
        map.fitBounds(bounds);
    }
}

function handleLocationError (content, position) {
    infoWindow.setPosition(position);
    infoWindow.setContent(content);
    infoWindow.open(map)
}
