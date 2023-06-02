// Add event listener to the button
document.getElementById("randomTeamButton").addEventListener("click", getRandomTeam);

// Function to call the API endpoint and handle the response
function getRandomTeam() {
    fetch("http://localhost:8000/pokemon/random_team")
        .then(response => response.json())
        .then(data => {
            // Process the response data here
            displayTeam(data); // Call the function to display the team
        })
        .catch(error => {
            // Handle any errors that occurred during the API call
            console.error(error);
        });
}

// Function to display the team on the page
function displayTeam(teamData) {
    const teamContainer = document.getElementById("teamContainer");
    teamContainer.innerHTML = ""; // Clear the previous content
    
    // Iterate over each Pokemon in the teamData
    teamData.forEach(pokemon => {
        const pokemonElement = document.createElement("p");
        pokemonElement.textContent = `${pokemon.name} (${pokemon.type1}) (${pokemon.type2})`;
        teamContainer.appendChild(pokemonElement);
    });
}

function searchPokemon() {
    const inputElement = document.getElementById('pokemonNameInput');
    const pokemonName = inputElement.value;
  
    fetch(`http://localhost:8000/pokemon/search/${pokemonName}`)
      .then(response => response.json())
      .then(data => {
        const pokemonListElement = document.getElementById('pokemonList');
        pokemonListElement.innerHTML = '';
  
        data.forEach(pokemon => {
          const listItem = document.createElement('li');
          listItem.textContent = pokemon.name;
          pokemonListElement.appendChild(listItem);
        });
      })
      .catch(error => {
        console.log('Error:', error);
      });
}
  
const searchButton = document.getElementById('searchButton');
searchButton.addEventListener('click', searchPokemon);