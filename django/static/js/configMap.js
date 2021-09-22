// Create the initial InfoWindow.
let infoWindow = [];

function SaveControl(controlDiv, map) {
  // Set CSS for the control border.
  const controlUI = document.createElement("div");

  controlUI.style.backgroundColor = "#0d6efd";
  controlUI.style.paddingLeft = "10px";
  controlUI.style.paddingRight = "10px";
  controlUI.style.borderRadius = "4px";
  controlUI.style.boxShadow = "0 2px 6px rgba(0,0,0,.3)";
  controlUI.style.cursor = "pointer";
  controlUI.style.marginTop = "8px";
  controlUI.style.marginBottom = "22px";
  controlUI.style.textAlign = "center";
  controlUI.title = "Clique para salvar os checkpoints";
  controlDiv.appendChild(controlUI);

  // Set CSS for the control interior.
  const controlText = document.createElement("div");

  controlText.style.color = "#fff";
  controlText.style.fontFamily = "Roboto,Arial,sans-serif";
  controlText.style.fontSize = "16px";
  controlText.style.lineHeight = "38px";
  controlText.style.paddingLeft = "5px";
  controlText.style.paddingRight = "5px";
  controlText.innerHTML = "Confirme os checkpoints";
  controlUI.appendChild(controlText);
  // Setup the click event listeners: simply set the map to Chicago.
  controlUI.addEventListener("click", () => {
    data = [];
    for (var i = 0; i < infoWindow.length;i++){
        data.push(infoWindow[i].content);
    }
    alert(data);
    $.post(url_rastrear, {data: data, csrfmiddlewaretoken: csrf_token}, function(response){
      window.location.href = url_rastrear;
    });
  });
}

function initMap() {
  const myLatlng = { lat: -22.9147, lng: -43.2563 };

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: myLatlng,
  });

  // Create the DIV to hold the control and call the CenterControl()
  // constructor passing in this DIV.
  const saveControlDiv = document.createElement("div");

  SaveControl(saveControlDiv, map);
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(saveControlDiv);


  // Configure the click listener.
  map.addListener("click", (mapsMouseEvent) => {
    // Create a new InfoWindow.
    checkpoint = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng, content: JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)});

    infoWindow.push(checkpoint);

    checkpoint.addListener('closeclick',function(){
        console.log("Teste de exclusão");
        index = infoWindow.indexOf(this);
        infoWindow.splice(index,1);
    });

    infoWindow[infoWindow.length-1].open(map);
  });


}