async function fetchDistance(address1, address2) {
    // Validate input parameters
    if (!address1 || !address2) {
        throw new Error('Both address1 and address2 are required');
    }

    // Convert addresses to strings if they aren't already
    const addr1 = String(address1).trim();
    const addr2 = String(address2).trim();

    // Format request body to match the API's expected structure
    const requestBody = {
        "address1": addr1,
        "address2": addr2
    };
    
    console.log("Request Body:", requestBody);

    const API_BASE_URL = 'http://localhost:5000';
    const response = await fetch(`${API_BASE_URL}/distance/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        },
        body: JSON.stringify(requestBody)
    });

    if (!response.ok) {
        const errorData = await response.json();
        console.error("API Error:", errorData);
        throw new Error(errorData.errors?.json?.address1?.[0] || errorData.status || 'API Error');
    }

    const data = await response.json();
    console.log("API Response:", data);
    return data;
}

export default fetchDistance;