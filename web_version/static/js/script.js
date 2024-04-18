document.addEventListener('DOMContentLoaded', function() {
  const driverLevelElement = document.getElementById('driver-level');
  const carLevelElement = document.getElementById('car-level');
  const pitCrewLevelElement = document.getElementById('pit-crew-level');
  const racesLeftElement = document.getElementById('races-left');
  const raceButton = document.getElementById('race-button');
  const textArea = document.getElementById('text-area');

  let numRaces = 5;

  raceButton.addEventListener('click', function() {
    textArea.innerHTML = '';

    axios.post('/run_race')
      .then(function(response) {
        const raceDetails = response.data;
        textArea.innerHTML += `<p>Race: ${raceDetails.race_name}</p>`;
        textArea.innerHTML += '<p>Race started!</p>';
        textArea.innerHTML += `<p>Player's driver level: ${raceDetails.player_driver_level}, Player's car level: ${raceDetails.player_car_level}</p>`;

        // Display race events and pit stop times
        raceDetails.events.forEach(function(event) {
          textArea.innerHTML += `<p>${event}</p>`;
        });

        textArea.innerHTML += '<p>Race finish!</p>';
        numRaces--;
        racesLeftElement.textContent = numRaces;

        if (numRaces === 0) {
          textArea.innerHTML += '<p>Game Over!</p>';
          raceButton.disabled = true;
        } else {
          // Show upgrade menu
          // ...
        }
      })
      .catch(function(error) {
        console.error('Error:', error);
      });
  });
});