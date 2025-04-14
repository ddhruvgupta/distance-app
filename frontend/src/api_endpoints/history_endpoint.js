async function fetchHistory(page, rowsPerPage) {

  const API_BASE_URL = "http://40.90.235.48:5000";
  try {
    const response = await fetch(
      `${API_BASE_URL}/history/?page=${page + 1}&limit=${rowsPerPage}`,
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Accept': '*/*',
          'Connection': 'keep-alive',
        },
      }
    );

    console.log("Response:", response);

    if (!response.ok) {
      throw new Error('Failed to fetch history data');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching history:', error);
    throw error;
  }
};

export default fetchHistory;