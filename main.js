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
        pokemonElement.textContent = `${pokemon.name} (${pokemon.type1})`;
        teamContainer.appendChild(pokemonElement);
    });
}