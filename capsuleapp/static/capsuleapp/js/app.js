async function searchMedicine() {

    const query = document.getElementById("searchInput").value;

    const response = await fetch(
        `http://127.0.0.1:8000/api/search/?q=${query}`
    );

    const data = await response.json();

    const resultsDiv = document.getElementById("results");

    resultsDiv.innerHTML = "";

    data.forEach(async (medicine) => {

        const altResponse = await fetch(
            `http://127.0.0.1:8000/api/alternatives/${medicine.id}/`
        );

        const altData = await altResponse.json();

        let alternativesHTML = "";

        altData.alternatives.forEach((alt) => {
            alternativesHTML += `
                <div class="alt-item">
                    ${alt.brand_name} - ${alt.manufacturer}
                </div>
            `;
        });

        resultsDiv.innerHTML += `
            <div class="card">

                <h2>${medicine.brand_name}</h2>

                <p><strong>Generic:</strong> ${medicine.generic_name}</p>

                <p><strong>Strength:</strong> ${medicine.strength}</p>

                <p><strong>Company:</strong> ${medicine.manufacturer}</p>

                <h3>Alternative Brands</h3>

                ${alternativesHTML}

            </div>
        `;
    });
}